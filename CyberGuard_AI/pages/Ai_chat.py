import customtkinter as ctk


def ai_chat_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="🤖 AI Chat",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=30)

    subtitle = ctk.CTkLabel(
        page,
        text="Your CyberGuard AI assistant",
        font=("Segoe UI", 16)
    )
    subtitle.pack()

    return page