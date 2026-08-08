import customtkinter as ctk


def reports_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="📊 Reports",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(30, 10))

    subtitle = ctk.CTkLabel(
        page,
        text="View and export your CyberGuard AI security reports",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=(0, 25))

    # Report options
    reports_frame = ctk.CTkFrame(
        page,
        fg_color="transparent"
    )
    reports_frame.pack(fill="x", padx=30)

    report_items = [
        ("🛡", "Security Report"),
        ("🌐", "URL Report"),
        ("🔒", "Password Report"),
        ("📧", "Email Report"),
        ("📁", "File Report"),
        ("🚨", "Scam Report"),
    ]

    for icon, name in report_items:

        card = ctk.CTkFrame(
            reports_frame,
            fg_color="#FFFDF9",
            corner_radius=12
        )
        card.pack(fill="x", pady=6)

        label = ctk.CTkLabel(
            card,
            text=f"{icon}  {name}",
            font=("Segoe UI", 16, "bold")
        )
        label.pack(side="left", padx=20, pady=15)

        view_button = ctk.CTkButton(
            card,
            text="View",
            width=100,
            height=35,
            corner_radius=8
        )
        view_button.pack(side="right", padx=20)

    # Export section
    export_frame = ctk.CTkFrame(
        page,
        fg_color="transparent",
        corner_radius=12
    )
    export_frame.pack(fill="x", padx=30, pady=25)

    export_title = ctk.CTkLabel(
        export_frame,
        text="📄 Export Report",
        font=("Segoe UI", 18, "bold")
    )
    export_title.pack(side="left", padx=20, pady=18)

    export_button = ctk.CTkButton(
        export_frame,
        text="Export",
        width=120,
        height=40,
        corner_radius=8
    )
    export_button.pack(side="right", padx=20)

    return page