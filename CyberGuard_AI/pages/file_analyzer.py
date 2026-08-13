import os
import customtkinter as ctk
from datetime import datetime
from tkinter import filedialog

from services.file_analyzer import analyze_file

# ============================================================
# REPORT CONNECTION
# ============================================================

from services.report_store import save_report


# ============================================================
# CYBERGUARD AI THEME
# ============================================================

BG_COLOR = "#F7F2E8"
CARD_COLOR = "#FFFDF9"
BORDER_COLOR = "#D8CFC2"

TEXT_COLOR = "#3E332B"
SECONDARY_TEXT = "#75685D"

ACCENT_COLOR = "#8B5E3C"
ACCENT_HOVER = "#7A5233"

SUCCESS_COLOR = "#2E9B57"
SUCCESS_BG = "#EAF3EE"

DANGER_COLOR = "#B85C5C"
DANGER_BG = "#FBE9E9"

WARNING_COLOR = "#C98A2D"
WARNING_BG = "#FBF3E3"

INFO_COLOR = "#3A6EA5"
INFO_BG = "#E8F0F8"

FONT = "Segoe UI"


# ============================================================
# RISK COLORS
# ============================================================

RISK_COLORS = {
    "SAFE": SUCCESS_COLOR,
    "LOW": INFO_COLOR,
    "MEDIUM": WARNING_COLOR,
    "HIGH": DANGER_COLOR,
    "CRITICAL": "#C0392B",
}

RISK_BG = {
    "SAFE": SUCCESS_BG,
    "LOW": INFO_BG,
    "MEDIUM": WARNING_BG,
    "HIGH": DANGER_BG,
    "CRITICAL": DANGER_BG,
}


# ============================================================
# CARD HELPER
# ============================================================

def _make_card(parent, corner_radius=16):
    return ctk.CTkFrame(
        parent,
        fg_color=CARD_COLOR,
        corner_radius=corner_radius,
        border_width=1,
        border_color=BORDER_COLOR,
    )


# ============================================================
# FILE SIZE FORMATTER
# ============================================================

def _format_size(size):
    try:
        if size < 1024:
            return f"{size} B"

        elif size < 1024 * 1024:
            return f"{size / 1024:.1f} KB"

        elif size < 1024 * 1024 * 1024:
            return f"{size / (1024 * 1024):.1f} MB"

        return f"{size / (1024 * 1024 * 1024):.1f} GB"

    except (TypeError, ValueError):
        return "Unknown"


# ============================================================
# FILE ANALYZER PAGE
# ============================================================

