"""
CyberGuard AI - Scam Detector Service

A clean, structured local heuristic scam analyzer.

This service analyzes text messages for common scam and social engineering
indicators. It integrates with the existing `url_analyzer` service to
evaluate any URLs found within the message.

SECURITY GUARANTEES:
  - Local heuristic analysis only.
  - NEVER uploads message content or sends it to external APIs.
  - NEVER returns full message content (only lightweight metadata).
"""

import re
from services.url_analyzer import analyze_url

# =========================
# RISK LEVELS
# =========================

SAFE = "SAFE"
LOW = "LOW"
MEDIUM = "MEDIUM"
HIGH = "HIGH"
CRITICAL = "CRITICAL"

# =========================
# HEURISTIC RULES
# =========================

# Keywords for various scam types and social engineering tactics
CREDENTIAL_REQUESTS = [
    "otp", "one-time password", "password", "pin", "cvv", "security question",
    "login", "credentials", "verify your identity", "account verification",
]

FINANCIAL_REQUESTS = [
    "bank account", "credit card", "debit card", "wire transfer", "payment",
    "transfer money", "send money", "upi", "paypal", "venmo", "zelle",
    "processing fee", "shipping fee", "customs fee", "tax", "refund",
    "investment", "cryptocurrency", "bitcoin", "wallet", "mining", "forex",
]

URGENCY_THREATS = [
    "urgent", "immediately", "asap", "act now", "within 24 hours", "final notice",
    "account will be suspended", "suspended", "locked", "blocked", "terminated",
    "legal action", "lawsuit", "investigation", "arrest warrant", "court order",
    "limited time", "expires soon", "don't miss out",
]

PRIZE_CLAIMS = [
    "you won", "prize", "lottery", "reward", "gift card", "congratulations",
    "claim your", "inheritance", "winner", "giveaway", "jackpot",
]

IMPERSONATION_INDICATORS = [
    "apple support", "microsoft support", "amazon support", "google support",
    "irs", "social security administration", "federal bureau of investigation",
    "police", "delivery service", "ups", "fedex", "dhl", "usps",
    "your bank", "bank of america", "wells fargo", "chase bank",
]

ATTACHMENT_DOWNLOAD_REQUESTS = [
    "attachment", "download", "open the file", "invoice.pdf", "document.pdf",
    "receipt.pdf", "scan the file", "enable macros", "click to view",
]

SUSPICIOUS_LINK_PHRASES = [
    "click here", "update your info", "verify your account", "secure your account",
    "track your package", "view invoice", "reset password", "confirm details",
]


def _classify(score):
    """Map a heuristic threat score (0-100) to a risk level."""
    if score <= 20:
        return SAFE
    elif score <= 40:
        return LOW
    elif score <= 60:
        return MEDIUM
    elif score <= 80:
        return HIGH
    return CRITICAL


def _extract_urls(text):
    """Extract URLs from text using regex."""
    # Regex to find http(s):// followed by non-whitespace characters
    url_pattern = re.compile(r"https?://[^\s<>'\"\]]+")
    return url_pattern.findall(text)


def _get_message_type(message, indicators):
    """Heuristically determine the message type based on content and indicators."""
    message_lower = message.lower()

    if any(kw in message_lower for kw in URGENCY_THREATS):
        if any(kw in message_lower for kw in CREDENTIAL_REQUESTS + FINANCIAL_REQUESTS):
            return "Account/Security Message"
        return "Urgent Alert"
    if any(kw in message_lower for kw in PRIZE_CLAIMS):
        return "Promotional/Prize Message"
    if any(kw in message_lower for kw in FINANCIAL_REQUESTS):
        return "Financial Message"
    if any(kw in message_lower for kw in IMPERSONATION_INDICATORS):
        return "Impersonation Attempt"
    if any(kw in message_lower for kw in ATTACHMENT_DOWNLOAD_REQUESTS):
        return "Attachment/Download Request"
    if any(kw in message_lower for kw in ["job offer", "hiring", "interview", "resume"]):
        return "Job/Investment Message"
    if any(kw in message_lower for kw in ["delivery", "package", "tracking", "shipment"]):
        return "Delivery Message"
    if any(kw in message_lower for kw in ["discount", "sale", "offer", "promotion"]):
        return "Promotional Message"

    if len(indicators) > 3:
        return "Potential Scam"
    if len(message) < 50:
        return "Short Message"

    return "General Message"


