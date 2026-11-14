#!/usr/bin/env python3
"""Turn a reference video (or images) into frames Claude can read.

usage:
  extract_reference.py REF OUTDIR [--scene 0.25] [--max 24]     frames at scene changes + contact sheet
  extract_reference.py REF OUTDIR --detail 3.2 [--span 1.5]     8 close-up frames from 3.2s, to read easing and timing

Writes OUTDIR/info.json, OUTDIR/frames/*.jpg, OUTDIR/frames.json (index -> seconds) and OUTDIR/contact.jpg.
Read contact.jpg first, then single frames only where you need detail.
"""
import argparse, json, math, re, shutil, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _tools import need_ffmpeg, probe

IMG = {".png", ".jpg", ".jpeg", ".webp"}


def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def contact(ff, frames_dir, out, cols=6):
    n = len(list(frames_dir.glob("*.jpg")))
    if not n:
        return
    rows = math.ceil(n / cols)
    sh([ff, "-y", "-loglevel", "error", "-pattern_type", "glob", "-i", str(frames_dir / "*.jpg"),
        "-vf", f"scale=320:-2,tile={min(cols, n)}x{rows}", "-frames:v", "1", "-q:v", "4", str(out)])


def main():
    a = argparse.ArgumentParser()
    a.add_argument("ref"); a.add_argument("outdir")
    a.add_argument("--scene", type=float, default=0.25)
    a.add_argument("--max", type=int, default=24)
    a.add_argument("--detail", type=float)
    a.add_argument("--span", type=float, default=1.5)
    a = a.parse_args()
    ref, out = Path(a.ref), Path(a.outdir)
    frames = out / ("detail" if a.detail is not None else "frames")
    shutil.rmtree(frames, ignore_errors=True); frames.mkdir(parents=True, exist_ok=True)
    ff = need_ffmpeg()

    if ref.suffix.lower() in IMG:                       # still reference: just copy it in
        shutil.copy2(ref, frames / "f_001.jpg") if ref.suffix.lower() in {".jpg", ".jpeg"} else sh([ff, "-y", "-loglevel", "error", "-i", str(ref), str(frames / "f_001.jpg")])
        (out / "info.json").write_text(json.dumps({"type": "image", "file": ref.name}, indent=2))
        contact(ff, frames, out / "contact.jpg"); print(f"1 image -> {out}"); return

    info = probe(ref); info["type"] = "video"; info["file"] = ref.name
    (out / "info.json").write_text(json.dumps(info, indent=2))
    dur = info["duration"] or 0

    if a.detail is not None:                            # close-up strip for reading easing
        step = a.span / 8
        times = [round(a.detail + i * step, 3) for i in range(8)]
        for i, t in enumerate(times, 1):
            sh([ff, "-y", "-loglevel", "error", "-ss", str(t), "-i", str(ref), "-frames:v", "1", "-vf", "scale=640:-2", "-q:v", "3", str(frames / f"d_{i:02d}.jpg")])
        (out / "detail.json").write_text(json.dumps(times))
        contact(ff, frames, out / "detail_contact.jpg", cols=4); print(f"8 detail frames -> {frames}"); return

    r = sh([ff, "-hide_banner", "-i", str(ref), "-vsync", "vfr", "-q:v", "3", "-vf", f"select='gt(scene,{a.scene})+eq(n,0)',showinfo,scale=640:-2", str(frames / "s_%03d.jpg")])
    times = [float(m) for m in re.findall(r"pts_time:([\d.]+)", r.stderr)]
    files = sorted(frames.glob("s_*.jpg"))
    if len(files) < 8 and dur:                          # slow or smooth video: sample evenly instead
        for f in files: f.unlink()
        n = 12; times = [round(dur * (i + 0.5) / n, 2) for i in range(n)]
        for i, t in enumerate(times, 1):
            sh([ff, "-y", "-loglevel", "error", "-ss", str(t), "-i", str(ref), "-frames:v", "1", "-vf", "scale=640:-2", "-q:v", "3", str(frames / f"s_{i:03d}.jpg")])
        files = sorted(frames.glob("s_*.jpg"))
    if len(files) > a.max:                              # thin evenly
        keep = {round(i * (len(files) - 1) / (a.max - 1)) for i in range(a.max)}
        for i, f in enumerate(files):
            if i not in keep: f.unlink()
        times = [t for i, t in enumerate(times) if i in keep]; files = sorted(frames.glob("s_*.jpg"))
    for i, f in enumerate(files, 1):
        f.rename(frames / f"f_{i:03d}.jpg")
    (out / "frames.json").write_text(json.dumps([{"frame": f"f_{i:03d}.jpg", "t": times[i - 1] if i <= len(times) else None} for i in range(1, len(files) + 1)], indent=1))
    contact(ff, frames, out / "contact.jpg")
    print(f"{len(files)} frames, {dur:.1f}s video -> {out}")


main()
