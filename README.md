# Claude skills

Free skills for Claude, built and shared on [timmymoser.com/claude](https://timmymoser.com/claude).

Every skill here is plain text. You can read every file before you install anything.

## Skills

| Skill | What it does | Version | Download |
|---|---|---|---|
| [motion-library](skills/motion-library) | Save any reference video as a reusable move, make videos from your library, and review drafts shot by shot. Nothing else needed | 1.0.0 | [zip](https://github.com/mosertimmy/claude-skills/raw/main/downloads/motion-library-v1.0.0.zip) |
| [avoid-ai-design-slop](skills/avoid-ai-design-slop) | Briefs Claude before it designs, then audits the result against 25 AI design tells | 1.0.0 | [zip](https://github.com/mosertimmy/claude-skills/raw/main/downloads/avoid-ai-design-slop-v1.0.0.zip) |
| [claude-workspace](skills/claude-workspace) | Walks you through setting up one folder on your computer, organised with 5S, that Claude reads first and saves everything into. Script included | 1.2.0 | [zip](https://github.com/mosertimmy/claude-skills/raw/main/downloads/claude-workspace-v1.2.0.zip) |
| [chat-handoff](skills/chat-handoff) | Saves unfinished work to one file and gives you a single line to paste into a new chat | 1.0.0 | [zip](https://github.com/mosertimmy/claude-skills/raw/main/downloads/chat-handoff-v1.0.0.zip) |
| [hook-ideation](skills/hook-ideation) | Turns any subject, clip or idea into a ranked table of hooks and formats for reels, Shorts and TikToks | 1.0.0 | [zip](https://github.com/mosertimmy/claude-skills/raw/main/downloads/hook-ideation-v1.0.0.zip) |

Each skill folder holds `SKILL.md` (the instructions Claude follows), a short `README.md` and a `CHANGELOG.md`. The zips are in the [downloads](downloads) folder.

## Install a skill

1. Click the **zip** link for the skill you want in the table above. It downloads straight away.
2. In Claude, open **Customize**, then **Skills**, then **Add**, then **Upload a skill**.
3. Pick the zip as it is. Do not unzip it first.

## Check a download is genuine

Every zip has a SHA-256 checksum. The full list is in [SHA256SUMS.txt](SHA256SUMS.txt) and next to the download button on [timmymoser.com/claude](https://timmymoser.com/claude). If your file's checksum matches, it has not been changed.

**Mac or Linux**

```
shasum -a 256 motion-library-v1.0.0.zip
```

**Windows (PowerShell)**

```
Get-FileHash motion-library-v1.0.0.zip -Algorithm SHA256
```

Compare the result with the checksum in `SHA256SUMS.txt`. If they differ, do not install the file.

Every change to a zip is also recorded in this repo's [commit history](../../commits/main), so a swapped file would show up as a visible change.

## Read before you install

A skill is a folder with a `SKILL.md` file of instructions for Claude, plus a README and changelog. Open the folder in this repo and read `SKILL.md` first. That is exactly what Claude will follow.

If a skill ever asks you to do something you do not understand, such as running a script or sharing a login, stop and ask.

## Report a problem

Found something wrong or suspicious? [Open an issue](../../issues) and it will be looked at.

## Licence

Free to use and adapt for your own work. Please do not resell the skills as they are.

## Links

- Website: [timmymoser.com](https://timmymoser.com)
- Skills page: [timmymoser.com/claude](https://timmymoser.com/claude)
