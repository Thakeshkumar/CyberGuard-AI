import customtkinter as ctk


def file_analyzer_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="📁 File Analyzer",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(40, 15))

    subtitle = ctk.CTkLabel(
        page,
        text="Analyze files for suspicious content and security risks",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=5)

    file_label = ctk.CTkLabel(
        page,
        text="No file selected",
        font=("Segoe UI", 15)
    )
    file_label.pack(pady=20)

    select_button = ctk.CTkButton(
        page,
        text="📂 Select File",
        width=200,
        height=50,
        corner_radius=12
    )
    select_button.pack(pady=10)

    analyze_button = ctk.CTkButton(
        page,
        text="🔍 Analyze File",
        width=200,
        height=50,
        corner_radius=12
    )
    analyze_button.pack(pady=10)

    return page