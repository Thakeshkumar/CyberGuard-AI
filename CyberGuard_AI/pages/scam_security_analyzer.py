import customtkinter as ctk
from datetime import datetime

from services.scam_detector import analyze_scam

# =========================
# CYBERGUARD AI THEME
# =========================

CARD_COLOR = "#FFFDF9"
BORDER_COLOR = "#D8CFC2"

TEXT_COLOR = "#3E332B"
SECONDARY_TEXT = "#75685D"

ACCENT_COLOR = "#8B5E3C"
ACCENT_HOVER = "#7A5233"

SUCCESS_COLOR = "#2E9B57"
SUCCESS_BG = "#EAF3EE"
DANGER_COLOR = "#B85C5C"
DANGER_BG = "#FBE9E9"
WARNING_COLOR = "#C98A2D"
WARNING_BG = "#FBF3E3"
INFO_COLOR = "#3A6EA5"
INFO_BG = "#E8F0F8"

FONT = "Segoe UI"

RISK_COLORS = {
    "SAFE": SUCCESS_COLOR,
    "LOW": INFO_COLOR,
    "MEDIUM": WARNING_COLOR,
    "HIGH": DANGER_COLOR,
    "CRITICAL": "#C0392B",
}
RISK_BG = {
    "SAFE": SUCCESS_BG,
    "LOW": INFO_BG,
    "MEDIUM": WARNING_BG,
    "HIGH": DANGER_BG,
    "CRITICAL": DANGER_BG,
}


def _make_card(parent, corner_radius=16):
    return ctk.CTkFrame(
        parent,
        fg_color=CARD_COLOR,
        corner_radius=corner_radius,
        border_width=1,
        border_color=BORDER_COLOR,
    )