def analyze_scam(message):
    """
    Analyze a message locally for scam and social engineering indicators.

    The message itself is NEVER included in the returned dictionary.

    Args:
        message (str): The text message content to analyze.

    Returns:
        dict: A structured result containing analysis details.
    """
    if not isinstance(message, str) or not message.strip():
        raise ValueError("Message cannot be empty.")

    original_message = message
    message_lower = message.lower()

    score = 0
    indicators = []
    recommendations = []
    links_details = []

    # --- 1. Keyword-based Indicators ---

    # Credential requests
    found_creds = [kw for kw in CREDENTIAL_REQUESTS if kw in message_lower]
    if found_creds:
        score += 25
        indicators.append(f"Credential/OTP request detected: {', '.join(found_creds[:2])}.")
        recommendations.append("Never share passwords, OTPs, or PINs.")

    # Financial requests
    found_financial = [kw for kw in FINANCIAL_REQUESTS if kw in message_lower]
    if found_financial:
        score += 20
        indicators.append(f"Financial/payment request detected: {', '.join(found_financial[:2])}.")
        recommendations.append("Verify financial requests through official channels before acting.")

    # Urgency/Threats
    found_urgency = [kw for kw in URGENCY_THREATS if kw in message_lower]
    if found_urgency:
        score += 15
        indicators.append(f"Urgency/threat language detected: {', '.join(found_urgency[:2])}.")
        recommendations.append("Be wary of messages creating a sense of urgency or fear.")

    # Prize/Reward claims
    found_prize = [kw for kw in PRIZE_CLAIMS if kw in message_lower]
    if found_prize:
        score += 15
        indicators.append(f"Prize/reward claim detected: {', '.join(found_prize[:2])}.")
        recommendations.append("Legitimate lotteries or giveaways do not ask for upfront payments.")

    # Impersonation
    found_impersonation = [kw for kw in IMPERSONATION_INDICATORS if kw in message_lower]
    if found_impersonation:
        score += 10
        indicators.append(f"Possible impersonation attempt detected: {', '.join(found_impersonation[:2])}.")
        recommendations.append("Always verify the sender's identity through an independently confirmed official channel.")

    # Attachment/Download requests
    found_attachments = [kw for kw in ATTACHMENT_DOWNLOAD_REQUESTS if kw in message_lower]
    if found_attachments:
        score += 10
        indicators.append(f"Request to open/download files detected: {', '.join(found_attachments[:2])}.")
        recommendations.append("Do not open or download unexpected attachments from unknown senders.")

    # Suspicious link phrases
    found_link_phrases = [kw for kw in SUSPICIOUS_LINK_PHRASES if kw in message_lower]
    if found_link_phrases:
        score += 5
        indicators.append(f"Suspicious link-related phrase detected: {', '.join(found_link_phrases[:2])}.")

    # --- 2. URL Extraction and Analysis (reusing url_analyzer) ---
    urls = _extract_urls(original_message)
    suspicious_links_count = 0

    for url in urls:
        url_analysis_result = analyze_url(url)
        links_details.append({
            "url": url,
            "domain": url_analysis_result["domain"],
            "scheme": url_analysis_result["scheme"],
            "https": url_analysis_result["https_status"],
            "risk": url_analysis_result["risk"],
            "security_score": url_analysis_result["security_score"],
        })
        if url_analysis_result["risk"] in (MEDIUM, HIGH, CRITICAL):
            suspicious_links_count += 1
            indicators.append(f"Suspicious link detected: {url_analysis_result['url']}")
            recommendations.append("Do not click on suspicious links. Manually type the official website address.")

    if suspicious_links_count == 1:
        score += 15
    elif suspicious_links_count >= 2:
        score += 30

    # --- 3. Social Engineering Patterns (combined indicators) ---
    # High risk if urgency + credential/financial request + suspicious link
    if (found_urgency and (found_creds or found_financial) and suspicious_links_count > 0):
        score += 20
        indicators.append("Strong social engineering pattern detected (urgency + sensitive request + suspicious link).")

    # --- 4. General message characteristics ---
    if len(original_message) > 500: # Very long messages can sometimes be spam/scam
        score += 5
        indicators.append("Message is unusually long.")
    if re.search(r"[!?]{3,}", original_message): # Excessive punctuation
        score += 5
        indicators.append("Excessive punctuation detected.")

    # --- Clamp score to 0-100 ---
    score = max(0, min(100, score))

    # --- Determine Risk Level ---
    risk_level = _classify(score)
    security_score = 100 - score

    # --- Determine Message Type ---
    message_type = _get_message_type(original_message, indicators)

    # --- Generate AI Verdict ---
    if risk_level == SAFE:
        verdict = "Local analysis found no significant suspicious indicators. The message appears safe."
    elif risk_level == LOW:
        verdict = "Local analysis found a few minor indicators. Review the message carefully before acting."
    elif risk_level == MEDIUM:
        verdict = "Local analysis detected several suspicious indicators. Treat this message with caution."
    elif risk_level == HIGH:
        verdict = "Local analysis detected strong social-engineering indicators. Do not trust this message."
    else: # CRITICAL
        verdict = "Local analysis found critical threat indicators. This message is highly likely a scam. Do NOT interact with it."

    # --- Final Recommendations (ensure uniqueness) ---
    final_recommendations = list(dict.fromkeys(recommendations)) # Remove duplicates
    if not final_recommendations:
        final_recommendations.append("No specific recommendations needed based on current analysis.")
    if risk_level in (MEDIUM, HIGH, CRITICAL):
        final_recommendations.append("If unsure, contact the sender via an independently verified official channel (not using contact info from the message).")
        final_recommendations.append("Report suspicious messages to your service provider or relevant authorities.")

    return {
        "message_type": message_type,
        "risk_level": risk_level,
        "security_score": security_score,
        "indicators": indicators,
        "links": links_details,
        "verdict": verdict,
        "recommendation": "\n".join(final_recommendations),
        "indicator_count": len(indicators),
        "is_demo": True, # Marks this as heuristic/DEMO analysis
    }