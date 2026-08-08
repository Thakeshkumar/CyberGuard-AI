import customtkinter as ctk


def history_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="📜 History",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(30, 10))

    subtitle = ctk.CTkLabel(
        page,
        text="View your recent CyberGuard AI activities",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=(0, 25))

    history_frame = ctk.CTkScrollableFrame(
        page,
        fg_color="transparent"
    )
    history_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    activities = [
        ("🌐", "URL Scan", "example.com", "SAFE"),
        ("🔒", "Password Analysis", "Password checked", "STRONG"),
        ("📧", "Email Analysis", "Email checked", "SAFE"),
        ("📁", "File Analysis", "report.pdf", "SAFE"),
        ("🚨", "Scam Detection", "Message analyzed", "THREAT"),
    ]

    for icon, activity, details, status in activities:

        card = ctk.CTkFrame(
            history_frame,
            fg_color="#FFFDF9",
            corner_radius=12
        )
        card.pack(
            fill="x",
            pady=6
        )

        left = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )
        left.pack(
            side="left",
            padx=20,
            pady=12
        )

        ctk.CTkLabel(
            left,
            text=icon,
            font=("Segoe UI Emoji", 22)
        ).pack(side="left", padx=(0, 12))

        text_frame = ctk.CTkFrame(
            left,
            fg_color="transparent"
        )
        text_frame.pack(side="left")

        ctk.CTkLabel(
            text_frame,
            text=activity,
            font=("Segoe UI", 15, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            text_frame,
            text=details,
            font=("Segoe UI", 13)
        ).pack(anchor="w")

        status_color = "#00D084"

        if status == "THREAT":
            status_color = "#FF4D4D"

        ctk.CTkLabel(
            card,
            text=status,
            text_color=status_color,
            font=("Segoe UI", 14, "bold")
        ).pack(
            side="right",
            padx=20
        )

    return page