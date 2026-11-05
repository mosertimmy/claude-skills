---
name: video-review-dashboard
description: Use right after the first draft of a motion graphics video renders, or when someone says "open the video review dashboard" or "apply my picks". Loads the draft into a review page where they scrub the timeline, swap moves shot by shot from their motion library and leave notes, then applies the picks and re-renders.
metadata:
  version: "1.2.0"
  author: Timmy Moser (timmymoser.com)
---

# Video review dashboard

Every motion graphics draft gets a review dashboard: the draft plays at the top, its shots sit on a timeline underneath, and each shot shows the move it uses plus the alternatives from the user's motion library in the same slot. The user scrubs, watches the samples, picks swaps and leaves notes. Then Claude applies them in one pass.

Works best with the **motion-library-builder** skill (moves with codes, slots and previews in `MOTION.md`). Without it, alternatives are listed by description instead of preview.

## Before you start: folder check

Run this once at the start of the chat, then start the job. Never re-teach setup here.

| You find | Do this |
|---|---|
| A folder with `WORKSPACE.md` | Read it, follow its house rules and paths, then start. Say nothing about setup |
| A folder, but no `WORKSPACE.md` | Ask once (multiple choice): **Use this folder as it is** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **Pick a different folder**. "As it is" means save this job's work in one subfolder named for the job |
| No folder | Ask once (multiple choice): **Add a folder: the + beside the message box, then Add folder** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **No folder: send me the files in this chat** |

If the added folder already holds the draft, treat it as "Use this folder as it is", say so in one line and don't ask. Without a folder, ask for the draft file in the chat; without `MOTION.md`, list alternatives by description.

After the answer: if they pick the fast setup, give the link and wait. If they pick a different folder, ask them to add it, then run this check again. If they pick no folder, work in the chat: ask for the files you need here, deliver every output as a file in the chat, and tell them where to save it on their computer.

Model: say in one line that Sonnet is the default.

## After the first draft renders

1. Make a 720p copy of the draft (`drafts/<project-id>/draft.mp4`; with no folder, in the chat workspace) so the page loads fast.
2. Write the shot list: `{id, label, scene, slot, move, t0, d}` per shot. `move` is the library code (e.g. `HL1`). `slot` is one of line, headline, list, pair, stat, screens, transition, card, photos, brand, icons, captions.
3. **Build or update the dashboard page:**
   - First time: publish an artifact page with a shared database (the `db` capability) and a `picks` collection. Layout: video player on top; a clickable timeline of shots (jumps the video to `t0`); per shot, the current move's preview and the alternatives from the same slot, a pick button and a note field. A project switcher at the top lists every draft, newest first.
   - Next times: read the live page, add the new draft to its `DRAFTS` list (newest first), keep everything else, and republish to the same link without changing its capabilities.
   - If artifacts aren't available, build the same page as a local HTML file that saves picks to a downloadable `picks.json`.
4. Open it for the user and say in one line: the draft is loaded, scrub the timeline, pick alternatives, then say "apply my picks".

## When the user says "apply my picks"

1. Read the `picks` collection (or `picks.json`). Doc ids are `<project>__<shot>`, fields `{project, shot, label, original, move, note, updatedAt}`.
2. Filter to the current project. A pick where `move` equals `original` but has a note is a note-only change.
3. Swap each shot's move in the project file and apply the notes.
4. Re-render, save as the next version (older versions go to `_superseded/` or are deleted), update the draft on the dashboard and republish.
5. Reply with a short table: shot, old move, new move, note handled.

## House rules

- Short replies with tables.
- Ask before spending credits in any paid tool.
- If a note asks for a move the library doesn't have, add it to the library first (component, preview, catalogue row), then use it.
