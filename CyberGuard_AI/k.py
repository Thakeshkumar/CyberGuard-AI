"""Copy scam service + UI into final locations."""
import os
import shutil

# 1. Copy root "Cyber" (scam service) -> services/scam_detector.py
src_svc = "Cyber"
dst_svc = "CyberGuard_AI/services/scam_detector.py"
shutil.copyfile(src_svc, dst_svc)
os.remove(src_svc)
print("Service copied:", os.path.exists(dst_svc))

# 2. Copy UI -> pages/scam_detector.py
src_ui = "CyberGuard_AI/pages/scam_security_analyzer.py"
dst_ui = "CyberGuard_AI/pages/scam_detector.py"
shutil.copyfile(src_ui, dst_ui)
os.remove(src_ui)
print("UI copied:", os.path.exists(dst_ui))

# Verify line counts
print("Service lines:", sum(1 for _ in open(dst_svc, encoding="utf-8")))
print("UI lines:", sum(1 for _ in open(dst_ui, encoding="utf-8")))
print("DONE")