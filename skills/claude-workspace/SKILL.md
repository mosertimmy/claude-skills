---
name: claude-workspace
description: Use to set up a Claude workspace folder, and on every later task that makes, edits or needs files once one exists. Walks a first-time user through the setup, organises it with 5S, then saves everything Claude makes into it automatically.
metadata:
  version: "1.1.0"
  author: Timmy Moser (timmymoser.com)
---

# Claude workspace

One folder on your computer where everything Claude makes and everything you give it lives. Claude reads a short map first on every task, so it never asks "where did we put that?".

Built for first-time users. Works on the first message. Every question is skippable.

Triggers: "set up my workspace", "get me organised", "where should I save this", "new project <name>", "save this", "tidy up", "where is <file>".

## 1. Can Claude reach the folder?

| Where you are | What to do |
|---|---|
| Claude Code | It works in the current folder. Ask which folder is the workspace, or make one |
| Claude desktop app with files linked | Ask for access to the parent folder (usually the Desktop) in one request |
| Claude on the web, nothing linked | Build the folder here and send it as a zip, then tell them to unzip it on their Desktop and open this chat in the desktop app next time |

Never say you can not use their computer before you have tried. If a call fails, say what to do in one line.

## 2. First run: set it up (max 4 questions, all multiple choice)

Say what is about to happen in plain words: "I will make one folder, put a map file in it, and from now on read that map first."

1. **Where?** Desktop (Recommended), Documents, or somewhere else.
2. **Name?** Claude Workspace (Recommended), or their own name.
3. **Your name?** For the map file. Skippable.
4. **Bring something in now?** Optional. Offer to sort an existing messy folder (see step 5), or start empty.

Then create the layout. Use `scripts/make_workspace.py` if you can run it, or create the same folders by hand:

```
Claude Workspace/
  START-HERE.md       the map. Claude reads this first
  1 Projects/         one folder per project: originals, drafts, README, CHANGELOG
  2 Outputs/          finished work, grouped by project
  3 Assets/           reusable originals: Brand, Images, Video, Audio, Reference, Docs
  4 Claude/           Handoffs for new chats, reusable Prompts
  5 Archive/          finished projects kept out of sight
  _to_delete/         anything to remove. Claude never deletes
```

Then make it automatic (step 2b). Finish by telling them what was made in two lines, and the five phrases they can now say (see Commands).

## 2b. Make it automatic

A skill only helps when it loads. Put a standing instruction where Claude always sees it, so every task starts from the folder. Offer this once, as multiple choice ("Make it automatic? Yes (Recommended) / No"):

| Where they use Claude | Where the instruction goes |
|---|---|
| Claude Code | Add the line below to `~/.claude/CLAUDE.md` (create it if missing) |
| Claude app | Give them the line to paste into Settings, Profile, personal preferences |
| A claude.ai Project | Give them the line to paste into the Project's instructions |

The line (fill in the real path):

```
Before any task, read START-HERE.md in <path to Claude Workspace>. Save everything you make into that folder as you go, log it, and tell me where it went.
```

Once a workspace exists, treat any task that makes or edits a file as in scope for this skill, even when the user never mentions the folder. Ask for access to the workspace folder at the start of the task if it is not already linked.

## 3. The 5S rules (this is what keeps it tidy)

| S | Meaning | What Claude does |
|---|---|---|
| Sort | Keep only what you use | One pass at setup. Unwanted things go to `_to_delete` or `5 Archive`, never straight to the bin |
| Set in order | One home per file | Check the map before saving. If nothing fits, ask once, then add a row to the map |
| Shine | Clean as you go | End of every task: no stray files in Downloads or the top level |
| Standardise | Same names, same notes | Names: `Subject - what it is - date`. Every project has a README with an Outputs table and a CHANGELOG |
| Sustain | Make it a habit | Read START-HERE first. Save as you go. Log changes. Offer "tidy up" once a week |

## 4. Every task after that

1. **Read `START-HERE.md`.** It is the map and the rules. The computer copy always wins over anything remembered in a chat.
2. **Open the project's README** and CHANGELOG before working. New work gets a project folder: `1 Projects/<Project>/`, plus `2 Outputs/<Project>/` once something is finished.
3. **Save as you go, automatically.** Do not wait to be asked. Anything made in a chat (images, documents, scripts, exports, attached files) goes into the right folder the moment it exists. Never leave it only in the chat.
4. **Originals are never edited in place.** Work on a copy.
5. **Log it.** One line in the project's CHANGELOG: date, chat, type (done, file, decision), what. Add a row to the README Outputs table for every finished output. Never edit earlier lines.
6. **Say where it went** in one line: "Saved to 2 Outputs/Spring launch/Poster - final - 2026-11-15.png".
7. **Deleting is off.** Move things to `_to_delete/` and tell the user.
8. If a file is missing, say so and ask. Do not guess or swap in something else.

Times come from the computer's clock, not from memory.

## 5. Sorting an existing mess

1. Ask for the folder. List what is there: names, sizes, dates. Do not open everything.
2. Propose a plan as a table: file or group, where it goes, why. Group by project first, then by type.
3. Wait for a yes. Then move, never copy-and-delete. Anything unclear goes to `_to_delete/`.
4. Log the move in a CHANGELOG line and tell them what changed.

## 6. Projects and chats

- **New project:** say "new project <name>". Claude makes `1 Projects/<name>/` from the template (README with two lines on what it is, plus an Outputs table, and a CHANGELOG) and adds it to the Projects table in START-HERE.
- **A claude.ai Project:** add one short note in the Project's instructions: "Before any task, read START-HERE.md in my Claude Workspace and save everything there." Then the Project follows the same map.
- **Moving to a new chat:** save a handoff file in `4 Claude/Handoffs/` and give the user one line to paste.
- **Old work in old chats:** ask which chats matter, and save only the files and decisions, not the whole conversation.

## 7. Commands the user can say

| Say | Claude does |
|---|---|
| "Set up my workspace" | Runs step 2 |
| "New project <name>" | Makes the project folder and adds it to the map |
| "Save this" | Files the last thing made, logs it, says where |
| "Tidy up" | Runs a 5S check: strays, unlogged outputs, missing READMEs. Shows a table, fixes with a yes |
| "Where is <thing>?" | Searches the map and project READMEs first, then the folders |

## 8. Changing the map

Folder changes happen only when the user agrees. Add a row to "Changes to this map" in START-HERE: date and what changed. Never rename or move top-level folders without asking.

## Smoke test

Prompt 1: "Set up my workspace." Pass if Claude asks at most four multiple-choice questions, creates the folders and START-HERE.md, offers the standing instruction, and ends with the five phrases.

Prompt 2, in a new chat: "Make me a one-page poster." Pass if Claude reads START-HERE.md first, saves the poster into the right folder without being asked, logs it, and says where it went.