def file_analyzer_page(parent):

    # ========================================================
    # MAIN PAGE
    # ========================================================

    page = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    page.pack(
        fill="both",
        expand=True
    )


    # ========================================================
    # MAIN CONTENT
    # ========================================================

    content = ctk.CTkFrame(
        page,
        fg_color="transparent"
    )

    content.pack(
        fill="both",
        expand=True,
        padx=22,
        pady=18
    )


    # ========================================================
    # HEADER
    # ========================================================

    ctk.CTkLabel(
        content,
        text="📁  File Security Scanner",
        font=(FONT, 28, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )

    ctk.CTkLabel(
        content,
        text="Analyze files for suspicious characteristics and security risks.",
        font=(FONT, 15),
        text_color=SECONDARY_TEXT,
    ).pack(
        anchor="w",
        pady=(4, 14)
    )


    # ========================================================
    # FILE SELECTION CARD
    # ========================================================

    select_card = _make_card(
        content,
        corner_radius=18
    )

    select_card.pack(
        fill="x"
    )


    select_inner = ctk.CTkFrame(
        select_card,
        fg_color="transparent"
    )

    select_inner.pack(
        fill="x",
        padx=22,
        pady=20
    )


    ctk.CTkLabel(
        select_inner,
        text="Select a file to analyze",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w"
    )


    # ========================================================
    # SELECTED FILE INFO
    # ========================================================

    file_info = ctk.CTkFrame(
        select_inner,
        fg_color="#FBF8F2",
        corner_radius=12
    )

    file_info.pack(
        fill="x",
        pady=(12, 0)
    )


    file_name_label = ctk.CTkLabel(
        file_info,
        text="No file selected",
        font=(FONT, 14, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
    )

    file_name_label.pack(
        anchor="w",
        padx=16,
        pady=(12, 2)
    )


    file_meta_label = ctk.CTkLabel(
        file_info,
        text="",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
        anchor="w",
        wraplength=900,
        justify="left",
    )

    file_meta_label.pack(
        anchor="w",
        padx=16,
        pady=(0, 12)
    )


    # ========================================================
    # BUTTON ROW
    # ========================================================

    btn_row = ctk.CTkFrame(
        select_inner,
        fg_color="transparent"
    )

    btn_row.pack(
        fill="x",
        pady=(14, 0)
    )


    choose_file_button = ctk.CTkButton(
        btn_row,
        text="📂  Choose File",
        height=48,
        width=140,
        corner_radius=12,
        fg_color="#FBF8F2",
        hover_color="#F0EBE2",
        border_width=1,
        border_color="#DED4C6",
        text_color=TEXT_COLOR,
        font=(FONT, 14, "bold"),
    )

    choose_file_button.pack(
        side="left",
        padx=(0, 8)
    )


    analyze_file_button = ctk.CTkButton(
        btn_row,
        text="🔍  Analyze File",
        height=48,
        corner_radius=12,
        fg_color=ACCENT_COLOR,
        hover_color=ACCENT_HOVER,
        text_color="#FFFFFF",
        font=(FONT, 14, "bold"),
        state="disabled",
    )

    analyze_file_button.pack(
        side="left",
        fill="x",
        expand=True
    )


    # ========================================================
    # ERROR LABEL
    # ========================================================

    error_label = ctk.CTkLabel(
        select_inner,
        text="",
        font=(FONT, 13),
        text_color=DANGER_COLOR,
        anchor="w",
        wraplength=900,
        justify="left",
    )

    error_label.pack(
        fill="x",
        pady=(10, 0)
    )


    # ========================================================
    # PRIVACY NOTE
    # ========================================================

    ctk.CTkLabel(
        select_inner,
        text="🔒  Local heuristic analysis — the file is NOT uploaded or sent anywhere.",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
        anchor="w",
    ).pack(
        anchor="w",
        pady=(10, 0)
    )


    # ========================================================
    # RESULT CARD
    # ========================================================

    result_card = _make_card(
        content,
        corner_radius=18
    )


    result_inner = ctk.CTkFrame(
        result_card,
        fg_color="transparent"
    )

    result_inner.pack(
        fill="x",
        padx=22,
        pady=20
    )


    # ========================================================
    # RESULT HEADER
    # ========================================================

    result_header = ctk.CTkFrame(
        result_inner,
        fg_color="transparent"
    )

    result_header.pack(
        fill="x"
    )


    ctk.CTkLabel(
        result_header,
        text="File Security Result",
        font=(FONT, 18, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        side="left"
    )


    risk_label = ctk.CTkLabel(
        result_header,
        text="NOT ANALYZED",
        font=(FONT, 13, "bold"),
        corner_radius=10,
        padx=16,
        pady=6,
        text_color=SECONDARY_TEXT,
        fg_color="#EEE7DE",
    )

    risk_label.pack(
        side="right"
    )


    # ========================================================
    # LOADING LABEL
    # ========================================================

    loading_label = ctk.CTkLabel(
        result_inner,
        text="Analyzing file...",
        font=(FONT, 14, "bold"),
        text_color=ACCENT_COLOR,
    )


    # ========================================================
    # RESULT GRID
    # ========================================================

    scored = ctk.CTkFrame(
        result_inner,
        fg_color="transparent"
    )

    scored.grid_columnconfigure(
        0,
        weight=1,
        uniform="res"
    )

    scored.grid_columnconfigure(
        1,
        weight=1,
        uniform="res"
    )


    # ========================================================
    # LEFT PANEL
    # ========================================================

    left_panel = ctk.CTkFrame(
        scored,
        fg_color="transparent"
    )

    left_panel.grid(
        row=0,
        column=0,
        padx=(0, 12),
        sticky="nsew"
    )


    details_frame = ctk.CTkFrame(
        left_panel,
        fg_color="transparent"
    )

    details_frame.pack(
        fill="x"
    )


    def _detail_row(
        frame,
        label,
        value_label,
        value_color=None
    ):

        row = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            pady=3
        )


        ctk.CTkLabel(
            row,
            text=label,
            font=(FONT, 13, "bold"),
            text_color=SECONDARY_TEXT,
            width=130,
            anchor="w",
        ).pack(
            side="left"
        )


        value_label.configure(
            text_color=value_color or TEXT_COLOR
        )

        value_label.pack(
            side="left",
            fill="x",
            expand=True
        )


    # ========================================================
    # DETAIL LABELS
    # ========================================================

    res_name = ctk.CTkLabel(
        details_frame,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
        wraplength=400,
        justify="left"
    )

    res_type = ctk.CTkLabel(
        details_frame,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w"
    )

    res_size = ctk.CTkLabel(
        details_frame,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w"
    )

    res_ext = ctk.CTkLabel(
        details_frame,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w"
    )

    res_hash = ctk.CTkLabel(
        details_frame,
        text="—",
        font=(FONT, 12),
        text_color=SECONDARY_TEXT,
        anchor="w",
        wraplength=400,
        justify="left"
    )


    _detail_row(
        details_frame,
        "File Name",
        res_name
    )

    _detail_row(
        details_frame,
        "File Type",
        res_type
    )

    _detail_row(
        details_frame,
        "File Size",
        res_size
    )

    _detail_row(
        details_frame,
        "Extension",
        res_ext
    )

    _detail_row(
        details_frame,
        "SHA-256",
        res_hash
    )


    # ========================================================
    # SECURITY CHECKS
    # ========================================================

    ctk.CTkLabel(
        left_panel,
        text="Security Checks",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w",
        pady=(14, 0)
    )


    checks_frame = ctk.CTkFrame(
        left_panel,
        fg_color="transparent"
    )

    checks_frame.pack(
        fill="x",
        pady=(8, 0)
    )


    # ========================================================
    # INDICATORS
    # ========================================================

    ctk.CTkLabel(
        left_panel,
        text="Suspicious Indicators",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        anchor="w",
        pady=(14, 0)
    )


    indicators_frame = ctk.CTkFrame(
        left_panel,
        fg_color="transparent"
    )

    indicators_frame.pack(
        fill="x",
        pady=(8, 0)
    )


    # ========================================================
    # RIGHT PANEL
    # ========================================================

    right_panel = ctk.CTkFrame(
        scored,
        fg_color="#FBF8F2",
        corner_radius=14
    )

    right_panel.grid(
        row=0,
        column=1,
        padx=(12, 0),
        sticky="nsew"
    )


    right_inner = ctk.CTkFrame(
        right_panel,
        fg_color="transparent"
    )

    right_inner.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=18
    )


    # ========================================================
    # SECURITY SCORE
    # ========================================================

    ctk.CTkLabel(
        right_inner,
        text="Security Score",
        font=(FONT, 14, "bold"),
        text_color=SECONDARY_TEXT,
        anchor="w",
    ).pack(
        anchor="w"
    )


    score_value = ctk.CTkLabel(
        right_inner,
        text="— / 100",
        font=(FONT, 34, "bold"),
        text_color=SUCCESS_COLOR,
    )

    score_value.pack(
        anchor="w",
        pady=(6, 4)
    )


    progress = ctk.CTkProgressBar(
        right_inner,
        height=12,
        corner_radius=6,
        fg_color="#E8E1D5",
        progress_color=SUCCESS_COLOR,
    )

    progress.set(0)

    progress.pack(
        fill="x",
        pady=(6, 12)
    )


    # ========================================================
    # AI VERDICT
    # ========================================================

    ctk.CTkLabel(
        right_inner,
        text="AI Verdict",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
    ).pack(
        anchor="w",
        pady=(8, 0)
    )


    verdict_label = ctk.CTkLabel(
        right_inner,
        text="—",
        font=(FONT, 13),
        text_color=TEXT_COLOR,
        anchor="w",
        justify="left",
        wraplength=430,
    )

    verdict_label.pack(
        anchor="w",
        pady=(4, 0)
    )


    # ========================================================
    # RECOMMENDATION
    # ========================================================

    ctk.CTkLabel(
        right_inner,
        text="Security Recommendation",
        font=(FONT, 15, "bold"),
        text_color=TEXT_COLOR,
        anchor="w",
    ).pack(
        anchor="w",
        pady=(14, 0)
    )


    rec_label = ctk.CTkLabel(
        right_inner,
        text="—",
        font=(FONT, 13),
        text_color=SECONDARY_TEXT,
        anchor="w",
        justify="left",
        wraplength=430,
    )

    rec_label.pack(
        anchor="w",
        pady=(4, 0)
    )


    # ========================================================
    # RECENT FILE SCANS
    # ========================================================

    history_card = _make_card(
        content,
        corner_radius=18
    )

    history_card.pack(
        fill="x",
        pady=(12, 0)
    )


    history_header = ctk.CTkFrame(
        history_card,
        fg_color="transparent"
    )

    history_header.pack(
        fill="x",
        padx=20,
        pady=(14, 8)
    )


    ctk.CTkLabel(
        history_header,
        text="Recent File Scans",
        font=(FONT, 17, "bold"),
        text_color=TEXT_COLOR,
    ).pack(
        side="left"
    )


    clear_button = ctk.CTkButton(
        history_header,
        text="Clear History",
        width=120,
        height=32,
        corner_radius=9,
        fg_color="#FBF8F2",
        hover_color="#F0EBE2",
        border_width=1,
        border_color="#DED4C6",
        text_color=DANGER_COLOR,
        font=(FONT, 12, "bold"),
    )

    clear_button.pack(
        side="right"
    )


    history_body = ctk.CTkFrame(
        history_card,
        fg_color="transparent"
    )

    history_body.pack(
        fill="x",
        padx=20,
        pady=(0, 16)
    )


    history = []


    history_rows = ctk.CTkFrame(
        history_body,
        fg_color="transparent"
    )

    history_rows.pack(
        fill="x"
    )


    # ========================================================
    # HISTORY RENDER
    # ========================================================

    def _render_history():

        for child in history_rows.winfo_children():
            child.destroy()


        if not history:

            ctk.CTkLabel(
                history_rows,
                text="No scans yet. Select and analyze a file to see it here.",
                font=(FONT, 13),
                text_color=SECONDARY_TEXT,
            ).pack(
                anchor="w",
                pady=8
            )

            return


        for entry in history:

            row = ctk.CTkFrame(
                history_rows,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                pady=3
            )


            ctk.CTkLabel(
                row,
                text=entry["file_name"],
                font=(FONT, 13),
                text_color=TEXT_COLOR,
                anchor="w",
                wraplength=300,
                justify="left",
            ).pack(
                side="left",
                fill="x",
                expand=True
            )


            ctk.CTkLabel(
                row,
                text=entry["time"],
                font=(FONT, 12),
                text_color=SECONDARY_TEXT,
                width=90,
                anchor="e",
            ).pack(
                side="right"
            )


            ctk.CTkLabel(
                row,
                text=f"{entry['score']}/100",
                font=(FONT, 12, "bold"),
                text_color=RISK_COLORS.get(
                    entry["risk"],
                    TEXT_COLOR
                ),
                width=64,
                anchor="e",
            ).pack(
                side="right",
                padx=(8, 6)
            )


            ctk.CTkLabel(
                row,
                text=entry["risk"],
                font=(FONT, 12, "bold"),
                text_color=RISK_COLORS.get(
                    entry["risk"],
                    TEXT_COLOR
                ),
                fg_color=RISK_BG.get(
                    entry["risk"],
                    "#F0EBE2"
                ),
                corner_radius=8,
                padx=10,
                pady=3,
            ).pack(
                side="right",
                padx=(0, 10)
            )


    # ========================================================
    # ADD HISTORY
    # ========================================================

    def _add_history(
        file_name,
        risk,
        score
    ):

        now = datetime.now().strftime(
            "%I:%M %p"
        )

        history.insert(
            0,
            {
                "file_name": file_name,
                "time": now,
                "risk": risk,
                "score": score
            }
        )

        _render_history()


    # ========================================================
    # CLEAR HISTORY
    # ========================================================

    def clear_history():

        history.clear()

        _render_history()


    clear_button.configure(
        command=clear_history
    )


    # ========================================================
    # SELECTED PATH
    # ========================================================

    selected_path = {
        "value": None
    }


    # ========================================================
    # CHOOSE FILE
    # ========================================================

    def choose_file():

        root = parent.winfo_toplevel()


        path = filedialog.askopenfilename(
            parent=root,
            title="Select a file to analyze",
            filetypes=[
                ("All files", "*.*")
            ],
        )


        if not path:
            return


        selected_path["value"] = path


        try:

            name = os.path.basename(path)

            size_text = _format_size(
                os.path.getsize(path)
            )

            file_name_label.configure(
                text=name
            )

            file_meta_label.configure(
                text=f"{size_text}  •  {path}"
            )

            error_label.configure(
                text=""
            )


            analyze_file_button.configure(
                state="normal"
            )


        except Exception as e:

            error_label.configure(
                text=f"⚠  Unable to read selected file: {e}"
            )


    # ========================================================
    # RENDER RESULT
    # ========================================================

    def _render_result(result):

        # ----------------------------------------------------
        # GET RESULT VALUES
        # ----------------------------------------------------

        risk = result["risk_level"]

        score = result["security_score"]

        risk_color = RISK_COLORS.get(
            risk,
            TEXT_COLOR
        )


        # ----------------------------------------------------
        # RISK
        # ----------------------------------------------------

        risk_label.configure(
            text=risk,
            text_color=risk_color,
            fg_color=RISK_BG.get(
                risk,
                "#F0EBE2"
            )
        )


        # ----------------------------------------------------
        # FILE DETAILS
        # ----------------------------------------------------

        res_name.configure(
            text=result["file_name"]
        )

        res_type.configure(
            text=result["file_type"]
        )

        res_size.configure(
            text=result["file_size_text"]
        )

        res_ext.configure(
            text=result["extension"]
        )

        res_hash.configure(
            text=result["sha256"]
        )


        # ----------------------------------------------------
        # SECURITY CHECKS
        # ----------------------------------------------------

        for child in checks_frame.winfo_children():
            child.destroy()


        for check in result.get(
            "checks",
            []
        ):

            c_row = ctk.CTkFrame(
                checks_frame,
                fg_color="transparent"
            )

            c_row.pack(
                fill="x",
                pady=2
            )


            mark = (
                "✓"
                if check["passed"]
                else "✗"
            )


            mark_color = (
                SUCCESS_COLOR
                if check["passed"]
                else DANGER_COLOR
            )


            ctk.CTkLabel(
                c_row,
                text=mark,
                font=(FONT, 14, "bold"),
                text_color=mark_color,
                width=24,
                anchor="w",
            ).pack(
                side="left"
            )


            ctk.CTkLabel(
                c_row,
                text=check["name"],
                font=(FONT, 13),
                text_color=TEXT_COLOR,
                anchor="w",
            ).pack(
                side="left"
            )


        # ----------------------------------------------------
        # SUSPICIOUS INDICATORS
        # ----------------------------------------------------

        for child in indicators_frame.winfo_children():
            child.destroy()


        indicators = result.get(
            "indicators",
            []
        )


        if not indicators:

            ctk.CTkLabel(
                indicators_frame,
                text="✅  No suspicious indicators found.",
                font=(FONT, 13),
                text_color=SUCCESS_COLOR,
                anchor="w",
            ).pack(
                anchor="w",
                pady=2
            )

        else:

            for ind in indicators:

                ctk.CTkLabel(
                    indicators_frame,
                    text="•  " + ind,
                    font=(FONT, 13),
                    text_color=WARNING_COLOR,
                    anchor="w",
                    justify="left",
                    wraplength=430,
                ).pack(
                    anchor="w",
                    pady=2
                )


        # ----------------------------------------------------
        # SCORE
        # ----------------------------------------------------

        score_value.configure(
            text=f"{score} / 100",
            text_color=risk_color
        )


        progress.set(
            score / 100
        )


        progress.configure(
            progress_color=risk_color
        )


        # ----------------------------------------------------
        # VERDICT
        # ----------------------------------------------------

        verdict = result.get(
            "verdict",
            "No verdict available."
        )


        recommendation = result.get(
            "recommendation",
            "No recommendation available."
        )


        verdict_label.configure(
            text=verdict
        )


        rec_label.configure(
            text=recommendation
        )


        # ====================================================
        # IMPORTANT: SAVE FILE ANALYZER REPORT
        # ====================================================
        #
        # save_report() expects:
        #
        # 1. scan_type
        # 2. target
        # 3. score
        # 4. risk
        # 5. verdict
        # 6. recommendation
        #
        # ====================================================

        try:

            save_report(
                "File Analyzer",
                result["file_name"],
                result["security_score"],
                result["risk_level"],
                result["verdict"],
                result["recommendation"]
            )

        except Exception as report_error:

            # Analysis itself should NOT fail
            # because of report saving.

            print(
                "Report save error:",
                report_error
            )


        # ----------------------------------------------------
        # ADD LOCAL HISTORY
        # ----------------------------------------------------

        _add_history(
            result["file_name"],
            risk,
            score
        )


    # ========================================================
    # ANALYZE SELECTED FILE
    # ========================================================

    def analyze_selected_file():

        error_label.configure(
            text=""
        )


        # ----------------------------------------------------
        # CHECK FILE SELECTED
        # ----------------------------------------------------

        if selected_path["value"] is None:

            error_label.configure(
                text="⚠  Please select a file to analyze."
            )

            return


        file_path = selected_path["value"]


        # ----------------------------------------------------
        # CHECK FILE EXISTS
        # ----------------------------------------------------

        if not os.path.exists(file_path):

            selected_path["value"] = None

            analyze_file_button.configure(
                state="disabled"
            )

            file_name_label.configure(
                text="No file selected"
            )

            file_meta_label.configure(
                text=""
            )

            error_label.configure(
                text=(
                    "⚠  The selected file was deleted "
                    "or moved. Please choose it again."
                )
            )

            return


        # ----------------------------------------------------
        # LOADING STATE
        # ----------------------------------------------------

        loading_label.pack(
            anchor="w",
            pady=(16, 0)
        )


        analyze_file_button.configure(
            state="disabled",
            text="Analyzing..."
        )


        # ----------------------------------------------------
        # RUN FILE ANALYZER
        # ----------------------------------------------------

        try:

            result = analyze_file(
                file_path
            )


        except FileNotFoundError:

            loading_label.pack_forget()

            analyze_file_button.configure(
                state="normal",
                text="🔍  Analyze File"
            )

            error_label.configure(
                text=(
                    "⚠  The selected file could not be found. "
                    "Please choose it again."
                )
            )

            return


        except PermissionError:

            loading_label.pack_forget()

            analyze_file_button.configure(
                state="normal",
                text="🔍  Analyze File"
            )

            error_label.configure(
                text=(
                    "⚠  Permission denied. "
                    "You do not have access to read this file."
                )
            )

            return


        except ValueError as e:

            loading_label.pack_forget()

            analyze_file_button.configure(
                state="normal",
                text="🔍  Analyze File"
            )

            error_label.configure(
                text=f"⚠  {str(e)}"
            )

            return


        except Exception as e:

            loading_label.pack_forget()

            analyze_file_button.configure(
                state="normal",
                text="🔍  Analyze File"
            )

            error_label.configure(
                text=f"⚠  Analysis failed: {str(e)}"
            )

            print(
                "FILE ANALYZER ERROR:",
                repr(e)
            )

            return


        # ----------------------------------------------------
        # ANALYSIS SUCCESS
        # ----------------------------------------------------

        loading_label.pack_forget()


        analyze_file_button.configure(
            state="normal",
            text="🔍  Analyze File"
        )


        # ----------------------------------------------------
        # SHOW RESULT CARD
        # ----------------------------------------------------

        result_card.pack(
            fill="x",
            pady=(12, 0)
        )


        # ----------------------------------------------------
        # RENDER RESULT + SAVE REPORT
        # ----------------------------------------------------

        try:

            _render_result(
                result
            )

        except Exception as e:

            error_label.configure(
                text=f"⚠  Result display failed: {str(e)}"
            )

            print(
                "RESULT DISPLAY ERROR:",
                repr(e)
            )


    # ========================================================
    # CONNECT BUTTONS
    # ========================================================

    choose_file_button.configure(
        command=choose_file
    )


    analyze_file_button.configure(
        command=analyze_selected_file
    )


    # ========================================================
    # INITIAL HISTORY
    # ========================================================

    _render_history()


    # ========================================================
    # RETURN PAGE
    # ========================================================

    return page