---
name: runway-people-generation
description: Use when someone wants realistic images or short clips of people made with Claude and Runway (product shots on models, lifestyle scenes in real places, their own likeness, keyframes, animations). Covers the cast, reference method, prompts, video keyframes and credit rules.
metadata:
  version: "1.2.0"
  author: Timmy Moser (timmymoser.com)
---

# Runway people generation (Claude + Runway)

Make realistic images and short clips of people in real places: AI models wearing or holding a product, lifestyle scenes, or the user themselves. Claude plans the shots, writes the prompts and runs Runway through the Runway connector. The user only ever pastes into Claude.

## Before you start: folder check

Run this once at the start of the chat, then start the job. Never re-teach setup here.

| You find | Do this |
|---|---|
| A folder with `WORKSPACE.md` | Read it, follow its house rules and paths, then start. Say nothing about setup |
| A folder, but no `WORKSPACE.md` | Ask once (multiple choice): **Use this folder as it is** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **Pick a different folder**. "As it is" means save this job's work in one subfolder named for the job |
| No folder | Ask once (multiple choice): **Add a folder: the + beside the message box, then Add folder** (Recommended) / **Do the fast setup first: timmymoser.com/claude/setup** / **No folder: send me the files in this chat** |

After the answer: if they pick the fast setup, give the link and wait. If they pick a different folder, ask them to add it, then run this check again. If they pick no folder, work in the chat: ask for the files you need here, deliver every output as a file in the chat, and tell them where to save it on their computer.

Model: say in one line that Sonnet is the default.

## Runway setup (first run)

1. Check the Runway connector is connected in Claude. If not, walk the user through adding it as a custom connector: open Connectors in Claude's settings (look for Customize or Settings, then Connectors), choose Add, name it Runway, paste `https://mcp.runwayml.com/mcp`, choose Continue and sign in to Runway. Then test it with a read-only call (list their workspaces).
   - Runway needs a paid plan with credits. If they don't have one, they can sign up at runwayml.com; Timmy Moser's code **mosertimmy25** gives 25% off any plan at checkout.
2. Make a subfolder for this job inside the folder from the folder check and save a `PEOPLE.md` in it: the brand or product, the cast, the reference library and the working rules below. Read it at the start of every chat. If `WORKSPACE.md` names a path for this kind of work, use that. With no folder, keep the same notes in the chat, save nothing, and ask the user to paste them back at the start of the next chat.
3. Ask for the files in one list (every other question is multiple choice):
   - **The product** (if any): clear photos from the front and back, plus the logo as a file. Describe where the logo sits ("small, on the wearer's left chest", "centred on the back").
   - **Places:** real photos of each location, ideally one from ground level where the person will stand.
   - **Look references:** 10 to 25 photos or ad stills whose camera, light and grade they love. These become the reference library.
   - **Their own photos** (only if they want themselves in the shots): 6 to 10 clear photos of their face from several angles, just them.

## Working rules

| Rule | Detail |
|---|---|
| Questions | Always multiple choice |
| Credits | Quote model, resolution, length and credits before every run. Wait for "go" |
| Cheap first | Draft stills at the lowest resolution. Go higher only when a logo must read or a face must hold. Draft video at 5 s on the cheapest model |
| One at a time | New looks run singly, so a bad prompt fails once |
| Review | Flag only what's wrong, never what's right |
| Major fails | Wrong logo text, a wrong or invented landmark, or the wrong face: don't keep it |
| Regenerate, don't edit | AI edits move or garble logos. Generate fresh |
| Fix with a fresh prompt | When an output has an issue (face drift, wrong pose, wrong logo), rewrite the prompt and rerun it from the original references only. Never feed a bad output back in as a reference or start frame. Chained re-edits compound the drift |
| Fix in post | One broken detail on a good take (a logo, a sign): fix it in an editor for 0 credits before any regen |
| Save | One outputs folder, `outputs/video/` for clips. Name files `<Place> - <light>.png`. Remove superseded versions once a new one is approved. With no folder, deliver every output as a file in the chat |

## Cast

1. **Make each model once and lock them.** Generate a portrait (head and shoulders, wearing the product) and a turnaround sheet (front, 3/4, back, full body). Approve both, then reuse them for every shot. Log each model's files in `PEOPLE.md`.
2. Never upload a real person's face unless it's the user themselves and they asked for it.
3. **When the model is the user:**
   - The face reference is a sheet of their real photos, used in every shot. Never swap in a generated portrait.
   - Use a 3/4 view instead of a side profile in turnarounds: profiles drift from the likeness.
   - Add "do not slim, lengthen or sharpen the face" to every prompt.

## Still method

Give every prompt its references by job, tagged so the model knows what each one controls:

| Tag | Source | Controls |
|---|---|---|
| @layout | A look reference | Camera height, angle, crop, subject size and position |
| @light | A different look reference | Time of day, sky, grade |
| @location | Real photo of the place | Buildings and the real standing spot only |
| @portrait | The model's portrait | Face, hair and logo position |
| @turnaround | The model's turnaround | Body and outfit |

- For a quick shot, one line of direction is enough ("Put the woman on the ferry with the skyline behind her, leaning on the rail"). Name exact references only when a shot needs one exact look.
- Write the pose new, in words, every time. Never feed an old output in as a pose.
- Give the subject size as a number ("about 45% of frame height") or people look pasted on.
- Real places stay accurate. The person stands somewhere that exists. No bokeh orbs, no lens flare circles, no readable signs or brand names; invent signage on generic streets.
- Logos read best at mid-thigh crops or tighter. Spell the letters out in the prompt ("the letters must read A-B-C").
- Leave flat product sheets out of still prompts if they pull the logo to the wrong place; let the portrait carry the logo position.

## Video

1. Before animating, ask: "Generate an end keyframe too?" Options: Yes, start + end locked (recommended when the person turns, walks towards camera or changes pose a lot: it stops face drift) / No, start frame only.
2. Before generating, show a short table of what the person does second by second, and wait for an OK.
3. **Start only:** use an approved still as the first frame. 5 s draft, same aspect ratio.
4. **Start + end:** generate the end keyframe fresh from the same original references as the start (never from the start frame or a clip), same scene, light and framing. Show both, then animate between them.
5. Motion prompt: locked camera, the scene moves, the person moves in one smooth continuous action. Write "fluid, natural, unhurried movement with no pauses". Face, hair and logo stay the same; buildings and signs don't morph.
6. Watch the draft frame by frame. If it passes, offer to upscale, extend to 10 s or build a multi-shot sequence (quote first). One broken detail: fix in post. Face drift or wrong motion: rerun with a fresh prompt.
