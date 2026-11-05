# Claude skills

Free skills for Claude, built and shared on [timmymoser.com/claude](https://timmymoser.com/claude).

Every skill here is plain text. You can read every file before you install anything.

## Skills

| Skill | What it does | Version |
|---|---|---|
| [fast-setup](skills/fast-setup) | One-time setup that gets Claude ready for the rest of the guides | 1.2.0 |
| [infographic-guide](skills/infographic-guide) | Builds a clean, step-by-step A4 guide from one real example | 1.3.0 |
| [project-to-blog](skills/project-to-blog) | Turns a Claude project into a blog post draft | 1.3.0 |

More skills are added here as they go live on the site.

## Install a skill

1. Go to the [Releases](../../releases) page and download the zip for the skill you want.
2. In Claude, open **Customize**, then **Skills**, then **Add**, then **Upload a skill**.
3. Pick the zip as it is. Do not unzip it first.

## Check a download is genuine

Each release lists a SHA-256 checksum. The same checksum is shown next to the download button on [timmymoser.com/claude](https://timmymoser.com/claude). If the two match, the file has not been changed.

**Mac or Linux**

```
shasum -a 256 fast-setup-v1.2.0.zip
```

**Windows (PowerShell)**

```
Get-FileHash fast-setup-v1.2.0.zip -Algorithm SHA256
```

Compare the result with the checksum on the release. If they differ, do not install the file.

## Read before you install

A skill is a folder with a `SKILL.md` file of instructions for Claude, and sometimes a few helper files. Open the folder in this repo and read `SKILL.md` first. That is exactly what Claude will follow.

If a skill ever asks you to do something you do not understand, such as running a script or sharing a login, stop and ask.

## Report a problem

Found something wrong or suspicious? [Open an issue](../../issues) and it will be looked at.

## Licence

Free to use and adapt for your own work. Please do not resell the skills as they are.

## Links

- Website: [timmymoser.com](https://timmymoser.com)
- Skills page: [timmymoser.com/claude](https://timmymoser.com/claude)
- Setup help: [timmymoser.com/claude/setup](https://timmymoser.com/claude/setup)
