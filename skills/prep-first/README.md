# Prep first

Makes Claude prepare a cheap local summary and contact sheet before it reads video, image batches or long files. Big token saving, same answers.

Includes `scripts/prep.py` (needs ffmpeg; tesseract optional).

## Install

**Claude app (claude.ai):** Settings, Capabilities, Skills, upload the zip.

**Claude Code:** unzip into `~/.claude/skills/` so you end up with `~/.claude/skills/prep-first/SKILL.md`.

Do not zip the folder again inside another folder. The skill folder must sit at the top level.

## Use

Attach a video or a batch of screenshots and ask your question. Say "token audit" for a review of where your tokens go.

## Update

Download the new zip and upload it again. It replaces the old version.

By Timmy Moser, timmymoser.com
