import customtkinter as ctk


def scam_detector_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="🚨 Scam Detector",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(40, 15))

    subtitle = ctk.CTkLabel(
        page,
        text="Analyze messages and content for suspicious patterns",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=5)

    scam_entry = ctk.CTkTextbox(
        page,
        width=600,
        height=250
    )
    scam_entry.pack(pady=25)

    analyze_button = ctk.CTkButton(
        page,
        text="🔍 Detect Scam",
        width=200,
        height=50,
        corner_radius=12
    )
    analyze_button.pack(pady=10)

    return page