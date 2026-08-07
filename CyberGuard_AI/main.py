import customtkinter as ctk
from pages.dashboard import dashboard_page

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CyberGuard AI")
app.geometry("1500x850")
app.configure(fg_color="#976730")

# ---------------- Sidebar ----------------
sidebar = ctk.CTkFrame(
    app,
    width=240,
    corner_radius=0,
    fg_color="#D3BB8E"
)
sidebar.pack(side="left", fill="y")

# ---------------- Main Area ----------------
main = ctk.CTkScrollableFrame(
    app,
    fg_color="#D3BB8E",
    corner_radius=0
)
dashboard = dashboard_page(main)
main.pack(side="right", fill="both", expand=True)

# ---------------- Logo ----------------
logo = ctk.CTkLabel(
    sidebar,
    text="🛡 CyberGuard AI",
    font=("Segoe UI", 26, "bold"),
    text_color="#976730"
)
logo.pack(pady=(30, 20))

# ---------------- Menu ----------------
menus = [
    "Dashboard",
    "AI Chat",
    "Voice Companion",
    "URL Scanner",
    "Password Analyzer",
    "Scam Detector",
    "File Analyzer",
    "Email Analyzer",
    "Reports",
    "Settings"
]

for item in menus:
    btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=240,
        height=45,
        corner_radius=10
    )
    btn.pack(pady=6)

# ---------------- Welcome ----------------
title = ctk.CTkLabel(
    main,
    text="Welcome to CyberGuard AI",
    font=("Segoe UI", 34, "bold"),
    text_color="#976730"
)
title.pack(pady=50)

# ===================== TOP HEADER =====================

header = ctk.CTkFrame(
    main,
    height=90,
    fg_color="#663D27",
    corner_radius=15
)
header.pack(fill="x", padx=20, pady=20)
header.pack_propagate(False)

# Left Side
left_frame = ctk.CTkFrame(header, fg_color="transparent")
left_frame.pack(side="left", padx=20)

title = ctk.CTkLabel(
    left_frame,
    text="👋 Hi Thakesh!",
    font=("Segoe UI", 24, "bold"),
    text_color="White"
)
title.pack(anchor="w")

subtitle = ctk.CTkLabel(
    left_frame,
    text="Your Personal AI Cyber Security Companion",
    font=("Segoe UI", 13),
    text_color="#181615"
)
subtitle.pack(anchor="w")

# Right Side
right_frame = ctk.CTkFrame(header, fg_color="transparent")
right_frame.pack(side="right", padx=20)

notify = ctk.CTkButton(
    right_frame,
    text="🔔",
    width=45,
    height=45,
    corner_radius=12
)
notify.pack(side="left", padx=10)

profile = ctk.CTkButton(
    right_frame,
    text="👤 Thakesh",
    width=130,
    height=45,
    corner_radius=12
)
profile.pack(side="left")

# ===================== DASHBOARD CARDS =====================

cards_frame = ctk.CTkFrame(
    main,
    fg_color="transparent"
)
cards_frame.pack(fill="x", padx=20, pady=10)

card_titles = [
    ("🛡 Security Score", "95%"),
    ("📊 Total Scans", "0"),
    ("⚠ Threats Found", "0"),
    ("✅ Safe Files", "0")
]

for title, value in card_titles:

    card = ctk.CTkFrame(
        cards_frame,
        width=250,
        height=140,
        corner_radius=18,
        fg_color="#6E4021"
    )

    card.pack(side="left", padx=10)
    card.pack_propagate(False)

    lbl1 = ctk.CTkLabel(
        card,
        text=title,
        font=("Segoe UI",16,"bold")
    )

    lbl1.pack(pady=(25,10))

    lbl2 = ctk.CTkLabel(
        card,
        text=value,
        font=("Segoe UI",28,"bold"),
        text_color="#DFBC88"
    )

    lbl2.pack()

# ---------------- Quick Actions ----------------
quick_frame = ctk.CTkFrame(
    main,
    fg_color="#4D3221",
    corner_radius=15
)
quick_frame.pack(fill="x", padx=20, pady=15)

quick_title = ctk.CTkLabel(
    quick_frame,
    text="Quick Actions",
    font=("Segoe UI", 20, "bold")
)
quick_title.pack(anchor="w", padx=20, pady=(15, 10))

buttons_frame = ctk.CTkFrame(
    quick_frame,
    fg_color="transparent"
)
buttons_frame.pack(padx=20, pady=(0,20))

btn1 = ctk.CTkButton(buttons_frame, text="🌐 Scan URL", width=180, height=55)
btn2 = ctk.CTkButton(buttons_frame, text="🔒 Password", width=180, height=55)
btn3 = ctk.CTkButton(buttons_frame, text="📄 Scan File", width=180, height=55)
btn4 = ctk.CTkButton(buttons_frame, text="⚠ Detect Scam", width=180, height=55)

btn1.grid(row=0, column=0, padx=10, pady=10)
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3.grid(row=1, column=0, padx=10, pady=10)
btn4.grid(row=1, column=1, padx=10, pady=10)

# ---------------- AI Voice Companion ----------------

voice_frame = ctk.CTkFrame(
    main,
    fg_color="#683B29",
    corner_radius=15
)
voice_frame.pack(fill="x", padx=20, pady=15)

voice_title = ctk.CTkLabel(
    voice_frame,
    text="AI Voice Companion",
    font=("Segoe UI", 20, "bold")
)
voice_title.pack(anchor="w", padx=20, pady=(15,10))

mic_label = ctk.CTkLabel(
    voice_frame,
    text="🎤",
    font=("Segoe UI Emoji", 60)
)
mic_label.pack(pady=(10,5))

status_label = ctk.CTkLabel(
    voice_frame,
    text="Hey CyberGuard...\nI'm listening. How can I help?",
    font=("Segoe UI",16),
    justify="center"
)
status_label.pack(pady=(0,15))

wave = ctk.CTkProgressBar(
    voice_frame,
    width=500
)
wave.pack(pady=(0,20))

wave.set(0.65)

# ---------------- Recent Activity ----------------

activity_frame = ctk.CTkFrame(
    main,
    fg_color="#351F16",
    corner_radius=15
)
activity_frame.pack(fill="x", padx=20, pady=15)

activity_title = ctk.CTkLabel(
    activity_frame,
    text="Recent Activity",
    font=("Segoe UI", 20, "bold")
)
activity_title.pack(anchor="w", padx=20, pady=(15,10))

activities = [
    ("🌐", "Scanned URL : https://example.com", "SAFE"),
    ("🔑", "Password Strength Checked", "STRONG"),
    ("📄", "File Scanned : report.pdf", "SAFE"),
    ("⚠", "Scam Message Detected", "THREAT")
]

for icon, text, status in activities:

    row = ctk.CTkFrame(
        activity_frame,
        fg_color="transparent"
    )
    row.pack(fill="x", padx=20, pady=5)

    ctk.CTkLabel(
        row,
        text=f"{icon}  {text}",
        font=("Segoe UI",14)
    ).pack(side="left")

    color = "#00FF88"

    if status == "THREAT":
        color = "#FF5555"

    ctk.CTkLabel(
        row,
        text=status,
        text_color=color,
        font=("Segoe UI",14,"bold")
    ).pack(side="right")




app.mainloop()