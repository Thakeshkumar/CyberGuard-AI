import customtkinter as ctk
from pages.dashboard import dashboard_page
from pages.Ai_chat import ai_chat_page
from pages.voice_companion import voice_companion_page
from pages.url_scanner import url_scanner_page
from pages.password import password_page
from pages.email_analyzer import email_analyzer_page
from pages.file_analyzer import file_analyzer_page
from pages.scam_detector import scam_detector_page
from pages.reports import reports_page
from pages.history import history_page
from pages.settings import settings_page

# =========================
# CYBERGUARD AI THEME
# =========================

BG_COLOR = "#F7F2E8"
SIDEBAR_COLOR = "#FBF8F2"
CARD_COLOR = "#FFFDF9"
BORDER_COLOR = "#D8CFC2"

TEXT_COLOR = "#3E332B"
SECONDARY_TEXT = "#75685D"

ACCENT_COLOR = "#8B5E3C"
ACCENT_LIGHT = "#E8D8C8"

SUCCESS_COLOR = "#5A9B7A"
DANGER_COLOR = "#B85C5C"

ctk.set_appearance_mode("Light")


app = ctk.CTk()
app.title("CyberGuard AI")
app.geometry("1500x850")
app.configure(bg=BG_COLOR)


# ---------------- Sidebar (EXACTLY ONE) ----------------
sidebar = ctk.CTkFrame(
    app,
    width=240,
    corner_radius=0,
    fg_color="#D3BB8E"
)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# ================= SIDEBAR LOGO =================
logo = ctk.CTkLabel(
    sidebar,
    text="🛡 CyberGuard AI",
    font=("Segoe UI", 22, "bold"),
    text_color="#FFFFFF"
)

logo.pack(
    pady=(28, 25),
    padx=15
)

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="⌂  Dashboard",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(dashboard_page)
)

dashboard_btn.pack(
    padx=15,
    pady=5,
    fill="x"
)

ai_chat_btn = ctk.CTkButton(
    sidebar,
    text="🤖  AI Chat",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(ai_chat_page)
)

ai_chat_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

voice_btn = ctk.CTkButton(
    sidebar,
    text="🎤  Voice Companion",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(voice_companion_page)
)

voice_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

url_btn = ctk.CTkButton(
    sidebar,
    text="🌐  URL Scanner",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(url_scanner_page)
)

url_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

password_btn = ctk.CTkButton(
    sidebar,
    text="🔒  Password Analyzer",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(password_page)
)

password_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

email_btn = ctk.CTkButton(
    sidebar,
    text="📧  Email Analyzer",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(email_analyzer_page)
)

email_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

file_btn = ctk.CTkButton(
    sidebar,
    text="📁  File Analyzer",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(file_analyzer_page)
)

file_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

scam_btn = ctk.CTkButton(
    sidebar,
    text="🚨  Scam Detector",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(scam_detector_page)
)

scam_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

reports_btn = ctk.CTkButton(
    sidebar,
    text="📊  Reports",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(reports_page)
)

reports_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

history_btn = ctk.CTkButton(
    sidebar,
    text="📜  History",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(history_page)
)

history_btn.pack(
    fill="x",
    padx=15,
    pady=5
)

settings_btn = ctk.CTkButton(
    sidebar,
    text="⚙  Settings",
    height=45,
    corner_radius=10,
    anchor="w",
    command=lambda: show_page(settings_page)
)

settings_btn.pack(
    fill="x",
    padx=15,
    pady=5
)


# ---------------- Main Area (EXACTLY ONE) ----------------
main = ctk.CTkScrollableFrame(
    app,
    fg_color=BG_COLOR,
    corner_radius=0
)
main.pack(
    side="left",
    fill="both",
    expand=True
)


current_page = None

def show_page(page_function):
    global current_page

    if current_page is not None:
        current_page.destroy()

    if page_function is dashboard_page:
        current_page = dashboard_page(main, on_navigate=show_page)
    else:
        current_page = page_function(main)

show_page(dashboard_page)


app.mainloop()