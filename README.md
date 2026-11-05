# Claude skills

Free skills for Claude, built and shared on [timmymoser.com/claude](https://timmymoser.com/claude).

Every skill here is plain text. You can read every file before you install anything.

## Skills

| Skill | What it does | Version |
|---|---|---|
| [fast-setup](skills/fast-setup) | One-time setup that gets Claude ready for making things: one folder, one project per idea, a few skills | 1.2.1 |
| [infographic-guide](skills/infographic-guide) | Builds a clean, step-by-step A4 guide that follows one real example | 1.3.1 |
| [project-to-blog](skills/project-to-blog) | Turns the work in a Claude project into a blog post draft | 1.3.1 |
| [project-update-check](skills/project-update-check) | Sweeps a Claude project and saves everything worth keeping to your workspace | 1.2.0 |
| [runway-people-generation](skills/runway-people-generation) | Makes realistic images and short clips of people with Claude and Runway | 1.2.0 |
| [video-review-dashboard](skills/video-review-dashboard) | Opens a first draft of a motion graphics video in a review page where you pick what to change | 1.2.0 |
| [motion-library-builder](skills/motion-library-builder) | Builds your own motion graphics library from sample videos and screen recordings | 1.2.0 |
| [motion-graphics-video](skills/motion-graphics-video) | A one-stop walkthrough for making a motion graphics video, from questions to final sound | 1.2.0 |

Each skill folder holds `SKILL.md` (the instructions Claude follows), a short `README.md` and a `CHANGELOG.md`.

## Install a skill

1. Go to the [Releases](../../releases) page and download the zip for the skill you want.
2. In Claude, open **Customize**, then **Skills**, then **Add**, then **Upload a skill**.
3. Pick the zip as it is. Do not unzip it first.

New to this? Start with **fast-setup**, or follow the guide at [timmymoser.com/claude/setup](https://timmymoser.com/claude/setup).

## Check a download is genuine

Every zip has a SHA-256 checksum. The full list is in [SHA256SUMS.txt](SHA256SUMS.txt), on each release, and next to the download button on [timmymoser.com/claude](https://timmymoser.com/claude). If your file's checksum matches, it has not been changed.

**Mac or Linux**

```
shasum -a 256 fast-setup-v1.2.1.zip
```

**Windows (PowerShell)**

```
Get-FileHash fast-setup-v1.2.1.zip -Algorithm SHA256
```

Compare the result with the checksum in `SHA256SUMS.txt`. If they differ, do not install the file.

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
- Setup help: [timmymoser.com/claude/setup](https://timmymoser.com/claude/setup)
