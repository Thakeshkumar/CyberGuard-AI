import customtkinter as ctk

from services.report_store import (
    get_all_reports,
    clear_all_reports
)


# ============================================================
# CYBERGUARD AI - SIMPLE SECURITY HISTORY
# History = Past Scan List
# Reports  = Detailed Analytics / Scores
# ============================================================

BG_COLOR = "#F7F2E8"
CARD_COLOR = "#FFFDF9"
BORDER_COLOR = "#D8CFC2"

TEXT_COLOR = "#2E3038"
SECONDARY_TEXT = "#75685D"

ACCENT_COLOR = "#8B5E3C"
ACCENT_HOVER = "#704728"

SUCCESS_COLOR = "#5A9B7A"
LOW_COLOR = "#3A6EA5"
MEDIUM_COLOR = "#C98A2D"
HIGH_COLOR = "#B85C5C"
CRITICAL_COLOR = "#A94442"

FONT = "Segoe UI"


# ============================================================
# RISK COLORS
# ============================================================

RISK_COLORS = {
    "SAFE": SUCCESS_COLOR,
    "LOW": LOW_COLOR,
    "MEDIUM": MEDIUM_COLOR,
    "HIGH": HIGH_COLOR,
    "CRITICAL": CRITICAL_COLOR
}


def get_risk_color(risk):
    return RISK_COLORS.get(
        str(risk).upper(),
        SECONDARY_TEXT
    )


# ============================================================
# HISTORY PAGE
# ============================================================

