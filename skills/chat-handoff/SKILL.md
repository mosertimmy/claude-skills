---
name: chat-handoff
description: Use when the user is moving to another chat, closing or deleting this one, wants to hand work over, save tokens by starting fresh, or asks for a handoff. Writes a short handoff file for the unfinished work and ends with a one-line prompt to paste into the next chat.
metadata:
  version: "1.0.0"
  author: Timmy Moser (timmymoser.com)
---

# Chat handoff

When someone moves work to another chat, or deletes this one, nothing may live only in the conversation. Write it down, then give them one line to paste.

Works on the first message. No setup needed. A folder or Project is a bonus, never a requirement.

Triggers include: "move this to another chat", "new chat for this", "I will delete this chat", "save tokens", "hand this over", "write a handoff".

## Steps

1. **Save real work first.** Files, decisions and edits that belong somewhere go there before the handoff is written. Do not park real work in the handoff.
2. **Write the handoff.** One short file, plain language. Name it `HANDOFF-<topic>.md`. If the work already has a handoff file, update it instead of adding a second. Sections:
   - **Pick up:** one sentence on what this is.
   - **What exists now:** a table of the things made (name, link or path, what it does).
   - **Open items:** numbered, most important first, each with a suggested answer or next step. Mark anything blocked and why.
   - **Still to do:** what the user or the next chat must do, in order.
   - **Rules to keep:** only rules specific to this work.
   - Use full URLs and full paths. Never paste passwords, keys or tokens.
3. **Put it where the next chat will find it.** Pick the first that works:
   - A connected project folder: save it there.
   - A Claude Project: add it to the Project docs.
   - Otherwise: send it to the user as a file and say where to keep it.
4. **Finish with the pickup prompt.** One line in a code block, always last, naming the file and the single next action:

   ```
   Read HANDOFF-<topic>.md and carry on with <the next action>.
   ```

5. **Say what is safe to delete.** One sentence confirming nothing is lost if they delete this chat, plus anything that is not safe to lose (an unsaved file, a pending approval, a running job).

## Rules

- Never end a chat move without the one-line prompt, even for a small job.
- Unsaved files, blocked permissions and half-applied changes go at the top of Still to do.
- Do not paste the whole conversation. Decisions and state only, so the next chat starts cheap.
- Do not ask whether to write it. The user has already said they are moving.
- Only ask a question when the answer changes what gets written or where it goes. Otherwise take the sensible default and say so in the handoff.

## Smoke test

Prompt: "I am moving this to a new chat, write a handoff." Pass if a `HANDOFF-*.md` file exists with all five sections and the reply ends with a single paste-ready line.
