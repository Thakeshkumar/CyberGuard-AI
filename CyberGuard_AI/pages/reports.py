import customtkinter as ctk

from services.report_store import (
    get_all_reports,
    clear_all_reports
)


# ============================================================
# CYBERGUARD AI - SECURITY REPORT DASHBOARD
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


# ============================================================
# RISK ORDER
# ============================================================

RISK_ORDER = {
    "SAFE": 0,
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4
}


# ============================================================
# HELPERS
# ============================================================

def get_risk_color(risk):
    return RISK_COLORS.get(
        str(risk).upper(),
        SECONDARY_TEXT
    )


def calculate_overall_risk(reports):
    """
    Calculate overall risk from all reports.

    Highest risk found gets priority.
    """

    if not reports:
        return "NO DATA"

    highest_risk = "SAFE"
    highest_value = -1

    for report in reports:

        risk = str(
            report.get(
                "risk",
                "SAFE"
            )
        ).upper()

        value = RISK_ORDER.get(
            risk,
            0
        )

        if value > highest_value:
            highest_value = value
            highest_risk = risk

    return highest_risk


def calculate_overall_score(reports):
    """
    Calculate average security score.
    """

    if not reports:
        return 0

    scores = []

    for report in reports:

        try:

            score = float(
                report.get(
                    "score",
                    0
                )
            )

            score = max(
                0,
                min(
                    100,
                    score
                )
            )

            scores.append(
                score
            )

        except (
            TypeError,
            ValueError
        ):
            continue

    if not scores:
        return 0

    return round(
        sum(scores) / len(scores)
    )


# ============================================================
# REPORT PAGE
# ============================================================

