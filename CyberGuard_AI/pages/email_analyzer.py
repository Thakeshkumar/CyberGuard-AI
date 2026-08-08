import customtkinter as ctk


def email_analyzer_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="📧 Email Analyzer",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(40, 15))

    subtitle = ctk.CTkLabel(
        page,
        text="Analyze an email for suspicious content and security risks",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=5)

    email_entry = ctk.CTkTextbox(
        page,
        width=600,
        height=250
    )
    email_entry.pack(pady=25)

    email_entry.insert(
        "1.0",
        "Paste email content here..."
    )

    analyze_button = ctk.CTkButton(
        page,
        text="🔍 Analyze Email",
        width=200,
        height=50,
        corner_radius=12
    )
    analyze_button.pack(pady=10)

    return page