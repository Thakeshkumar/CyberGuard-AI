import json
import os
from datetime import datetime


# ============================================================
# CYBERGUARD AI - CENTRAL REPORT STORE
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

REPORT_FILE = os.path.join(
    DATA_DIR,
    "reports.json"
)


# ============================================================
# STORAGE SETUP
# ============================================================

def _ensure_storage():
    os.makedirs(
        DATA_DIR,
        exist_ok=True
    )

    if not os.path.exists(REPORT_FILE):
        with open(
            REPORT_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                [],
                file,
                indent=4
            )


# ============================================================
# GET ALL REPORTS
# ============================================================

def get_all_reports():

    _ensure_storage()

    try:
        with open(
            REPORT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        if isinstance(data, list):
            return data

        # Old single-report format support
        if isinstance(data, dict):
            return [data]

        return []

    except Exception as e:
        print("Report read error:", e)
        return []


# ============================================================
# SAVE REPORT
# ============================================================

def save_report(
    scan_type,
    target,
    score,
    risk,
    verdict,
    recommendation,
    extra=None
):

    _ensure_storage()

    reports = get_all_reports()

    report = {
        "id": datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        ),

        "scan_type": str(
            scan_type
        ),

        "target": str(
            target
        ),

        "score": int(
            score
        ),

        "risk": str(
            risk
        ).upper(),

        "verdict": str(
            verdict
        ),

        "recommendation": str(
            recommendation
        ),

        "date_time": datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        ),

        "extra": (
            extra
            if isinstance(extra, dict)
            else {}
        )
    }

    # IMPORTANT:
    # Append instead of replacing.
    reports.append(report)

    try:

        with open(
            REPORT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                reports,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"Report saved: {scan_type}"
        )

        return True

    except Exception as e:

        print(
            "Report save error:",
            e
        )

        return False


# ============================================================
# GET LATEST REPORT
# ============================================================

def get_latest_report():

    reports = get_all_reports()

    if not reports:
        return None

    return reports[-1]


# ============================================================
# CLEAR ALL REPORTS
# ============================================================

def clear_all_reports():

    _ensure_storage()

    try:

        with open(
            REPORT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )

        return True

    except Exception as e:

        print(
            "Clear report error:",
            e
        )

        return False