def reports_page(parent):

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
        pady=(25, 5)
    )


    ctk.CTkLabel(
        header,
        text="📊  Security Reports",
        font=(FONT, 28, "bold"),
        text_color=TEXT_COLOR
    ).pack(
        anchor="w"
    )


    ctk.CTkLabel(
        header,
        text="Overall security overview and complete CyberGuard AI analysis reports.",
        font=(FONT, 13),
        text_color=SECONDARY_TEXT
    ).pack(
        anchor="w",
        pady=(4, 0)
    )


    # ========================================================
    # SCROLLABLE CONTENT
    # ========================================================

    content = ctk.CTkFrame(
        page,
        fg_color="transparent",
        corner_radius=0
    )

    content.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(15, 25)
    )


    # ========================================================
    # GET REPORTS
    # ========================================================

    all_reports = get_all_reports()

    if all_reports is None:
        all_reports = []


    # ========================================================
    # SUMMARY
    # ========================================================

    summary = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    summary.pack(
        fill="x"
    )


    for i in range(5):

        summary.grid_columnconfigure(
            i,
            weight=1
        )


    # ========================================================
    # SUMMARY CARD HELPER
    # ========================================================

    summary_values = {}

    def create_summary_card(
        column,
        key,
        title,
        value,
        color
    ):

        card = ctk.CTkFrame(
            summary,
            fg_color=CARD_COLOR,
            corner_radius=16,
            border_width=1,
            border_color=BORDER_COLOR
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=5
        )


        ctk.CTkLabel(
            card,
            text=title,
            font=(FONT, 12),
            text_color=SECONDARY_TEXT
        ).pack(
            anchor="w",
            padx=16,
            pady=(15, 4)
        )


        value_label = ctk.CTkLabel(
            card,
            text=str(value),
            font=(FONT, 24, "bold"),
            text_color=color
        )

        value_label.pack(
            anchor="w",
            padx=16,
            pady=(0, 15)
        )


        summary_values[key] = value_label


    # ========================================================
    # SUMMARY CARDS
    # ========================================================

    create_summary_card(
        0,
        "total",
        "Total Reports",
        0,
        ACCENT_COLOR
    )

    create_summary_card(
        1,
        "safe",
        "SAFE",
        0,
        SUCCESS_COLOR
    )

    create_summary_card(
        2,
        "low",
        "LOW",
        0,
        LOW_COLOR
    )

    create_summary_card(
        3,
        "medium",
        "MEDIUM",
        0,
        MEDIUM_COLOR
    )

    create_summary_card(
        4,
        "danger",
        "HIGH / CRITICAL",
        0,
        HIGH_COLOR
    )


    # ========================================================
    # OVERALL SECURITY SCORE CARD
    # ========================================================

    overall_card = ctk.CTkFrame(
        content,
        fg_color=CARD_COLOR,
        corner_radius=18,
        border_width=1,
        border_color=BORDER_COLOR
    )

    overall_card.pack(
        fill="x",
        pady=(16, 16)
    )


    overall_left = ctk.CTkFrame(
        overall_card,
        fg_color="transparent"
    )

    overall_left.pack(
        side="left",
        fill="x",
        expand=True,
        padx=25,
        pady=20
    )


    ctk.CTkLabel(
        overall_left,
        text="Overall Security Score",
        font=(FONT, 18, "bold"),
        text_color=TEXT_COLOR
    ).pack(
        anchor="w"
    )


    overall_score_label = ctk.CTkLabel(
        overall_left,
        text="0 / 100",
        font=(FONT, 34, "bold"),
        text_color=SUCCESS_COLOR
    )

    overall_score_label.pack(
        anchor="w",
        pady=(5, 7)
    )


    overall_progress = ctk.CTkProgressBar(
        overall_left,
        height=13,
        corner_radius=7,
        fg_color="#E8E1D5",
        progress_color=SUCCESS_COLOR
    )

    overall_progress.set(0)

    overall_progress.pack(
        fill="x"
    )


    # ========================================================
    # OVERALL RISK PANEL
    # ========================================================

    overall_right = ctk.CTkFrame(
        overall_card,
        fg_color="#F7F3EC",
        corner_radius=14,
        width=240
    )

    overall_right.pack(
        side="right",
        padx=25,
        pady=20
    )

    overall_right.pack_propagate(
        False
    )


    ctk.CTkLabel(
        overall_right,
        text="Overall Risk",
        font=(FONT, 13),
        text_color=SECONDARY_TEXT
    ).pack(
        pady=(15, 4)
    )


    overall_risk_label = ctk.CTkLabel(
        overall_right,
        text="NO DATA",
        font=(FONT, 22, "bold"),
        text_color=SECONDARY_TEXT
    )

    overall_risk_label.pack(
        pady=(0, 15)
    )


    # ========================================================
    # FILTER AREA
    # ========================================================

    filter_card = ctk.CTkFrame(
        content,
        fg_color=CARD_COLOR,
        corner_radius=16,
        border_width=1,
        border_color=BORDER_COLOR
    )

    filter_card.pack(
        fill="x",
        pady=(0, 15)
    )


    filter_inner = ctk.CTkFrame(
        filter_card,
        fg_color="transparent"
    )

    filter_inner.pack(
        fill="x",
        padx=18,
        pady=14
    )


    ctk.CTkLabel(
        filter_inner,
        text="Filter Reports",
        font=(FONT, 14, "bold"),
        text_color=TEXT_COLOR
    ).pack(
        side="left",
        padx=(0, 12)
    )


    current_filter = {
        "value": "All"
    }


    # ========================================================
    # REPORT LIST CONTAINER
    # ========================================================

    reports_container = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    reports_container.pack(
        fill="x"
    )


    # ========================================================
    # CREATE REPORT CARD
    # ========================================================

    def create_report_card(
        report,
        index
    ):

        scan_type = report.get(
            "scan_type",
            "Unknown"
        )

        target = report.get(
            "target",
            "Unknown"
        )

        score = report.get(
            "score",
            0
        )

        risk = str(
            report.get(
                "risk",
                "UNKNOWN"
            )
        ).upper()

        verdict = report.get(
            "verdict",
            "No verdict available."
        )

        recommendation = report.get(
            "recommendation",
            "No recommendation available."
        )

        date_time = report.get(
            "date_time",
            "Unknown"
        )


        risk_color = get_risk_color(
            risk
        )


        # ----------------------------------------------------
        # OUTER CARD
        # ----------------------------------------------------

        report_card = ctk.CTkFrame(
            reports_container,
            fg_color=CARD_COLOR,
            corner_radius=16,
            border_width=1,
            border_color=BORDER_COLOR
        )

        report_card.pack(
            fill="x",
            pady=(0, 15)
        )


        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        report_header = ctk.CTkFrame(
            report_card,
            fg_color="transparent"
        )

        report_header.pack(
            fill="x",
            padx=20,
            pady=(18, 8)
        )


        ctk.CTkLabel(
            report_header,
            text=f"REPORT #{index}",
            font=(FONT, 12, "bold"),
            text_color=SECONDARY_TEXT
        ).pack(
            side="left"
        )


        ctk.CTkLabel(
            report_header,
            text=risk,
            font=(FONT, 11, "bold"),
            text_color="#FFFFFF",
            fg_color=risk_color,
            corner_radius=8,
            padx=12,
            pady=5
        ).pack(
            side="right"
        )


        # ----------------------------------------------------
        # MINI SUMMARY
        # ----------------------------------------------------

        mini_summary = ctk.CTkFrame(
            report_card,
            fg_color="transparent"
        )

        mini_summary.pack(
            fill="x",
            padx=20,
            pady=(0, 14)
        )


        for i in range(4):

            mini_summary.grid_columnconfigure(
                i,
                weight=1
            )


        def mini_box(
            column,
            title,
            value,
            value_color
        ):

            box = ctk.CTkFrame(
                mini_summary,
                fg_color="#F7F3EC",
                corner_radius=10
            )

            box.grid(
                row=0,
                column=column,
                sticky="nsew",
                padx=4
            )


            ctk.CTkLabel(
                box,
                text=title,
                font=(FONT, 10),
                text_color=SECONDARY_TEXT
            ).pack(
                anchor="w",
                padx=12,
                pady=(10, 2)
            )


            ctk.CTkLabel(
                box,
                text=str(value),
                font=(FONT, 13, "bold"),
                text_color=value_color,
                anchor="w",
                justify="left",
                wraplength=250
            ).pack(
                anchor="w",
                padx=12,
                pady=(0, 10)
            )


        mini_box(
            0,
            "SCAN TYPE",
            scan_type,
            ACCENT_COLOR
        )


        mini_box(
            1,
            "SECURITY SCORE",
            f"{score}/100",
            risk_color
        )


        mini_box(
            2,
            "TARGET / FILE",
            target,
            TEXT_COLOR
        )


        mini_box(
            3,
            "DATE & TIME",
            date_time,
            SECONDARY_TEXT
        )


        # ----------------------------------------------------
        # VERDICT AREA
        # ----------------------------------------------------

        verdict_card = ctk.CTkFrame(
            report_card,
            fg_color="#F7F3EC",
            corner_radius=12
        )

        verdict_card.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )


        ctk.CTkLabel(
            verdict_card,
            text="AI Verdict",
            font=(FONT, 14, "bold"),
            text_color=TEXT_COLOR
        ).pack(
            anchor="w",
            padx=18,
            pady=(14, 5)
        )


        ctk.CTkLabel(
            verdict_card,
            text=str(verdict),
            font=(FONT, 12),
            text_color=TEXT_COLOR,
            anchor="w",
            justify="left",
            wraplength=1000
        ).pack(
            fill="x",
            padx=18,
            pady=(0, 14)
        )


        # ----------------------------------------------------
        # RECOMMENDATION
        # ----------------------------------------------------

        recommendation_card = ctk.CTkFrame(
            report_card,
            fg_color="#F7F3EC",
            corner_radius=12
        )

        recommendation_card.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )


        ctk.CTkLabel(
            recommendation_card,
            text="Security Recommendation",
            font=(FONT, 14, "bold"),
            text_color=TEXT_COLOR
        ).pack(
            anchor="w",
            padx=18,
            pady=(14, 5)
        )


        ctk.CTkLabel(
            recommendation_card,
            text=str(recommendation),
            font=(FONT, 12),
            text_color=SECONDARY_TEXT,
            anchor="w",
            justify="left",
            wraplength=1000
        ).pack(
            fill="x",
            padx=18,
            pady=(0, 14)
        )


    # ========================================================
    # DISPLAY REPORTS
    # ========================================================

    def display_reports():

        for child in reports_container.winfo_children():
            child.destroy()


        selected = current_filter["value"]


        # ----------------------------------------------------
        # FILTER REPORTS
        # ----------------------------------------------------

        filtered_reports = []

        for report in all_reports:

            scan_type = str(
                report.get(
                    "scan_type",
                    ""
                )
            ).lower()


            if selected == "All":

                filtered_reports.append(
                    report
                )

            elif selected.lower() in scan_type:

                filtered_reports.append(
                    report
                )


        # Latest first
        filtered_reports = list(
            reversed(
                filtered_reports
            )
        )


        # ----------------------------------------------------
        # EMPTY FILTER RESULT
        # ----------------------------------------------------

        if not filtered_reports:

            empty = ctk.CTkFrame(
                reports_container,
                fg_color=CARD_COLOR,
                corner_radius=16,
                border_width=1,
                border_color=BORDER_COLOR
            )

            empty.pack(
                fill="x",
                pady=20
            )


            ctk.CTkLabel(
                empty,
                text="No reports found",
                font=(FONT, 19, "bold"),
                text_color=TEXT_COLOR
            ).pack(
                pady=(30, 5)
            )


            ctk.CTkLabel(
                empty,
                text="Try another analyzer filter.",
                font=(FONT, 12),
                text_color=SECONDARY_TEXT
            ).pack(
                pady=(0, 30)
            )

            return


        # ----------------------------------------------------
        # CREATE CARDS
        # ----------------------------------------------------

        for index, report in enumerate(
            filtered_reports,
            start=1
        ):

            create_report_card(
                report,
                index
            )


    # ========================================================
    # FILTER BUTTONS
    # ========================================================

    filters = [
        "All",
        "File Analyzer",
        "Scam Detector",
        "URL Analyzer",
        "Password Analyzer",
        "Email Analyzer"
    ]


    filter_buttons = {}


    def set_filter(
        value
    ):

        current_filter["value"] = value

        for name, button in filter_buttons.items():

            if name == value:

                button.configure(
                    fg_color=ACCENT_COLOR,
                    text_color="#FFFFFF"
                )

            else:

                button.configure(
                    fg_color="#FBF8F2",
                    text_color=TEXT_COLOR
                )

        display_reports()


    for filter_name in filters:

        button = ctk.CTkButton(
            filter_inner,
            text=filter_name,
            height=34,
            corner_radius=9,
            fg_color=(
                ACCENT_COLOR
                if filter_name == "All"
                else "#FBF8F2"
            ),
            hover_color=(
                ACCENT_HOVER
                if filter_name == "All"
                else "#F0EBE2"
            ),
            text_color=(
                "#FFFFFF"
                if filter_name == "All"
                else TEXT_COLOR
            ),
            border_width=1,
            border_color=BORDER_COLOR,
            font=(FONT, 11, "bold"),
            command=lambda name=filter_name: set_filter(
                name
            )
        )

        button.pack(
            side="left",
            padx=3
        )

        filter_buttons[
            filter_name
        ] = button


    # ========================================================
    # CLEAR BUTTON
    # ========================================================

    clear_row = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    clear_row.pack(
        fill="x",
        pady=(12, 5)
    )


    def clear_reports():

        if not all_reports:
            return

        # Clear storage
        clear_all_reports()

        # Clear local list
        all_reports.clear()

        # Reset summary
        update_dashboard()

        # Display empty state
        display_reports()


    ctk.CTkButton(
        clear_row,
        text="🗑  Clear All Reports",
        width=160,
        height=38,
        corner_radius=9,
        fg_color="#E8D8C8",
        hover_color="#D9C5B0",
        text_color=TEXT_COLOR,
        font=(FONT, 11, "bold"),
        command=clear_reports
    ).pack(
        side="right"
    )


    # ========================================================
    # DASHBOARD UPDATE
    # ========================================================

    def update_dashboard():

        total = len(
            all_reports
        )


        safe_count = 0
        low_count = 0
        medium_count = 0
        danger_count = 0


        for report in all_reports:

            risk = str(
                report.get(
                    "risk",
                    ""
                )
            ).upper()


            if risk == "SAFE":

                safe_count += 1

            elif risk == "LOW":

                low_count += 1

            elif risk == "MEDIUM":

                medium_count += 1

            elif risk in (
                "HIGH",
                "CRITICAL"
            ):

                danger_count += 1


        # ----------------------------------------------------
        # UPDATE SUMMARY
        # ----------------------------------------------------

        summary_values[
            "total"
        ].configure(
            text=str(total)
        )

        summary_values[
            "safe"
        ].configure(
            text=str(safe_count)
        )

        summary_values[
            "low"
        ].configure(
            text=str(low_count)
        )

        summary_values[
            "medium"
        ].configure(
            text=str(medium_count)
        )

        summary_values[
            "danger"
        ].configure(
            text=str(danger_count)
        )


        # ----------------------------------------------------
        # OVERALL SCORE
        # ----------------------------------------------------

        overall_score = calculate_overall_score(
            all_reports
        )

        overall_score_label.configure(
            text=f"{overall_score} / 100"
        )

        overall_progress.set(
            overall_score / 100
        )


        # ----------------------------------------------------
        # OVERALL RISK
        # ----------------------------------------------------

        overall_risk = calculate_overall_risk(
            all_reports
        )

        overall_risk_label.configure(
            text=overall_risk,
            text_color=get_risk_color(
                overall_risk
            )
        )

        overall_progress.configure(
            progress_color=get_risk_color(
                overall_risk
            )
        )

        overall_score_label.configure(
            text_color=get_risk_color(
                overall_risk
            )
        )


        if overall_risk == "NO DATA":

            overall_progress.set(0)


    # ========================================================
    # INITIAL UPDATE
    # ========================================================

    update_dashboard()
    display_reports()


    return page