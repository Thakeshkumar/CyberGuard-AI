import customtkinter as ctk


def settings_page(parent):

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        page,
        text="⚙ Settings",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(pady=(30, 10))

    subtitle = ctk.CTkLabel(
        page,
        text="Manage your CyberGuard AI preferences",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=(0, 25))

    settings_frame = ctk.CTkFrame(
        page,
        fg_color="transparent"
    )
    settings_frame.pack(
        fill="both",
        expand=True,
        padx=30
    )

    settings = [
        ("👤", "Profile", "Manage your personal information"),
        ("🔐", "Change Password", "Update your account password"),
        ("🌙", "Theme", "Change application appearance"),
        ("🔔", "Notifications", "Manage notification preferences"),
        ("🌐", "Language", "Choose your preferred language"),
        ("ℹ️", "About", "About CyberGuard AI"),
    ]

    for icon, title_text, description in settings:

        card = ctk.CTkFrame(
            settings_frame,
            fg_color="#FFFDF9",
            corner_radius=12
        )
        card.pack(
            fill="x",
            pady=6
        )

        text_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )
        text_frame.pack(
            side="left",
            padx=20,
            pady=15
        )

        ctk.CTkLabel(
            text_frame,
            text=f"{icon}  {title_text}",
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            text_frame,
            text=description,
            font=("Segoe UI", 13)
        ).pack(anchor="w", pady=(3, 0))

        button = ctk.CTkButton(
            card,
            text="Open",
            width=90,
            height=35,
            corner_radius=8
        )
        button.pack(
            side="right",
            padx=20
        )

    # Logout
    logout_button = ctk.CTkButton(
        page,
        text="🚪  Logout",
        width=180,
        height=45,
        corner_radius=10,
        fg_color="#C0392B",
        hover_color="#E74C3C"
    )
    logout_button.pack(
        pady=25
    )

    return page