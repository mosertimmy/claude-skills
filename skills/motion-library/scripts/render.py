#!/usr/bin/env python3
"""Render moves or a whole project to video, or write a live preview page.

usage:
  render.py LIB --move HL1 [--props '{"text":"Hi"}'] --format 9:16 --out previews/HL1_916.mp4
  render.py LIB --project projects/demo/project.json --out projects/demo/draft.mp4 [--scale 0.5] [--footage clip.mp4]
  render.py LIB --project projects/demo/project.json --live preview.html     (no Chromium needed: plays in any browser)

LIB is the library folder (holds library.json, moves/, engine/). Overlays are transparent when --footage is given.
"""
import argparse, json, subprocess, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _tools import need_ffmpeg, SKILL_DIR


def build_html(lib, project):
    eng = lib / "engine" if (lib / "engine" / "project.html").exists() else SKILL_DIR / "engine"
    library = json.loads((lib / "library.json").read_text())
    used = {s["move"] for s in project["shots"]}
    moves = []
    for m in library["moves"]:
        if m["code"] in used:
            f = lib / m["file"]
            if not f.exists():
                sys.exit(f"Move {m['code']} points at {m['file']} but that file is missing.")
            moves.append(f.read_text())
    missing = used - {m["code"] for m in library["moves"]}
    if missing:
        sys.exit(f"Not in library.json: {', '.join(sorted(missing))}")
    html = (eng / "project.html").read_text()
    data = "window.PROJECT=" + json.dumps(project) + ";window.LIBRARY=" + json.dumps({"brand": library.get("brand", {})}) + ";"
    safe = lambda s: s.replace("</script", "<\\/script")
    return (html.replace("/*__MOTION__*/", safe((eng / "motion.js").read_text()))
                .replace("/*__MOVES__*/", safe("\n".join(moves)))
                .replace("/*__DATA__*/", safe(data)))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("lib"); a.add_argument("--move"); a.add_argument("--props", default="{}")
    a.add_argument("--project"); a.add_argument("--format", default=None, choices=["9:16", "16:9"])
    a.add_argument("--out"); a.add_argument("--live"); a.add_argument("--fps", type=int, default=30)
    a.add_argument("--scale", type=float, default=1.0); a.add_argument("--footage")
    a = a.parse_args()
    lib = Path(a.lib)
    if a.project:
        project = json.loads(Path(a.project).read_text())
    elif a.move:
        project = {"format": "9:16", "shots": [{"id": "s1", "move": a.move, "t0": 0, "props": json.loads(a.props)}]}
    else:
        sys.exit(__doc__)
    if a.format:
        project["format"] = a.format
    fmt = project.get("format", "16:9")
    W, H = (1080, 1920) if fmt == "9:16" else (1920, 1080)

    if a.live:
        project.setdefault("bg", "#F5F5F4")
        Path(a.live).write_text(build_html(lib, project))
        print(f"Live preview written to {a.live}. Open it in a browser."); return
    if not a.out:
        sys.exit("--out is required to render a video")

    project["bg"] = "transparent" if a.footage else project.get("bg") or "#F5F5F4"
    html = build_html(lib, project)
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        sys.exit("Playwright is missing. Run scripts/setup_check.py, or use --live for a browser preview.")
    ff = need_ffmpeg()
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    ow, oh = int(W * a.scale) // 2 * 2, int(H * a.scale) // 2 * 2
    cmd = [ff, "-y", "-loglevel", "error"]
    if a.footage:
        cmd += ["-i", a.footage]
    cmd += ["-f", "image2pipe", "-c:v", "png", "-framerate", str(a.fps), "-i", "-"]
    if a.footage:
        cmd += ["-filter_complex", f"[0:v]scale={ow}:{oh}:force_original_aspect_ratio=increase,crop={ow}:{oh}[b];[1:v]scale={ow}:{oh}[o];[b][o]overlay=shortest=1[v]",
                "-map", "[v]", "-map", "0:a?", "-c:a", "aac", "-shortest"]
    cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "veryfast", "-crf", "18", a.out]
    errf = tempfile.TemporaryFile()
    enc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=errf)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=a.scale)
        pg.add_init_script("window.__RENDER = true")
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "p.html"; f.write_text(html); pg.goto(f.as_uri())
        pg.wait_for_function("window.__ready === true", timeout=20000)
        dur = pg.evaluate("window.__duration")
        n = round(dur * a.fps)
        try:
            for i in range(n):
                pg.evaluate(f"window.seek({i / a.fps})")
                enc.stdin.write(pg.screenshot(omit_background=True, type="png"))
        except BrokenPipeError:
            pass                                    # footage ended before the overlays did: normal with --footage
        b.close()
    try:
        enc.stdin.close()
    except BrokenPipeError:
        pass
    enc.wait()
    if enc.returncode:
        errf.seek(0); sys.exit("ffmpeg failed:\n" + errf.read().decode(errors="replace")[-800:])
    print(f"Rendered {n} frames ({dur:.1f}s, {ow}x{oh}) -> {a.out}")


main()
