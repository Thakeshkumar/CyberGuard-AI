import customtkinter as ctk

from services.report_store import get_all_reports

# Page functions used by Quick Actions / Voice Companion
from pages.url_scanner import url_scanner_page
from pages.password import password_page
from pages.file_analyzer import file_analyzer_page
from pages.scam_detector import scam_detector_page
from pages.voice_companion import voice_companion_page


# ============================================================
# CYBERGUARD AI THEME
# ============================================================

BG_COLOR = "#F7F2E8"
CARD_COLOR = "#FFFDF9"
BORDER_COLOR = "#D8CFC2"

TEXT_COLOR = "#3E332B"
SECONDARY_TEXT = "#75685D"

ACCENT_COLOR = "#8B5E3C"
ACCENT_LIGHT = "#E8D8C8"
ACCENT_HOVER = "#7A5233"

SUCCESS_COLOR = "#5A9B7A"
SUCCESS_BG = "#EAF3EE"

DANGER_COLOR = "#B85C5C"
DANGER_BG = "#FBE9E9"

WARNING_COLOR = "#C98A2D"
WARNING_BG = "#FBF3E3"

LOW_COLOR = "#3A6EA5"
HIGH_COLOR = "#B85C5C"
CRITICAL_COLOR = "#A94442"

FONT = "Segoe UI"
FONT_EMOJI = "Segoe UI Emoji"


# ============================================================
# DAILY TIPS
# ============================================================

DAILY_TIPS = [
    "Never share your OTP, passwords, or personal information with anyone — even if they claim to be from your bank.",
    "Use a unique, strong password for every account and enable two-factor authentication (2FA) wherever possible.",
    "Beware of urgent messages asking for money or credentials — always verify the sender through an official channel.",
    "Keep your software, browsers, and antivirus up to date to stay protected against known vulnerabilities.",
]


# ============================================================
# RISK COLORS
# ============================================================

RISK_COLORS = {
    "SAFE": SUCCESS_COLOR,
    "LOW": LOW_COLOR,
    "MEDIUM": WARNING_COLOR,
    "HIGH": DANGER_COLOR,
    "CRITICAL": CRITICAL_COLOR,
}


RISK_PRIORITY = {
    "SAFE": 0,
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4,
}


# ============================================================
# HELPERS
# ============================================================

def _make_card(parent, corner_radius=16):

    return ctk.CTkFrame(
        parent,
        fg_color=CARD_COLOR,
        corner_radius=corner_radius,
        border_width=1,
        border_color=BORDER_COLOR,
    )


def _make_section_title(parent, text):

    return ctk.CTkLabel(
        parent,
        text=text,
        font=(FONT, 18, "bold"),
        text_color=TEXT_COLOR,
    )


def _risk_color(risk):

    return RISK_COLORS.get(
        str(risk).upper(),
        SECONDARY_TEXT
    )


def _calculate_overall_score(reports):

    if not reports:
        return 0

    scores = []

    for report in reports:

        try:

            score = float(
                report.get(
                    "score",
                    0
                )
            )

            score = max(
                0,
                min(
                    100,
                    score
                )
            )

            scores.append(
                score
            )

        except (
            TypeError,
            ValueError
        ):
            continue

    if not scores:
        return 0

    return round(
        sum(scores) / len(scores)
    )


def _calculate_overall_risk(reports):

    if not reports:
        return "NO DATA"

    selected = "SAFE"
    selected_value = -1

    for report in reports:

        risk = str(
            report.get(
                "risk",
                "SAFE"
            )
        ).upper()

        value = RISK_PRIORITY.get(
            risk,
            0
        )

        if value > selected_value:

            selected = risk
            selected_value = value

    return selected


# ============================================================
# DASHBOARD
# ============================================================

