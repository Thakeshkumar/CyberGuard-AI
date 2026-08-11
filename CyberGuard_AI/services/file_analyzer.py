"""
CyberGuard AI - File Security Analyzer Service

A clean, read-only local file analyzer.

This builds on the project's existing file_scanner() extension-based risk
approach (Day 9_CyberGuard.py) and extends it with metadata + SHA-256 hashing.

SECURITY GUARANTEES:
  - NEVER executes, modifies, renames, or uploads the selected file.
  - NEVER sends the file to external APIs.
  - NEVER returns file contents.
  - Only reads lightweight metadata and calculates the hash.
  - SHA-256 is computed by reading the file in chunks (no full load to memory).
"""

import hashlib
import os

# =========================
# RISK LEVELS
# =========================

SAFE = "SAFE"
LOW = "LOW"
MEDIUM = "MEDIUM"
HIGH = "HIGH"
CRITICAL = "CRITICAL"


# =========================
# EXTENSION RISK LISTS
# =========================

# High-risk executable / script extensions
HIGH_RISK_EXTENSIONS = {
    ".exe", ".bat", ".cmd", ".js", ".vbs", ".scr", ".pif", ".com",
    ".jar", ".ps1", ".msi", ".dll", ".sh", ".py", ".hta", ".apk",
}

# Medium-risk archive / macro-enabled / document extensions
MEDIUM_RISK_EXTENSIONS = {
    ".zip", ".rar", ".7z", ".tar", ".gz", ".iso", ".dmg",
    ".docm", ".xlsm", ".pptm", ".wsf", ".lnk", ".chm",
}

# Extensions considered generally safe
SAFE_EXTENSIONS = {
    ".txt", ".jpg", ".jpeg", ".png", ".gif", ".mp3", ".mp4",
    ".avi", ".mkv", ".doc", ".docx", ".xls", ".xlsx", ".ppt",
    ".pptx", ".pdf", ".csv", ".md", ".json", ".xml", ".html",
    ".css", ".svg", ".webp", ".bmp", ".wav", ".flac",
}

# Suspicious filenames / keywords
SUSPICIOUS_NAME_KEYWORDS = [
    "invoice", "payment", "receipt", "document", "update", "urgent",
    "password", "scan", "copy", "final", "report", "resume", "image",
    "photo", "details", "account", "secure", "verify", "order",
]

# File size thresholds (bytes)
UNUSUALLY_SMALL = 1024  # 1 KB
UNUSUALLY_LARGE = 50 * 1024 * 1024  # 50 MB


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


def _format_size(size):
    """Format a byte count into a human-readable string."""
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


def _extension_of(filename):
    """Return the lowercase extension of a filename (with dot), or empty."""
    if not filename:
        return ""
    # Handle hidden files like .env -> no extension
    base = os.path.basename(filename)
    if base.startswith(".") and base.count(".") == 1:
        return ""
    if "." in base:
        return "." + base.rsplit(".", 1)[1].lower()
    return ""


def _check_double_extension(filename):
    """Detect double extensions like 'file.pdf.exe'."""
    base = os.path.basename(filename)
    parts = base.split(".")
    return len(parts) >= 3 and parts[0] != ""


def _check_hidden_file(filename):
    """Detect hidden-file indicators."""
    base = os.path.basename(filename)
    return base.startswith(".") or base.startswith("__")


def _check_suspicious_name(filename):
    """Detect suspicious common phishing filenames."""
    base = os.path.basename(filename).lower().replace("_", " ").replace("-", " ")
    return any(kw in base for kw in SUSPICIOUS_NAME_KEYWORDS)


def _sha256_chunked(file_path, chunk_size=1024 * 1024):
    """Compute SHA-256 by reading the file in chunks.

    Chunked reading avoids loading huge files fully into memory.
    Raises OSError on permission/read errors.
    """
    sha = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()


