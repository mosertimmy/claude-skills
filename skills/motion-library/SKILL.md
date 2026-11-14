---
name: motion-library
description: Use when someone wants their own motion graphics library with Claude. They give a reference (a video, screen recording or screenshots) and Claude saves it as a reusable move. Also makes videos from the library and opens a review page to swap moves shot by shot. Works from the first message, no other skill needed.
metadata:
  version: "1.0.0"
  author: Timmy Moser (timmymoser.com)
---

# Motion library

A personal library of animated "moves" (headline reveals, cards, stats, transitions) that grows from the user's own references. Three jobs:

1. **Add a reference.** The user gives a video, screen recording or screenshots. Claude reads it, builds the move, renders a preview and saves it to the library.
2. **Make a draft.** Claude builds a shot list from the library and renders a draft, over the user's footage if they have it.
3. **Review and apply.** A review page opens. The user swaps moves and leaves notes shot by shot. Claude applies the picks and re-renders.

Everything is shipped in this skill: a starter library of four neutral moves, the render engine, the review page and the scripts. No other skill, no setup guide, no folder is needed to start.

## Start (silent, once per chat)

1. Run `python3 scripts/setup_check.py` (path is inside this skill's folder). It checks ffmpeg and a headless browser and installs what is missing. Never narrate it. If something stays missing, use the fallback named in its output and carry on:
   - No browser: previews and drafts play live in a browser page (`render.py --live`). Say so in one line.
   - No ffmpeg: work from still images only, and say so.
2. Find the library:
   - The user's folder has a `Motion library/` folder with `library.json`: use it.
   - A folder is connected but has no library: create `Motion library/` in it with `python3 scripts/init_library.py "<folder>/Motion library"`.
   - No folder: create it in the workspace with the same script. At the end of any job that changed it, send `motion-library.zip` and tell the user in one line to attach it next time. Nothing else survives between chats without a folder.
3. Read `MOTION.md` (the user's rules) and `library.json` (the catalogue) before every job.

## Optional quick start (once per library, max 4 items, every item skippable)

Offer it as one multiple-choice question set the first time, and never block on it:

- Brand colours or a brand guide (default: neutral ink, paper and blue)
- Fonts or a logo (default: system sans, no logo)
- Format they make most: 9:16, 16:9 or both (default: both)
- Existing videos to learn from (default: none, start from the starter moves)

"Skip all" means start now with the neutral defaults. Save any answers into `library.json` under `brand`.

## Job 1: add a reference

1. Save the file in `references/<short-name>/`. Run `python3 scripts/extract_reference.py <file> references/<short-name>`.
2. Look at `contact.jpg` first. Then look at single frames only where the motion needs detail. For the exact easing and timing of one moment, run it again with `--detail <seconds>` and read `detail_contact.jpg`.
3. Write what you see in `references/<short-name>/notes.md`: what moves, from where, how long, the easing, the layout, and what job it does.
4. Decide how many moves it holds. A short clip is usually one move. Group by slot: headline, card, stat, transition, lower-third, screens, photos, captions, icons, end-screen.
5. Build each move as `moves/<code>.js` with `defineMove(code, meta, create)`. Read `moves/hl1.js` first as the pattern. Rules for a move:
   - A move is a pure function of time. `seek(t)` draws the frame at `t` seconds. No timers, no CSS animations.
   - Lay out from `ctx.w` and `ctx.h`, never fixed pixels, so it works in 9:16 and 16:9.
   - Content comes in through `props`. Nothing hard-coded. Colours and font come from `ctx.brand`.
   - Recreate the motion, not the sample's content, logos or artwork. Use the user's own text and brand.
   - Screen recordings are content: composite the real recording, never redraw a screen by hand.
6. Add the move to `library.json` (code, name, slot, formats, file, status "live", source = the reference name, props, rules).
7. Render a preview in each format: `python3 scripts/render.py <lib> --move <CODE> --format 9:16 --scale 0.5 --out previews/<CODE>_916.mp4` and the same with `16:9` and `_169`. Look at one frame of each before showing it.
8. Reply with a short table of what was added and the previews. Ask (multiple choice) whether to keep, tweak or retire each move.

Adding five references at once is the same loop, one reference at a time.

## Job 2: make a draft

1. Get the content: a script, notes or footage. Transcribe footage first.
2. Pick the format. Portrait or "Reel, Short, TikTok" is 9:16. Landscape or "YouTube" is 16:9. Ask if unclear.
3. Write `projects/<name>/project.json`: `format` plus `shots`, each `{id, label, slot, move, t0, d, props}`. Use only live moves. If a style is missing, add it through Job 1 first. See `templates/project.example.json`.
4. Render the draft at half size: `python3 scripts/render.py <lib> --project projects/<name>/project.json --scale 0.5 [--footage <clip>] --out projects/<name>/draft.mp4`. With `--footage` the moves sit over the clip, with its audio kept.
5. Build the review page: `python3 scripts/make_review.py <lib> projects/<name>`. Open `review.html` for the user (double-click works, no server). If the Artifact tool is available, publish the folder's files as an artifact instead.
6. Say in one line: the draft is ready, pick swaps and notes in the review page, then say "apply my picks".

Render the final at full size (no `--scale`) only after the user signs off. Keep the latest draft and the final.

## Job 3: apply picks

1. Read the `picks.json` the user attached or pasted: `{project, picks: [{shot, original, move, note}]}`.
2. Update `project.json`: change each shot's `move`. A pick whose `move` equals `original` with a note is a note-only change.
3. Re-render, rebuild the review page, and reply with a table: shot, old move, new move, note handled.

## Rules that apply unless the user's `MOTION.md` says otherwise

- Every "never do X" or "always do Y" from the user goes into `MOTION.md` with the date. A rejected move stays in the catalogue with status "retired".
- No text over a face. In 9:16 keep text and cards below the chin. In 16:9 keep them beside the speaker.
- Captions follow sentences and are checked against what was said.
- Morph or transition between shots. No dips to black.
- One idea per graphic. Buttons and pills sized to their label with real padding. Nothing clipped or touching an edge.
- Real screens and official logos only.
- Ask every question as multiple choice. Never ask the user to run a command Claude can run.
- Ask before spending credits in any paid tool. This skill needs none.

## Keeping it consistent

When a move changes, update in one pass: the move file, its previews, its `library.json` row and `MOTION.md` if a rule changed. Before overwriting a file another chat may have edited, read it again and merge.

## Smoke test

Prompt on a fresh chat with nothing installed and no folder: "Here is a reference clip. Add it to my motion library, then make a 10 second 9:16 draft using it." Pass when: the library is created without questions beyond the optional quick start, a move built from the clip appears in `library.json` with previews in both formats, `draft.mp4` plays, `review.html` opens, and a pick plus `apply my picks` changes the next render.
