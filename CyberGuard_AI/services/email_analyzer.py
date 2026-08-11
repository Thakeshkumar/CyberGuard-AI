"""
CyberGuard AI - Email Security Analyzer Service

A clean, structured local heuristic email analyzer.

This builds on the project's existing email_analyzer() approach
(Day 9_CyberGuard.py) and extends it with subject/body/header analysis and
URL extraction (reusing services/url_analyzer.py for link indicators).

SECURITY GUARANTEES:
  - Local heuristic analysis only.
  - NEVER uploads email content or sends it to external APIs.
  - NEVER returns full email body content (only lightweight metadata).
  - SPF/DKIM/DMARC are ONLY reported when actually present in supplied headers.
"""

import re
from urllib.parse import urlparse

from services.url_analyzer import urlparse as _urlparse, analyze_url

# We need urlparse for domain extraction; reuse the service's helpers.
from services.url_analyzer import SUSPICIOUS_KEYWORDS as _URL_SUSPICIOUS_KEYWORDS

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

# Suspicious subject phrases (indicators only, NOT proof of fraud)
SUBJECT_INDICATORS = [
    "urgent", "action required", "account will be suspended", "suspended",
    "verify your account", "you won", "payment required", "payment",
    "password reset", "reset your password", "confirm your identity",
    "account locked", "unusual activity", "security alert", "final notice",
    "act now", "limited time", "claim your", "prize", "lottery", "gift card",
    "reward", "refund", "overdue", "invoice", "wire transfer",
]

# Suspicious content phrases (indicators only)
CONTENT_INDICATORS = [
    "urgent", "immediately", "asap", "act now", "within 24 hours",
    "account will be suspended", "suspended", "locked", "verify your account",
    "verify your identity", "password", "otp", "one-time password",
    "bank account", "payment", "wire transfer", "credit card", "debit card",
    "social security", "personal information", "ssn", "atm", "cvv",
    "click here", "login", "credentials", "unusual activity",
    "you won", "prize", "lottery", "reward", "gift card", "congratulations",
    "inheritance", "refund", "investment", "guaranteed", "risk-free",
    "money back", "attachment", "download", "malware", "phishing", "scam",
]

# Fear / threat / urgency language
FEAR_INDICATORS = [
    "account will be suspended", "suspended", "locked", "illegal activity",
    "legal action", "lawsuit", "investigation", "terminated", "will be closed",
    "verify your identity immediately",
]

# Credential / sensitive info requests
CREDENTIAL_INDICATORS = [
    "password", "otp", "one-time password", "credentials", "login",
    "verification code", "pin", "cvv", "security question",
]

# Payment / financial requests
PAYMENT_INDICATORS = [
    "payment", "wire transfer", "bank account", "credit card", "debit card",
    "refund", "invoice", "overdue", "money", "western union",
]

# Reward / prize language
PRIZE_INDICATORS = [
    "you won", "prize", "lottery", "reward", "gift card", "congratulations",
    "claim your", "inheritance", "winner",
]

# Suspicious attachments mentioned
ATTACHMENT_INDICATORS = [
    "attachment", "download", "open the file", "invoice.pdf", "document.pdf",
    "receipt.pdf", "scan the file", "enable macros",
]

