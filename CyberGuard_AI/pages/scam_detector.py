import re
import customtkinter as ctk

from services.report_store import save_report


# ============================================================
# CYBERGUARD AI - SCAM DETECTOR
# ============================================================

BG_COLOR = "#F7F2E8"
CARD_COLOR = "#FFFDF9"
TEXT_COLOR = "#2E3038"
SECONDARY_TEXT = "#75685D"

ACCENT_COLOR = "#8B5E3C"
ACCENT_HOVER = "#70472D"

SAFE_COLOR = "#5A9B7A"
LOW_COLOR = "#4F9DA6"
MEDIUM_COLOR = "#D69A3A"
HIGH_COLOR = "#C76B4B"
CRITICAL_COLOR = "#A94442"

BORDER_COLOR = "#D8CFC2"


# ============================================================
# SCAM ANALYSIS
# ============================================================

def analyze_scam_message(message):

    text = message.strip()

    if not text:
        return {
            "risk": "SAFE",
            "score": 100,
            "reasons": [
                "Please enter a message to analyze."
            ],
            "recommendation":
                "Paste a suspicious message and click Analyze Message."
        }

    lower = text.lower()

    score = 100
    reasons = []

    # --------------------------------------------------------
    # URGENCY
    # --------------------------------------------------------

    urgency_patterns = [
        r"\burgent\b",
        r"\bimmediately\b",
        r"\bact now\b",
        r"\blast chance\b",
        r"\bexpires?\b",
        r"\bdeadline\b",
        r"\baccount.*blocked\b",
        r"\baccount.*suspend"
    ]

    if any(
        re.search(p, lower)
        for p in urgency_patterns
    ):
        score -= 15
        reasons.append(
            "Urgency or pressure language detected."
        )

    # --------------------------------------------------------
    # FINANCIAL / CREDENTIAL
    # --------------------------------------------------------

    financial_patterns = [
        r"\botp\b",
        r"\bpin\b",
        r"\bupi\b",
        r"\bcvv\b",
        r"\bpassword\b",
        r"\bcredit card\b",
        r"\bdebit card\b",
        r"\bbank account\b",
        r"\bnet banking\b",
        r"\brefund\b",
        r"\bcashback\b",
        r"\bpayment\b"
    ]

    if any(
        re.search(p, lower)
        for p in financial_patterns
    ):
        score -= 20
        reasons.append(
            "Financial, OTP or credential-related information detected."
        )

    # --------------------------------------------------------
    # PRIZE / LOTTERY
    # --------------------------------------------------------

    prize_patterns = [
        r"\byou.*won\b",
        r"\byou.*win\b",
        r"\bwon.*prize\b",
        r"\blottery\b",
        r"\bjackpot\b",
        r"\breward\b",
        r"\bfree gift\b",
        r"\bcongratulations\b"
    ]

    if any(
        re.search(p, lower)
        for p in prize_patterns
    ):
        score -= 20
        reasons.append(
            "Prize, lottery or reward-related language detected."
        )

    # --------------------------------------------------------
    # URL
    # --------------------------------------------------------

    urls = re.findall(
        r"(?:https?://|www\.)[^\s]+",
        text,
        flags=re.IGNORECASE
    )

    if urls:

        suspicious_words = [
            "login",
            "verify",
            "verification",
            "secure",
            "security",
            "update",
            "claim",
            "reward",
            "free",
            "bank",
            "wallet"
        ]

        suspicious = False

        for url in urls:

            clean_url = url.rstrip(
                ".,!?;:)"
            )

            if any(
                word in clean_url.lower()
                for word in suspicious_words
            ):
                suspicious = True

            if re.search(
                r"https?://(?:\d{1,3}\.){3}\d{1,3}",
                clean_url,
                re.IGNORECASE
            ):
                suspicious = True

        if suspicious:
            score -= 25
            reasons.append(
                "A potentially suspicious URL was detected."
            )
        else:
            score -= 5
            reasons.append(
                "A URL is present. Verify the destination before opening it."
            )

    # --------------------------------------------------------
    # SOCIAL ENGINEERING
    # --------------------------------------------------------

    social_patterns = [
        r"\bdo not tell anyone\b",
        r"\bkeep this secret\b",
        r"\bshare.*otp\b",
        r"\bsend.*otp\b",
        r"\btell me.*otp\b",
        r"\bclick.*link\b",
        r"\bverify.*now\b",
        r"\bconfirm.*now\b",
        r"\bdownload.*app\b",
        r"\binstall.*app\b",
        r"\bremote access\b",
        r"\banydesk\b",
        r"\bteamviewer\b"
    ]

    if any(
        re.search(p, lower)
        for p in social_patterns
    ):
        score -= 25
        reasons.append(
            "Social-engineering or suspicious-action language detected."
        )

    # --------------------------------------------------------
    # EXCESSIVE !
    # --------------------------------------------------------

    if text.count("!") >= 3:
        score -= 5
        reasons.append(
            "Multiple exclamation marks indicate possible pressure."
        )

    # --------------------------------------------------------
    # FINAL SCORE
    # --------------------------------------------------------

    score = max(
        0,
        min(100, score)
    )

    if score >= 85:
        risk = "SAFE"
    elif score >= 70:
        risk = "LOW"
    elif score >= 50:
        risk = "MEDIUM"
    elif score >= 25:
        risk = "HIGH"
    else:
        risk = "CRITICAL"

    recommendations = {

        "SAFE":
            "No major scam indicators detected. Still verify unexpected messages independently.",

        "LOW":
            "Some caution indicators detected. Avoid sharing sensitive information.",

        "MEDIUM":
            "Multiple warning signs detected. Do not click suspicious links or share credentials.",

        "HIGH":
            "Strong scam indicators detected. Do not click links, send money or share OTP/passwords.",

        "CRITICAL":
            "Very strong scam indicators detected. Do not interact with links, payments or credential requests."
    }

    if not reasons:
        reasons.append(
            "No significant suspicious patterns were detected."
        )

    return {
        "risk": risk,
        "score": score,
        "reasons": reasons,
        "recommendation": recommendations[risk]
    }


