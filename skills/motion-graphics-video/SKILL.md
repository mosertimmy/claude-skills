---
name: motion-graphics-video
description: "Use when someone wants to make a motion graphics video with Claude (a product film, app promo, launch or brand video), or says \"make a motion graphics video\" or \"start a new video\". Walks them through the whole process in one go: asks for each input with simple choices (upload now, later, skip or type it out), sorts what they drop in, plans, storyboards, builds, reviews and adds sound, and keeps a list of what is still missing."
metadata:
  version: "1.2.0"
  author: Timmy Moser (timmymoser.com)
---

# Motion graphics video

One skill for the whole video. The user never needs another prompt: you ask for what you need, build with what you have, use placeholders for the rest, and always say what is still missing.

## How to run it

- Ask with multiple-choice questions (the pop-up when the app has one), never a wall of text. Always include these choices where they fit: **Upload now**, **I'll upload it later**, **Skip it**, **Type it out**.
- One question round at a time, at most four questions per round.
- Never stop because something is missing. Use a clearly labelled placeholder and carry on.
- Keep `STATUS.md` in the video's folder: every input, its state (have, later, skipped, placeholder) and what it blocks. Show the **Still needed** table at the end of every stage.
- Write in plain short lines. Show tables for plans and timings.
- Ask before spending credits (e.g. Runway) or deleting anything. Draft at 720p; render full size only when the user says it's final.

## Before you start: folder check

Run this once at the start of the chat, then start the job. Never re-teach setup here.

| You find | Do this |
|---|---|
| A folder with `WORKSPACE.md` | Read it, follow its house rules and paths, then start. Say nothing about setup |
| A folder, but no `WORKSPACE.md` | Ask once (multiple choice): **Use this folder as it is** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **Pick a different folder**. "As it is" means save this job's work in one subfolder named for the job |
| No folder | Ask once (multiple choice): **Add a folder: the + beside the message box, then Add folder** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **No folder: send me the files in this chat** |

After the answer: if they pick the fast setup, give the link and wait. If they pick a different folder, ask them to add it, then run this check again. If they pick no folder, work in the chat: ask for the files you need here, deliver every output as a file in the chat, and tell them where to save it on their computer.

Model: say in one line that Sonnet is the default. If this job needs Opus, say that too, before you start (the model guide is the "Which model?" card on timmymoser.com/claude/setup).

## Stage 0: Tool check (first video only)

1. The folder is already settled by the folder check above.
2. Check for ffmpeg, Python, Node, and Playwright with Chromium. Install what's missing. If a download source is blocked, find another official one. Render a 2 second test clip and report one line per tool.
3. Save the working rules to `STATUS.md`: never edit originals, ask before spending or deleting, plan before building, one version at a time, replace the old draft with each new one.

## Stage 1: Intake

Ask these in two rounds. Each has: Upload now / I'll upload it later / Skip it / Type it out (where it makes sense).

**Round 1**
| Question | Notes |
|---|---|
| Do you have a brief? | No brief? Offer "Type out the idea" and write a one-page brief from their answer for them to approve. |
| How long, and what size? | Choices: 15s, 30s, 60s, other. 1920x1080, 1080x1920, 1080x1080. |
| Which brand? | Upload brand guide or fonts, type the colours and fonts, or "Pick a clean neutral look". |
| Videos you'd like it to feel like? | Screen recordings of videos they love (on a Mac: Shift-Command-5). Skip = you use a clean default style. |

**Round 2**
| Question | Notes |
|---|---|
| Product screens? | Exported as SVG from Figma (or PNG). Later = placeholder screens labelled with what goes there. |
| Icons, logos, photos, video clips? | One question, multi-select. |
| A sound effects pack? | Upload one, "Make me a free one" (build it with ffmpeg), or skip sound. |
| Any shots to animate with AI (e.g. Runway)? | Optional. Only with a connected video tool and a quote before every run. |

Make the video's folder as `[video name]/` inside the working folder from the folder check (with a `WORKSPACE.md`, put it where that map says, e.g. `2 Projects/[name]/Motion/[video name]/`). With no folder, build it in the chat's workspace and deliver the files at the end. Then sort everything into it: `brief/`, `references/`, `assets/screens/`, `assets/icons/`, `assets/photos/`, `assets/clips/`, `assets/fonts/`, `audio/`, `renders/`. Name each file by what it shows. Check every screen, icon and logo renders cleanly and load the fonts. Never edit the originals.

## Stage 2: Plan

Read the brief and write a plan: every scene with a time, the assets you have against the ones still missing, and anything that needs a decision (e.g. the brief's timings add up to more than the target length). Show the timing table and ask the user to approve it or change it.

## Stage 3: Learn the style

**Use the one shared library.** First look for an existing motion library (a `MOTION.md`, made by this skill or by motion-library-builder; check `WORKSPACE.md` and `5 Claude/Motion library/`). If there is one, read it and use its live moves; only add moves this video needs.

If there's none, create it in `5 Claude/Motion library/` (or, without that layout, `Motion library/` next to the video's folder) with the same structure motion-library-builder uses: `MOTION.md` (brand, rules, catalogue of moves with codes like `HL1`, `SC2`, `TR3`), `HANDOFF.md`, `REFERENCES.md`, `references/`, `moves/`, `previews/`, `projects/`, `exports/`.

If they gave reference recordings: take a frame every second with the time on it as a contact sheet, take close-ups of key moments, and measure type sizes and weights, colours, how long each beat holds, the easing and how each shot moves into the next. Turn each move into a reusable component in `moves/` with a preview and a catalogue row in `MOTION.md`, in the user's brand. Reuse the library on every future video, and add new moves to it as you make them.

No references: use a clean default (one idea per shot, hard cuts, big type, brand colours only) and say so.

## Stage 4: Storyboard and animatic

One frame per shot with its number, start time, length, scene and what happens, marked HAVE or NEED for its assets, with placeholders where something is missing. Export it as a PDF, then an animatic (the frames at their real timings, as an MP4). Ask the user to move, cut or retime shots now.

## Stage 5: Build and review

1. Build the first draft: each shot is a move from the motion library (by its code) filled with that shot's own words, screens and photos. Real screens only, brand colours only. Render frame by frame in Chromium, encode with ffmpeg at 720p, save as v1.
2. Build a Draft page: if the video-review-dashboard skill is installed, hand over to it. Otherwise make an HTML page or artifact with the draft at the top, the shot list down the side, and for any shot they click, every other move from the library that fits, playing live with that shot's content. Let them leave notes and save picks.
3. When they say "apply my picks", re-render only the shots that changed and put the new version on the page. Repeat until it's right.

## Stage 6: Sound and final

Use only their sound pack (or the one you made). A whoosh on every cut and a cue on each move inside a shot (words landing, cards flying in, icons popping, screens sliding), aligned on the sound's peak, not its start, with short fades. No music unless they add a track. When they say it's final, render full size, save it in `exports/` and clear old drafts.

## Finish

Show the **Still needed** table one last time: every placeholder still in the video and every skipped input, with what it would improve. Offer to swap them in as soon as they arrive.
