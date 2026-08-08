from email import header

import customtkinter as ctk


def dashboard_page(parent):

    dashboard = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    dashboard.pack(fill="both", expand=True)

# =========================
# DASHBOARD HEADER
# =========================

    header = ctk.CTkFrame(
    dashboard,
    fg_color="#FFFDF9",
    corner_radius=18,
    border_width=1,
    border_color="#D8CFC2"
    )

    header.pack(
    fill="x",
    padx=25,
    pady=(20, 15)
    )

    welcome = ctk.CTkLabel(
    header,
    text="👋 Hi Thakesh!",
    font=("Arial", 24, "bold"),
    text_color="#3E332B"
    )

    welcome.pack(
    anchor="w",
    padx=25,
    pady=(18, 2)
    )

    subtitle = ctk.CTkLabel(
    header,
    text="Your Personal AI Cyber Security Companion",
    font=("Arial", 14),
    text_color="#75685D"
    )

    subtitle.pack(
    anchor="w",
    padx=25,
    pady=(0, 18)
    )

# =========================
# SECURITY STAT CARDS
# =========================

    stats_frame = ctk.CTkFrame(
    dashboard,
    fg_color="transparent"
    )

    stats_frame.pack(
    fill="x",
    padx=25,
    pady=10
    )

# Card 1
    score_card = ctk.CTkFrame(
    stats_frame,
    fg_color="#FFFDF9",
    corner_radius=15,
    border_width=1,
    border_color="#D8CFC2"
    )

    score_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=6
    )

    ctk.CTkLabel(
    score_card,
    text="🛡 Overall Security Score",
    font=("Arial", 14, "bold"),
    text_color="#3E332B"
    ).pack(pady=(18, 5))

    ctk.CTkLabel(
    score_card,
    text="82 /100",
    font=("Arial", 25, "bold"),
    text_color="#5A9B7A"
    ).pack()

    ctk.CTkLabel(
    score_card,
    text="Good",
    font=("Arial", 13),
    text_color="#5A9B7A"
    ).pack(pady=(0, 18))


# Card 2
    scans_card = ctk.CTkFrame(
    stats_frame,
    fg_color="#FFFDF9",
    corner_radius=15,
    border_width=1,
    border_color="#D8CFC2"
    )

    scans_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=6
    )

    ctk.CTkLabel(
    scans_card,
    text="▣ Total Scans",
    font=("Arial", 14, "bold"),
    text_color="#3E332B"
    ).pack(pady=(18, 5))

    ctk.CTkLabel(
    scans_card,
    text="128",
    font=("Arial", 25, "bold"),
    text_color="#3E332B"
    ).pack()

    ctk.CTkLabel(
    scans_card,
    text="This Month",
    font=("Arial", 13),
    text_color="#75685D"
    ).pack(pady=(0, 18))


# Card 3
    threat_card = ctk.CTkFrame(
    stats_frame,
    fg_color="#FFFDF9",
    corner_radius=15,
    border_width=1,
    border_color="#D8CFC2"
    )

    threat_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=6
    )

    ctk.CTkLabel(
    threat_card,
    text="⚠ Threats Detected",
    font=("Arial", 14, "bold"),
    text_color="#3E332B"
    ).pack(pady=(18, 5))

    ctk.CTkLabel(
    threat_card,
    text="7",
    font=("Arial", 25, "bold"),
    text_color="#B85C5C"
    ).pack()

    ctk.CTkLabel(
    threat_card,
    text="This Month",
    font=("Arial", 13),
    text_color="#75685D"
    ).pack(pady=(0, 18))