def analyze_file(file_path):
    """
    Analyze a local file (read-only) and return a structured result.

    The file is NEVER executed, modified, uploaded, or read into memory fully.
    File contents are NEVER returned.

    Returns a dict with fields suitable for the UI to render.
    Raises FileNotFoundError / PermissionError for missing/blocked files.
    """
    if not file_path:
        raise ValueError("No file selected.")

    # --- Basic existence / permission checks ---
    if not os.path.exists(file_path):
        raise FileNotFoundError("The selected file does not exist.")

    if not os.path.isfile(file_path):
        raise ValueError("The selected path is not a file.")

    # --- Metadata ---
    file_name = os.path.basename(file_path)
    extension = _extension_of(file_name)
    try:
        file_size = os.path.getsize(file_path)
    except OSError:
        file_size = 0

    # --- SHA-256 (chunked, read-only) ---
    sha256 = _sha256_chunked(file_path)

    # --- Scoring (heuristic) ---
    score = 0
    indicators = []
    checks = []

    # 1. File exists
    checks.append({"name": "File exists", "passed": True})

    # 2. File type identified
    type_identified = bool(extension)
    checks.append({"name": "File type identified", "passed": type_identified})
    if not type_identified:
        score += 5
        indicators.append("File type could not be identified (no known extension).")

    # 3. Extension consistency (matches a known category)
    if extension in HIGH_RISK_EXTENSIONS:
        consistency = True
    elif extension in MEDIUM_RISK_EXTENSIONS:
        consistency = True
    elif extension in SAFE_EXTENSIONS:
        consistency = True
    else:
        consistency = False
    checks.append({"name": "Extension consistency", "passed": consistency})
    if not consistency and extension:
        score += 10
        indicators.append(f"Unusual or uncommon extension detected: {extension}")

    # 4. File size
    checks.append({"name": "File size", "passed": file_size > 0})
    if file_size == 0:
        score += 10
        indicators.append("File is empty (0 bytes).")
    elif file_size < UNUSUALLY_SMALL:
        score += 5
        indicators.append("File is unusually small.")
    elif file_size > UNUSUALLY_LARGE:
        score += 5
        indicators.append("File is unusually large for its type.")

    # 5. SHA-256 hash generated
    checks.append({"name": "SHA-256 hash generated", "passed": bool(sha256)})

    # --- Risk indicators ---
    if extension in HIGH_RISK_EXTENSIONS:
        score += 30
        indicators.append(f"Executable/script file type detected ({extension}).")

    if extension in MEDIUM_RISK_EXTENSIONS:
        score += 15
        indicators.append(f"Archive/macro-enabled file type detected ({extension}).")

    if _check_double_extension(file_name):
        score += 20
        indicators.append("Double extension detected (possible disguised file).")

    if _check_hidden_file(file_name):
        score += 15
        indicators.append("Hidden file indicator detected.")

    if _check_suspicious_name(file_name):
        score += 10
        indicators.append("Suspicious filename detected.")

    # --- Clamp ---
    score = max(0, min(100, score))
    risk = _classify(score)
    security_score = 100 - score

    # --- Verdict (rule-based, NOT a real AI/malware engine) ---
    if risk == SAFE:
        verdict = "Local analysis indicates low risk based on the detected file characteristics."
    elif risk == LOW:
        verdict = "The file shows minor characteristics that warrant a quick review."
    elif risk == MEDIUM:
        verdict = "The file has some characteristics commonly associated with risky files."
    elif risk == HIGH:
        verdict = "The file type or characteristics are high-risk. Avoid executing it."
    else:
        verdict = "The file shows critical risk characteristics. Do not open it."

    # --- Recommendation ---
    if risk in (HIGH, CRITICAL):
        recommendation = "Do not execute this file. Verify the source and scan it with a trusted antivirus solution."
    elif risk == MEDIUM:
        recommendation = "Verify the file source before opening. Scan with a trusted antivirus solution."
    elif risk == LOW:
        recommendation = "Exercise caution. Confirm the file is from a trusted sender before opening."
    else:
        recommendation = "File appears safe. Always verify the source of downloaded files before opening."

    return {
        "file_name": file_name,
        "file_type": extension.lstrip(".").upper() if extension else "Unknown",
        "file_size": file_size,
        "file_size_text": _format_size(file_size),
        "extension": extension if extension else "None",
        "sha256": sha256,
        "risk_level": risk,
        "security_score": security_score,
        "checks": checks,
        "indicators": indicators,
        "verdict": verdict,
        "recommendation": recommendation,
        "is_demo": True,  # Local heuristic only, not a real malware engine
    }