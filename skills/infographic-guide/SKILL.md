---
name: infographic-guide
description: Use when someone wants an instructional infographic, guide PDF or how-to graphic about a workflow with AI tools (e.g. Claude + Runway). Builds a clean step-by-step A4 guide that follows one real example from start to finish.
metadata:
  version: "1.3.2"
  author: Timmy Moser (timmymoser.com)
---

# Instructional infographic guide

Build an easy-to-follow, actionable guide as a set of designed A4 pages that export to one PDF. The guide follows one real piece of work from the first step to the finished output, so the reader sees exactly what they will get.

## Before you start: folder check

Do this once at the start of the chat, then start the job. Never explain it.

| You find | Do this |
|---|---|
| A folder is connected | Work in it. Save this job's work in one subfolder named for the job. If the folder holds a `WORKSPACE.md`, read it and follow it |
| No folder | Work in the chat. Ask for the files you need here, deliver every output as a file in the chat, and tell the user where to save it on their computer. Offer once (multiple choice) to add a folder: **Add a folder: click Add folder under the message box** / **Carry on in this chat** |

Model: say in one line that Sonnet is the default. If this job needs Opus, say that too, before you start.

## Where to build it

- Build it in Claude as a design: one artboard per page, A4 fixed pages (794 x 1123 px), exported together as one PDF.
- If the Design artifact type isn't available, build each page as an A4 HTML page and export to PDF.
- Ask every question as a multiple-choice pop-up where the app supports it.

## Before designing

1. **Source the method.** Use the user's own notes, chats, blog posts or project files. Never invent steps, settings or costs. If something is missing, ask.
2. **Pick one real output to follow the whole way** (e.g. one finished image and the clip made from it). Find its real inputs: reference photos, product shots, portraits, screenshots, video frames. Ask the user to attach them if you can't reach them.
3. **Branding.** Ask which brand to use: the user's own (colours, font, logo) or a clean neutral look (black, white and one accent colour).
4. **Logos.** Use official tool logos only. Ask for any you don't have rather than drawing one.

## Page structure

1. **Cover:** black, big title naming the tools (one accent colour on the tool names), a one-line subtitle, and the followed output as one large image. No eyebrow pill or label above the title, no boxes on the image, no header strip.
2. **The steps:** one row per step (never a grid or columns): number, title, one-line description, tool tag. The guide's own tool setup is step 0.
3. **How each tool is used:** black page, one white box per tool, tool logo on top with its role left-aligned underneath. Rows of best practices, each with a short line on what it gives you ("saves tokens and speeds up every review"). Editing apps can share one box.
4. **Before you start (one box, no setup steps):** the guide never re-teaches setup. One line: attach your files to the chat or add a folder. Then, only if the guide's own tool must be connected (e.g. the Runway connector), a step 0 page for that tool alone: real screenshots, one per action, plus the link in a copy box.
5. **One page per step** (spill onto a "continued" page if needed):
   - Headline "Step N: [action]", with no highlight behind the words.
   - One-line explanation underneath.
   - A single-line header like "DO THIS IN CLAUDE".
   - Walkthrough rows numbered by their step: N.1, N.2, N.3 (setup rows are 0.1, 0.2). Each has a bold lead. Steps that spill onto a "continued" page keep counting (4.4, 4.5).
   - The prompt sits inside the row where it's used, in a filled grey box, with "Copy this prompt" and its subline stacked left-aligned.
   - Images go below the text of the row that produces or adds them, on a light grey card (#F5F5F5, 16 px radius, 16 px padding), shown uncropped (never cut off heads or covered by a label). Back-to-back images with no text between them share one card.
   - Choices inside a step are "Option 1" and "Option 2" rows, each with its own prompt.
6. **End page:** black, the word "End" centred, then a QR code to the author's page on a white rounded card (140 px card, 100 px code, 20 px padding) so it has a clear quiet zone. Build the QR as an inline SVG and test-scan it before export.

## Content rules

- Simpler is better. No commentary blocks (golden rules, stats, "what Claude found"), no settings tables, no folder diagrams. Settings live in the step text or the prompt.
- Happy flow only: checks are steps, fixes are the last step. No troubleshooting asides, no prep-only steps.
- If one tool drives the others (e.g. you only ever paste into Claude, and Claude runs the other apps through connectors), say so everywhere. Every prompt opens with the instruction to the tool.
- The general working rules (ask before deleting, plan before building, save to the project folder) are the reader's own and are never repeated. The guide's first prompt carries only the tool's own rules: ask before spending credits, draft on the cheapest settings first, run one look at a time, remove superseded versions.
- Prompts are generic, with [brackets] for what the reader swaps in. No private brand names, people or client details.
- Ask once whether the user has a referral or discount code for any tool in the guide. If they do, show it in a copy box wherever that tool is set up, and on the costs line.
- Plain short lines, left-aligned labels and sublines, no em dashes.

## Process

1. Outline the pages in one message, then build the cover and steps page first.
2. Publish page by page, say what's on each page in a short table, and remind the user to check nothing is clipped at the bottom of full pages.
3. If the user edits pages by hand between turns, re-read any page they touched before changing it, keep their edits, and say if a publish replaced anything.
4. When the guide is done, offer to turn it into a blog post with the same structure.
- **Chat-first prompts.** Every lesson must work with no setup: prompts assume the reader attaches or pastes the content into the Claude chat ("the take I've attached to this chat"), never a folder or file path.
- **Name every product and link its official page** (no tracking parameters), in the guide and in any blog post.
- **Check every page fits A4** before export: render each page at 794 x 1123 and tighten images or spacing on any page that runs over.
- **If you also write a blog post from the guide:** same steps, titles, numbering and prompts. Layout: intro, result image or video, free skill box if one exists, a "What is [tool]?" section when one tool is the star, the steps, then at the very end a "What it costs" line, Related guides and a closing line. Offer the guide PDF through the post's download button only, never as an inline line, and never with a page count. A blog never repeats the guide's "The steps" or "How each tool is used" pages.
