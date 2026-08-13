import customtkinter as ctk
from datetime import datetime

from services.url_analyzer import (
    analyze_url,
    is_valid_url
)

from services.report_store import save_report


# =========================
# CYBERGUARD AI THEME
# =========================

BG_COLOR = "#F7F2E8"
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
FONT_EMOJI = "Segoe UI Emoji"


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


# Initial demo history rows
DEMO_HISTORY = [
    ("https://example.com", "12:30 PM", "SAFE", 92),
    ("https://bit.ly/3xYz", "11:05 AM", "MEDIUM", 58),
    ("http://login-bank-verify.com", "10:20 AM", "HIGH", 34),
]


def _make_card(parent, corner_radius=16):

    return ctk.CTkFrame(
        parent,
        fg_color=CARD_COLOR,
        corner_radius=corner_radius,
        border_width=1,
        border_color=BORDER_COLOR,
    )


def _risk_chip(
    parent,
    text,
    risk
):

    return ctk.CTkLabel(
        parent,
        text=text,
        font=(FONT, 12, "bold"),
        text_color=RISK_COLORS.get(
            risk,
            TEXT_COLOR
        ),
        fg_color=RISK_BG.get(
            risk,
            "#F0EBE2"
        ),
        corner_radius=8,
        padx=12,
        pady=4,
    )


def SECURITY_COLOR(score):

    if score >= 80:
        return SUCCESS_COLOR

    elif score >= 55:
        return WARNING_COLOR

    return DANGER_COLOR


