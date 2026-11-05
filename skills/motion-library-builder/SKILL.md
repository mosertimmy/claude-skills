---
name: motion-library-builder
description: Use when someone wants to build or grow their own motion graphics library with Claude (train it on sample videos and screen recordings, add new moves), or edit a reel, Short, TikTok or YouTube video from their footage using the library. For one whole motion graphics video made from scratch, use motion-graphics-video, which shares this same library.
metadata:
  version: "1.2.0"
  author: Timmy Moser (timmymoser.com)
---

# Motion library builder

Build a personal motion graphics library that Claude learns from the user's own samples, then use it to make every video. The library is a folder of reusable animated "moves" (title reveals, cards, screen frames, transitions, captions), each with a code, a preview and rules for when to use it. Videos are only ever made from moves in the library, so every video looks like the user's brand and gets better as the library grows.

Pairs with the **video-review-dashboard** skill, which lets the user scrub a draft and swap moves shot by shot, and with **motion-graphics-video**, which makes whole motion graphics videos from the same library. There is only ever one library: always look for an existing `MOTION.md` before creating one.

## Before you start: folder check

Run this once at the start of the chat, then start the job. Never re-teach setup here.

| You find | Do this |
|---|---|
| A folder with `WORKSPACE.md` | Read it, follow its house rules and paths, then start. Say nothing about setup |
| A folder, but no `WORKSPACE.md` | Ask once (multiple choice): **Use this folder as it is** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **Pick a different folder**. "As it is" means save this job's work in one subfolder named for the job |
| No folder | Ask once (multiple choice): **Add a folder: the + beside the message box, then Add folder** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **No folder: send me the files in this chat** |

After the answer: if they pick the fast setup, give the link and wait. If they pick a different folder, ask them to add it, then run this check again. If they pick no folder, work in the chat: ask for the files you need here, deliver every output as a file in the chat, and tell them where to save it on their computer.

Model: say in one line that Sonnet is the default. If this job needs Opus, say that too, before you start (the model guide is the "Which model?" card on timmymoser.com/claude/setup).

## What the user needs to feed it

Tell the user this up front, in one short list, and ask them to attach what they have (skip anything they already attached):

1. **Brand basics:** logo (SVG or PNG), colours, fonts (files or names).
2. **Samples, 3 to 10 videos:** motion graphics they love and want to look like. Ads, reels, product launches, explainers. Downloads or screen recordings of them both work. The more samples, the better the library.
3. **Screen recordings of their own product or tools:** whatever will appear on screen in their videos. Record at full resolution, 60 fps if possible, clean UI, no cursor wobble, a few seconds of stillness at the start and end of each action.
4. **Their footage style** (optional): a talking-head clip or B-roll they usually use, so moves are designed around it.

Samples teach the motion. Screen recordings are the content. Never redraw a screen by hand when a real recording exists.

## First run: format, engine and library folder

1. Ask which format they make most: 9:16 (Reels, Shorts, TikTok), 16:9 (YouTube) or both.
2. Pick the engine. Default to **Remotion** (React, renders MP4 with Node). If they can't run code locally, use HTML + GSAP pages rendered frame by frame with Playwright and ffmpeg in Claude's workspace.
3. Create the library folder, once: in `5 Claude/Motion library/` if the workspace folder has a `5 Claude/` folder, otherwise as `Motion library/` inside the job subfolder from the folder check (with no folder, in the chat workspace, delivered as files). Note its path in `WORKSPACE.md` if there is one.

```
motion-library/
  MOTION.md        brand, rules, the catalogue of moves (source of truth)
  HANDOFF.md       latest state, open items, links
  REFERENCES.md    what each sample taught, with frame grabs
  references/      the samples and screen recordings
  moves/           one component per move
  previews/        a short preview clip per move, per format
  projects/        one folder per video
  exports/         finished videos only
```

## Training: turn samples into moves

1. **Break each sample down.** Extract frames at every scene change (ffmpeg scene detection) and at key moments. For each moment, write what moves, from where, how long it takes, the easing, the layout and what job it does.
2. **Group into slots** (the job a move does): line, headline, list, pair, stat, screens, transition, card, photos, brand, icons, captions, end screen.
3. **Propose the moves** as a table: code, name, slot, format (9:16, 16:9 or both), which sample it came from, one line on the look. Codes are short and stable (e.g. `HL1` headline, `SC2` screens, `TR3` transition).
4. **Ask which to build** (multiple choice). Build each picked move as a component with props (text, image, screen recording, colours from the brand), never hard-coded content.
5. **Render a preview** of each move (3 to 5 s, with placeholder content in the user's brand) and show them together. If artifacts are available, publish a library page: previews grouped by slot, with a 9:16 / 16:9 switch.
6. **Log every move in `MOTION.md`:** code, slot, format, status (live or retired), source sample, props, and its do's and don'ts.
7. **Feedback becomes rules.** Every time the user says "never do X" or "always Y", add it to the rules in `MOTION.md` with the date, and retire moves they reject (keep the row, mark it retired).

Add new samples any time: "add this to my motion library" runs steps 1 to 6 for just that sample.

## Making a video with the library

1. Read `MOTION.md` first, every time, then `HANDOFF.md`.
2. Pick the format: portrait talking head or "Reel / Short / TikTok" means 9:16; landscape or "YouTube" means 16:9; ask if it's unclear.
3. Transcribe the footage first. Cut restarts and repeats across the whole take, and cover look-aways with graphics or B-roll.
4. Write a shot list: `{id, label, slot, move, t0, duration}`. Use only live moves from the catalogue. A new style gets added to the library (component, preview, catalogue row) before it's used.
5. Render a low-res draft first, then hand over to the video-review-dashboard skill if it's installed.
6. Render the final at full size only once the user signs off. Keep only the latest draft and the final; remove superseded renders.

## Default rules (the user's own rules override these)

- No text over a face. In 9:16, text and cards sit below the chin; in 16:9, beside the speaker.
- Captions follow sentences, no all-caps words, and are checked against what was actually said (speech-to-text drops words).
- No dips to black. Morph or transition between shots.
- Don't push or zoom between two shots that share the same frame of the speaker. Move the camera only when the layout changes.
- Real screens and official logos only.
- One idea per graphic. No mixed bold and regular words animating in one title; let captions carry the words.
- Check every card before rendering: buttons and pills sized to their label with real padding, nothing clipped or touching an edge.
- B-roll: never repeat a clip in one video, use each clip's best stable stretch.
- Never play live footage inside a browser render (seeks aren't frame-exact and it stutters). Composite real footage frames with ffmpeg or Python instead.
- Ask questions as multiple choice. Never ask the user to run commands Claude can run.

## Keeping it in sync

When the library changes, update in one go: the move's component, its previews, the catalogue row in `MOTION.md`, `HANDOFF.md` and the library page. Before overwriting a file that another chat may have edited, re-read it and merge.
