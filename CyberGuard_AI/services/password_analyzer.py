"""
CyberGuard AI - Password Security Analyzer Service

A clean, structured local heuristic password analyzer.

NOTE: This is a pure local heuristic analysis. It does NOT:
  - Store, log, save, or transmit the password
  - Perform breach/database checks (no real backend exists)
  - Use external APIs

Security guarantee: the password is used only during analysis and is
immediately discarded. It is never written to files, history, logs, or
included in any returned result data.
"""

import re

# =========================
# STRENGTH TIERS
# =========================

VERY_WEAK = "VERY WEAK"
WEAK = "WEAK"
MODERATE = "MODERATE"
STRONG = "STRONG"
VERY_STRONG = "VERY STRONG"

SPECIAL_CHARS = frozenset("@#$%^&*!?_-+=()[]{}<>~")


def _check_repeated_chars(password):
    """Detect repeated characters (e.g. 'aaa', '111')."""
    return bool(re.search(r"(.)\1{2,}", password))


def _check_sequential_chars(password):
    """Detect sequential patterns like 'abc' or '123'."""
    lowered = password.lower()
    for i in range(len(lowered) - 2):
        a, b, c = lowered[i], lowered[i + 1], lowered[i + 2]
        if ord(a) + 1 == ord(b) and ord(b) + 1 == ord(c):
            return True
    return False


def _check_common_patterns(password):
    """Detect common weak patterns."""
    common = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "letmein", "admin", "welcome", "monkey", "dragon",
        "iloveyou", "password1", "qwerty123",
    ]
    lowered = password.lower()
    return lowered in common or all(ord(c) in (50, 51, 52, 53, 54, 55, 56, 57) for c in lowered[:4])


def analyze_password(password):
    """
    Analyze a password locally and return a structured result.

    The password itself is NEVER included in the returned dictionary.
    Returns: {
        "strength": str,
        "score": int (0-100),
        "checks": [ {name, passed} ... ],
        "warnings": [str...],
        "recommendations": [str...]
    }
    """
    if not isinstance(password, str):
        password = ""

    length = len(password)
    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    special = sum(1 for c in password if c in SPECIAL_CHARS)
    other = length - (upper + lower + digits + special)

    score = 0
    warnings = []

    # ---------- Scoring ----------
    # Length (up to 30 points)
    if length >= 16:
        score += 30
    elif length >= 12:
        score += 24
    elif length >= 8:
        score += 15
    elif length >= 6:
        score += 8
        warnings.append("Password is too short (6-7 characters). Use at least 8.")
    else:
        warnings.append("Password is too short. Use at least 8 characters.")

    # Character variety (up to 50 points)
    if upper > 0:
        score += 12
    if lower > 0:
        score += 10
    if digits > 0:
        score += 12
    if special > 0:
        score += 16

    # Missing character warnings
    if upper == 0:
        warnings.append("Missing uppercase characters.")
    if lower == 0:
        warnings.append("Missing lowercase characters.")
    if digits == 0:
        warnings.append("Missing numbers.")
    if special == 0:
        warnings.append("Missing special characters.")

    # Character variety bonus (up to 10)
    unique_chars = len(set(password))
    if unique_chars >= 10:
        score += 10
    elif unique_chars >= 6:
        score += 5

    # ---------- Penalties ----------
    if _check_common_patterns(password):
        score -= 20
        warnings.append("Common password pattern detected.")

    if _check_repeated_chars(password):
        score -= 10
        warnings.append("Repeated characters detected.")

    if _check_sequential_chars(password):
        score -= 10
        warnings.append("Sequential characters detected (e.g. abc, 123).")

    if other > 0 and score < 100:
        # Non-standard characters add complexity but aren't required
        score += 2

    # ---------- Clamp ----------
    score = max(0, min(100, score))

    # ---------- Strength tier ----------
    if score >= 90:
        strength = VERY_STRONG
    elif score >= 75:
        strength = STRONG
    elif score >= 55:
        strength = MODERATE
    elif score >= 35:
        strength = WEAK
    else:
        strength = VERY_WEAK

    # ---------- Checks (for UI checklist) ----------
    checks = [
        {"name": "Length (at least 8 characters)", "passed": length >= 8},
        {"name": "Uppercase characters", "passed": upper > 0},
        {"name": "Lowercase characters", "passed": lower > 0},
        {"name": "Numbers", "passed": digits > 0},
        {"name": "Special characters", "passed": special > 0},
        {"name": "Character variety", "passed": unique_chars >= 6},
    ]

    # ---------- Recommendations ----------
    recommendations = []
    if length < 8:
        recommendations.append("Use at least 8 characters — longer passwords are harder to crack.")
    elif length < 12:
        recommendations.append("Consider a password of 12+ characters for stronger protection.")
    if upper == 0:
        recommendations.append("Add at least one uppercase letter (A-Z).")
    if lower == 0:
        recommendations.append("Add at least one lowercase letter (a-z).")
    if digits == 0:
        recommendations.append("Add at least one number (0-9).")
    if special == 0:
        recommendations.append("Add at least one special character (@, #, $, %, etc.).")
    if _check_common_patterns(password):
        recommendations.append("Avoid common passwords or patterns like 'password' or '123456'.")
    if _check_repeated_chars(password):
        recommendations.append("Avoid repeated characters (e.g. 'aaa' or '111').")
    if _check_sequential_chars(password):
        recommendations.append("Avoid sequential patterns like 'abc' or '123'.")
    if strength in (STRONG, VERY_STRONG):
        recommendations.append("Great job! Keep using unique passwords for every account.")
    recommendations.append("Enable two-factor authentication (2FA) wherever possible.")

    return {
        "strength": strength,
        "score": score,
        "checks": checks,
        "warnings": warnings,
        "recommendations": recommendations,
    }