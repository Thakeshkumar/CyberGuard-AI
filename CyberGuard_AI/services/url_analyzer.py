"""
CyberGuard AI - URL Security Analyzer Service

A clean, structured URL analysis service.

NOTE: This is a HEURISTIC / DEMO analyzer based on the project's existing
console-based url_analyzer() logic (Day 9_CyberGuard.py). It performs local
pattern checks only and does NOT make external API calls.

It is structured as a service interface so it can later be connected to real
threat-intelligence backends (VirusTotal, URLScan.io, Google Safe Browsing,
SSL certificate checks, redirect analysis, etc.) without changing the UI.
"""

import re
from urllib.parse import urlparse

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

# Suspicious keywords commonly used in phishing / malicious URLs
SUSPICIOUS_KEYWORDS = [
    "login", "verify", "update", "bank", "secure", "account",
    "password", "confirm", "billing", "webscr", "signin", "auth",
]

# URL-shortening domains
URL_SHORTENERS = [
    "bit.ly", "tinyurl.com", "goo.gl", "t.co", "is.gd", "buff.ly",
    "ow.ly", "rebrand.ly", "cutt.ly", "shorturl.at", "rb.gy",
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


def _recommendation(risk, indicators):
    """Build a suggestion based on the detected risk level."""
    if risk == SAFE:
        return "No obvious suspicious indicators detected. The URL appears safe to browse."
    if risk == LOW:
        return "Minor concerns detected. Review the highlighted indicators before proceeding."
    if risk == MEDIUM:
        return "Multiple suspicious indicators found. Avoid entering any personal information."
    if risk == HIGH:
        return "Strong signs of a potentially malicious URL. Do NOT open or share this link."
    return "Critical threat indicators detected. Block this URL immediately and report it."


def _ai_verdict(risk):
    """Generate a human-readable AI verdict summary."""
    if risk == SAFE:
        return "The URL passed local heuristic checks. No immediate red flags were found."
    if risk == LOW:
        return "The URL looks mostly normal, but a few indicators deserve a closer look."
    if risk == MEDIUM:
        return "The URL shows a mix of normal and suspicious signals. Proceed with caution."
    if risk == HIGH:
        return "The URL strongly resembles common phishing or malicious patterns. Do not trust it."
    return "The URL contains critical risk markers. Treat it as malicious until proven otherwise."


def is_valid_url(url):
    """Quick validation that the input looks like a URL."""
    if not url or not isinstance(url, str):
        return False
    url = url.strip()
    if not url:
        return False
    # Must start with http:// or https:// and contain a domain
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    parsed = urlparse(url)
    return bool(parsed.netloc and "." in parsed.netloc)


def analyze_url(url):
    """
    Analyze a URL and return a structured result dictionary.

    This is a DEMO / PLACEHOLDER heuristic analyzer. It does NOT perform
    real external security checks. It is structured so a real backend can
    be connected later (see the TODO list below).

    Returns a dict with fields suitable for the UI to render.
    """
    url = url.strip()

    # --- Normalize ---
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url

    parsed = urlparse(url)
    scheme = parsed.scheme
    domain = parsed.netloc
    # Strip port if present for display
    if ":" in domain:
        display_domain = domain.split(":")[0]
    else:
        display_domain = domain

    score = 0
    indicators = []

    # --- 1. HTTPS status ---
    https_status = "SECURE" if scheme == "https" else "NOT SECURE"
    if scheme != "https":
        score += 20
        indicators.append("Connection is not using HTTPS (data is unencrypted).")

    # --- 2. URL length ---
    if len(url) > 75:
        score += 15
        indicators.append("URL is unusually long for a legitimate site.")
    elif len(url) > 50:
        score += 8
        indicators.append("URL length is above average.")

    # --- 3. @ symbol ---
    if "@" in url:
        score += 25
        indicators.append("URL contains an '@' symbol, often used to hide the real destination.")

    # --- 4. IP-based URL ---
    ip_pattern = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")
    is_ip = bool(ip_pattern.match(display_domain))
    if is_ip:
        score += 20
        indicators.append("URL uses a raw IP address instead of a domain name.")

    # --- 5. Number of subdomains ---
    subdomain_parts = display_domain.split(".") if not is_ip else []
    if len(subdomain_parts) >= 4:
        score += 15
        indicators.append("Excessive number of subdomains detected.")
    elif len(subdomain_parts) == 3:
        score += 5
        indicators.append("Multiple subdomains detected.")

    # --- 6. Suspicious keywords ---
    found_keywords = [w for w in SUSPICIOUS_KEYWORDS if w in url.lower()]
    if found_keywords:
        score += 15
        indicators.append(
            "Contains suspicious keyword(s): " + ", ".join(found_keywords) + "."
        )

    # --- 7. URL shortener ---
    if any(short in display_domain.lower() for short in URL_SHORTENERS):
        score += 10
        indicators.append("URL is shortened, hiding the true destination.")

    # --- 8. Suspicious characters ---
    suspicious_chars = []
    for ch in ["%", "\\", ";", "..", "=="]:
        if ch in url:
            suspicious_chars.append(ch)
    if suspicious_chars:
        score += 10
        indicators.append(
            "URL contains suspicious character(s): " + " ".join(suspicious_chars) + "."
        )

    # --- 9. Port in URL (non-standard) ---
    if ":" in domain and not domain.endswith((":80", ":443")):
        score += 10
        indicators.append("URL uses a non-standard port, which can indicate a malicious host.")

    # --- Clamp score to 0-100 ---
    score = max(0, min(100, score))

    risk = _classify(score)
    security_score = 100 - score

    return {
        "url": url,
        "scheme": scheme,
        "https_status": https_status,
        "domain": display_domain,
        "is_ip": is_ip,
        "indicators": indicators,
        "risk": risk,
        "risk_score": score,
        "security_score": security_score,
        "ai_verdict": _ai_verdict(risk),
        "recommendation": _recommendation(risk, indicators),
        "is_demo": True,  # Marks this as heuristic/DEMO analysis
    }


# Future backend integration points (TO BE IMPLEMENTED):
# - HTTPS validation via SSL certificate inspection
# - Domain reputation API (VirusTotal, URLScan.io, Google Safe Browsing)
# - Redirect chain analysis
# - Threat intelligence API calls
# - Real-time domain/IP reputation scores