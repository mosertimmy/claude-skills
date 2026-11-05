---
name: project-to-blog
description: Use when someone wants a blog post from the work in a Claude project, or says "blog this project", "write a blog" or "check for new blogs". Researches the project, pitches topics, drafts instructional posts and (optionally) puts them in the site's CMS as drafts.
metadata:
  version: "1.3.1"
  author: Timmy Moser (timmymoser.com)
---

# Project to blog

Turn the work in the current Claude project into blog posts. Posts are instructional case studies: each teaches one useful method, shares the author's thinking and shows their skills. They are never summaries of everything that happened.

## Before you start: folder check

Run this once at the start of the chat, then start the job. Never re-teach setup here.

| You find | Do this |
|---|---|
| A folder with `WORKSPACE.md` | Read it, follow its house rules and paths, then start. Say nothing about setup |
| A folder, but no `WORKSPACE.md` | Ask once (multiple choice): **Use this folder as it is** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **Pick a different folder**. "As it is" means save this job's work in one subfolder named for the job |
| No folder | Ask once (multiple choice): **Add a folder: click Add folder under the message box, then Add folder again in the list** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **No folder: send me the files in this chat** |

After the answer: if they pick the fast setup, give the link and wait. If they pick a different folder, ask them to add it, then run this check again. If they pick no folder, work in the chat: ask for the files you need here, deliver every output as a file in the chat, and tell them where to save it on their computer.

## Ground rules

- **Questions:** ask every question as a multiple-choice pop-up (max 4 options per question). Never bury a question in a reply.
- **No employer or client work:** never name an employer, client, their products, people, internal docs or results. Write the method in generic terms ("a branded T-shirt", "a fintech app screen"). Prompts too: strip brand colours, logos, copy and names, and use [brackets] for what the reader swaps in.
- **Name the tools:** say clearly what made the work ("every image here was generated in Runway", "Claude planned the shots and wrote the prompts").
- **Never invent facts.** Write [ADD: what's needed] instead.
- **Never publish.** CMS items are always drafts.

## First run: blog choices

If `BLOG_SETUP.md` doesn't exist yet, ask once (after the folder check), then save the answers in it, in the blog folder named in `WORKSPACE.md` or the folder from the folder check:

1. Their style guide, if they have one. If not, offer to write a short one from 2 or 3 posts they like.
2. Their CMS (multiple choice, max 4 options): Framer / Webflow / WordPress / Other or none (markdown only). If a connector for it is available in Claude, note the collection and field names.
3. Categories they use.

With no folder, keep `BLOG_SETUP.md` and the tracker in the chat and deliver them as files.

Keep a tracker (`index.md`): one row per post, plus a "Chats covered" list per project and a "Last checked" date.

## 1. Research (never ask the user to paste anything, except files when there is no folder)

1. Read the style guide and the tracker.
2. Search and read every chat in this project, fully. If a chat isn't searchable, say so and use the project docs that cover it.
3. Read the project docs and project files.

## 2. Map the topics

- Group the chats into distinct topics. One topic = one method someone could learn.
- Per topic: short name, the angle in one sentence (name the method, not the project), chats it draws on, and whether it has enough for a post alone.
- Prefer one complete post that follows a method end to end over a split series, unless it would run far past 2,500 words.

## 3. Ask what to write (pop-up)

- Q1 (multi-select): "Which topics should I write about?" One option per topic, angle as the description.
- If more than one is picked, Q2: "One combined post or separate posts?" Options: one combined post / separate posts (a series) / let me group them.
- Wait for answers.

## 4. Draft

Instructional posts about AI tools follow this guide format:

- **Hook:** 1 to 3 short lines, no heading.
- **Intro:** one paragraph on what the reader gets, the tools, and where they work (e.g. "you only ever paste into Claude, which runs Runway").
- **Follow one output the whole way:** one real image or clip, with its real inputs and outputs shown at each step.
- **No "The steps" overview and no "How each tool is used" section.** The numbered steps below are the whole method; name the tool in each step heading instead.
- **"What is [tool]?" (only when one tool is the star):** its own H2, two lines on what the tool is and what it does in this method, then one image of it: its logo or a crop of its interface (the prompt area only; no names, avatars, credits, tabs or browser UI).
- **Free skill box right after the intro** when the author has a matching free skill: the skill name and one install line.
- **Setup:** never explain it in the post body and never mention the setup guide. Only a tool the post is about (e.g. a connector) gets its own "Step 0" with real screenshots.
- **Numbered step H2s** in the order you'd do the work: "Step N: [action] with [tool]", a one-line explanation, then bold-lead paragraphs numbered by their step ("**2.1 Make a folder:** ...", "**2.2 ...**"; a tool's setup is 0.1, 0.2) so images and prompts can sit between them. Use the same numbers as the guide when there is one.
- **Bold "Copy this prompt:"** directly above every prompt block, inside the step where it's used. Prompts are full, generic, with [brackets], and open with the instruction to the tool.
- **Images right after the line that produces or adds them.**
- **Happy flows only.** Fold fixes into the step or prompt so the reader never hits the problem. No troubleshooting sections.
- **No prep-only steps:** every step ends with something made.
- **No commentary blocks:** no golden rules, stats boxes, settings tables or folder diagrams.
- **Teach the method, not the inventory:** one line on the idea plus the rule that makes it work.
- **Series (only if chosen):** each part stands alone; mention the other parts by name.
- **At the very end, in this order:** a "What it costs" line, then "Related guides" by name (two at most), then one useful or dry closing line. If the project has a guide, offer the PDF through Button 1 only (label "Download the guide (PDF)"), never as an inline line in the body and never with a page or step count. A post with no guide has no PDF button. No conclusion heading.
- Length: 900 to 2,200 words.
- Fields above the body: Title, Slug, Category, Lead (110 to 155 characters), Date, Read time (words / 220, rounded up), Cover + alt.
- Draft one post at a time.

## 5. Visuals

- Pick the best 6 to 14 images or videos: the followed output's real inputs and outputs, setup screenshots, before/after pairs.
- Mark each spot as `[IMAGE: alt text (media/name.ext)]` or `[VIDEO: ...]`, with context in the next paragraph.
- Copy, never move, originals. Web versions: images 2000 px max, JPEG quality 85; video H.264 MP4, 1080p, no audio.
- Missing visual (e.g. a screenshot not taken yet): use a plain grey placeholder and list it in `media/todo.md`.
- Flag anything confidential: work data, client names, personal files, real people, third-party photos.

## 6. Save and send to the CMS

Save `post.md`, `sources.md` (chats used with dates, files, where each fact came from) and `media/`. Keep earlier versions in `drafts/`. Update the tracker.

If a CMS connector is set up:
- Create the item as a draft, with every field filled, including category.
- Upload images through the connector's upload flow and insert them where the markers are.
- Prompts: use a copyable prompt block or component if the site has one; otherwise a code block.
- Don't put a code block inside a numbered list (most CMSs restart the numbering). Use bold-lead paragraphs instead.
- Tell the user what to check in the editor (video blocks, alt text, layout).

No connector: hand over `post.md` and the `media/web/` files ready to paste in.

## 7. Recheck ("check for new blogs")

1. Read this project's tracker section, then find chats, docs and files that are new or changed since the last check.
2. Sort into: new topics, updates to existing posts, additions to a series, or nothing new (say so in one line and stop).
3. Pop-up: which items to act on. For updates to a written post: "Update the existing post, or write a follow-up?"
4. Update "Last checked" even when nothing is new.

## Finish

One short summary: what was drafted, where it is, and anything to check in the editor.