def scam_detector_page(parent):
    """Modern CyberGuard AI Scam Detector.

    Creates EXACTLY ONE page frame and returns it.
    Works through show_page(scam_detector_page).
    """

    page = ctk.CTkFrame(parent, fg_color="transparent")
    page.pack(fill="both", expand=True)

    content = ctk.CTkFrame(page, fg_color="transparent")
    content.pack(fill="both", expand=True, padx=22, pady=18)

    # =========================
    # HEADER
    # =========================

    ctk.CTkLabel(
        content,
        text="🎣  Scam Detector",
        font=(FONT, 28, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w")

    ctk.CTkLabel(
        content,
        text="Analyze messages, links, and suspicious requests for common scam indicators.",
        font=(FONT, 15),
        text_color=SECONDARY_TEXT,
    ).pack(anchor="w", pady=(4, 14))

    # =========================
    # MESSAGE INPUT CARD
    # =========================

    input_card = _make_card(content, corner_radius=18)
    input_card.pack(fill="x")

    input_inner = ctk.CTkFrame(input_card, fg_color="transparent")
    input_inner.pack(fill="x", padx=22, pady=20)

    ctk.CTkLabel(
        input_inner,
        text="Paste Message or Suspicious Content",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w")

    message_textbox = ctk.CTkTextbox(
        input_inner,
        height=220,
        corner_radius=12,
        fg_color="#FBF8F2",
        border_width=1,
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 13),
    )
    message_textbox.pack(fill="x", pady=(10, 0))
    message_textbox.insert(
        "1.0",
        "Paste an SMS, WhatsApp message, email text, payment request, or suspicious message here...",
    )

    # Analyze button
    analyze_button = ctk.CTkButton(
        input_inner,
        text="🔍  Detect Scam",
        height=48,
        corner_radius=12,
        fg_color=ACCENT_COLOR,
        hover_color=ACCENT_HOVER,
        text_color="#FFFFFF",
        font=(FONT, 15, "bold"),
    )
    analyze_button.pack(fill="x", pady=(14, 0))

    # Privacy note
    ctk.CTkLabel(
        input_inner,
        text="🔒  Analysis is performed locally. Your message is not uploaded.",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
        anchor="w",
    ).pack(anchor="w", pady=(12, 0))

    # Error label (hidden by default)
    error_label = ctk.CTkLabel(
        input_inner,
        text="",
        font=(FONT, 13),
        text_color=DANGER_COLOR,
        anchor="w",
        wraplength=700,
        justify="left",
    )
    error_label.pack(fill="x", pady=(6, 0))

    # =========================
    # RESULT SECTION (hidden until analysis)
    # =========================

    result_card = _make_card(content, corner_radius=18)

    result_inner = ctk.CTkFrame(result_card, fg_color="transparent")
    result_inner.pack(fill="x", padx=22, pady=20)

    result_header = ctk.CTkFrame(result_inner, fg_color="transparent")
    result_header.pack(fill="x")

    ctk.CTkLabel(
        result_header,
        text="Analysis Result",
        font=(FONT, 18, "bold"),
        text_color=TEXT_COLOR,
    ).pack(side="left")

    risk_label = ctk.CTkLabel(
        result_header,
        text="—",
        font=(FONT, 14, "bold"),
        text_color=None,
        corner_radius=10,
        padx=16,
        pady=6,
    )
    risk_label.configure(text_color=RISK_COLORS["SAFE"], fg_color=RISK_BG["SAFE"])
    risk_label.pack(side="right")

    loading_label = ctk.CTkLabel(
        result_inner,
        text="Analyzing...",
        font=(FONT, 14, "bold"),
        text_color=ACCENT_COLOR,
    )

    # =========================
    # ANALYSIS SUMMARY (top strip)
    # =========================

    summary_frame = ctk.CTkFrame(result_inner, fg_color="#FBF8F2", corner_radius=12)
    summary_frame.pack(fill="x", pady=(14, 0))

    for col in range(5):
        summary_frame.grid_columnconfigure(col, weight=1, uniform="sum")

    summary_labels = {}

    summary_items = [
        ("Message Type", "message_type"),
        ("Risk Level", "risk"),
        ("Security Score", "score"),
        ("Indicators", "indicators"),
        ("Links", "links"),
    ]

    for idx, (label, key) in enumerate(summary_items):
        box = ctk.CTkFrame(summary_frame, fg_color="transparent")
        box.grid(row=0, column=idx, padx=10, pady=14, sticky="nsew")
        ctk.CTkLabel(
            box, text=label, font=(FONT, 11, "bold"), text_color=SECONDARY_TEXT, anchor="w"
        ).pack(anchor="w")
        summary_labels[key] = ctk.CTkLabel(
            box, text="—", font=(FONT, 15, "bold"), text_color=TEXT_COLOR, anchor="w"
        )
        summary_labels[key].pack(anchor="w", pady=(4, 0))

    # =========================
    # MAIN RESULT: left (indicators + links) / right (score + verdict)
    # =========================

    scored = ctk.CTkFrame(result_inner, fg_color="transparent")
    scored.pack(fill="x", pady=(14, 0))

    scored.grid_columnconfigure(0, weight=1, uniform="res")
    scored.grid_columnconfigure(1, weight=1, uniform="res")
    scored.grid_rowconfigure(0, weight=1)

    # -- Left: indicators + links --
    left_panel = ctk.CTkFrame(scored, fg_color="transparent")
    left_panel.grid(row=0, column=0, padx=(0, 12), sticky="nsew")

    ctk.CTkLabel(
        left_panel,
        text="⚠  Suspicious Indicators",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w")

    indicators_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
    indicators_frame.pack(fill="x", pady=(8, 0))

    ctk.CTkLabel(
        left_panel,
        text="🔗  Links Found",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w", pady=(14, 0))

    links_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
    links_frame.pack(fill="x", pady=(8, 0))

    # -- Right: score + verdict + recommendation --
    right_panel = ctk.CTkFrame(scored, fg_color="#FBF8F2", corner_radius=14)
    right_panel.grid(row=0, column=1, padx=(12, 0), sticky="nsew")

    right_inner = ctk.CTkFrame(right_panel, fg_color="transparent")
    right_inner.pack(fill="both", expand=True, padx=20, pady=18)

    ctk.CTkLabel(
        right_inner,
        text="Security Score",
        font=(FONT, 14, "bold"),
        text_color=SECONDARY_TEXT,
        anchor="w",
    ).pack(anchor="w")

    score_value = ctk.CTkLabel(
        right_inner,
        text="— / 100",
        font=(FONT, 34, "bold"),
        text_color=SUCCESS_COLOR,
    )
    score_value.pack(anchor="w", pady=(6, 4))

    progress = ctk.CTkProgressBar(
        right_inner,
        height=12,
        corner_radius=6,
        fg_color="#E8E1D5",
        progress_color=SUCCESS_COLOR,
    )
    progress.set(0)
    progress.pack(fill="x", pady=(6, 12))

    ctk.CTkLabel(
        right_inner,
        text="🤖 AI Verdict (rule-based local analysis)",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
    ).pack(anchor="w", pady=(8, 0))

    verdict_label = ctk.CTkLabel(
        right_inner,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
        justify="left",
        wraplength=430,
    )
    verdict_label.pack(anchor="w", pady=(4, 0))

    ctk.CTkLabel(
        right_inner,
        text="🛡  Security Recommendation",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
    ).pack(anchor="w", pady=(14, 0))

    rec_label = ctk.CTkLabel(
        right_inner,
        text="—",
        font=(FONT, 13),
        text_color=SECONDARY_TEXT,
        anchor="w",
        justify="left",
        wraplength=430,
    )
    rec_label.pack(anchor="w", pady=(4, 0))

    # =========================
    # RECENT SCAM ANALYSES
    # =========================

    history_card = _make_card(content, corner_radius=18)
    history_card.pack(fill="x", pady=(12, 0))

    history_header = ctk.CTkFrame(history_card, fg_color="transparent")
    history_header.pack(fill="x", padx=20, pady=(14, 8))

    ctk.CTkLabel(
        history_header,
        text="🕘  Recent Scam Analyses",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(side="left")

    ctk.CTkLabel(
        history_header,
        text="(Message content is not stored)",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
    ).pack(side="left", padx=(10, 0), pady=(4, 0))

    clear_button = ctk.CTkButton(
        history_header,
        text="Clear History",
        width=120,
        height=32,
        corner_radius=9,
        fg_color="#FBF8F2",
        hover_color="#F0EBE2",
        border_width=1,
        border_color="#DED4C6",
        text_color=DANGER_COLOR,
        font=(FONT, 12, "bold"),
    )
    clear_button.pack(side="right")

    history_body = ctk.CTkFrame(history_card, fg_color="transparent")
    history_body.pack(fill="x", padx=20, pady=(0, 16))

    # ---- History state (metadata only, no message content) ----
    history = []

    history_rows = ctk.CTkFrame(history_body, fg_color="transparent")
    history_rows.pack(fill="x")

    def _render_history():
        for child in history_rows.winfo_children():
            child.destroy()

        if not history:
            ctk.CTkLabel(
                history_rows,
                text="No analyses yet. Run a scan to see it here.",
                font=(FONT, 13),
                text_color=SECONDARY_TEXT,
            ).pack(anchor="w", pady=8)
            return

        for entry in history:
            row = ctk.CTkFrame(history_rows, fg_color="transparent")
            row.pack(fill="x", pady=3)

            ctk.CTkLabel(
                row,
                text=entry["message_type"],
                font=(FONT, 13),
                text_color=TEXT_COLOR,
                anchor="w",
                width=180,
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=f"{entry['indicator_count']} ind.",
                font=(FONT, 12),
                text_color=SECONDARY_TEXT,
                width=60,
                anchor="w",
            ).pack(side="left", padx=(8, 0))

            ctk.CTkLabel(
                row,
                text=entry["time"],
                font=(FONT, 12),
                text_color=SECONDARY_TEXT,
                width=90,
                anchor="e",
            ).pack(side="right")

            ctk.CTkLabel(
                row,
                text=f"{entry['score']}/100",
                font=(FONT, 12, "bold"),
                text_color=RISK_COLORS.get(entry["risk"], TEXT_COLOR),
                width=64,
                anchor="e",
            ).pack(side="right", padx=(8, 6))

            ctk.CTkLabel(
                row,
                text=entry["risk"],
                font=(FONT, 12, "bold"),
                text_color=RISK_COLORS.get(entry["risk"], TEXT_COLOR),
                fg_color=RISK_BG.get(entry["risk"], "#F0EBE2"),
                corner_radius=8,
                padx=10,
                pady=3,
            ).pack(side="right", padx=(0, 10))

    def _add_history(message_type, risk, score, indicator_count):
        now = datetime.now().strftime("%I:%M %p")
        history.insert(0, {
            "message_type": message_type,
            "risk": risk,
            "score": score,
            "indicator_count": indicator_count,
            "time": now,
        })
        _render_history()

    def clear_history():
        history.clear()
        _render_history()

    clear_button.configure(command=clear_history)

    # =========================
    # ANALYSIS LOGIC
    # =========================

    def _render_result(result):
        risk = result["risk_level"]
        risk_color = RISK_COLORS.get(risk, TEXT_COLOR)

        risk_label.configure(
            text=risk,
            text_color=risk_color,
            fg_color=RISK_BG.get(risk, "#F0EBE2"),
        )

        # Summary
        summary_labels["message_type"].configure(text=result["message_type"])
        summary_labels["risk"].configure(text=risk, text_color=risk_color)
        summary_labels["score"].configure(text=f"{result['security_score']}/100", text_color=risk_color)
        summary_labels["indicators"].configure(text=str(len(result["indicators"])))
        summary_labels["links"].configure(text=str(len(result["links"])))

        # Suspicious indicators
        for child in indicators_frame.winfo_children():
            child.destroy()

        indicators = result["indicators"]
        if not indicators:
            ctk.CTkLabel(
                indicators_frame,
                text="✅  No suspicious scam indicators detected",
                font=(FONT, 13),
                text_color=SUCCESS_COLOR,
                anchor="w",
            ).pack(anchor="w", pady=2)
        else:
            for ind in indicators[:10]:
                ctk.CTkLabel(
                    indicators_frame,
                    text="⚠  " + ind,
                    font=(FONT, 13),
                    text_color=TEXT_COLOR,
                    anchor="w",
                    justify="left",
                    wraplength=430,
                ).pack(anchor="w", pady=2)
            if len(indicators) > 10:
                ctk.CTkLabel(
                    indicators_frame,
                    text=f"  ... and {len(indicators) - 10} more indicators.",
                    font=(FONT, 12),
                    text_color=SECONDARY_TEXT,
                    anchor="w",
                ).pack(anchor="w", pady=2)

        # Links
        for child in links_frame.winfo_children():
            child.destroy()

        links = result["links"]
        if not links:
            ctk.CTkLabel(
                links_frame,
                text="✅  No URLs detected",
                font=(FONT, 13),
                text_color=SECONDARY_TEXT,
                anchor="w",
            ).pack(anchor="w", pady=2)
        else:
            for link in links[:5]:
                risk_text = link["risk"]
                risk_c = RISK_COLORS.get(risk_text, SECONDARY_TEXT)
                ctk.CTkLabel(
                    links_frame,
                    text=f"•  {link['url'][:60]}{'...' if len(link['url']) > 60 else ''}",
                    font=(FONT, 12),
                    text_color=TEXT_COLOR,
                    anchor="w",
                    wraplength=430,
                    justify="left",
                ).pack(anchor="w", pady=2)
                ctk.CTkLabel(
                    links_frame,
                    text=f"   Domain: {link['domain']}  |  HTTPS: {link['https']}  |  {risk_text}",
                    font=(FONT, 12),
                    text_color=risk_c or SECONDARY_TEXT,
                    anchor="w",
                ).pack(anchor="w", pady=(0, 4))
            if len(links) > 5:
                ctk.CTkLabel(
                    links_frame,
                    text=f"  ... and {len(links) - 5} more links.",
                    font=(FONT, 12),
                    text_color=SECONDARY_TEXT,
                    anchor="w",
                ).pack(anchor="w", pady=2)

        # Score + progress
        score = result["security_score"]
        score_value.configure(text=f"{score} / 100", text_color=risk_color)
        progress.set(score / 100)
        progress.configure(progress_color=risk_color)

        verdict_label.configure(text=result["verdict"])
        rec_label.configure(text=result["recommendation"])

        # Add to history (metadata only)
        _add_history(result["message_type"], risk, score, len(indicators))

    def _run_analysis():
        error_label.configure(text="")

        message = message_textbox.get("1.0", "end").strip()
        if message == "Paste an SMS, WhatsApp message, email text, payment request, or suspicious message here...":
            message = ""

        # Validate empty input
        if not message:
            error_label.configure(text="⚠  Please paste a message to analyze.")
            return

        # Reject excessively large input (> 20k chars) to prevent UI freeze
        if len(message) > 20000:
            error_label.configure(text="⚠  The message is too large to analyze (max 20,000 characters).")
            return

        # Loading state
        loading_label.pack(anchor="w", pady=(16, 0))
        analyze_button.configure(state="disabled", text="Analyzing...")

        try:
            result = analyze_scam(message)
        except ValueError:
            loading_label.pack_forget()
            analyze_button.configure(state="normal", text="🔍  Detect Scam")
            error_label.configure(text="⚠  Please paste a message to analyze.")
            return
        except Exception:
            loading_label.pack_forget()
            analyze_button.configure(state="normal", text="🔍  Detect Scam")
            error_label.configure(text="⚠  Unexpected error during analysis. Please try again.")
            return

        loading_label.pack_forget()
        analyze_button.configure(state="normal", text="🔍  Detect Scam")
        result_card.pack(fill="x", pady=(12, 0))
        _render_result(result)

    analyze_button.configure(command=_run_analysis)

    _render_history()

    return page