import customtkinter as ctk

# Page functions used by Quick Actions / Voice Companion (navigation is handled by main.py)
from pages.url_scanner import url_scanner_page
from pages.password import password_page
from pages.file_analyzer import file_analyzer_page
from pages.scam_detector import scam_detector_page
from pages.voice_companion import voice_companion_page

# =========================
# CYBERGUARD AI THEME
# =========================

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

FONT = "Segoe UI"
FONT_EMOJI = "Segoe UI Emoji"

DAILY_TIPS = [
    "Never share your OTP, passwords, or personal information with anyone — even if they claim to be from your bank.",
    "Use a unique, strong password for every account and enable two-factor authentication (2FA) wherever possible.",
    "Beware of urgent messages asking for money or credentials — always verify the sender through an official channel.",
    "Keep your software, browsers, and antivirus up to date to stay protected against known vulnerabilities.",
]


def _make_card(parent, corner_radius=16):
    """Helper to create a consistent modern rounded card."""
    return ctk.CTkFrame(
        parent,
        fg_color=CARD_COLOR,
        corner_radius=corner_radius,
        border_width=1,
        border_color=BORDER_COLOR,
    )


def _make_section_title(parent, text):
    """Helper for consistent section titles inside cards."""
    return ctk.CTkLabel(
        parent,
        text=text,
        font=(FONT, 18, "bold"),
        text_color=TEXT_COLOR,
    )


