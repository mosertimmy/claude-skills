---
name: project-update-check
description: Use when someone says "project update check", "run an update check" or "sync this project". Sweeps a Claude project's chats, docs and artifacts, saves everything worth keeping to their workspace folder, updates docs and skills, tidies old files and only asks about real issues.
metadata:
  version: "1.2.0"
  author: Timmy Moser (timmymoser.com)
---

# Project update check

A housekeeping sweep for any Claude project. It finds everything from the project's chats that should live in the user's workspace folder, saves it there, updates docs and skills, and tidies old files. Works in any project, whatever the topic.

**Runs on its own.** Don't stop for approval. Do every safe action straight away. Only stop to ask about real issues (below), as multiple-choice questions with the recommended option first.

## Before you start: folder check

Run this once at the start of the chat, then start the job. Never re-teach setup here.

| You find | Do this |
|---|---|
| A folder with `WORKSPACE.md` | Read it, follow its house rules and paths, then start. Say nothing about setup |
| A folder with no `WORKSPACE.md`, or no folder | Stop. Ask nothing, guess nothing, build nothing. Say in one line: "Do the fast setup first: timmymoser.com/claude/setup, then run this again." |

`WORKSPACE.md` is the folder map. Read it at the start of every run. It must name the project folders, the shared assets folder, the Downloads folder and the never-touch folders; if one is missing, treat it as a "no clear home" question.

## What needs your question

Ask only about these. Everything else, just do.

| Issue | Recommended default |
|---|---|
| A file with the same name but different content is already in the folder | Keep both (new one saved beside it) |
| No clear home for a file, or no project folder fits this project | Best-guess folder, named in the option |
| A new rule from the chats contradicts an existing doc or skill | Use the newer rule from the chat |
| A file is mentioned in a chat but was never attached or can't be found | Skip and list in the report |
| A tidy candidate is borderline (could be live work or a final) | Leave it |
| A chat can't be read | Keep the chat, mark it not captured |

- Collect issues as you go and ask them together at the end of step 6 (up to 4 per question pop-up). Each question names the file or rule and the chat it came from.
- Keep doing everything else while waiting.
- If nobody answers (scheduled run, or no reply), apply the recommended default and list it under "Decided for you" in the report.

## 1. Open the workspace

- Request access to the workspace folder and Downloads in one request. If a folder with `WORKSPACE.md` is found but the computer can't be reached, say so once, do steps 2 to 4, and save results into the Claude project for the next run.
- Read `WORKSPACE.md`, work out which project folder this project belongs to, and read its README.md and CHANGELOG.md.

## 2. Read the project

- Read every project doc and the project memory.
- List every chat in the project (past-chat search), back to the first one. If `update-check-log.md` exists in the project, focus on chats since the last check.
- Read each chat in range fully. Rules and decisions often sit mid-chat.
- List the project's artifacts and match them to chats.
- If past-chat search isn't available, say so and work from the project docs and files only.

## 3. Find what needs saving

| Look for | Where it goes |
|---|---|
| Files made or attached in chats (renders, images, scripts, docs, exports) not in the folder yet | Project folder, originals in `references/` or `source/` |
| Project docs with no copy in the folder | Project folder, same file name |
| Published artifacts whose source isn't saved | Project folder, `pages/` |
| Decisions, status changes, open items | The project README.md (status, Outputs table) and a dated line in CHANGELOG.md |
| New standing rules ("always", "never", "from now on") | The project README and the matching skill |
| New or renamed folders | WORKSPACE.md |
| Logos, icons, fonts, sounds the user supplied | A shared assets folder |

Check each candidate against the folder first: a same-name file with identical content is already saved.

## 4. Check the skills

- Read every installed skill this project touches.
- Note every rule, path, step or preference from the chats that a skill is missing or has out of date.
- Note repeated multi-step procedures with no skill yet as new skill ideas.

## 5. Sync

- Copy, never move. Keep file names. Check each copy matches its source.
- Never overwrite a different file: save the new one beside it as `<name> (from chat YYYY-MM-DD)` and raise it as an issue.
- Update the project README.md (status, Outputs table, open items, new paths), add dated lines to its CHANGELOG.md, and update WORKSPACE.md if folders changed.
- Save key docs back into the Claude project so other chats can see them.

## 6. Tidy

Candidates: `_to_delete/` folders, drafts and test renders superseded by a final (v1, v2, test, draft names, or identical copies), stray files in the wrong folder or loose in the root, empty folders.

- Never touch anything changed in the last few hours unless it's clearly from this project; raise it as borderline instead.
- Never touch finals, `exports/`, `references/` originals or the never-touch folders.
- Misplaced files: move them and update any doc that pointed at the old path.
- Old files: ask for delete permission once. If it's declined, move them into `_to_delete/` in the same folder.

Now ask the collected issues and apply the answers.

## 7. Update skills

Write the complete updated SKILL.md for every skill with missing or outdated content (keep everything still valid), plus any new skill ideas, and propose them for the user to save. Skip any change waiting on a contradiction question until it's answered.

## 8. Log and report

- Add a dated entry to `update-check-log.md` in the Claude project and a dated entry in the project's `CHANGELOG.md`: chats covered, files saved, docs and skills updated, files tidied, issues and how each was decided.
- Finish with a short table: Saved, Updated, Tidied, Decided for you, Needs you.
- End with the chats that are now fully captured and safe to delete, and any that aren't.
