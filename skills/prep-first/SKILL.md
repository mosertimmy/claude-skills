---
name: prep-first
description: Use before reading any video, a batch of images or screenshots, a long transcript, log or big file. Makes a one-page summary and one contact sheet locally and reads those instead of the raw files. Also for a token audit.
metadata:
  version: "1.0.0"
  author: Timmy Moser (timmymoser.com)
---

# Prep first, then read

Reading raw video, image batches and long files is where most tokens go. Make a cheap local version first, read that, and only open the raw material for the exact bit the task needs. One summary and one image can replace 90 percent or more of the reading.

Works on the first message. The script ships inside this skill.

## When to use it

| Material | Prep, then read |
|---|---|
| A video or screen recording | `summary.json` plus one `sheet.jpg` (steps 1 to 3) |
| 5 or more images or screenshots | One contact sheet per 12 to 30 images (`ffmpeg -pattern_type glob -i '*.png' -vf scale=288:-1,tile=5x3`) |
| A long transcript, log or text file | `wc -l`, the headings, `grep` for the topic, then read only those line ranges |
| A web page | Fetch with a specific question, not the whole page |
| A big folder | List names, sizes and dates first. Read only what changed |

Skip it when exact detail is the job: judging colour, kerning, easing or a single seam in an edit. Then open the full-size frame, but only at the timestamp you need. Skip it too for one small image or a short file.

## 1. Check the tools

The script needs `ffmpeg` and `ffprobe`. With `tesseract` installed it also reads on-screen text. Check with `which ffmpeg ffprobe tesseract`. If ffmpeg is missing, try to install it. If that is blocked, say so and fall back to the plain-text rows in the table above.

## 2. Run it

```
python3 scripts/prep.py <video> [outdir]
```

It writes into `outdir` (default `<video>-prep/`):
- `summary.json`: duration, size, fps, loudness (LUFS), scene cuts and their times, average shot length, cuts per 10 seconds, and any on-screen text. About 1 KB.
- `sheet.jpg`: one image of up to 30 evenly spaced frames, with the spacing in the summary.
- `hook.jpg`: the first frame, small.

## 3. Read in this order

1. `summary.json`. It often answers the question on its own.
2. `sheet.jpg`, once.
3. Only if the task needs it: full-size frames at the timestamps from `cut_times_s` or the sheet spacing (`ffmpeg -ss <t> -frames:v 1`).

For spoken content, add a local transcript if one is available and read its word count and opening lines first. Never paste a full transcript in unless the task is about the words.

## 4. Say the saving on big jobs

For a job with 20 or more frames, give one line before and after, for example: "Raw: 75 frames, about 59,000 tokens. Prep: one sheet and a summary, about 3,200. About 95 percent less."

Estimate an image at width x height / 750 tokens, with the long edge capped at about 1,568 px. Say it is an estimate.

## 5. Token audit (when asked)

1. List the 5 tasks in recent chats where the most tokens went. For each, say what Claude was reading (images, video frames, long files, transcripts, web pages) and roughly what it cost each time.
2. For each, say whether a local step could do the heavy lifting first: ffmpeg (contact sheet, scene cuts, loudness), OCR, a local transcript, `grep`, `wc`.
3. For the top two, build the prep step and show a before and after estimate.
4. Wait for an OK before installing anything.

## Saving

Save every prep folder next to the source file. Delete nothing.

## Smoke test

Prompt: "Look at this screen recording and tell me what happens." Pass if Claude runs `prep.py` first, reads `summary.json` then `sheet.jpg`, and does not read the raw video frame by frame.
