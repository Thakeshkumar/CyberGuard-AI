import customtkinter as ctk
from datetime import datetime

from services.email_analyzer import analyze_email
from services.report_store import save_report


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
    "HIGH": HIGH_COLOR if "HIGH_COLOR" in globals() else "#B85C5C",
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


def email_analyzer_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(
        fill="both",
        expand=True
    )

    content = ctk.CTkFrame(
        page,
        fg_color="transparent"
    )

    content.pack(
        fill="both",
        expand=True,
        padx=22,
        pady=18
    )

    # ========================================================
    # HEADER
    # ========================================================

    ctk.CTkLabel(
        content,
        text="📧  Email Security Analyzer",
        font=(FONT, 28, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    ctk.CTkLabel(
        content,
        text=(
            "Analyze emails for suspicious content, links, "
            "sender information, and security indicators."
        ),
        font=(FONT, 15),
        text_color=SECONDARY_TEXT,
    ).pack(
        anchor="w",
        pady=(4, 14)
    )

    # ========================================================
    # INPUT CARD
    # ========================================================

    input_card = _make_card(
        content,
        corner_radius=18
    )

    input_card.pack(
        fill="x"
    )

    input_inner = ctk.CTkFrame(
        input_card,
        fg_color="transparent"
    )

    input_inner.pack(
        fill="x",
        padx=22,
        pady=20
    )

    # Sender
    ctk.CTkLabel(
        input_inner,
        text="Sender Email",
        font=(FONT, 14, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    sender_entry = ctk.CTkEntry(
        input_inner,
        height=42,
        corner_radius=10,
        placeholder_text="sender@example.com",
        fg_color="#FBF8F2",
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 14),
    )

    sender_entry.pack(
        fill="x",
        pady=(6, 14)
    )

    # Recipient
    ctk.CTkLabel(
        input_inner,
        text="Recipient Email",
        font=(FONT, 14, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    recipient_entry = ctk.CTkEntry(
        input_inner,
        height=48,
        corner_radius=10,
        placeholder_text="recipient@example.com",
        fg_color="#FBF8F2",
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 14),
    )

    recipient_entry.pack(
        fill="x",
        pady=(6, 14)
    )

    # Subject
    ctk.CTkLabel(
        input_inner,
        text="Subject",
        font=(FONT, 14, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    subject_entry = ctk.CTkEntry(
        input_inner,
        height=48,
        corner_radius=10,
        placeholder_text="Enter email subject",
        fg_color="#FBF8F2",
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 14),
    )

    subject_entry.pack(
        fill="x",
        pady=(6, 14)
    )

    # Body
    ctk.CTkLabel(
        input_inner,
        text="Email Content",
        font=(FONT, 14, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    body_textbox = ctk.CTkTextbox(
        input_inner,
        height=220,
        corner_radius=12,
        fg_color="#FBF8F2",
        border_width=1,
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 13),
    )

    body_textbox.pack(
        fill="x",
        pady=(6, 0)
    )

    body_textbox.insert(
        "1.0",
        "Paste the email message here..."
    )

    # Headers
    ctk.CTkLabel(
        input_inner,
        text="Email Headers (Optional)",
        font=(FONT, 14, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w",
        pady=(14, 0)
    )

    headers_textbox = ctk.CTkTextbox(
        input_inner,
        height=120,
        corner_radius=12,
        fg_color="#FBF8F2",
        border_width=1,
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 12),
    )

    headers_textbox.pack(
        fill="x",
        pady=(6, 0)
    )

    headers_textbox.insert(
        "1.0",
        "Paste raw email headers if available for additional analysis."
    )

    # Analyze button
    btn_row = ctk.CTkFrame(
        input_inner,
        fg_color="transparent"
    )

    btn_row.pack(
        fill="x",
        pady=(16, 0)
    )

    analyze_button = ctk.CTkButton(
        btn_row,
        text="🔍  Analyze Email",
        height=48,
        corner_radius=12,
        fg_color=ACCENT_COLOR,
        hover_color=ACCENT_HOVER,
        text_color="#FFFFFF",
        font=(FONT, 15, "bold"),
    )

    analyze_button.pack(
        fill="x"
    )

    ctk.CTkLabel(
        input_inner,
        text="🔒  Email content is analyzed locally and is not uploaded.",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
        anchor="w",
    ).pack(
        anchor="w",
        pady=(12, 0)
    )

    error_label = ctk.CTkLabel(
        input_inner,
        text="",
        font=(FONT, 13),
        text_color=DANGER_COLOR,
        anchor="w",
        wraplength=700,
        justify="left",
    )

    error_label.pack(
        fill="x",
        pady=(6, 0)
    )

    # ========================================================
    # RESULT CARD
    # ========================================================

    result_card = _make_card(
        content,
        corner_radius=18
    )

    result_inner = ctk.CTkFrame(
        result_card,
        fg_color="transparent"
    )

    result_inner.pack(
        fill="x",
        padx=22,
        pady=20
    )

    result_header = ctk.CTkFrame(
        result_inner,
        fg_color="transparent"
    )

    result_header.pack(
        fill="x"
    )

    ctk.CTkLabel(
        result_header,
        text="Analysis Result",
        font=(FONT, 18, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        side="left"
    )

    risk_label = ctk.CTkLabel(
        result_header,
        text="—",
        font=(FONT, 14, "bold"),
        corner_radius=10,
        padx=16,
        pady=6,
    )

    risk_label.configure(
        text_color=RISK_COLORS["SAFE"],
        fg_color=RISK_BG["SAFE"]
    )

    risk_label.pack(
        side="right"
    )

    loading_label = ctk.CTkLabel(
        result_inner,
        text="Analyzing email...",
        font=(FONT, 14, "bold"),
        text_color=ACCENT_COLOR,
    )

    scored = ctk.CTkFrame(
        result_inner,
        fg_color="transparent"
    )

    scored.grid_columnconfigure(
        0,
        weight=1,
        uniform="res"
    )

    scored.grid_columnconfigure(
        1,
        weight=1,
        uniform="res"
    )

    scored.grid_rowconfigure(
        0,
        weight=1
    )

    # ========================================================
    # LEFT
    # ========================================================

    left_panel = ctk.CTkFrame(
        scored,
        fg_color="transparent"
    )

    left_panel.grid(
        row=0,
        column=0,
        padx=(0, 12),
        sticky="nsew"
    )

    details_frame = ctk.CTkFrame(
        left_panel,
        fg_color="transparent"
    )

    details_frame.pack(
        fill="x"
    )

    def _detail_row(
        frame,
        label,
        value_label,
        value_color=None
    ):

        row = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            pady=2
        )

        ctk.CTkLabel(
            row,
            text=label,
            font=(FONT, 13, "bold"),
            text_color=SECONDARY_TEXT,
            width=100,
            anchor="w",
        ).pack(
            side="left"
        )

        value_label.configure(
            text_color=value_color or TEXT_COLOR
        )

        value_label.pack(
            side="left",
            fill="x",
            expand=True
        )

    res_sender = ctk.CTkLabel(
        details_frame,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
        wraplength=380,
        justify="left"
    )

    res_recipient = ctk.CTkLabel(
        details_frame,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
        wraplength=380,
        justify="left"
    )

    res_subject = ctk.CTkLabel(
        details_frame,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
        wraplength=380,
        justify="left"
    )

    _detail_row(
        details_frame,
        "From",
        res_sender
    )

    _detail_row(
        details_frame,
        "To",
        res_recipient
    )

    _detail_row(
        details_frame,
        "Subject",
        res_subject
    )

    # Authentication
    auth_frame = ctk.CTkFrame(
        left_panel,
        fg_color="transparent"
    )

    auth_frame.pack(
        fill="x",
        pady=(10, 0)
    )

    ctk.CTkLabel(
        auth_frame,
        text="Authentication",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    spf_label = ctk.CTkLabel(
        auth_frame,
        text="SPF: —",
        font=(FONT, 13, "bold"),
        text_color=SECONDARY_TEXT,
        anchor="w"
    )

    dkim_label = ctk.CTkLabel(
        auth_frame,
        text="DKIM: —",
        font=(FONT, 13, "bold"),
        text_color=SECONDARY_TEXT,
        anchor="w"
    )

    dmarc_label = ctk.CTkLabel(
        auth_frame,
        text="DMARC: —",
        font=(FONT, 13, "bold"),
        text_color=SECONDARY_TEXT,
        anchor="w"
    )

    spf_label.pack(
        anchor="w",
        pady=2
    )

    dkim_label.pack(
        anchor="w",
        pady=2
    )

    dmarc_label.pack(
        anchor="w",
        pady=2
    )

    auth_note = ctk.CTkLabel(
        auth_frame,
        text="Email authentication information unavailable.",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
        anchor="w",
    )

    auth_note.pack(
        anchor="w",
        pady=4
    )

    # Indicators
    ctk.CTkLabel(
        left_panel,
        text="⚠  Suspicious Indicators",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w",
        pady=(14, 0)
    )

    indicators_frame = ctk.CTkFrame(
        left_panel,
        fg_color="transparent"
    )

    indicators_frame.pack(
        fill="x",
        pady=(8, 0)
    )

    # Links
    links_frame = ctk.CTkFrame(
        left_panel,
        fg_color="transparent"
    )

    links_frame.pack(
        fill="x",
        pady=(10, 0)
    )

    ctk.CTkLabel(
        links_frame,
        text="Links Found",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    links_detail = ctk.CTkFrame(
        links_frame,
        fg_color="transparent"
    )

    links_detail.pack(
        fill="x",
        pady=(6, 0)
    )

    # ========================================================
    # RIGHT
    # ========================================================

    right_panel = ctk.CTkFrame(
        scored,
        fg_color="#FBF8F2",
        corner_radius=14
    )

    right_panel.grid(
        row=0,
        column=1,
        padx=(12, 0),
        sticky="nsew"
    )

    right_inner = ctk.CTkFrame(
        right_panel,
        fg_color="transparent"
    )

    right_inner.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=18
    )

    ctk.CTkLabel(
        right_inner,
        text="Security Score",
        font=(FONT, 14, "bold"),
        text_color=SECONDARY_TEXT,
        anchor="w",
    ).pack(
        anchor="w"
    )

    score_value = ctk.CTkLabel(
        right_inner,
        text="— / 100",
        font=(FONT, 34, "bold"),
        text_color=SUCCESS_COLOR,
    )

    score_value.pack(
        anchor="w",
        pady=(6, 4)
    )

    progress = ctk.CTkProgressBar(
        right_inner,
        height=12,
        corner_radius=6,
        fg_color="#E8E1D5",
        progress_color=SUCCESS_COLOR,
    )

    progress.set(0)

    progress.pack(
        fill="x",
        pady=(6, 12)
    )

    ctk.CTkLabel(
        right_inner,
        text="🤖 AI Verdict",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
    ).pack(
        anchor="w",
        pady=(8, 0)
    )

    verdict_label = ctk.CTkLabel(
        right_inner,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
        justify="left",
        wraplength=430,
    )

    verdict_label.pack(
        anchor="w",
        pady=(4, 0)
    )

    ctk.CTkLabel(
        right_inner,
        text="Security Recommendation",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
    ).pack(
        anchor="w",
        pady=(14, 0)
    )

    rec_label = ctk.CTkLabel(
        right_inner,
        text="—",
        font=(FONT, 13),
        text_color=SECONDARY_TEXT,
        anchor="w",
        justify="left",
        wraplength=430,
    )

    rec_label.pack(
        anchor="w",
        pady=(4, 0)
    )

    # ========================================================
    # HISTORY
    # ========================================================

    history_card = _make_card(
        content,
        corner_radius=18
    )

    history_card.pack(
        fill="x",
        pady=(12, 0)
    )

    history_header = ctk.CTkFrame(
        history_card,
        fg_color="transparent"
    )

    history_header.pack(
        fill="x",
        padx=20,
        pady=(14, 8)
    )

    ctk.CTkLabel(
        history_header,
        text="Recent Email Analyses",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        side="left"
    )

    ctk.CTkLabel(
        history_header,
        text="(No content stored)",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
    ).pack(
        side="left",
        padx=(10, 0),
        pady=(4, 0)
    )

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

    clear_button.pack(
        side="right"
    )

    history_body = ctk.CTkFrame(
        history_card,
        fg_color="transparent"
    )

    history_body.pack(
        fill="x",
        padx=20,
        pady=(0, 16)
    )

    history = []

    history_rows = ctk.CTkFrame(
        history_body,
        fg_color="transparent"
    )

    history_rows.pack(
        fill="x"
    )

    def _render_history():

        for child in history_rows.winfo_children():
            child.destroy()

        if not history:

            ctk.CTkLabel(
                history_rows,
                text="No analyses yet. Run a scan to see it here.",
                font=(FONT, 13),
                text_color=SECONDARY_TEXT,
            ).pack(
                anchor="w",
                pady=8
            )

            return

        for entry in history:

            row = ctk.CTkFrame(
                history_rows,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                pady=3
            )

            ctk.CTkLabel(
                row,
                text=entry["sender"],
                font=(FONT, 13),
                text_color=TEXT_COLOR,
                anchor="w",
                wraplength=250,
                justify="left",
            ).pack(
                side="left",
                fill="x",
                expand=True
            )

            ctk.CTkLabel(
                row,
                text=entry["time"],
                font=(FONT, 12),
                text_color=SECONDARY_TEXT,
                width=90,
                anchor="e",
            ).pack(
                side="right"
            )

            ctk.CTkLabel(
                row,
                text=f"{entry['score']}/100",
                font=(FONT, 12, "bold"),
                text_color=RISK_COLORS.get(
                    entry["risk"],
                    TEXT_COLOR
                ),
                width=64,
                anchor="e",
            ).pack(
                side="right",
                padx=(8, 6)
            )

            ctk.CTkLabel(
                row,
                text=entry["risk"],
                font=(FONT, 12, "bold"),
                text_color=RISK_COLORS.get(
                    entry["risk"],
                    TEXT_COLOR
                ),
                fg_color=RISK_BG.get(
                    entry["risk"],
                    "#F0EBE2"
                ),
                corner_radius=8,
                padx=10,
                pady=3,
            ).pack(
                side="right",
                padx=(0, 10)
            )

    def _add_history(
        sender,
        risk,
        score
    ):

        now = datetime.now().strftime(
            "%I:%M %p"
        )

        history.insert(
            0,
            {
                "sender": sender,
                "time": now,
                "risk": risk,
                "score": score
            }
        )

        _render_history()

    def clear_history():

        history.clear()
        _render_history()

    clear_button.configure(
        command=clear_history
    )

    # ========================================================
    # RESULT RENDER
    # ========================================================

    def _render_result(result):

        risk = result["risk_level"]

        risk_color = RISK_COLORS.get(
            risk,
            TEXT_COLOR
        )

        risk_label.configure(
            text=risk,
            text_color=risk_color,
            fg_color=RISK_BG.get(
                risk,
                "#F0EBE2"
            )
        )

        res_sender.configure(
            text=result["sender"]
            if result["sender"]
            else "(none)"
        )

        res_recipient.configure(
            text=result["recipient"]
            if result["recipient"]
            else "(none)"
        )

        res_subject.configure(
            text=result["subject"]
            if result["subject"]
            else "(none)"
        )

        # Authentication
        auth = result["authentication"]

        if auth["available"]:

            auth_note.configure(
                text="Authentication data present."
            )

            spf_label.configure(
                text=f"SPF: {auth['spf']}"
            )

            dkim_label.configure(
                text=f"DKIM: {auth['dkim']}"
            )

            dmarc_label.configure(
                text=f"DMARC: {auth['dmarc']}"
            )

            def _auth_color(val):

                if val == "PASS":
                    return SUCCESS_COLOR

                if val == "FAIL":
                    return DANGER_COLOR

                return SECONDARY_TEXT

            spf_label.configure(
                text_color=_auth_color(
                    auth["spf"]
                )
            )

            dkim_label.configure(
                text_color=_auth_color(
                    auth["dkim"]
                )
            )

            dmarc_label.configure(
                text_color=_auth_color(
                    auth["dmarc"]
                )
            )

            auth_note.configure(
                text=""
            )

        else:

            spf_label.configure(
                text="SPF: —"
            )

            dkim_label.configure(
                text="DKIM: —"
            )

            dmarc_label.configure(
                text="DMARC: —"
            )

            auth_note.configure(
                text="Email authentication information unavailable."
            )

        # Indicators
        for child in indicators_frame.winfo_children():
            child.destroy()

        indicators = result["indicators"]

        if not indicators:

            ctk.CTkLabel(
                indicators_frame,
                text="✅  No suspicious indicators detected.",
                font=(FONT, 13),
                text_color=SUCCESS_COLOR,
                anchor="w",
            ).pack(
                anchor="w",
                pady=2
            )

        else:

            for ind in indicators[:10]:

                ctk.CTkLabel(
                    indicators_frame,
                    text="•  " + ind,
                    font=(FONT, 13),
                    text_color=TEXT_COLOR,
                    anchor="w",
                    justify="left",
                    wraplength=430,
                ).pack(
                    anchor="w",
                    pady=2
                )

        # Links
        for child in links_detail.winfo_children():
            child.destroy()

        links = result["links"]

        if not links:

            ctk.CTkLabel(
                links_detail,
                text="No links found in email content.",
                font=(FONT, 13),
                text_color=SECONDARY_TEXT,
                anchor="w",
            ).pack(
                anchor="w",
                pady=2
            )

        else:

            for link in links[:5]:

                risk_text = link["risk"]

                link_color = RISK_COLORS.get(
                    risk_text,
                    SECONDARY_TEXT
                )

                ctk.CTkLabel(
                    links_detail,
                    text=(
                        f"•  {link['url'][:80]}"
                        f"{'...' if len(link['url']) > 80 else ''}"
                    ),
                    font=(FONT, 12),
                    text_color=TEXT_COLOR,
                    anchor="w",
                    wraplength=430,
                    justify="left",
                ).pack(
                    anchor="w",
                    pady=2
                )

                ctk.CTkLabel(
                    links_detail,
                    text=(
                        f"   Domain: {link['domain']}  |  "
                        f"HTTPS: {link['https']}  |  "
                        f"{risk_text}"
                    ),
                    font=(FONT, 12),
                    text_color=link_color,
                    anchor="w",
                ).pack(
                    anchor="w",
                    pady=(0, 4)
                )

        score = result["security_score"]

        score_value.configure(
            text=f"{score} / 100",
            text_color=risk_color
        )

        progress.set(
            score / 100
        )

        progress.configure(
            progress_color=risk_color
        )

        verdict_label.configure(
            text=result["verdict"]
        )

        rec_label.configure(
            text=result["recommendation"]
        )

        _add_history(
            result["sender"]
            or result["sender_domain"]
            or "(unknown)",
            risk,
            score
        )

    # ========================================================
    # RUN ANALYSIS
    # ========================================================

    def _run_analysis():

        error_label.configure(
            text=""
        )

        sender = sender_entry.get().strip()
        recipient = recipient_entry.get().strip()
        subject = subject_entry.get().strip()

        body = body_textbox.get(
            "1.0",
            "end"
        ).strip()

        if not sender:

            error_label.configure(
                text="⚠  Please enter a sender email address."
            )

            return

        if (
            not body
            or body == "Paste the email message here..."
        ):

            error_label.configure(
                text="⚠  Please enter email content to analyze."
            )

            return

        headers = headers_textbox.get(
            "1.0",
            "end"
        ).strip()

        if headers == (
            "Paste raw email headers if available for additional analysis."
        ):

            headers = ""

        loading_label.pack(
            anchor="w",
            pady=(16, 0)
        )

        analyze_button.configure(
            state="disabled",
            text="Analyzing..."
        )

        try:

            result = analyze_email(
                sender,
                recipient,
                subject,
                body,
                headers
            )

        except Exception as e:

            loading_label.pack_forget()

            analyze_button.configure(
                state="normal",
                text="🔍  Analyze Email"
            )

            error_label.configure(
                text=f"⚠  Unexpected error during analysis: {e}"
            )

            return

        loading_label.pack_forget()

        analyze_button.configure(
            state="normal",
            text="🔍  Analyze Email"
        )

        result_card.pack(
            fill="x",
            pady=(12, 0)
        )

        _render_result(
            result
        )

        # ====================================================
        # REPORT CONNECTION
        # ====================================================

        # Do NOT store email body.
        # Store sender/domain metadata only.

        target = (
            result.get(
                "sender_domain"
            )
            or result.get(
                "sender"
            )
            or "Email Analysis"
        )

        verdict = result.get(
            "verdict",
            "Email security analysis completed."
        )

        recommendation = result.get(
            "recommendation",
            ""
        )

        findings = result.get(
            "indicators",
            []
        )

        save_report(
            "Email Analyzer",
            target,
            result["security_score"],
            result["risk_level"],
            verdict,
            recommendation,
            extra={
                "sender_domain": result.get(
                    "sender_domain",
                    ""
                ),
                "links_found": len(
                    result.get(
                        "links",
                        []
                    )
                ),
                "indicators": findings
            }
        )

    analyze_button.configure(
        command=_run_analysis
    )

    _render_history()

    return page