# Card 4
    safe_card = ctk.CTkFrame(
    stats_frame,
    fg_color="#FFFDF9",
    corner_radius=15,
    border_width=1,
    border_color="#D8CFC2"
    )

    safe_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=6
    )

    ctk.CTkLabel(
    safe_card,
    text="✓ Safe Items",
    font=("Arial", 14, "bold"),
    text_color="#3E332B"
    ).pack(pady=(18, 5))

    ctk.CTkLabel(
    safe_card,
    text="121",
    font=("Arial", 25, "bold"),
    text_color="#5A9B7A"
    ).pack()

    ctk.CTkLabel(
    safe_card,
    text="This Month",
    font=("Arial", 13),
    text_color="#75685D"
    ).pack(pady=(0, 18))

# =========================
# QUICK ACTIONS
# =========================

    quick_frame = ctk.CTkFrame(
    dashboard,
    fg_color="#FFFDF9",
    corner_radius=15,
    border_width=1,
    border_color="#D8CFC2"
)

    quick_frame.pack(
    fill="x",
    padx=25,
    pady=(15, 10)
)

    quick_title = ctk.CTkLabel(
    quick_frame,
    text="Quick Actions",
    font=("Arial", 20, "bold"),
    text_color="#3E332B"
)

    quick_title.pack(
    anchor="w",
    padx=20,
    pady=(15, 10)
)

# Buttons container
    button_frame = ctk.CTkFrame(
    quick_frame,
    fg_color="transparent"
)

    button_frame.pack(
    fill="x",
    padx=20,
    pady=(0, 20)
)

# Row 1
    url_button = ctk.CTkButton(
    button_frame,
    text="🌐  Scan a URL",
    height=50,
    corner_radius=10,
    fg_color="#FFFDF9",
    hover_color="#E8D8C8",
    text_color="#3E332B",
    border_width=1,
    border_color="#D8CFC2",
    font=("Arial", 14)
)

    url_button.grid(
    row=0,
    column=0,
    padx=6,
    pady=6,
    sticky="ew"
)


    password_button = ctk.CTkButton(
    button_frame,
    text="🔒  Check Password",
    height=50,
    corner_radius=10,
    fg_color="#FFFDF9",
    hover_color="#E8D8C8",
    text_color="#3E332B",
    border_width=1,
    border_color="#D8CFC2",
    font=("Arial", 14)
)

    password_button.grid(
    row=0,
    column=1,
    padx=6,
    pady=6,
    sticky="ew"
)