def dashboard_page(parent, on_navigate=None):
    """Modern CyberGuard AI dashboard.

    Creates EXACTLY ONE dashboard frame, packs it into `parent`, and returns it.

    Args:
        parent: The parent container (main.py's CTkScrollableFrame).
        on_navigate: Optional callback provided by main.py's show_page() so
                     Quick Actions / Voice Companion buttons can switch pages
                     through the existing navigation system.
    """

    # ---------------- ROOT DASHBOARD FRAME (EXACTLY ONE) ----------------
    dashboard = ctk.CTkFrame(parent, fg_color="transparent")
    dashboard.pack(fill="both", expand=True)

    # Content wrapper for consistent internal spacing
    content = ctk.CTkFrame(dashboard, fg_color="transparent")
    content.pack(fill="both", expand=True, padx=22, pady=18)

    # =========================
    # 1. WELCOME HEADER
    # =========================

    header = _make_card(content, corner_radius=18)
    header.pack(fill="x")

    header_inner = ctk.CTkFrame(header, fg_color="transparent")
    header_inner.pack(fill="x", padx=24, pady=20)

    header_top = ctk.CTkFrame(header_inner, fg_color="transparent")
    header_top.pack(fill="x")

    # Profile chip (right side, preserves the user-profile element)
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
    profile_chip.pack(side="right")

    # Status badge (right side, to the left of profile)
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
    status_badge.pack(side="right", padx=(0, 12))

    # Welcome text (left side)
    welcome = ctk.CTkLabel(
        header_top,
        text="👋  Welcome back, Thakesh!",
        font=(FONT, 26, "bold"),
        text_color=TEXT_COLOR,
    )
    welcome.pack(side="left")

    subtitle = ctk.CTkLabel(
        header_inner,
        text="Your AI-powered cybersecurity companion — scan URLs, analyze passwords, files, emails, and more.",
        font=(FONT, 14),
        text_color=SECONDARY_TEXT,
    )
    subtitle.pack(anchor="w", pady=(12, 0))

    # =========================
    # 2. SECURITY STATISTICS
    # =========================

    stats = ctk.CTkFrame(content, fg_color="transparent")
    stats.pack(fill="x", pady=(18, 8))

    for col in range(4):
        stats.grid_columnconfigure(col, weight=1, uniform="stats")
    stats.grid_rowconfigure(0, weight=1)

    stats_data = [
        ("🛡", "Security Score", "82/100", SUCCESS_COLOR, "Good"),
        ("▣", "Total Scans", "128", TEXT_COLOR, "This Month"),
        ("⚠", "Threats Detected", "7", DANGER_COLOR, "This Month"),
        ("✓", "Safe Items", "121", SUCCESS_COLOR, "This Month"),
    ]

    for col, (icon, title, value, value_color, caption) in enumerate(stats_data):

        card = _make_card(stats)
        card.grid(row=0, column=col, padx=5, pady=4, sticky="nsew")

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=16)

        ctk.CTkLabel(
            inner,
            text=icon,
            font=(FONT_EMOJI, 22),
            text_color=TEXT_COLOR,
        ).pack(anchor="w")

        ctk.CTkLabel(
            inner,
            text=title,
            font=(FONT, 13, "bold"),
            text_color=SECONDARY_TEXT,
        ).pack(anchor="w", pady=(10, 2))

        ctk.CTkLabel(
            inner,
            text=value,
            font=(FONT, 28, "bold"),
            text_color=value_color,
        ).pack(anchor="w")

        ctk.CTkLabel(
            inner,
            text=caption,
            font=(FONT, 12),
            text_color=SECONDARY_TEXT,
        ).pack(anchor="w", pady=(2, 0))

    # =========================
    # 3. QUICK ACTIONS
    # =========================

    quick_card = _make_card(content)
    quick_card.pack(fill="x", pady=8)

    quick_header = ctk.CTkFrame(quick_card, fg_color="transparent")
    quick_header.pack(fill="x", padx=20, pady=(16, 8))

    _make_section_title(quick_header, "Quick Actions").pack(side="left")

    ctk.CTkLabel(
        quick_header,
        text="One-click security tools",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
    ).pack(side="right", pady=(6, 0))

    quick_body = ctk.CTkFrame(quick_card, fg_color="transparent")
    quick_body.pack(fill="x", padx=20, pady=(0, 18))

    for col in range(2):
        quick_body.grid_columnconfigure(col, weight=1, uniform="quick")

    quick_actions = [
        ("🌐", "Scan a URL", url_scanner_page),
        ("🔒", "Check Password", password_page),
        ("📄", "Scan a File", file_analyzer_page),
        ("🚨", "Detect Scam", scam_detector_page),
    ]

    for i, (icon, label, page_func) in enumerate(quick_actions):

        row, col = divmod(i, 2)

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
        btn.grid(row=row, column=col, padx=6, pady=6, sticky="ew")

        if on_navigate is not None:
            btn.configure(command=lambda f=page_func: on_navigate(f))

    # =========================
    # 4. RECENT ACTIVITY
    # =========================

    activity_card = _make_card(content)
    activity_card.pack(fill="x", pady=8)

    activity_header = ctk.CTkFrame(activity_card, fg_color="transparent")
    activity_header.pack(fill="x", padx=20, pady=(16, 8))

    _make_section_title(activity_header, "Recent Activity").pack(side="left")

    activities = [
        ("🌐", "Scanned URL: https://example.com", "Safe"),
        ("🔐", "Checked Password Strength", "Strong"),
        ("📄", "Scanned File: report.pdf", "Safe"),
        ("⚠", "Scam Message Detected", "Threat"),
    ]

    for icon, text, status in activities:

        row = ctk.CTkFrame(activity_card, fg_color="transparent")
        row.pack(fill="x", padx=20, pady=5)

        is_safe = status in ("Safe", "Strong")
        status_color = SUCCESS_COLOR if is_safe else DANGER_COLOR
        status_bg = SUCCESS_BG if is_safe else DANGER_BG

        ctk.CTkLabel(
            row,
            text=status,
            font=(FONT, 12, "bold"),
            text_color=status_color,
            fg_color=status_bg,
            corner_radius=8,
            padx=10,
            pady=3,
        ).pack(side="right")

        ctk.CTkLabel(
            row,
            text=text,
            font=(FONT, 14),
            text_color=TEXT_COLOR,
        ).pack(side="left", padx=(8, 0))

        ctk.CTkLabel(
            row,
            text=icon,
            font=(FONT_EMOJI, 16),
            text_color=TEXT_COLOR,
        ).pack(side="left", padx=(0, 4), pady=6)

    # Bottom padding for the activity card content
    ctk.CTkFrame(activity_card, fg_color="transparent", height=8).pack(fill="x")

    # =========================
    # 5. BOTTOM ROW: VOICE COMPANION + DAILY TIP
    # =========================

    bottom = ctk.CTkFrame(content, fg_color="transparent")
    bottom.pack(fill="x", pady=8)

    bottom.grid_columnconfigure(0, weight=1, uniform="bottom")
    bottom.grid_columnconfigure(1, weight=1, uniform="bottom")
    bottom.grid_rowconfigure(0, weight=1)

    # ----- AI VOICE COMPANION CARD -----
    voice_card = _make_card(bottom)
    voice_card.grid(row=0, column=0, padx=(0, 6), pady=4, sticky="nsew")

    voice_inner = ctk.CTkFrame(voice_card, fg_color="transparent")
    voice_inner.pack(fill="both", expand=True, padx=20, pady=18)

    ctk.CTkLabel(
        voice_inner,
        text="🎙",
        font=(FONT_EMOJI, 34),
        text_color=TEXT_COLOR,
    ).pack(anchor="w")

    ctk.CTkLabel(
        voice_inner,
        text="AI Voice Companion",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w", pady=(10, 4))

    ctk.CTkLabel(
        voice_inner,
        text="Talk to CyberGuard AI and get instant, hands-free answers to your security questions.",
        font=(FONT, 13),
        text_color=SECONDARY_TEXT,
        justify="left",
        wraplength=340,
    ).pack(anchor="w")

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
    voice_btn.pack(anchor="w", pady=(16, 0))

    if on_navigate is not None:
        voice_btn.configure(command=lambda: on_navigate(voice_companion_page))

    # ----- DAILY CYBER TIP CARD -----
    tip_card = _make_card(bottom)
    tip_card.grid(row=0, column=1, padx=(6, 0), pady=4, sticky="nsew")

    tip_inner = ctk.CTkFrame(tip_card, fg_color="transparent")
    tip_inner.pack(fill="both", expand=True, padx=20, pady=18)

    ctk.CTkLabel(
        tip_inner,
        text="💡  Daily Cyber Tip",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(anchor="w")

    tip_text = ctk.CTkLabel(
        tip_inner,
        text=DAILY_TIPS[0],
        font=(FONT, 13),
        text_color=SECONDARY_TEXT,
        justify="left",
        wraplength=340,
    )
    tip_text.pack(anchor="w", pady=(10, 0))

    tip_index = {"value": 0}

    def next_tip():
        tip_index["value"] = (tip_index["value"] + 1) % len(DAILY_TIPS)
        tip_text.configure(text=DAILY_TIPS[tip_index["value"]])

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
    ).pack(anchor="w", pady=(14, 0))

    return dashboard