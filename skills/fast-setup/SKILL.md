---
name: fast-setup
description: Use when someone wants to set up Claude for making things (reels, YouTube videos, blog posts, guides, AI images, motion graphics), says "set me up with the fast setup", "set up Claude", or "continue my Claude setup". A guided one-time setup of their folder, working rules, first project, apps and the other free skills.
metadata:
  version: "1.2.1"
  author: Timmy Moser (timmymoser.com)
---

# Fast setup for Claude

A guided one-time setup by Timmy Moser (timmymoser.com). One folder, one project per idea, a few skills. This skill carries the whole script, so it works without web access. Run it as a guided setup.

## How to work

- One step at a time. Finish a step, say what you did in one line, then start the next.
- Every question as multiple choice (the question pop-up if you have one), recommended option first.
- Do the work yourself wherever you can. When only the person can do it (a click in settings, a sign-in), stop, tell them where to click in plain words, and wait for them to say done.
- Never delete anything. Never overwrite a file that already exists: save beside it.
- Ask before installing anything or spending money or credits.
- Use the person's language and spelling. Plain words, short lines.
- App menus move. If a click path here doesn't match what the person sees, describe what to look for ("the Connectors page", "the Skills list") and ask them what they see.
- If a step needs something you can't do in this app, say so plainly in one line and skip it.
- Keep the **Setup checklist** in WORKSPACE.md up to date after every step (step 3 creates it). If the person says "continue my Claude setup", read it and resume at the first step not done.
- Model: say in one line that Sonnet is the default for almost everything.

## Step 0: Check the basics

Check in this order and stop at the first one that's missing:

| Check | If missing, tell them |
|---|---|
| A paid plan (Pro, Max, Team or Enterprise) | Skills and file work need one. Upgrade at claude.ai/upgrade, then come back to this chat |
| They're in the Claude desktop app | Download it from claude.ai/download, open this chat there and send a message |
| Code execution and file creation are on | Settings, then Capabilities, then switch on "Create and edit files" |

## Step 1: Get to know them

Ask in one round:
1. What do you want to make? (multi-select) Reels or short videos / YouTube videos / Blog posts / Guides or infographics / AI images and videos of people / Motion graphics videos
2. Which apps do you use? (multi-select) Your website builder (Framer, Webflow, WordPress) / Canva / Runway / Google Drive / Notion
3. Where should your Claude work live? Documents/Claude (recommended) / Desktop/Claude / Somewhere else
4. How should I write for you? Short and punchy / Detailed / Formal

## Step 2: Add the folder

Tell them:
1. Make an empty folder where they chose (e.g. a folder called Claude inside Documents).
2. In this chat, click **Add folder** under the message box, then click **Add folder** again in the list and pick it.

Then check you can see the folder by listing it. If you can't, ask them to try again or describe what they see. Don't continue until the folder works.

## Step 3: Build the master folder

In their folder, create:

```
1 Website/      site pages and blog posts (only if they have a site)
2 Projects/     one folder per idea
3 Work/         client or job work, kept separate
4 Assets/       logos, reused footage, photos, sound, references
5 Claude/       skills, motion library, tools, notes
_to_delete/     scratch waiting to be cleared
WORKSPACE.md    the map
```

Write `WORKSPACE.md` with:
- A table: each folder, what it holds, what to read first.
- **House rules:** their writing style from step 1, every question as multiple choice, ask before deleting, installing or spending credits, move scratch to `_to_delete/`, save every output in its project folder.
- **Naming:** `Subject - what happens - original ID` (e.g. `A-roll 01 - main take - IMG_2981.MOV`).
- An empty **Moved paths** table and **Folder changes log**, with a note: update both whenever a folder is added, moved or renamed.
- A **Setup checklist** with steps 0 to 9 of this skill, ticking off what's done.

Show them the folder tree you made.

## Step 4: Save the working rules

Write this block, filled in with their answers, in a copy box:

> My Claude work lives in [folder]. Read WORKSPACE.md there before any task. Ask me every question as multiple choice. Show me the plan before you build. Ask before you delete anything, install anything or spend credits. Draft on the cheapest settings first, one version at a time. Remind me to use Sonnet for everyday tasks and tell me when a job needs Opus. Save every output in its project folder. Write [their style].

Ask them to paste it into their personal preferences in Claude's settings (click your name in the lower-left corner, then Settings, then Profile, or General on some versions, and find the box "What personal preferences should Claude consider in responses?"), so every chat starts with it. Then ask them to pick Sonnet in the model menu under the message box and keep it as their default. Opus and Fable use the weekly limit much faster: Opus is for hard planning, deep research or when Sonnet gets stuck; Fable is for the hardest, longest jobs and costs extra on Pro. Haiku is fine for quick lookups.

## Step 5: Make their first project

Ask for the idea's name (or offer "My first project"). Create:

```
2 Projects/[name]/
  README.md          what's in here, plus an Outputs table: type, name, status, where it lives
  CHANGELOG.md       one dated line per change
  PROJECT-RECORD.md  the full record, written when it's finished
```

