#!/usr/bin/env python3
"""make_workspace.py: create a Claude workspace folder with the 5S layout.

Usage: python3 make_workspace.py <parent-folder> [--name "Claude Workspace"] [--owner "Your name"]
Creates <parent-folder>/<name>/ with numbered folders, a short README in each, and START-HERE.md.
Never overwrites an existing file. Safe to run twice.
"""
import argparse, datetime, os, sys

FOLDERS = {
    "1 Projects": "One folder per project. Working material lives here: originals, drafts, project files.\nEach project folder holds README.md (what it is, plus an Outputs table) and CHANGELOG.md.",
    "2 Outputs": "Finished things, grouped by project: 2 Outputs/<Project>/. Videos, documents, images, exports.\nIf you would send it, post it or hand it in, it belongs here.",
    "3 Assets": "Things you reuse across projects: Brand, Images, Video, Audio, Reference, Docs.\nOriginals only. Edited versions go in the project.",
    "4 Claude": "Claude's own notes: Handoffs (for moving to a new chat), Prompts you reuse, Skills notes.",
    "5 Archive": "Finished projects you want to keep but not see. Move a whole project folder here.",
    "_to_delete": "Nothing is deleted automatically. Move anything you no longer want here, then delete this folder's contents yourself when you are sure.",
}
ASSET_SUB = ["Brand", "Images", "Video", "Audio", "Reference", "Docs"]
CLAUDE_SUB = ["Handoffs", "Prompts"]

START = """# START HERE

This is {owner} Claude workspace. Claude reads this file first on every task.

Created {date}.

## Map

| Folder | What goes in it |
|---|---|
| 1 Projects | One folder per project: originals, drafts, working files, README, CHANGELOG |
| 2 Outputs | Finished work, grouped by project |
| 3 Assets | Reusable originals: brand, images, video, audio, reference, docs |
| 4 Claude | Handoffs for new chats, reusable prompts |
| 5 Archive | Finished projects kept out of sight |
| _to_delete | Anything to remove. Claude never deletes, it moves things here |

## The 5S rules

| S | Rule |
|---|---|
| Sort | Keep only what you use. Everything else goes to _to_delete or 5 Archive |
| Set in order | Every file has one home. Check the map before saving |
| Shine | Tidy at the end of every task: no stray files in Downloads or the top level |
| Standardise | Names: `Subject - what it is - date`. Every project has a README and a CHANGELOG |
| Sustain | Read this file first. Save as you go. Log every change. Say "tidy up" weekly |

## House rules

- Claude asks questions as multiple choice.
- Originals are never edited in place. Work on a copy.
- Anything made in a chat is saved here the moment it exists, never left only in the chat.
- If a file is missing, Claude says so and asks. It does not guess.
- Times come from this computer's clock.

## Projects

| Project | What it is | Status |
|---|---|---|
| (none yet) | Say "new project <name>" | |

## Changes to this map

| Date | Change |
|---|---|
| {date} | Workspace created |
"""

PROJECT_README = """# {project}

One or two lines on what this project is.

## References

Everything added to a chat for this project. Originals are saved in Originals/.

| Name | Source | Why it matters | Saved to |
|---|---|---|---|

## Outputs

| Type | Name | Status | Path |
|---|---|---|---|
"""

def write(path, text):
    if os.path.exists(path):
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("parent")
    ap.add_argument("--name", default="Claude Workspace")
    ap.add_argument("--owner", default="my")
    a = ap.parse_args()
    parent = os.path.expanduser(a.parent)
    if not os.path.isdir(parent):
        sys.exit(f"Parent folder not found: {parent}")
    root = os.path.join(parent, a.name)
    os.makedirs(root, exist_ok=True)
    date = datetime.date.today().isoformat()
    for folder, blurb in FOLDERS.items():
        p = os.path.join(root, folder)
        os.makedirs(p, exist_ok=True)
        write(os.path.join(p, "README.md"), f"# {folder}\n\n{blurb}\n")
    for sub in ASSET_SUB:
        os.makedirs(os.path.join(root, "3 Assets", sub), exist_ok=True)
    for sub in CLAUDE_SUB:
        os.makedirs(os.path.join(root, "4 Claude", sub), exist_ok=True)
    owner_text = a.owner + "'s" if a.owner != "my" else "your"
    write(os.path.join(root, "START-HERE.md"), START.format(owner=owner_text, date=date))
    os.makedirs(os.path.join(root, "1 Projects", "_Project template", "Originals"), exist_ok=True)
    write(os.path.join(root, "1 Projects", "_Project template", "README.md"), PROJECT_README.format(project="Project name"))
    write(os.path.join(root, "1 Projects", "_Project template", "CHANGELOG.md"), "# Changelog\n\nOne line per change, newest at the bottom. Never edit earlier lines.\n\n| Date | Chat | Type | What |\n|---|---|---|---|\n")
    print(f"Workspace ready: {root}")

if __name__ == "__main__":
    main()
