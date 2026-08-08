import customtkinter as ctk


def url_scanner_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="🌐 URL Scanner",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(40, 15))

    subtitle = ctk.CTkLabel(
        page,
        text="Analyze a website URL for potential security threats",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=5)

    url_entry = ctk.CTkEntry(
        page,
        width=500,
        height=45,
        placeholder_text="Enter website URL..."
    )
    url_entry.pack(pady=25)

    scan_button = ctk.CTkButton(
        page,
        text="🔍 Scan URL",
        width=200,
        height=50,
        corner_radius=12
    )
    scan_button.pack(pady=10)

    return page