def history_page(parent):

    # ========================================================
    # MAIN PAGE
    # ========================================================

    page = ctk.CTkFrame(
        parent,
        fg_color=BG_COLOR,
        corner_radius=0
    )

    page.pack(
        fill="both",
        expand=True
    )

    # ========================================================
    # HEADER
    # ========================================================

    header = ctk.CTkFrame(
        page,
        fg_color="transparent"
    )

    header.pack(
        fill="x",
        padx=35,
        pady=(25, 8)
    )

    title_row = ctk.CTkFrame(
        header,
        fg_color="transparent"
    )

    title_row.pack(
        fill="x"
    )

    ctk.CTkLabel(
        title_row,
        text="📜  Security History",
        font=(FONT, 28, "bold"),
        text_color=TEXT_COLOR
    ).pack(
        side="left"
    )

    # Clear history button
    clear_button = ctk.CTkButton(
        title_row,
        text="🗑  Clear History",
        width=135,
        height=38,
        corner_radius=9,
        fg_color="#E8D8C8",
        hover_color="#D9C5B0",
        text_color=TEXT_COLOR,
        font=(FONT, 11, "bold")
    )

    clear_button.pack(
        side="right"
    )

    ctk.CTkLabel(
        header,
        text="A simple timeline of your previous CyberGuard AI security scans.",
        font=(FONT, 13),
        text_color=SECONDARY_TEXT
    ).pack(
        anchor="w",
        pady=(5, 0)
    )

    # ========================================================
    # SEARCH / FILTER CARD
    # ========================================================

    filter_card = ctk.CTkFrame(
        page,
        fg_color=CARD_COLOR,
        corner_radius=16,
        border_width=1,
        border_color=BORDER_COLOR
    )

    filter_card.pack(
        fill="x",
        padx=35,
        pady=(8, 12)
    )

    filter_row = ctk.CTkFrame(
        filter_card,
        fg_color="transparent"
    )

    filter_row.pack(
        fill="x",
        padx=18,
        pady=14
    )

    # Search
    search_entry = ctk.CTkEntry(
        filter_row,
        width=330,
        height=38,
        corner_radius=9,
        placeholder_text="🔎 Search scan type or target...",
        fg_color="#FBF8F2",
        border_color=BORDER_COLOR,
        text_color=TEXT_COLOR,
        font=(FONT, 12)
    )

    search_entry.pack(
        side="left",
        padx=(0, 10)
    )

    # Analyzer filter
    analyzer_filter = ctk.CTkOptionMenu(
        filter_row,
        values=[
            "All",
            "File Analyzer",
            "Scam Detector",
            "URL Analyzer",
            "Password Analyzer",
            "Email Analyzer"
        ],
        width=170,
        height=38,
        corner_radius=9,
        fg_color=ACCENT_COLOR,
        button_color=ACCENT_COLOR,
        button_hover_color=ACCENT_HOVER,
        text_color="#FFFFFF",
        font=(FONT, 11, "bold")
    )

    analyzer_filter.pack(
        side="left",
        padx=5
    )

    # Risk filter
    risk_filter = ctk.CTkOptionMenu(
        filter_row,
        values=[
            "All Risk",
            "SAFE",
            "LOW",
            "MEDIUM",
            "HIGH",
            "CRITICAL"
        ],
        width=130,
        height=38,
        corner_radius=9,
        fg_color="#FBF8F2",
        button_color="#FBF8F2",
        button_hover_color="#F0EBE2",
        text_color=TEXT_COLOR,
        font=(FONT, 11, "bold")
    )

    risk_filter.pack(
        side="left",
        padx=5
    )

    # ========================================================
    # HISTORY TITLE
    # ========================================================

    history_title = ctk.CTkFrame(
        page,
        fg_color="transparent"
    )

    history_title.pack(
        fill="x",
        padx=35,
        pady=(5, 7)
    )

    count_label = ctk.CTkLabel(
        history_title,
        text="Scan History",
        font=(FONT, 18, "bold"),
        text_color=TEXT_COLOR
    )

    count_label.pack(
        side="left"
    )

    # ========================================================
    # SCROLLABLE HISTORY AREA
    # ========================================================

    history_scroll = ctk.CTkFrame(
        page,
        fg_color="transparent",
        corner_radius=0
    )

    history_scroll.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(0, 25)
    )

    # ========================================================
    # LOAD REPORTS
    # ========================================================

    all_reports = get_all_reports()

    if not isinstance(
        all_reports,
        list
    ):
        all_reports = []

    # ========================================================
    # DETAILS POPUP
    # ========================================================

    def show_details(report):

        dialog = ctk.CTkToplevel(
            page
        )

        dialog.title(
            "Security Scan Details"
        )

        dialog.geometry(
            "700x580"
        )

        dialog.configure(
            fg_color=BG_COLOR
        )

        dialog.transient(
            page.winfo_toplevel()
        )

        dialog.grab_set()

        # Header
        ctk.CTkLabel(
            dialog,
            text="🔍  Security Scan Details",
            font=(FONT, 24, "bold"),
            text_color=TEXT_COLOR
        ).pack(
            anchor="w",
            padx=25,
            pady=(22, 5)
        )

        ctk.CTkLabel(
            dialog,
            text="Information from the selected security scan.",
            font=(FONT, 12),
            text_color=SECONDARY_TEXT
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 12)
        )

        # Scroll details
        detail_scroll = ctk.CTkScrollableFrame(
            dialog,
            fg_color="transparent"
        )

        detail_scroll.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        # ====================================================
        # MAIN DETAILS CARD
        # ====================================================

        details_card = ctk.CTkFrame(
            detail_scroll,
            fg_color=CARD_COLOR,
            corner_radius=16,
            border_width=1,
            border_color=BORDER_COLOR
        )

        details_card.pack(
            fill="x",
            pady=5
        )

        risk = str(
            report.get(
                "risk",
                "UNKNOWN"
            )
        ).upper()

        def detail_row(
            label,
            value,
            value_color=TEXT_COLOR
        ):

            row = ctk.CTkFrame(
                details_card,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=18,
                pady=7
            )

            ctk.CTkLabel(
                row,
                text=label,
                width=150,
                anchor="w",
                font=(FONT, 12, "bold"),
                text_color=SECONDARY_TEXT
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                row,
                text=str(value),
                anchor="w",
                justify="left",
                wraplength=450,
                font=(FONT, 12),
                text_color=value_color
            ).pack(
                side="left",
                fill="x",
                expand=True
            )

        detail_row(
            "Scan Type",
            report.get(
                "scan_type",
                "Unknown"
            )
        )

        detail_row(
            "Target / File",
            report.get(
                "target",
                "Unknown"
            )
        )

        detail_row(
            "Date & Time",
            report.get(
                "date_time",
                "Unknown"
            )
        )

        detail_row(
            "Risk Level",
            risk,
            get_risk_color(risk)
        )

        # ====================================================
        # VERDICT CARD
        # ====================================================

        verdict_card = ctk.CTkFrame(
            detail_scroll,
            fg_color=CARD_COLOR,
            corner_radius=16,
            border_width=1,
            border_color=BORDER_COLOR
        )

        verdict_card.pack(
            fill="x",
            pady=8
        )

        ctk.CTkLabel(
            verdict_card,
            text="AI Verdict",
            font=(FONT, 15, "bold"),
            text_color=TEXT_COLOR
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 5)
        )

        ctk.CTkLabel(
            verdict_card,
            text=str(
                report.get(
                    "verdict",
                    "No verdict available."
                )
            ),
            font=(FONT, 12),
            text_color=TEXT_COLOR,
            anchor="w",
            justify="left",
            wraplength=600
        ).pack(
            fill="x",
            padx=18,
            pady=(0, 15)
        )

        # ====================================================
        # RECOMMENDATION CARD
        # ====================================================

        recommendation_card = ctk.CTkFrame(
            detail_scroll,
            fg_color=CARD_COLOR,
            corner_radius=16,
            border_width=1,
            border_color=BORDER_COLOR
        )

        recommendation_card.pack(
            fill="x",
            pady=8
        )

        ctk.CTkLabel(
            recommendation_card,
            text="Security Recommendation",
            font=(FONT, 15, "bold"),
            text_color=TEXT_COLOR
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 5)
        )

        ctk.CTkLabel(
            recommendation_card,
            text=str(
                report.get(
                    "recommendation",
                    "No recommendation available."
                )
            ),
            font=(FONT, 12),
            text_color=SECONDARY_TEXT,
            anchor="w",
            justify="left",
            wraplength=600
        ).pack(
            fill="x",
            padx=18,
            pady=(0, 15)
        )

        # Close
        ctk.CTkButton(
            dialog,
            text="Close",
            width=110,
            height=38,
            corner_radius=9,
            fg_color=ACCENT_COLOR,
            hover_color=ACCENT_HOVER,
            command=dialog.destroy
        ).pack(
            pady=15
        )

    # ========================================================
    # DISPLAY HISTORY
    # ========================================================

    def display_history(*args):

        # Clear old cards
        for child in history_scroll.winfo_children():
            child.destroy()

        query = search_entry.get().strip().lower()

        selected_analyzer = analyzer_filter.get()

        selected_risk = risk_filter.get()

        filtered_reports = []

        # ----------------------------------------------------
        # FILTER
        # ----------------------------------------------------

        for report in all_reports:

            scan_type = str(
                report.get(
                    "scan_type",
                    ""
                )
            )

            target = str(
                report.get(
                    "target",
                    ""
                )
            )

            risk = str(
                report.get(
                    "risk",
                    ""
                )
            ).upper()

            # Search
            searchable = (
                scan_type
                + " "
                + target
            ).lower()

            if query:

                if query not in searchable:
                    continue

            # Analyzer filter
            if selected_analyzer != "All":

                if selected_analyzer.lower() not in scan_type.lower():
                    continue

            # Risk filter
            if selected_risk != "All Risk":

                if risk != selected_risk:
                    continue

            filtered_reports.append(
                report
            )

        # Latest scan first
        filtered_reports.reverse()

        # Update count
        count_label.configure(
            text=f"Scan History  •  {len(filtered_reports)} scan(s)"
        )

        # ----------------------------------------------------
        # EMPTY
        # ----------------------------------------------------

        if not filtered_reports:

            empty_card = ctk.CTkFrame(
                history_scroll,
                fg_color=CARD_COLOR,
                corner_radius=16,
                border_width=1,
                border_color=BORDER_COLOR
            )

            empty_card.pack(
                fill="x",
                pady=25
            )

            ctk.CTkLabel(
                empty_card,
                text="📭  No matching scans",
                font=(FONT, 19, "bold"),
                text_color=TEXT_COLOR
            ).pack(
                pady=(30, 5)
            )

            ctk.CTkLabel(
                empty_card,
                text="Try changing the search or filters.",
                font=(FONT, 12),
                text_color=SECONDARY_TEXT
            ).pack(
                pady=(0, 30)
            )

            return

        # ----------------------------------------------------
        # HISTORY CARDS
        # ----------------------------------------------------

        for index, report in enumerate(
            filtered_reports,
            start=1
        ):

            scan_type = report.get(
                "scan_type",
                "Unknown"
            )

            target = report.get(
                "target",
                "Unknown"
            )

            date_time = report.get(
                "date_time",
                "Unknown"
            )

            risk = str(
                report.get(
                    "risk",
                    "UNKNOWN"
                )
            ).upper()

            risk_color = get_risk_color(
                risk
            )

            # ================================================
            # HISTORY CARD
            # ================================================

            card = ctk.CTkFrame(
                history_scroll,
                fg_color=CARD_COLOR,
                corner_radius=16,
                border_width=1,
                border_color=BORDER_COLOR
            )

            card.pack(
                fill="x",
                pady=(0, 12)
            )

            # Top row
            top_row = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            top_row.pack(
                fill="x",
                padx=18,
                pady=(15, 6)
            )

            ctk.CTkLabel(
                top_row,
                text=f"SCAN #{index}",
                font=(FONT, 11, "bold"),
                text_color=SECONDARY_TEXT
            ).pack(
                side="left"
            )

            # Risk badge
            ctk.CTkLabel(
                top_row,
                text=risk,
                font=(FONT, 11, "bold"),
                text_color="#FFFFFF",
                fg_color=risk_color,
                corner_radius=8,
                padx=11,
                pady=4
            ).pack(
                side="right"
            )

            # ------------------------------------------------
            # MAIN INFO
            # ------------------------------------------------

            info_card = ctk.CTkFrame(
                card,
                fg_color="#F7F3EC",
                corner_radius=12
            )

            info_card.pack(
                fill="x",
                padx=18,
                pady=(0, 10)
            )

            # Scan type
            scan_info = ctk.CTkFrame(
                info_card,
                fg_color="transparent"
            )

            scan_info.pack(
                side="left",
                fill="x",
                expand=True,
                padx=16,
                pady=13
            )

            ctk.CTkLabel(
                scan_info,
                text="Scan Type",
                font=(FONT, 10),
                text_color=SECONDARY_TEXT
            ).pack(
                anchor="w"
            )

            ctk.CTkLabel(
                scan_info,
                text=scan_type,
                font=(FONT, 14, "bold"),
                text_color=ACCENT_COLOR,
                anchor="w"
            ).pack(
                anchor="w",
                pady=(3, 0)
            )

            # Target
            target_info = ctk.CTkFrame(
                info_card,
                fg_color="transparent"
            )

            target_info.pack(
                side="left",
                fill="x",
                expand=True,
                padx=16,
                pady=13
            )

            ctk.CTkLabel(
                target_info,
                text="Target / File",
                font=(FONT, 10),
                text_color=SECONDARY_TEXT
            ).pack(
                anchor="w"
            )

            ctk.CTkLabel(
                target_info,
                text=target,
                font=(FONT, 12, "bold"),
                text_color=TEXT_COLOR,
                anchor="w",
                wraplength=300,
                justify="left"
            ).pack(
                anchor="w",
                pady=(3, 0)
            )

            # Date
            date_info = ctk.CTkFrame(
                info_card,
                fg_color="transparent"
            )

            date_info.pack(
                side="left",
                padx=16,
                pady=13
            )

            ctk.CTkLabel(
                date_info,
                text="Date & Time",
                font=(FONT, 10),
                text_color=SECONDARY_TEXT
            ).pack(
                anchor="w"
            )

            ctk.CTkLabel(
                date_info,
                text=date_time,
                font=(FONT, 11),
                text_color=SECONDARY_TEXT,
                anchor="w"
            ).pack(
                anchor="w",
                pady=(3, 0)
            )

            # ------------------------------------------------
            # VIEW DETAILS
            # ------------------------------------------------

            ctk.CTkButton(
                card,
                text="View Details",
                width=120,
                height=34,
                corner_radius=8,
                fg_color="#FBF8F2",
                hover_color="#F0EBE2",
                border_width=1,
                border_color=BORDER_COLOR,
                text_color=TEXT_COLOR,
                font=(FONT, 11, "bold"),
                command=lambda r=report: show_details(r)
            ).pack(
                anchor="e",
                padx=18,
                pady=(0, 14)
            )

    # ========================================================
    # FILTER EVENTS
    # ========================================================

    analyzer_filter.configure(
        command=lambda value: display_history()
    )

    risk_filter.configure(
        command=lambda value: display_history()
    )

    search_entry.bind(
        "<KeyRelease>",
        lambda event: display_history()
    )

    # ========================================================
    # CLEAR HISTORY
    # ========================================================

    def clear_history():

        clear_all_reports()

        all_reports.clear()

        display_history()

    clear_button.configure(
        command=clear_history
    )

    # ========================================================
    # INITIAL LOAD
    # ========================================================

    display_history()

    return page