Add Footage/A-roll/ and Footage/B-roll/ only if they make video. Add YouTube/, Reels/[name]/ or Infographic/ (each with Final Output/) only when that output exists. Add the project to WORKSPACE.md.

Then ask them to make a Claude Project with the same name (Projects in the sidebar, then New project) and add one doc called `START-HERE-pointer.md` with this text in it (give it in a copy box):

> [Project name]. The project folder is 2 Projects/[name]/ inside [folder]. Read WORKSPACE.md and this project's README.md before any work. The copy on my computer always wins.

Tell them: one chat per output inside the Project (REEL, YOUTUBE, BLOG, GUIDE, WRAP UP). If a new chat can't see the folder, add it again with Add folder under the message box.

## Step 6: Connect their apps

Only for the apps they picked in step 1, one at a time. Connectors live in Claude's settings (click Customize in the left sidebar, then the Connectors tab).

| App | How | What Claude can do |
|---|---|---|
| Google Drive, Notion, Canva | Pick it from the Connectors list and sign in | Read and make files and designs |
| Framer, Webflow, WordPress | Pick it from the list if it's there. If not, skip it: Claude hands over the finished text to paste in | Add blog posts and pages as drafts |
| Runway | Customize, Connectors, Add, Add custom connector. Name it Runway, paste `https://mcp.runwayml.com/mcp`, save. Then search "runway" on the Connectors tab, click Connect, Continue connecting, sign in, Allow access, Continue to Claude. Runway now shows Disconnect | Make images and video for them |

For Runway: if they don't have a plan yet, tell them they can sign up at runwayml.com and use Timmy's code **mosertimmy25** at checkout for 25% off any plan. Runway uses paid credits.

After each one, test it with a read-only call (list their files, projects or workspaces) and report one line.

## Step 7: Check the tools

Most work runs in your own workspace, not on their computer. Check what you have there for what they make:

| They make | Tools |
|---|---|
| Anything | Python, Node.js |
| Videos, reels, motion graphics | ffmpeg, Playwright with Chromium |
| Guides or infographics | Playwright with Chromium |

Install anything missing in your workspace (no need to ask: it doesn't touch their computer). Only if you work directly on their computer and a tool is missing there, ask first, then install from the official source. Report one line per tool. Never ask the person to type commands.

## Step 8: Add the skills

The skills are free at timmymoser.com/claude. Recommend only what their answers need:

| They make | Skill | What it does |
|---|---|---|
| Anything | project-update-check | Saves everything from a project's chats into the folder and keeps it tidy |
| Blog posts | project-to-blog | Pitches and drafts blog posts from a project |
| Guides or infographics | infographic-guide | Step-by-step A4 guides that follow one real example |
| Motion graphics videos | motion-graphics-video | Makes a whole motion graphics video, from questions to final |
| Reels, YouTube, motion graphics | motion-library-builder | Builds their own library of motion moves from videos they love |
| Reels, YouTube, motion graphics | video-review-dashboard | A page to review each draft shot by shot |
| AI images and videos of people | runway-people-generation | Consistent people in Runway images and clips |

Tell them how, one skill at a time:
1. On timmymoser.com/claude, select Download next to the skill. Keep the zip as it is (don't unzip it).
2. In Claude, open Skills (click Customize in the left sidebar, then the Skills tab), choose Add, then Upload a skill, and pick the zip.
3. Make sure the skill is switched on.

Wait for "done" after each, then tick it off in the checklist.

## Step 9: Finish and hand over

Show one table: what was set up, where it lives, what's still to do. Tick the checklist.

Then explain: skills only load in a new chat. Ask **What do you want to make first?** (Reel or short video / YouTube video / Blog post / Guide or infographic / AI images and videos of people / Motion graphics video) and give them the matching starter prompt in a copy box, filled with their project name. Tell them to open their Project, start a new chat, add the folder and paste it.

| First thing | Starter prompt |
|---|---|
| Reel or short | Read WORKSPACE.md and 2 Projects/[name]/README.md. I want to make a 9:16 reel about [topic]. Use the motion-library-builder skill. If I have no motion library yet, help me build one from 3 videos I love first. |
| YouTube video | Read WORKSPACE.md and 2 Projects/[name]/README.md. I want to make a 16:9 YouTube video about [topic]. Plan it with me as a shot list, then use my motion library for the graphics. |
| Blog post | Read WORKSPACE.md and 2 Projects/[name]/README.md. Use the project-to-blog skill to pitch blog posts from this project. |
| Guide or infographic | Read WORKSPACE.md and 2 Projects/[name]/README.md. Use the infographic-guide skill to make a step-by-step A4 guide on [method], following one real example the whole way. |
| AI photos and videos of people | Read WORKSPACE.md and 2 Projects/[name]/README.md. Use the runway-people-generation skill to make [what] of [who] in [place]. Quote credits before every run. |
| Motion graphics video | Read WORKSPACE.md and 2 Projects/[name]/README.md. Use the motion-graphics-video skill to make a [length] [size] video about [product or idea]. |

End with one line: there's no one starting point. Every output reads from the project and writes back to it, so the first thing they make becomes the start of the next.

*Fast setup v1.2.1 · Timmy Moser · timmymoser.com*
