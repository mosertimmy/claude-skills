#!/usr/bin/env python3
"""prep.py: make a cheap local summary of a video so Claude reads that, not the raw file.

Usage: python3 prep.py <video> [outdir]
Needs: ffmpeg and ffprobe. Optional: tesseract (reads on-screen text).
Writes into outdir (default <video>-prep/):
  summary.json  duration, size, fps, loudness, scene cuts, on-screen text (about 1 KB)
  sheet.jpg     one image of up to 30 evenly spaced frames
  hook.jpg      the first frame, small
"""
import json, os, re, shutil, subprocess, sys, tempfile

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def need(tool):
    if not shutil.which(tool):
        sys.exit(f"{tool} not found. Install ffmpeg (it includes ffprobe) and run again.")

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    video = sys.argv[1]
    if not os.path.isfile(video):
        sys.exit(f"File not found: {video}")
    need("ffmpeg"); need("ffprobe")
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(video)[0] + "-prep"
    os.makedirs(out, exist_ok=True)

    p = run(["ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=width,height,r_frame_rate,codec_type",
             "-of", "json", video])
    info = json.loads(p.stdout or "{}")
    dur = float(info.get("format", {}).get("duration", 0) or 0)
    size = int(info.get("format", {}).get("size", 0) or 0)
    vs = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), {})
    fps = 0.0
    try:
        a, b = vs.get("r_frame_rate", "0/1").split("/")
        fps = round(float(a) / float(b), 2)
    except Exception:
        pass

    # scene cuts
    cuts = []
    r = run(["ffmpeg", "-hide_banner", "-i", video, "-vf", "select='gt(scene,0.3)',showinfo", "-an", "-f", "null", "-"])
    for m in re.finditer(r"pts_time:([0-9.]+)", r.stderr):
        cuts.append(round(float(m.group(1)), 2))

    # loudness
    lufs = None
    r = run(["ffmpeg", "-hide_banner", "-i", video, "-af", "ebur128=peak=true", "-vn", "-f", "null", "-"])
    m = re.findall(r"I:\s+(-?[0-9.]+) LUFS", r.stderr)
    if m:
        lufs = float(m[-1])

    # contact sheet (up to 30 frames)
    n = max(1, min(30, int(dur // 2) or 1))
    step = dur / n if n and dur else 1
    cols = 5
    rows = -(-n // cols)
    r = run(["ffmpeg", "-y", "-v", "error", "-i", video, "-vf",
             f"fps=1/{max(step,0.1):.3f},scale=288:-1,tile={cols}x{rows}", "-frames:v", "1", "-q:v", "4",
             os.path.join(out, "sheet.jpg")])
    run(["ffmpeg", "-y", "-v", "error", "-i", video, "-frames:v", "1", "-vf", "scale=480:-1",
         os.path.join(out, "hook.jpg")])

    # on-screen text (optional)
    text = []
    if shutil.which("tesseract"):
        with tempfile.TemporaryDirectory() as td:
            run(["ffmpeg", "-y", "-v", "error", "-i", video, "-vf", f"fps=1/{max(dur/6,0.5):.3f},scale=960:-1",
                 "-frames:v", "6", os.path.join(td, "f%02d.png")])
            seen = set()
            for f in sorted(os.listdir(td)):
                t = run(["tesseract", os.path.join(td, f), "-", "--psm", "6"]).stdout
                for line in t.splitlines():
                    line = line.strip()
                    if len(line) > 3 and line.lower() not in seen:
                        seen.add(line.lower()); text.append(line)
            text = text[:20]

    summary = {
        "file": os.path.basename(video),
        "duration_s": round(dur, 2),
        "size_mb": round(size / 1e6, 2),
        "resolution": f"{vs.get('width','?')}x{vs.get('height','?')}",
        "fps": fps,
        "loudness_lufs": lufs,
        "scene_cuts": len(cuts),
        "cut_times_s": cuts[:60],
        "avg_shot_length_s": round(dur / (len(cuts) + 1), 2) if dur else None,
        "cuts_per_10s": round(len(cuts) / dur * 10, 2) if dur else None,
        "sheet_frames": n,
        "sheet_spacing_s": round(step, 2),
        "on_screen_text": text,
    }
    with open(os.path.join(out, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    print(json.dumps(summary, indent=1))
    print(f"\nWrote {out}/summary.json, sheet.jpg, hook.jpg")

if __name__ == "__main__":
    main()
