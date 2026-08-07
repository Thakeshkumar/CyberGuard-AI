import customtkinter as ctk


def dashboard_page(parent):

    dashboard = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    dashboard.pack(fill="both", expand=True)

    title = ctk.CTkLabel(
        dashboard,
        text="🏠 Dashboard",
        font=("Arial", 30, "bold"),
        text_color="#814B1F"
    )
    title.pack(pady=20)

    return dashboard