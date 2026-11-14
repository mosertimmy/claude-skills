#!/usr/bin/env python3
"""Check (and where possible install) what the motion library needs. Never blocks.

Prints one line per tool. Needs: ffmpeg (to read references, encode video) and
Playwright + Chromium (to render moves to video). If Chromium cannot be installed,
the library still works: previews and drafts play live in a browser page.
"""
import subprocess, sys, shutil
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _tools import ffmpeg_path


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def pip(*pkgs):
    r = run([sys.executable, "-m", "pip", "install", "-q", "--break-system-packages", *pkgs])
    if r.returncode != 0:
        r = run([sys.executable, "-m", "pip", "install", "-q", *pkgs])
    return r.returncode == 0


def chromium_ok():
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch()
            b.close()
        return True
    except Exception:
        return False


report = []
if ffmpeg_path():
    report.append(("OK", "ffmpeg", ""))
elif pip("imageio-ffmpeg") and ffmpeg_path():
    report.append(("FIXED", "ffmpeg", "installed a bundled copy"))
else:
    report.append(("MISSING", "ffmpeg", "install from ffmpeg.org; until then Claude can only work from images, not video references"))

if chromium_ok():
    report.append(("OK", "chromium", ""))
else:
    try:
        import playwright  # noqa: F401
        have = True
    except Exception:
        have = pip("playwright")
    if have:
        run([sys.executable, "-m", "playwright", "install", "chromium"])
    if chromium_ok():
        report.append(("FIXED", "chromium", "installed"))
    else:
        report.append(("MISSING", "chromium", "cannot render MP4 here. Fallback: previews and drafts play live in a browser page (render.py --live)"))

for status, name, note in report:
    print(f"{status:8}{name:10}{note}")