# ============================================================
# RISK COLOR
# ============================================================

def get_risk_color(risk):

    return {

        "SAFE": SAFE_COLOR,
        "LOW": LOW_COLOR,
        "MEDIUM": MEDIUM_COLOR,
        "HIGH": HIGH_COLOR,
        "CRITICAL": CRITICAL_COLOR

    }.get(
        risk,
        SECONDARY_TEXT
    )


# ============================================================
# SCAM DETECTOR PAGE
# ============================================================

def scam_detector_page(parent):

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
        fg_color="transparent",
        height=75
    )

    header.pack(
        fill="x",
        padx=35,
        pady=(15, 0)
    )

    header.pack_propagate(False)

    ctk.CTkLabel(
        header,
        text="🕵  Scam Detector",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 27, "bold")
    ).pack(
        anchor="w"
    )

    ctk.CTkLabel(
        header,
        text="Analyze messages for scam and social-engineering indicators",
        text_color=SECONDARY_TEXT,
        font=("Segoe UI", 13)
    ).pack(
        anchor="w",
        pady=(2, 0)
    )

    # ========================================================
    # CONTENT
    # ========================================================

    content = ctk.CTkFrame(
        page,
        fg_color="transparent"
    )

    content.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(5, 15)
    )

    content.grid_columnconfigure(
        0,
        weight=1
    )

    content.grid_columnconfigure(
        1,
        weight=1
    )

    content.grid_rowconfigure(
        0,
        weight=1
    )

    # ========================================================
    # INPUT CARD
    # ========================================================

    input_card = ctk.CTkFrame(
        content,
        fg_color=CARD_COLOR,
        corner_radius=16,
        border_width=1,
        border_color=BORDER_COLOR
    )

    input_card.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=(0, 8)
    )

    ctk.CTkLabel(
        input_card,
        text="Message Analysis",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 19, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(18, 3)
    )

    ctk.CTkLabel(
        input_card,
        text="Paste SMS, WhatsApp or email message",
        text_color=SECONDARY_TEXT,
        font=("Segoe UI", 12)
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 10)
    )

    scam_entry = ctk.CTkTextbox(
        input_card,
        height=185,
        corner_radius=10,
        border_width=1,
        border_color=BORDER_COLOR,
        fg_color="#FFFFFF",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 13),
        wrap="word"
    )

    scam_entry.pack(
        fill="x",
        padx=20,
        pady=(0, 12)
    )

    button_frame = ctk.CTkFrame(
        input_card,
        fg_color="transparent"
    )

    button_frame.pack(
        fill="x",
        padx=20,
        pady=(0, 12)
    )

    # ========================================================
    # RESULT CARD
    # ========================================================

    result_card = ctk.CTkFrame(
        content,
        fg_color=CARD_COLOR,
        corner_radius=16,
        border_width=1,
        border_color=BORDER_COLOR
    )

    result_card.grid(
        row=0,
        column=1,
        sticky="nsew",
        padx=(8, 0)
    )

    ctk.CTkLabel(
        result_card,
        text="Security Assessment",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 19, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(18, 10)
    )

    risk_row = ctk.CTkFrame(
        result_card,
        fg_color="transparent"
    )

    risk_row.pack(
        fill="x",
        padx=20
    )

    ctk.CTkLabel(
        risk_row,
        text="Risk Level",
        text_color=SECONDARY_TEXT,
        font=("Segoe UI", 13)
    ).pack(
        side="left"
    )

    risk_value = ctk.CTkLabel(
        risk_row,
        text="NOT ANALYZED",
        text_color=SECONDARY_TEXT,
        fg_color="#EEE7DE",
        corner_radius=9,
        padx=14,
        pady=5,
        font=("Segoe UI", 12, "bold")
    )

    risk_value.pack(
        side="right"
    )

    score_label = ctk.CTkLabel(
        result_card,
        text="Security Score: --/100",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 15, "bold")
    )

    score_label.pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )

    score_bar = ctk.CTkProgressBar(
        result_card,
        height=11,
        corner_radius=6,
        fg_color="#E6DED4",
        progress_color=SAFE_COLOR
    )

    score_bar.set(0)

    score_bar.pack(
        fill="x",
        padx=20
    )

    ctk.CTkLabel(
        result_card,
        text="Detection Findings",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 14, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(13, 5)
    )

    reasons_box = ctk.CTkTextbox(
        result_card,
        height=95,
        corner_radius=9,
        border_width=1,
        border_color=BORDER_COLOR,
        fg_color="#FFFFFF",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 12),
        wrap="word"
    )

    reasons_box.pack(
        fill="x",
        padx=20
    )

    reasons_box.insert(
        "1.0",
        "Enter a message and click Analyze Message."
    )

    reasons_box.configure(
        state="disabled"
    )

    ctk.CTkLabel(
        result_card,
        text="Security Recommendation",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 14, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(12, 5)
    )

    recommendation = ctk.CTkLabel(
        result_card,
        text="No analysis performed yet.",
        text_color=SECONDARY_TEXT,
        fg_color="#F5EFE7",
        corner_radius=9,
        justify="left",
        anchor="w",
        wraplength=470,
        padx=12,
        pady=10,
        font=("Segoe UI", 12)
    )

    recommendation.pack(
        fill="x",
        padx=20,
        pady=(0, 15)
    )

    # ========================================================
    # ANALYSIS
    # ========================================================

    def run_analysis():

        message = scam_entry.get(
            "1.0",
            "end"
        ).strip()

        result = analyze_scam_message(
            message
        )

        risk = result["risk"]
        score = result["score"]

        color = get_risk_color(
            risk
        )

        # ----------------------------------------------------
        # UPDATE UI
        # ----------------------------------------------------

        risk_value.configure(
            text=risk,
            text_color="#FFFFFF",
            fg_color=color
        )

        score_label.configure(
            text=f"Security Score: {score}/100"
        )

        score_bar.configure(
            progress_color=color
        )

        score_bar.set(
            score / 100
        )

        reasons_box.configure(
            state="normal"
        )

        reasons_box.delete(
            "1.0",
            "end"
        )

        for reason in result["reasons"]:

            reasons_box.insert(
                "end",
                f"• {reason}\n"
            )

        reasons_box.configure(
            state="disabled"
        )

        recommendation.configure(
            text=result["recommendation"],
            text_color=TEXT_COLOR
        )

        # ====================================================
        # SAVE SCAM REPORT
        # ====================================================

        verdict_text = {
            "SAFE":
                "No significant scam indicators were detected.",
            "LOW":
                "Some minor scam indicators were detected.",
            "MEDIUM":
                "Multiple warning signs were detected.",
            "HIGH":
                "Strong scam indicators were detected.",
            "CRITICAL":
                "Very strong scam indicators were detected."
        }.get(
            risk,
            "Security analysis completed."
        )

        save_report(
            scan_type="Scam Detector",
            target=message[:120] if message else "Empty message",
            score=score,
            risk=risk,
            verdict=verdict_text,
            recommendation=result["recommendation"],
            extra={
                "reasons": result["reasons"]
            }
        )

    # ========================================================
    # CLEAR
    # ========================================================

    def clear_analysis():

        scam_entry.delete(
            "1.0",
            "end"
        )

        risk_value.configure(
            text="NOT ANALYZED",
            text_color=SECONDARY_TEXT,
            fg_color="#EEE7DE"
        )

        score_label.configure(
            text="Security Score: --/100"
        )

        score_bar.configure(
            progress_color=SAFE_COLOR
        )

        score_bar.set(0)

        reasons_box.configure(
            state="normal"
        )

        reasons_box.delete(
            "1.0",
            "end"
        )

        reasons_box.insert(
            "1.0",
            "Enter a message and click Analyze Message."
        )

        reasons_box.configure(
            state="disabled"
        )

        recommendation.configure(
            text="No analysis performed yet.",
            text_color=SECONDARY_TEXT
        )

    # ========================================================
    # BUTTONS
    # ========================================================

    ctk.CTkButton(
        button_frame,
        text="🔍  Analyze Message",
        height=42,
        width=175,
        corner_radius=10,
        fg_color=ACCENT_COLOR,
        hover_color=ACCENT_HOVER,
        text_color="#FFFFFF",
        font=("Segoe UI", 13, "bold"),
        command=run_analysis
    ).pack(
        side="left"
    )

    ctk.CTkButton(
        button_frame,
        text="Clear",
        height=42,
        width=100,
        corner_radius=10,
        fg_color="#E8D8C8",
        hover_color="#D9C5B0",
        text_color=TEXT_COLOR,
        font=("Segoe UI", 13),
        command=clear_analysis
    ).pack(
        side="left",
        padx=(10, 0)
    )

    # ========================================================
    # PRIVACY
    # ========================================================

    ctk.CTkLabel(
        page,
        text="🔒 Local analysis • Message content is not uploaded to external APIs",
        text_color=SECONDARY_TEXT,
        font=("Segoe UI", 11)
    ).pack(
        pady=(0, 8)
    )

    return page