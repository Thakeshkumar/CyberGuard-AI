import customtkinter as ctk


def password_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="🔒 Password Analyzer",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(40, 15))

    subtitle = ctk.CTkLabel(
        page,
        text="Check the strength and security of a password",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=5)

    password_entry = ctk.CTkEntry(
        page,
        width=500,
        height=45,
        placeholder_text="Enter password...",
        show="*"
    )
    password_entry.pack(pady=25)

    analyze_button = ctk.CTkButton(
        page,
        text="🔍 Analyze Password",
        width=200,
        height=50,
        corner_radius=12
    )
    analyze_button.pack(pady=10)

    return page