def dashboard_page(parent, on_navigate=None):

    # ========================================================
    # ROOT
    # ========================================================

    dashboard = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    dashboard.pack(
        fill="both",
        expand=True
    )


    # ========================================================
    # MAIN CONTENT
    # ========================================================

    content = ctk.CTkFrame(
        dashboard,
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

    header = _make_card(
        content,
        corner_radius=18
    )

    header.pack(
        fill="x"
    )


    header_inner = ctk.CTkFrame(
        header,
        fg_color="transparent"
    )

    header_inner.pack(
        fill="x",
        padx=24,
        pady=20
    )


    header_top = ctk.CTkFrame(
        header_inner,
        fg_color="transparent"
    )

    header_top.pack(
        fill="x"
    )


    # Refresh button
    refresh_button = ctk.CTkButton(
        header_top,
        text="🔄  Refresh",
        width=105,
        height=36,
        corner_radius=9,
        fg_color=ACCENT_COLOR,
        hover_color=ACCENT_HOVER,
        text_color="#FFFFFF",
        font=(FONT, 11, "bold"),
    )

    refresh_button.pack(
        side="right"
    )


    # Profile
    profile_chip = ctk.CTkLabel(
        header_top,
        text="👤  Thakesh",
        font=(FONT, 13, "bold"),
        text_color=TEXT_COLOR,
        fg_color=ACCENT_LIGHT,
        corner_radius=10,
        padx=14,
        pady=6,
    )

    profile_chip.pack(
        side="right",
        padx=(10, 0)
    )


    # Status
    status_badge = ctk.CTkLabel(
        header_top,
        text="🟢  All Systems Operational",
        font=(FONT, 13, "bold"),
        text_color=SUCCESS_COLOR,
        fg_color=SUCCESS_BG,
        corner_radius=10,
        padx=14,
        pady=6,
    )

    status_badge.pack(
        side="right",
        padx=(0, 12)
    )


    # Welcome
    welcome = ctk.CTkLabel(
        header_top,
        text="👋  Welcome back, Thakesh!",
        font=(FONT, 26, "bold"),
        text_color=TEXT_COLOR,
    )

    welcome.pack(
        side="left"
    )


    subtitle = ctk.CTkLabel(
        header_inner,
        text=(
            "Your AI-powered cybersecurity companion — "
            "scan URLs, analyze passwords, files, emails, and more."
        ),
        font=(FONT, 14),
        text_color=SECONDARY_TEXT,
    )

    subtitle.pack(
        anchor="w",
        pady=(12, 0)
    )


    # Last refreshed text
    last_refresh_label = ctk.CTkLabel(
        header_inner,
        text="Last refreshed: just now",
        font=(FONT, 11),
        text_color=SECONDARY_TEXT
    )

    last_refresh_label.pack(
        anchor="w",
        pady=(6, 0)
    )


    # ========================================================
    # STATISTICS SECTION
    # ========================================================

    stats = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    stats.pack(
        fill="x",
        pady=(18, 8)
    )


    for col in range(4):

        stats.grid_columnconfigure(
            col,
            weight=1,
            uniform="stats"
        )


    stats_labels = {}


    def create_stat_card(
        column,
        key,
        icon,
        title,
        value,
        color,
        caption
    ):

        card = _make_card(
            stats
        )

        card.grid(
            row=0,
            column=column,
            padx=5,
            pady=4,
            sticky="nsew"
        )


        inner = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        inner.pack(
            fill="x",
            padx=16,
            pady=16
        )


        ctk.CTkLabel(
            inner,
            text=icon,
            font=(FONT_EMOJI, 22),
            text_color=TEXT_COLOR,
        ).pack(
            anchor="w"
        )


        ctk.CTkLabel(
            inner,
            text=title,
            font=(FONT, 13, "bold"),
            text_color=SECONDARY_TEXT,
        ).pack(
            anchor="w",
            pady=(10, 2)
        )


        value_label = ctk.CTkLabel(
            inner,
            text=str(value),
            font=(FONT, 28, "bold"),
            text_color=color
        )

        value_label.pack(
            anchor="w"
        )


        ctk.CTkLabel(
            inner,
            text=caption,
            font=(FONT, 12),
            text_color=SECONDARY_TEXT,
        ).pack(
            anchor="w",
            pady=(2, 0)
        )


        stats_labels[key] = value_label


    create_stat_card(
        0,
        "score",
        "🛡",
        "Security Score",
        "0/100",
        SECONDARY_TEXT,
        "No scans yet"
    )


    create_stat_card(
        1,
        "total",
        "▣",
        "Total Scans",
        "0",
        TEXT_COLOR,
        "All Time"
    )


    create_stat_card(
        2,
        "threats",
        "⚠",
        "Threats Detected",
        "0",
        SUCCESS_COLOR,
        "No threats detected"
    )


    create_stat_card(
        3,
        "safe",
        "✓",
        "Safe Items",
        "0",
        SUCCESS_COLOR,
        "SAFE reports"
    )


    # ========================================================
    # OVERALL SECURITY CARD
    # ========================================================

    overall_card = _make_card(
        content,
        corner_radius=18
    )

    overall_card.pack(
        fill="x",
        pady=(16, 16)
    )


    overall_left = ctk.CTkFrame(
        overall_card,
        fg_color="transparent"
    )

    overall_left.pack(
        side="left",
        fill="x",
        expand=True,
        padx=25,
        pady=20
    )


    ctk.CTkLabel(
        overall_left,
        text="Overall Security Status",
        font=(FONT, 19, "bold"),
        text_color=TEXT_COLOR
    ).pack(
        anchor="w"
    )


    overall_score_label = ctk.CTkLabel(
        overall_left,
        text="0 / 100",
        font=(FONT, 34, "bold"),
        text_color=SECONDARY_TEXT
    )

    overall_score_label.pack(
        anchor="w",
        pady=(5, 7)
    )


    overall_progress = ctk.CTkProgressBar(
        overall_left,
        height=13,
        corner_radius=7,
        fg_color="#E8E1D5",
        progress_color=SUCCESS_COLOR
    )

    overall_progress.set(0)

    overall_progress.pack(
        fill="x"
    )


    overall_right = ctk.CTkFrame(
        overall_card,
        fg_color="#F7F3EC",
        corner_radius=14,
        width=220,
        height=100
    )

    overall_right.pack(
        side="right",
        padx=25,
        pady=20
    )

    overall_right.pack_propagate(
        False
    )


    ctk.CTkLabel(
        overall_right,
        text="Overall Risk",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT
    ).pack(
        pady=(14, 3)
    )


    overall_risk_label = ctk.CTkLabel(
        overall_right,
        text="NO DATA",
        font=(FONT, 22, "bold"),
        text_color=SECONDARY_TEXT
    )

    overall_risk_label.pack()


    # ========================================================
    # LATEST SCAN
    # ========================================================

    latest_card = _make_card(
        content
    )

    latest_card.pack(
        fill="x",
        pady=(0, 16)
    )


    latest_header = ctk.CTkFrame(
        latest_card,
        fg_color="transparent"
    )

    latest_header.pack(
        fill="x",
        padx=20,
        pady=(16, 8)
    )


    _make_section_title(
        latest_header,
        "Latest Security Scan"
    ).pack(
        side="left"
    )


    latest_risk_label = ctk.CTkLabel(
        latest_header,
        text="NO DATA",
        font=(FONT, 11, "bold"),
        text_color=SECONDARY_TEXT,
        fg_color="#EEE7DE",
        corner_radius=8,
        padx=11,
        pady=4
    )

    latest_risk_label.pack(
        side="right"
    )


    latest_info = ctk.CTkFrame(
        latest_card,
        fg_color="#F7F3EC",
        corner_radius=12
    )

    latest_info.pack(
        fill="x",
        padx=20,
        pady=(0, 18)
    )


    latest_labels = {}


    def create_latest_row(
        key,
        label
    ):

        row = ctk.CTkFrame(
            latest_info,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=16,
            pady=6
        )


        ctk.CTkLabel(
            row,
            text=label,
            width=140,
            anchor="w",
            font=(FONT, 12, "bold"),
            text_color=SECONDARY_TEXT
        ).pack(
            side="left"
        )


        value_label = ctk.CTkLabel(
            row,
            text="—",
            anchor="w",
            justify="left",
            wraplength=750,
            font=(FONT, 12),
            text_color=TEXT_COLOR
        )

        value_label.pack(
            side="left",
            fill="x",
            expand=True
        )


        latest_labels[key] = value_label


    create_latest_row(
        "scan_type",
        "Scan Type"
    )


    create_latest_row(
        "target",
        "Target / File"
    )


    create_latest_row(
        "date",
        "Date & Time"
    )


    create_latest_row(
        "score",
        "Security Score"
    )


    # ========================================================
    # QUICK ACTIONS
    # ========================================================

    quick_card = _make_card(
        content
    )

    quick_card.pack(
        fill="x",
        pady=8
    )


    quick_header = ctk.CTkFrame(
        quick_card,
        fg_color="transparent"
    )

    quick_header.pack(
        fill="x",
        padx=20,
        pady=(16, 8)
    )


    _make_section_title(
        quick_header,
        "Quick Actions"
    ).pack(
        side="left"
    )


    ctk.CTkLabel(
        quick_header,
        text="One-click security tools",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
    ).pack(
        side="right",
        pady=(6, 0)
    )


    quick_body = ctk.CTkFrame(
        quick_card,
        fg_color="transparent"
    )

    quick_body.pack(
        fill="x",
        padx=20,
        pady=(0, 18)
    )


    for col in range(2):

        quick_body.grid_columnconfigure(
            col,
            weight=1,
            uniform="quick"
        )


    quick_actions = [
        (
            "🌐",
            "Scan a URL",
            url_scanner_page
        ),
        (
            "🔒",
            "Check Password",
            password_page
        ),
        (
            "📄",
            "Scan a File",
            file_analyzer_page
        ),
        (
            "🚨",
            "Detect Scam",
            scam_detector_page
        ),
    ]


    for i, (
        icon,
        label,
        page_func
    ) in enumerate(
        quick_actions
    ):

        row, col = divmod(
            i,
            2
        )


        btn = ctk.CTkButton(
            quick_body,
            text=f"{icon}  {label}",
            height=52,
            corner_radius=12,
            fg_color="#FBF8F2",
            hover_color=ACCENT_LIGHT,
            text_color=TEXT_COLOR,
            border_width=1,
            border_color="#DED4C6",
            font=(FONT, 14, "bold"),
            anchor="w",
            border_spacing=16,
        )


        btn.grid(
            row=row,
            column=col,
            padx=6,
            pady=6,
            sticky="ew"
        )


        if on_navigate is not None:

            btn.configure(
                command=lambda f=page_func: on_navigate(f)
            )


    # ========================================================
    # RECENT ACTIVITY
    # ========================================================

    activity_card = _make_card(
        content
    )

    activity_card.pack(
        fill="x",
        pady=8
    )


    activity_header = ctk.CTkFrame(
        activity_card,
        fg_color="transparent"
    )

    activity_header.pack(
        fill="x",
        padx=20,
        pady=(16, 8)
    )


    _make_section_title(
        activity_header,
        "Recent Activity"
    ).pack(
        side="left"
    )


    ctk.CTkLabel(
        activity_header,
        text="Latest security scans",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT
    ).pack(
        side="right",
        pady=(6, 0)
    )


    activity_body = ctk.CTkFrame(
        activity_card,
        fg_color="transparent"
    )

    activity_body.pack(
        fill="x"
    )


    # ========================================================
    # SECURITY BREAKDOWN
    # ========================================================

    breakdown_card = _make_card(
        content
    )

    breakdown_card.pack(
        fill="x",
        pady=8
    )


    breakdown_header = ctk.CTkFrame(
        breakdown_card,
        fg_color="transparent"
    )

    breakdown_header.pack(
        fill="x",
        padx=20,
        pady=(16, 8)
    )


    _make_section_title(
        breakdown_header,
        "Security Breakdown"
    ).pack(
        side="left"
    )


    ctk.CTkLabel(
        breakdown_header,
        text="Current report distribution",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT
    ).pack(
        side="right",
        pady=(6, 0)
    )


    breakdown_body = ctk.CTkFrame(
        breakdown_card,
        fg_color="transparent"
    )

    breakdown_body.pack(
        fill="x",
        padx=20,
        pady=(0, 10)
    )


    # ========================================================
    # VOICE + DAILY TIP
    # ========================================================

    bottom = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    bottom.pack(
        fill="x",
        pady=8
    )


    bottom.grid_columnconfigure(
        0,
        weight=1,
        uniform="bottom"
    )

    bottom.grid_columnconfigure(
        1,
        weight=1,
        uniform="bottom"
    )

    bottom.grid_rowconfigure(
        0,
        weight=1
    )


    # ========================================================
    # VOICE COMPANION
    # ========================================================

    voice_card = _make_card(
        bottom
    )

    voice_card.grid(
        row=0,
        column=0,
        padx=(0, 6),
        pady=4,
        sticky="nsew"
    )


    voice_inner = ctk.CTkFrame(
        voice_card,
        fg_color="transparent"
    )

    voice_inner.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=18
    )


    ctk.CTkLabel(
        voice_inner,
        text="🎙",
        font=(FONT_EMOJI, 34),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )


    ctk.CTkLabel(
        voice_inner,
        text="AI Voice Companion",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w",
        pady=(10, 4)
    )


    ctk.CTkLabel(
        voice_inner,
        text=(
            "Talk to CyberGuard AI and get instant, "
            "hands-free answers to your security questions."
        ),
        font=(FONT, 13),
        text_color=SECONDARY_TEXT,
        justify="left",
        wraplength=340,
    ).pack(
        anchor="w"
    )


    voice_btn = ctk.CTkButton(
        voice_inner,
        text="🎤  Open Voice Companion",
        height=42,
        corner_radius=10,
        fg_color=ACCENT_COLOR,
        hover_color=ACCENT_HOVER,
        text_color="#FFFFFF",
        font=(FONT, 13, "bold"),
    )

    voice_btn.pack(
        anchor="w",
        pady=(16, 0)
    )


    if on_navigate is not None:

        voice_btn.configure(
            command=lambda: on_navigate(
                voice_companion_page
            )
        )


    # ========================================================
    # DAILY TIP
    # ========================================================

    tip_card = _make_card(
        bottom
    )

    tip_card.grid(
        row=0,
        column=1,
        padx=(6, 0),
        pady=4,
        sticky="nsew"
    )


    tip_inner = ctk.CTkFrame(
        tip_card,
        fg_color="transparent"
    )

    tip_inner.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=18
    )


    ctk.CTkLabel(
        tip_inner,
        text="💡  Daily Cyber Tip",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )


    tip_text = ctk.CTkLabel(
        tip_inner,
        text=DAILY_TIPS[0],
        font=(FONT, 13),
        text_color=SECONDARY_TEXT,
        justify="left",
        wraplength=340,
    )

    tip_text.pack(
        anchor="w",
        pady=(10, 0)
    )


    tip_index = {
        "value": 0
    }


    def next_tip():

        tip_index["value"] = (
            tip_index["value"] + 1
        ) % len(
            DAILY_TIPS
        )

        tip_text.configure(
            text=DAILY_TIPS[
                tip_index["value"]
            ]
        )


    ctk.CTkButton(
        tip_inner,
        text="Next Tip  →",
        width=110,
        height=34,
        corner_radius=9,
        fg_color=CARD_COLOR,
        hover_color="#F0EBE2",
        border_width=1,
        border_color="#D0C8BC",
        text_color=TEXT_COLOR,
        font=(FONT, 12, "bold"),
        command=next_tip,
    ).pack(
        anchor="w",
        pady=(14, 0)
    )


    # ========================================================
    # DASHBOARD REFRESH FUNCTION
    # ========================================================

    def refresh_dashboard():

        # ----------------------------------------------------
        # Reload reports from disk
        # ----------------------------------------------------

        current_reports = get_all_reports()

        if not isinstance(
            current_reports,
            list
        ):
            current_reports = []


        # ----------------------------------------------------
        # Recalculate statistics
        # ----------------------------------------------------

        total = len(
            current_reports
        )

        safe = 0
        low = 0
        medium = 0
        high = 0
        critical = 0

        for report in current_reports:

            risk = str(
                report.get(
                    "risk",
                    ""
                )
            ).upper()

            if risk == "SAFE":
                safe += 1

            elif risk == "LOW":
                low += 1

            elif risk == "MEDIUM":
                medium += 1

            elif risk == "HIGH":
                high += 1

            elif risk == "CRITICAL":
                critical += 1


        threats = (
            medium
            + high
            + critical
        )


        score = _calculate_overall_score(
            current_reports
        )

        risk = _calculate_overall_risk(
            current_reports
        )

        risk_color = _risk_color(
            risk
        )


        # ----------------------------------------------------
        # Update stat cards
        # ----------------------------------------------------

        stats_labels[
            "score"
        ].configure(
            text=f"{score}/100",
            text_color=(
                risk_color
                if current_reports
                else SECONDARY_TEXT
            )
        )


        stats_labels[
            "total"
        ].configure(
            text=str(total)
        )


        stats_labels[
            "threats"
        ].configure(
            text=str(threats),
            text_color=(
                DANGER_COLOR
                if threats > 0
                else SUCCESS_COLOR
            )
        )


        stats_labels[
            "safe"
        ].configure(
            text=str(safe)
        )


        # ----------------------------------------------------
        # Update overall score
        # ----------------------------------------------------

        overall_score_label.configure(
            text=f"{score} / 100",
            text_color=(
                risk_color
                if current_reports
                else SECONDARY_TEXT
            )
        )


        overall_progress.set(
            score / 100
        )


        overall_progress.configure(
            progress_color=(
                risk_color
                if current_reports
                else SUCCESS_COLOR
            )
        )


        overall_risk_label.configure(
            text=risk,
            text_color=(
                risk_color
                if current_reports
                else SECONDARY_TEXT
            )
        )


        # ----------------------------------------------------
        # Update latest scan
        # ----------------------------------------------------

        if current_reports:

            latest = current_reports[-1]

            latest_risk = str(
                latest.get(
                    "risk",
                    "UNKNOWN"
                )
            ).upper()

            latest_color = _risk_color(
                latest_risk
            )


            latest_risk_label.configure(
                text=latest_risk,
                text_color="#FFFFFF",
                fg_color=latest_color
            )


            latest_labels[
                "scan_type"
            ].configure(
                text=latest.get(
                    "scan_type",
                    "Unknown"
                )
            )


            latest_labels[
                "target"
            ].configure(
                text=latest.get(
                    "target",
                    "Unknown"
                )
            )


            latest_labels[
                "date"
            ].configure(
                text=latest.get(
                    "date_time",
                    "Unknown"
                )
            )


            latest_labels[
                "score"
            ].configure(
                text=f"{latest.get('score', 0)}/100",
                text_color=latest_color
            )

        else:

            latest_risk_label.configure(
                text="NO DATA",
                text_color=SECONDARY_TEXT,
                fg_color="#EEE7DE"
            )


            latest_labels[
                "scan_type"
            ].configure(
                text="—"
            )


            latest_labels[
                "target"
            ].configure(
                text="—"
            )


            latest_labels[
                "date"
            ].configure(
                text="—"
            )


            latest_labels[
                "score"
            ].configure(
                text="—",
                text_color=SECONDARY_TEXT
            )


        # ----------------------------------------------------
        # Update recent activity
        # ----------------------------------------------------

        for child in activity_body.winfo_children():
            child.destroy()


        if current_reports:

            recent_reports = list(
                reversed(
                    current_reports
                )
            )[:5]


            for report in recent_reports:

                scan_type = str(
                    report.get(
                        "scan_type",
                        "Security Scan"
                    )
                )

                target = str(
                    report.get(
                        "target",
                        "Unknown"
                    )
                )

                scan_risk = str(
                    report.get(
                        "risk",
                        "UNKNOWN"
                    )
                ).upper()

                date_time = str(
                    report.get(
                        "date_time",
                        ""
                    )
                )


                icon_map = {

                    "File Analyzer": "📄",

                    "Scam Detector": "🚨",

                    "URL Analyzer": "🌐",

                    "Password Analyzer": "🔐",

                    "Email Analyzer": "📧"
                }


                icon = icon_map.get(
                    scan_type,
                    "🛡"
                )


                row = ctk.CTkFrame(
                    activity_body,
                    fg_color="transparent"
                )

                row.pack(
                    fill="x",
                    padx=20,
                    pady=5
                )


                safe_state = scan_risk in (
                    "SAFE",
                    "LOW"
                )


                status_color = (
                    SUCCESS_COLOR
                    if safe_state
                    else DANGER_COLOR
                )


                status_bg = (
                    SUCCESS_BG
                    if safe_state
                    else DANGER_BG
                )


                ctk.CTkLabel(
                    row,
                    text=scan_risk,
                    font=(FONT, 11, "bold"),
                    text_color=status_color,
                    fg_color=status_bg,
                    corner_radius=8,
                    padx=10,
                    pady=3,
                ).pack(
                    side="right"
                )


                ctk.CTkLabel(
                    row,
                    text=date_time,
                    font=(FONT, 10),
                    text_color=SECONDARY_TEXT,
                    width=115,
                    anchor="e"
                ).pack(
                    side="right",
                    padx=(8, 0)
                )


                ctk.CTkLabel(
                    row,
                    text=f"{scan_type}: {target}",
                    font=(FONT, 13),
                    text_color=TEXT_COLOR,
                    anchor="w",
                    justify="left",
                    wraplength=700
                ).pack(
                    side="left",
                    padx=(8, 0),
                    fill="x",
                    expand=True
                )


                ctk.CTkLabel(
                    row,
                    text=icon,
                    font=(FONT_EMOJI, 16),
                    text_color=TEXT_COLOR,
                ).pack(
                    side="left",
                    padx=(0, 4),
                    pady=6
                )

        else:

            empty = ctk.CTkFrame(
                activity_body,
                fg_color="#F7F3EC",
                corner_radius=12
            )

            empty.pack(
                fill="x",
                padx=20,
                pady=(0, 15)
            )


            ctk.CTkLabel(
                empty,
                text="📭  No security scans yet.",
                font=(FONT, 14, "bold"),
                text_color=TEXT_COLOR
            ).pack(
                pady=(20, 4)
            )


            ctk.CTkLabel(
                empty,
                text="Start your first security analysis.",
                font=(FONT, 12),
                text_color=SECONDARY_TEXT
            ).pack(
                pady=(0, 20)
            )


        # ----------------------------------------------------
        # Update security breakdown
        # ----------------------------------------------------

        for child in breakdown_body.winfo_children():
            child.destroy()


        breakdown = [
            (
                "SAFE",
                safe,
                SUCCESS_COLOR
            ),
            (
                "LOW",
                low,
                LOW_COLOR
            ),
            (
                "MEDIUM",
                medium,
                WARNING_COLOR
            ),
            (
                "HIGH",
                high,
                HIGH_COLOR
            ),
            (
                "CRITICAL",
                critical,
                CRITICAL_COLOR
            )
        ]


        for risk_name, count, color in breakdown:

            row = ctk.CTkFrame(
                breakdown_body,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                pady=4
            )


            ctk.CTkLabel(
                row,
                text=risk_name,
                width=90,
                anchor="w",
                font=(FONT, 12, "bold"),
                text_color=color
            ).pack(
                side="left"
            )


            bar = ctk.CTkProgressBar(
                row,
                height=10,
                corner_radius=5,
                fg_color="#E8E1D5",
                progress_color=color
            )


            if total > 0:

                percentage = count / total

            else:

                percentage = 0


            bar.set(
                percentage
            )


            bar.pack(
                side="left",
                fill="x",
                expand=True,
                padx=10
            )


            ctk.CTkLabel(
                row,
                text=str(count),
                width=40,
                anchor="e",
                font=(FONT, 12, "bold"),
                text_color=TEXT_COLOR
            ).pack(
                side="right"
            )


        # ----------------------------------------------------
        # Timestamp
        # ----------------------------------------------------

        from datetime import datetime

        now = datetime.now().strftime(
            "%I:%M:%S %p"
        )

        last_refresh_label.configure(
            text=f"Last refreshed: {now}"
        )


    # ========================================================
    # CONNECT REFRESH BUTTON
    # ========================================================

    refresh_button.configure(
        command=refresh_dashboard
    )


    # ========================================================
    # INITIAL LOAD
    # ========================================================

    refresh_dashboard()


    # ========================================================
    # AUTO REFRESH
    # Every 5 seconds
    # ========================================================

    def auto_refresh():

        try:

            if dashboard.winfo_exists():

                refresh_dashboard()

                dashboard.after(
                    5000,
                    auto_refresh
                )

        except Exception:

            pass


    dashboard.after(
        5000,
        auto_refresh
    )


    return dashboard