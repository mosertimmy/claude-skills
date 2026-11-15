---
name: avoid-ai-design-slop
description: Use before and after designing any page, slide, infographic or UI with Claude. Briefs the design to dodge AI slop tells, then audits the result against a 25-point checklist.
metadata:
  version: "1.0.0"
  author: Timmy Moser (timmymoser.com)
---

# Avoid AI design slop

Claude reaches for the most probable design choice when nobody decides. This skill makes the decisions first, then checks the result against known tells.

Works on the first message. No setup, no folder, no other skill needed.

## 1. Brief first (before building)

Settle these before drawing anything. If the user already has a brand or design system, use it. If not, ask once, as multiple choice, and let them skip any item:

1. **Fonts:** one display font and one body font, named, with a role for each.
2. **Palette:** four to six named hex colours, each with a role. No Claude orange (#D97757) and no cream plus terracotta unless it is the user's own brand.
3. **Content:** which text and numbers are real. Use only figures the user supplied. Leave a stat blank or marked as a placeholder rather than inventing it.
4. **One idea per screen.** Say what is being left out.

If they skip everything, pick a plain neutral default (one sans font, black, white and one accent) and say what you picked.

## 2. Build rules

- Plain headings. No eyebrow or label above a title unless it does real work.
- One font family and weight system. No serif over mono pairing as a reflex.
- Rows or tables for lists. Vary size by importance. Do not repeat one rounded card with a coloured left stripe.
- No highlighted word in a headline (italic, bold or coloured).
- No emoji as icons.
- Short, specific copy. No filler such as "seamless", "unlock", "magic" or "supercharge".

## 3. Audit (after building)

Check the output against all 25 tells and list every one it hits, with the fix. Fix them, then re-check once.

**Core seven**
1. Too much detail: subtitles, stat strips, footnotes, badges nobody asked for
2. Floating eyebrow: small all-caps label above a heading
3. Default font: unchosen Inter or system stack, or a serif headline over a mono label
4. Claude's orange: terracotta accent on cream
5. The same card everywhere: identical rounded boxes, soft shadow, left stripe, centred hero over three equal cards
6. One highlighted word in a headline
7. Invented numbers and filler copy: "10,000+ users", made-up ratings, "Get Started"

**Type**
8. Instrument Serif headings
9. Tight negative letter spacing
10. Excessive italics
11. Mono fonts everywhere
12. ALL CAPS subtitles
13. A full stop at the end of titles

**Layout**
14. Tags and pills
15. Dividers between everything
16. A border around every container
17. Numbered sections (01, 02, 03) on things that are not a sequence
18. Code-style breadcrumbs

**Decoration**
19. Gradient backgrounds
20. Dithering
21. ASCII art images
22. Squircle shapes
23. Too many colour shades and opacities

**Detail and copy**
24. Over-detailed UI mockups and diagrams
25. Wordy text that repeats itself

## 4. Report

End with a short table: tell, where it appeared, what changed. If a tell is kept on purpose (for example a cream page for a brand that owns it), say so and why.

## Smoke test

Prompt: "Design a one-page landing for a plant shop." Pass if Claude asks or states fonts and palette first, builds without invented stats, and ends with the audit table.

## Source

The first seven come from the post "7 signs Claude designed your visuals" on timmymoser.com. Tells 8 to 25 draw on a TikTok checklist of 20 AI design slop indicators by @charles.unemployed, merged with overlaps removed.