# Row 2
    file_button = ctk.CTkButton(
    button_frame,
    text="📄  Scan a File",
    height=50,
    corner_radius=10,
    fg_color="#FFFDF9",
    hover_color="#E8D8C8",
    text_color="#3E332B",
    border_width=1,
    border_color="#D8CFC2",
    font=("Arial", 14)
)

    file_button.grid(
    row=1,
    column=0,
    padx=6,
    pady=6,
    sticky="ew"
)


    scam_button = ctk.CTkButton(
    button_frame,
    text="🛡  Detect Scam",
    height=50,
    corner_radius=10,
    fg_color="#FFFDF9",
    hover_color="#E8D8C8",
    text_color="#3E332B",
    border_width=1,
    border_color="#D8CFC2",
    font=("Arial", 14)
)

    scam_button.grid(
    row=1,
    column=1,
    padx=6,
    pady=6,
    sticky="ew"
)


    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

        # ---------------- RECENT ACTIVITY ----------------

    activity_card = ctk.CTkFrame(
        dashboard,
        fg_color="#FFFDF9",
        corner_radius=15,
        border_width=1,
        border_color="#D8D2C8"
    )
    activity_card.pack(
        fill="x",
        padx=20,
        pady=(15, 10)
    )

    activity_title = ctk.CTkLabel(
        activity_card,
        text="Recent Activity",
        font=("Arial", 18, "bold"),
        text_color="#333333"
    )
    activity_title.pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    activities = [
        ("🌐", "Scanned URL: https://example.com", "Safe"),
        ("🔐", "Checked Password Strength", "Strong"),
        ("📄", "Scanned File: report.pdf", "Safe"),
        ("⚠", "Scam Message Detected", "Threat")
    ]

    for icon, text, status in activities:

        row = ctk.CTkFrame(
            activity_card,
            fg_color="transparent"
        )
        row.pack(
            fill="x",
            padx=20,
            pady=5
        )

        ctk.CTkLabel(
            row,
            text=icon,
            font=("Arial", 17)
        ).pack(side="left", padx=(0, 10))

        ctk.CTkLabel(
            row,
            text=text,
            font=("Arial", 14),
            text_color="#333333"
        ).pack(side="left")

        status_color = "#2E9B57" if status in ["Safe", "Strong"] else "#C94C4C"

        ctk.CTkLabel(
            row,
            text=status,
            font=("Arial", 14, "bold"),
            text_color=status_color
        ).pack(side="right")

        # ---------------- AI VOICE COMPANION ----------------

    voice_card = ctk.CTkFrame(
        dashboard,
        fg_color="#FFFDF9",
        corner_radius=15,
        border_width=1,
        border_color="#D8D2C8"
    )
    voice_card.pack(
        fill="x",
        padx=20,
        pady=10
    )

    ctk.CTkLabel(
        voice_card,
        text="AI Voice Companion",
        font=("Arial", 18, "bold"),
        text_color="#333333"
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )

    voice_content = ctk.CTkFrame(
        voice_card,
        fg_color="transparent"
    )
    voice_content.pack(
        fill="x",
        padx=20,
        pady=(5, 18)
    )

    ctk.CTkLabel(
        voice_content,
        text="🎙",
        font=("Arial", 45)
    ).pack(side="left", padx=(20, 30))

    voice_text = ctk.CTkLabel(
        voice_content,
        text="Hey CyberGuard...\nI'm listening. How can I help?",
        font=("Arial", 16),
        text_color="#555555",
        justify="left"
    )
    voice_text.pack(side="left")


    # ---------------- DAILY CYBER TIP ----------------

    tip_card = ctk.CTkFrame(
        dashboard,
        fg_color="#FFFDF9",
        corner_radius=15,
        border_width=1,
        border_color="#D8D2C8"
    )
    tip_card.pack(
        fill="x",
        padx=20,
        pady=10
    )

    ctk.CTkLabel(
        tip_card,
        text="Daily Cyber Tip",
        font=("Arial", 18, "bold"),
        text_color="#333333"
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 8)
    )

    ctk.CTkLabel(
        tip_card,
        text="🛡  Never share your OTP, passwords,\n"
             "     or personal information with anyone,\n"
             "     even if they claim to be from your bank.",
        font=("Arial", 14),
        text_color="#444444",
        justify="left"
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 15)
    )

        # ---------------- NEXT TIP BUTTON ----------------

    next_tip_button = ctk.CTkButton(
        tip_card,
        text="Next Tip  →",
        width=130,
        height=38,
        corner_radius=10,
        fg_color="#FFFFFF",
        hover_color="#F0EBE2",
        border_width=1,
        border_color="#D0C8BC",
        text_color="#333333",
        font=("Arial", 13, "bold")
    )
    next_tip_button.pack(
        anchor="e",
        padx=25,
        pady=(0, 18)
    )

        # ---------------- USER PROFILE ----------------

    profile_frame = ctk.CTkFrame(
        dashboard,
        fg_color="#FFFDF9",
        corner_radius=15,
        border_width=1,
        border_color="#D8D2C8"
    )
    profile_frame.pack(
        anchor="ne",
        padx=20,
        pady=(5, 10)
    )

    ctk.CTkLabel(
        profile_frame,
        text="👤",
        font=("Arial", 20)
    ).pack(side="left", padx=(15, 8), pady=10)

    ctk.CTkLabel(
        profile_frame,
        text="User Profile",
        font=("Arial", 14, "bold"),
        text_color="#333333"
    ).pack(side="left", padx=(0, 15))


    return dashboard