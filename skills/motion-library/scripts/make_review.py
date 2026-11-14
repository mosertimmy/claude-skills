#!/usr/bin/env python3
"""Build the review page for a draft. Output is a plain folder that opens by double-click.

usage: make_review.py LIB PROJECT_DIR
PROJECT_DIR holds project.json and draft.mp4. Creates review.html, review.data.js and previews/ inside it.
"""
import json, shutil, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
if len(sys.argv) != 3:
    sys.exit(__doc__)
lib, proj = Path(sys.argv[1]), Path(sys.argv[2])
project = json.loads((proj / "project.json").read_text())
library = json.loads((lib / "library.json").read_text())
if not (proj / "draft.mp4").exists():
    sys.exit("draft.mp4 not found in the project folder. Render the draft first.")
(proj / "previews").mkdir(exist_ok=True)
fmt = project.get("format", "16:9"); key = "916" if fmt == "9:16" else "169"
moves = []
for m in library["moves"]:
    if m.get("status") == "retired" or fmt not in m.get("formats", [fmt]):
        continue
    src = lib / "previews" / f"{m['code']}_{key}.mp4"
    has = src.exists()
    if has:
        shutil.copy2(src, proj / "previews" / src.name)
    moves.append({"code": m["code"], "name": m["name"], "slot": m["slot"], "preview": f"previews/{src.name}" if has else None, "rules": m.get("rules", [])})
data = {"project": project.get("name", proj.name), "format": fmt, "video": "draft.mp4",
        "shots": [{k: s.get(k) for k in ("id", "label", "slot", "move", "t0", "d")} for s in project["shots"]], "moves": moves}
(proj / "review.data.js").write_text("window.REVIEW=" + json.dumps(data, indent=1) + ";")
shutil.copy2(SKILL / "templates" / "review.html", proj / "review.html")
print(f"Review page ready: {proj / 'review.html'}")