def url_scanner_page(parent):

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
    # TITLE
    # ========================================================

    title = ctk.CTkLabel(
        content,
        text="🌐  URL Security Scanner",
        font=(FONT, 28, "bold"),
        text_color=TEXT_COLOR,
    )

    title.pack(
        anchor="w"
    )

    subtitle = ctk.CTkLabel(
        content,
        text="Analyze a website URL for common security and suspicious indicators.",
        font=(FONT, 15),
        text_color=SECONDARY_TEXT,
    )

    subtitle.pack(
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

    ctk.CTkLabel(
        input_inner,
        text="Enter Website URL",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    url_entry = ctk.CTkEntry(
        input_inner,
        height=46,
        corner_radius=12,
        placeholder_text="https://example.com",
        fg_color="#FBF8F2",
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 15),
    )

    url_entry.pack(
        fill="x",
        pady=(10, 0)
    )

    error_label = ctk.CTkLabel(
        input_inner,
        text="",
        font=(FONT, 13),
        text_color=DANGER_COLOR,
        anchor="w",
    )

    error_label.pack(
        fill="x",
        pady=(6, 0)
    )

    scan_button = ctk.CTkButton(
        input_inner,
        text="🔍  Analyze URL",
        height=48,
        corner_radius=12,
        fg_color=ACCENT_COLOR,
        hover_color=ACCENT_HOVER,
        text_color="#FFFFFF",
        font=(FONT, 15, "bold"),
    )

    scan_button.pack(
        fill="x",
        pady=(14, 0)
    )

    demo_note = ctk.CTkLabel(
        input_inner,
        text=(
            "ℹ️  This is a DEMO/heuristic analyzer. "
            "Results are local pattern checks, not real threat-intelligence."
        ),
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
        anchor="w",
        wraplength=700,
        justify="left",
    )

    demo_note.pack(
        anchor="w",
        pady=(12, 0)
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
        text_color=RISK_COLORS["SAFE"],
        fg_color=RISK_BG["SAFE"],
        corner_radius=10,
        padx=16,
        pady=6,
    )

    risk_label.pack(
        side="right"
    )

    loading_label = ctk.CTkLabel(
        result_inner,
        text="Analyzing URL...",
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
    # DETAILS
    # ========================================================

    details = ctk.CTkFrame(
        scored,
        fg_color="transparent"
    )

    details.grid(
        row=0,
        column=0,
        padx=(0, 12),
        sticky="nsew"
    )

    detail_rows = ctk.CTkFrame(
        details,
        fg_color="transparent"
    )

    detail_rows.pack(
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
            pady=3
        )

        ctk.CTkLabel(
            row,
            text=label,
            font=(FONT, 13, "bold"),
            text_color=SECONDARY_TEXT,
            width=150,
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

    url_value = ctk.CTkLabel(
        detail_rows,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
        wraplength=430,
        justify="left",
    )

    https_value = ctk.CTkLabel(
        detail_rows,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
    )

    domain_value = ctk.CTkLabel(
        detail_rows,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
    )

    ip_value = ctk.CTkLabel(
        detail_rows,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
    )

    _detail_row(
        detail_rows,
        "URL",
        url_value
    )

    _detail_row(
        detail_rows,
        "HTTPS Status",
        https_value
    )

    _detail_row(
        detail_rows,
        "Domain",
        domain_value
    )

    _detail_row(
        detail_rows,
        "Domain/IP",
        ip_value
    )

    indicators_frame = ctk.CTkFrame(
        details,
        fg_color="transparent"
    )

    indicators_frame.pack(
        fill="x",
        pady=(10, 0)
    )

    # ========================================================
    # SCORE PANEL
    # ========================================================

    score_panel = ctk.CTkFrame(
        scored,
        fg_color="#FBF8F2",
        corner_radius=14
    )

    score_panel.grid(
        row=0,
        column=1,
        padx=(12, 0),
        sticky="nsew"
    )

    score_inner = ctk.CTkFrame(
        score_panel,
        fg_color="transparent"
    )

    score_inner.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=18
    )

    ctk.CTkLabel(
        score_inner,
        text="Security Score",
        font=(FONT, 14, "bold"),
        text_color=SECONDARY_TEXT,
        anchor="w",
    ).pack(
        anchor="w"
    )

    score_value = ctk.CTkLabel(
        score_inner,
        text="— / 100",
        font=(FONT, 34, "bold"),
        text_color=SUCCESS_COLOR,
    )

    score_value.pack(
        anchor="w",
        pady=(6, 4)
    )

    progress = ctk.CTkProgressBar(
        score_inner,
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

    verdict_label = ctk.CTkLabel(
        score_inner,
        text="AI Verdict: —",
        font=(FONT, 13, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
        justify="left",
        wraplength=430,
    )

    verdict_label.pack(
        anchor="w"
    )

    rec_label = ctk.CTkLabel(
        score_inner,
        text="Recommendation: —",
        font=(FONT, 13),
        text_color=SECONDARY_TEXT,
        anchor="w",
        justify="left",
        wraplength=430,
    )

    rec_label.pack(
        anchor="w",
        pady=(10, 0)
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
        text="Recent URL Scans",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        side="left"
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
                text="No scans yet. Run an analysis to see it here.",
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
                text=entry["url"],
                font=(FONT, 13),
                text_color=TEXT_COLOR,
                anchor="w",
                wraplength=380,
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

            _risk_chip(
                row,
                entry["risk"],
                entry["risk"]
            ).pack(
                side="right",
                padx=(0, 10)
            )

            ctk.CTkLabel(
                row,
                text=f"{entry['score']}/100",
                font=(FONT, 12, "bold"),
                text_color=SECURITY_COLOR(
                    entry["score"]
                ),
                width=64,
                anchor="e",
            ).pack(
                side="right",
                padx=(8, 6)
            )

    def _add_history(
        url,
        risk,
        score
    ):

        now = datetime.now().strftime(
            "%I:%M %p"
        )

        history.insert(
            0,
            {
                "url": url,
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
    # SHOW RESULT
    # ========================================================

    def _show_result(result):

        risk = result["risk"]

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

        url_value.configure(
            text=result["url"]
        )

        https_value.configure(
            text=result["https_status"]
        )

        domain_value.configure(
            text=result["domain"]
        )

        ip_value.configure(
            text="Yes"
            if result["is_ip"]
            else "No"
        )

        # Indicators
        for child in indicators_frame.winfo_children():
            child.destroy()

        indicators = result["indicators"]

        if not indicators:

            ctk.CTkLabel(
                indicators_frame,
                text="✅  No suspicious indicators found.",
                font=(FONT, 13),
                text_color=SUCCESS_COLOR,
                anchor="w",
            ).pack(
                anchor="w",
                pady=2
            )

        else:

            for ind in indicators:

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

        verdict = result["ai_verdict"]

        recommendation = result["recommendation"]

        verdict_label.configure(
            text="AI Verdict: " + verdict
        )

        rec_label.configure(
            text="Recommendation: " + recommendation
        )

        _add_history(
            result["url"],
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

        raw = url_entry.get()

        if not raw.strip():

            error_label.configure(
                text="⚠  Please enter a URL to analyze."
            )

            return

        if not is_valid_url(raw):

            error_label.configure(
                text=(
                    "⚠  Invalid URL. Please enter a valid URL "
                    "(e.g. https://example.com)."
                )
            )

            return

        loading_label.pack(
            anchor="w",
            pady=(16, 0)
        )

        scan_button.configure(
            state="disabled",
            text="Analyzing..."
        )

        error_label.configure(
            text=""
        )

        try:

            result = analyze_url(
                raw
            )

        except Exception as e:

            error_label.configure(
                text=f"⚠  Unexpected error during analysis: {e}"
            )

            loading_label.pack_forget()

            scan_button.configure(
                state="normal",
                text="🔍  Analyze URL"
            )

            return

        loading_label.pack_forget()

        scan_button.configure(
            state="normal",
            text="🔍  Analyze URL"
        )

        result_card.pack(
            fill="x",
            pady=(12, 0)
        )

        _show_result(
            result
        )

        # ====================================================
        # REPORT CONNECTION
        # ====================================================

        save_report(
            "URL Analyzer",
            result["url"],
            result["security_score"],
            result["risk"],
            result["ai_verdict"],
            result["recommendation"],
            extra={
                "domain": result["domain"],
                "https_status": result["https_status"],
                "is_ip": result["is_ip"],
                "indicators": result["indicators"]
            }
        )

    scan_button.configure(
        command=_run_analysis
    )

    url_entry.bind(
        "<Return>",
        lambda e: _run_analysis()
    )

    # Keep existing demo history
    for entry in DEMO_HISTORY:

        history.append(
            {
                "url": entry[0],
                "time": entry[1],
                "risk": entry[2],
                "score": entry[3]
            }
        )

    _render_history()

    return page