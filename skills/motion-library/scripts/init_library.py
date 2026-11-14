#!/usr/bin/env python3
"""Create a motion library folder from the starter kit. Safe to re-run: never overwrites.

usage: init_library.py LIBRARY_DIR
"""
import shutil, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
if len(sys.argv) != 2:
    sys.exit(__doc__)
lib = Path(sys.argv[1])
for sub in ("moves", "previews", "references", "projects", "exports"):
    (lib / sub).mkdir(parents=True, exist_ok=True)


def copy_tree(src, dst):
    for f in src.rglob("*"):
        if f.is_file():
            t = dst / f.relative_to(src)
            if not t.exists():
                t.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, t)


copy_tree(SKILL / "engine", lib / "engine")
copy_tree(SKILL / "starter" / "moves", lib / "moves")
for name in ("library.json", "MOTION.md"):
    src = SKILL / "templates" / name
    if src.exists() and not (lib / name).exists():
        shutil.copy2(src, lib / name)
print(f"Library ready at {lib}")
