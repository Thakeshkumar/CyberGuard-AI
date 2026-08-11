import customtkinter as ctk
from datetime import datetime

from services.password_analyzer import analyze_password

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

# Strength tier → colors
STRENGTH_COLORS = {
    "VERY WEAK": DANGER_COLOR,
    "WEAK": "#D66A2D",
    "MODERATE": WARNING_COLOR,
    "STRONG": INFO_COLOR,
    "VERY STRONG": SUCCESS_COLOR,
}
STRENGTH_BG = {
    "VERY WEAK": DANGER_BG,
    "WEAK": "#FBE9E2",
    "MODERATE": WARNING_BG,
    "STRONG": INFO_BG,
    "VERY STRONG": SUCCESS_BG,
}


def _make_card(parent, corner_radius=16):
    return ctk.CTkFrame(
        parent,
        fg_color=CARD_COLOR,
        corner_radius=corner_radius,
        border_width=1,
        border_color=BORDER_COLOR,
    )


def password_page(parent):
    """Modern CyberGuard AI Password Security Analyzer.

    Creates EXACTLY ONE page frame and returns it.
    Works through show_page(password_page).

    SECURITY: The password is analyzed locally and is NEVER displayed
    in the result, history, terminal, or stored anywhere.
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
        text="🔐  Password Security Analyzer",
        font=(FONT, 28, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w")

    ctk.CTkLabel(
        content,
        text="Evaluate password strength and identify security weaknesses.",
        font=(FONT, 15),
        text_color=SECONDARY_TEXT,
    ).pack(anchor="w", pady=(4, 14))

    # =========================
    # PASSWORD INPUT CARD
    # =========================

    input_card = _make_card(content, corner_radius=18)
    input_card.pack(fill="x")

    input_inner = ctk.CTkFrame(input_card, fg_color="transparent")
    input_inner.pack(fill="x", padx=22, pady=20)

    ctk.CTkLabel(
        input_inner,
        text="Enter Password",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w")

    # Entry row: password entry + show/hide toggle
    entry_row = ctk.CTkFrame(input_inner, fg_color="transparent")
    entry_row.pack(fill="x", pady=(10, 0))

    password_entry = ctk.CTkEntry(
        entry_row,
        height=46,
        corner_radius=12,
        placeholder_text="Enter your password...",
        show="•",
        fg_color="#FBF8F2",
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 15),
    )
    password_entry.pack(side="left", fill="x", expand=True)

    # Show/hide toggle state
    show_state = {"visible": False}

    def toggle_visibility():
        show_state["visible"] = not show_state["visible"]
        password_entry.configure(show="" if show_state["visible"] else "•")
        toggle_button.configure(
            text="🙈  Hide" if show_state["visible"] else "👁  Show"
        )

    toggle_button = ctk.CTkButton(
        entry_row,
        text="👁  Show",
        width=90,
        height=46,
        corner_radius=12,
        fg_color="#FBF8F2",
        hover_color="#F0EBE2",
        border_width=1,
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 13, "bold"),
        command=toggle_visibility,
    )
    toggle_button.pack(side="left", padx=(8, 0))

    # Error label (hidden by default)
    error_label = ctk.CTkLabel(
        input_inner,
        text="",
        font=(FONT, 13),
        text_color=DANGER_COLOR,
        anchor="w",
    )
    error_label.pack(fill="x", pady=(6, 0))

    analyze_button = ctk.CTkButton(
        input_inner,
        text="🔍  Analyze Password",
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
        text="🔒  Your password is analyzed locally and is not stored.",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
        anchor="w",
    ).pack(anchor="w", pady=(12, 0))

    # =========================
    # RESULT SECTION (hidden until analysis)
    # =========================

    result_card = _make_card(content, corner_radius=18)

    result_inner = ctk.CTkFrame(result_card, fg_color="transparent")
    result_inner.pack(fill="x", padx=22, pady=20)

    # Result header
    result_header = ctk.CTkFrame(result_inner, fg_color="transparent")
    result_header.pack(fill="x")

    ctk.CTkLabel(
        result_header,
        text="Analysis Result",
        font=(FONT, 18, "bold"),
        text_color=TEXT_COLOR,
    ).pack(side="left")

    strength_label = ctk.CTkLabel(
        result_header,
        text="—",
        font=(FONT, 14, "bold"),
        text_color=None,
        corner_radius=10,
        padx=16,
        pady=6,
    )
    strength_label.configure(text_color=STRENGTH_COLORS["MODERATE"], fg_color=STRENGTH_BG["MODERATE"])
    strength_label.pack(side="right")

    loading_label = ctk.CTkLabel(
        result_inner,
        text="Analyzing password...",
        font=(FONT, 14, "bold"),
        text_color=ACCENT_COLOR,
    )

    # Scored: left (checks + warnings) / right (score + recommendations)
    scored = ctk.CTkFrame(result_inner, fg_color="transparent")
    scored.grid_columnconfigure(0, weight=1, uniform="res")
    scored.grid_columnconfigure(1, weight=1, uniform="res")
    scored.grid_rowconfigure(0, weight=1)

    # -- Left: checks + warnings --
    left_panel = ctk.CTkFrame(scored, fg_color="transparent")
    left_panel.grid(row=0, column=0, padx=(0, 12), sticky="nsew")

    ctk.CTkLabel(
        left_panel,
        text="Security Checks",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w")

    checks_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
    checks_frame.pack(fill="x", pady=(8, 0))

    warnings_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
    warnings_frame.pack(fill="x", pady=(12, 0))

    # -- Right: score + recommendations --
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
        text="Security Recommendations",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
    ).pack(anchor="w", pady=(14, 0))

    recs_frame = ctk.CTkFrame(right_inner, fg_color="transparent")
    recs_frame.pack(fill="x", pady=(6, 0))

    # =========================
    # ANONYMOUS HISTORY
    # =========================

    history_card = _make_card(content, corner_radius=18)
    history_card.pack(fill="x", pady=(12, 0))

    history_header = ctk.CTkFrame(history_card, fg_color="transparent")
    history_header.pack(fill="x", padx=20, pady=(14, 8))

    ctk.CTkLabel(
        history_header,
        text="Recent Password Analyses",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(side="left")

    ctk.CTkLabel(
        history_header,
        text="(No passwords stored)",
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

    # ---- Anonymous history state (strength/score/time only) ----
    history = []

    history_rows = ctk.CTkFrame(history_body, fg_color="transparent")
    history_rows.pack(fill="x")

    def _render_history():
        for child in history_rows.winfo_children():
            child.destroy()

        if not history:
            ctk.CTkLabel(
                history_rows,
                text="No analyses yet. Run a check to see it here.",
                font=(FONT, 13),
                text_color=SECONDARY_TEXT,
            ).pack(anchor="w", pady=8)
            return

        for entry in history:
            row = ctk.CTkFrame(history_rows, fg_color="transparent")
            row.pack(fill="x", pady=3)

            ctk.CTkLabel(
                row,
                text=entry["strength"],
                font=(FONT, 13, "bold"),
                text_color=STRENGTH_COLORS.get(entry["strength"], TEXT_COLOR),
                width=140,
                anchor="w",
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=f"{entry['score']}/100",
                font=(FONT, 13, "bold"),
                text_color=STRENGTH_COLORS.get(entry["strength"], TEXT_COLOR),
                width=70,
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

    def _add_history(strength, score):
        now = datetime.now().strftime("%I:%M %p")
        history.insert(0, {"strength": strength, "score": score, "time": now})
        _render_history()

    def clear_history():
        history.clear()
        _render_history()

    clear_button.configure(command=clear_history)

    # =========================
    # ANALYSIS LOGIC
    # =========================

    def _render_result(result):
        strength = result["strength"]
        color = STRENGTH_COLORS.get(strength, TEXT_COLOR)
        bg = STRENGTH_BG.get(strength, "#F0EBE2")

        strength_label.configure(text=strength, text_color=color, fg_color=bg)

        # Score + progress
        score = result["score"]
        score_value.configure(text=f"{score} / 100", text_color=color)
        progress.set(score / 100)
        progress.configure(progress_color=color)

        # --- Security checks ---
        for child in checks_frame.winfo_children():
            child.destroy()

        for check in result["checks"]:
            row = ctk.CTkFrame(checks_frame, fg_color="transparent")
            row.pack(fill="x", pady=2)
            mark = "✓" if check["passed"] else "✗"
            mark_color = SUCCESS_COLOR if check["passed"] else DANGER_COLOR

            ctk.CTkLabel(
                row,
                text=mark,
                font=(FONT, 14, "bold"),
                text_color=mark_color,
                width=24,
                anchor="w",
            ).pack(side="left")
            ctk.CTkLabel(
                row,
                text=check["name"],
                font=(FONT, 13),
                text_color=TEXT_COLOR,
                anchor="w",
            ).pack(side="left")

        # --- Warnings ---
        for child in warnings_frame.winfo_children():
            child.destroy()

        if result["warnings"]:
            for warning in result["warnings"]:
                ctk.CTkLabel(
                    warnings_frame,
                    text="⚠  " + warning,
                    font=(FONT, 13),
                    text_color=WARNING_COLOR,
                    anchor="w",
                    justify="left",
                    wraplength=430,
                ).pack(anchor="w", pady=2)

        # --- Recommendations ---
        for child in recs_frame.winfo_children():
            child.destroy()

        for rec in result["recommendations"]:
            ctk.CTkLabel(
                recs_frame,
                text="•  " + rec,
                font=(FONT, 13),
                text_color=SECONDARY_TEXT,
                anchor="w",
                justify="left",
                wraplength=430,
            ).pack(anchor="w", pady=2)

        # Add anonymous history entry
        _add_history(strength, score)

    def _run_analysis():
        # Clear previous error
        error_label.configure(text="")

        password = password_entry.get()

        # Empty input handling
        if not password.strip():
            error_label.configure(text="⚠  Please enter a password to analyze.")
            return

        # Loading state
        loading_label.pack(anchor="w", pady=(16, 0))
        analyze_button.configure(state="disabled", text="Analyzing...")

        # Local analysis (fast, no network)
        try:
            result = analyze_password(password)
        except Exception:
            loading_label.pack_forget()
            analyze_button.configure(state="normal", text="🔍  Analyze Password")
            error_label.configure(
                text="⚠  Unexpected error during analysis. Please try again."
            )
            return

        # Display result
        loading_label.pack_forget()
        analyze_button.configure(state="normal", text="🔍  Analyze Password")
        result_card.pack(fill="x", pady=(12, 0))
        _render_result(result)

        # Clear the password input for security
        password_entry.delete(0, "end")
        if show_state["visible"]:
            toggle_visibility()

    analyze_button.configure(command=_run_analysis)
    password_entry.bind("<Return>", lambda e: _run_analysis())

    _render_history()

    return page