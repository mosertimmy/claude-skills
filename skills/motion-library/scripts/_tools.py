"""Shared helpers: find ffmpeg and read basic video info, with fallbacks."""
import json, re, shutil, subprocess, sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent


def ffmpeg_path():
    p = shutil.which("ffmpeg")
    if p:
        return p
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def need_ffmpeg():
    p = ffmpeg_path()
    if not p:
        sys.exit("ffmpeg not found. Run scripts/setup_check.py, it installs a fallback.")
    return p


def probe(video):
    """Return {duration, width, height, fps} using ffprobe, or ffmpeg -i as a fallback."""
    video = str(video)
    fp = shutil.which("ffprobe")
    if fp:
        out = subprocess.run([fp, "-v", "error", "-select_streams", "v:0", "-show_entries",
                              "stream=width,height,r_frame_rate:format=duration", "-of", "json", video],
                             capture_output=True, text=True).stdout
        d = json.loads(out or "{}")
        s = (d.get("streams") or [{}])[0]
        n, _, m = (s.get("r_frame_rate") or "0/1").partition("/")
        fps = float(n) / float(m or 1) if float(m or 1) else 0
        return {"duration": float((d.get("format") or {}).get("duration") or 0),
                "width": s.get("width"), "height": s.get("height"), "fps": round(fps, 2)}
    err = subprocess.run([need_ffmpeg(), "-i", video], capture_output=True, text=True).stderr
    dur = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    size = re.search(r"Video:.*?, (\d{2,5})x(\d{2,5})", err)
    fps = re.search(r"([\d.]+) fps", err)
    return {"duration": int(dur[1]) * 3600 + int(dur[2]) * 60 + float(dur[3]) if dur else 0,
            "width": int(size[1]) if size else None, "height": int(size[2]) if size else None,
            "fps": float(fps[1]) if fps else 0}