# Suspicious sender domains (common free/webmail that are frequent in phishing)
SUSPICIOUS_SENDER_DOMAINS = [
    "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com",
    "live.com", "mail.com", "protonmail.com", "yandex.com", "icloud.com",
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


def _is_valid_email(email):
    """Simple email format check."""
    if not email or not isinstance(email, str):
        return False
    email = email.strip()
    if "@" not in email:
        return False
    local, domain = email.rsplit("@", 1)
    if not bool(local) or "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith(".") or ".." in domain:
        return False
    # Domain labels: letters, digits, hyphens (hyphens not at start/end)
    labels = domain.split(".")
    for label in labels:
        if not label:
            return False
        if label.startswith("-") or label.endswith("-"):
            return False
        if not all(c.isalnum() or c == "-" for c in label):
            return False
    return True


def _domain_of(email):
    """Extract the domain from an email address."""
    if not email or "@" not in email:
        return ""
    return email.rsplit("@", 1)[1].strip().lower()


def _extract_urls(body):
    """Extract URLs from email body text using regex."""
    url_pattern = re.compile(r"https?://[^\s<>'\"\]]+")
    return url_pattern.findall(body)


def _analyze_headers(headers):
    """
    Analyze optional raw email headers.

    Returns a dict with fields only for headers that are actually present.
    SPF/DKIM/DMARC are NEVER invented.
    """
    result = {
        "available": False,
        "from": None,
        "to": None,
        "reply_to": None,
        "return_path": None,
        "message_id": None,
        "spf": "UNKNOWN",
        "dkim": "UNKNOWN",
        "dmarc": "UNKNOWN",
        "parsed_lines": [],
    }

    if not headers or not headers.strip():
        result["available"] = False
        return result

    result["available"] = True
    auth_blob = ""

    for line in headers.splitlines():
        lower = line.lower()
        result["parsed_lines"].append(line.strip())

        if lower.startswith("from:"):
            result["from"] = line.split(":", 1)[1].strip()
        elif lower.startswith("to:"):
            result["to"] = line.split(":", 1)[1].strip()
        elif lower.startswith("reply-to:"):
            result["reply_to"] = line.split(":", 1)[1].strip()
        elif lower.startswith("return-path:"):
            result["return_path"] = line.split(":", 1)[1].strip()
        elif lower.startswith("message-id:"):
            result["message_id"] = line.split(":", 1)[1].strip()
        elif lower.startswith("authentication-results:"):
            auth_blob += line.split(":", 1)[1].strip() + " "

    # Parse authentication-results (only if actually present)
    if auth_blob:
        auth_lower = auth_blob.lower()
        for mechanism, key in [("spf", "spf"), ("dkim", "dkim"), ("dmarc", "dmarc")]:
            if key in auth_lower:
                # Check for pass/fail
                if re.search(rf"{key}\s*=\s*pass", auth_lower):
                    result[mechanism] = "PASS"
                elif re.search(rf"{key}\s*=\s*fail", auth_lower):
                    result[mechanism] = "FAIL"
                elif re.search(rf"{key}\s*=\s*(softfail|neutral|none)", auth_lower):
                    result[mechanism] = "UNKNOWN"
                else:
                    result[mechanism] = "PRESENT"
            else:
                result[mechanism] = "UNKNOWN"
    else:
        result["spf"] = "UNKNOWN"
        result["dkim"] = "UNKNOWN"
        result["dmarc"] = "UNKNOWN"

    return result


def analyze_email(sender, recipient, subject, body, headers=""):
    """
    Analyze an email locally (heuristic) and return a structured result.

    This is DEMO/heuristic analysis — it does NOT confirm phishing or
    guarantee safety. The full body is NEVER returned (only indicators, links,
    and metadata).
    """
    sender = (sender or "").strip()
    recipient = (recipient or "").strip()
    subject = (subject or "").strip()
    body = (body or "").strip()

    score = 0
    indicators = []

    # ---------- Sender / recipient validation ----------
    sender_valid = _is_valid_email(sender)
    recipient_valid = _is_valid_email(recipient)

    if not sender:
        indicators.append("Missing sender email.")
        score += 15
    elif not sender_valid:
        indicators.append("Invalid sender email format.")
        score += 15

    if not recipient:
        indicators.append("Missing recipient email.")
        score += 5
    elif not recipient_valid:
        indicators.append("Invalid recipient email format.")
        score += 5

    sender_domain = _domain_of(sender)
    if sender_valid and sender_domain in SUSPICIOUS_SENDER_DOMAINS:
        indicators.append(
            f"Suspicious/free-mail sender domain detected: {sender_domain}"
        )
        score += 10

    # ---------- Subject analysis ----------
    subject_lower = subject.lower()
    found_subject_indicators = [
        phrase for phrase in SUBJECT_INDICATORS if phrase in subject_lower
    ]
    if found_subject_indicators:
        indicators.append(
            "Suspicious subject language: " + ", ".join(found_subject_indicators[:3]) + "."
        )
        score += min(10 + 10 * len(found_subject_indicators), 30)

    # Excessive punctuation in subject
    if re.search(r"[!?]{3,}", subject):
        indicators.append("Excessive punctuation detected in subject.")
        score += 5

    # ---------- Body analysis ----------
    body_lower = body.lower()

    found_fear = [p for p in FEAR_INDICATORS if p in body_lower]
    if found_fear:
        indicators.append("Fear/threat language detected: " + ", ".join(found_fear[:3]) + ".")
        score += min(10 + 10 * len(found_fear), 30)

    found_credentials = [p for p in CREDENTIAL_INDICATORS if p in body_lower]
    if found_credentials:
        indicators.append("Credential/OTP request detected: " + ", ".join(found_credentials[:3]) + ".")
        score += 15

    found_payment = [p for p in PAYMENT_INDICATORS if p in body_lower]
    if found_payment:
        indicators.append("Payment/banking request detected: " + ", ".join(found_payment[:3]) + ".")
        score += 15

    found_prize = [p for p in PRIZE_INDICATORS if p in body_lower]
    if found_prize:
        indicators.append("Reward/prize language detected: " + ", ".join(found_prize[:3]) + ".")
        score += 15

    found_attachment = [p for p in ATTACHMENT_INDICATORS if p in body_lower]
    if found_attachment:
        indicators.append("Suspicious attachment reference detected.")
        score += 10

    # Social engineering pattern (combination of urgency + request)
    if (found_fear or "urgent" in body_lower) and (found_credentials or found_payment):
        indicators.append("Possible social engineering pattern detected (urgency + request).")
        score += 10

    # ---------- URL extraction (reuse url_analyzer service) ----------
    urls = _extract_urls(body)
    link_details = []
    suspicious_links = 0

    for url in urls:
        info = analyze_url(url)  # reuse the URL analyzer service
        link_details.append({
            "url": url,
            "domain": info["domain"],
            "scheme": info["scheme"],
            "https": info["https_status"],
            "risk": info["risk"],
            "security_score": info["security_score"],
        })
        if info["risk"] in ("MEDIUM", "HIGH", "CRITICAL"):
            suspicious_links += 1
            indicators.append(f"Suspicious link detected: {url}")

    if suspicious_links == 1:
        score += 10
    elif suspicious_links >= 2:
        score += 20

    # ---------- Header analysis ----------
    auth = _analyze_headers(headers)

    if auth["available"]:
        if auth["spf"] == "FAIL":
            indicators.append("SPF authentication result: FAIL.")
            score += 15
        if auth["dkim"] == "FAIL":
            indicators.append("DKIM authentication result: FAIL.")
            score += 15
        if auth["dmarc"] == "FAIL":
            indicators.append("DMARC authentication result: FAIL.")
            score += 15
    else:
        # Do not invent results
        pass

    # ---------- Clamp ----------
    score = max(0, min(100, score))
    risk = _classify(score)
    security_score = 100 - score

    # ---------- Verdict (rule-based, NOT a real AI model) ----------
    if risk == SAFE:
        verdict = "Local analysis found no significant suspicious indicators."
    elif risk == LOW:
        verdict = "Local analysis found a few minor indicators worth reviewing."
    elif risk == MEDIUM:
        verdict = "Local analysis detected several suspicious indicators. Treat this email with caution."
    elif risk == HIGH:
        verdict = "Local analysis detected multiple social-engineering indicators. Do not trust this email."
    else:
        verdict = "Local analysis found critical threat indicators. Do not open, click, or reply to this email."

    # ---------- Recommendation ----------
    recommendations = []
    if risk in (HIGH, CRITICAL):
        recommendations.append("Do not click any links or open attachments.")
    if "Credential" in " ".join(indicators) or "OTP" in body:
        recommendations.append("Never share passwords, OTPs, or verification codes.")
    if "Payment" in " ".join(indicators):
        recommendations.append("Do not send money or provide banking details.")
    if risk in (MEDIUM, HIGH, CRITICAL):
        recommendations.append("Verify the sender through an official website or channel.")
        recommendations.append("Avoid opening unexpected attachments.")
        recommendations.append("Contact the organization directly using a known official number.")
    recommendations.append("Do not share personal information via email.")

    return {
        "sender": sender,
        "recipient": recipient,
        "subject": subject,
        "sender_valid": sender_valid,
        "recipient_valid": recipient_valid,
        "sender_domain": sender_domain,
        "risk_level": risk,
        "security_score": security_score,
        "indicators": indicators,
        "links": link_details,
        "authentication": auth,
        "verdict": verdict,
        "recommendation": " ".join(dict.fromkeys(recommendations)),
        "is_demo": True,  # local heuristic only
    }