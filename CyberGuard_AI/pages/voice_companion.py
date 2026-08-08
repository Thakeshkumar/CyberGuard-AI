import customtkinter as ctk


def voice_companion_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="🎤 Voice Companion",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(40, 15))

    mic = ctk.CTkLabel(
        page,
        text="🎤",
        font=("Segoe UI Emoji", 80)
    )
    mic.pack(pady=20)

    status = ctk.CTkLabel(
        page,
        text="I'm ready to help you",
        font=("Segoe UI", 18)
    )
    status.pack(pady=10)

    start_button = ctk.CTkButton(
        page,
        text="Start Listening",
        width=200,
        height=50,
        corner_radius=12
    )
    start_button.pack(pady=25)

    return page