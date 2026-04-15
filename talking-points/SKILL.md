---
name: talking-points
description: Use when the user wants livestream, long-form video, or shorts talking points in the Ship Sh!t Show style, especially when they have source links, rough ideas, or topic notes and want them turned into structured sections, hooks, clips, stats, and distribution ideas.
---

# Talking Points

Determine the skill directory from the path of this `SKILL.md` and use that as `$SKILL_DIR` when reading bundled references.

This skill turns raw research, source links, notes, or a rough thesis into Ship Sh!t Show style talking points.

## Inputs

Use any combination of:

- `vault_path`
- `vault_repo_url`
- `episode_path`
- a pasted topic brief
- source links
- transcripts
- trend research
- target runtime
- format constraint:
  - livestream
  - long-form video
  - short

If the user provides a real episode path from the vault, read `notes.md` first when present. Otherwise read `overview.md`, then `description.md`, then `transcript.md` as supporting context.

## What This Skill Produces

Use this skill to generate:

- livestream rundown notes
- long-form video talking points
- segment-by-segment outlines
- intro hooks
- clip callouts
- conclusion beats
- source and stat sections
- distribution notes

## Core Rule

Do not generate bland bullet lists.

Your output should feel like a real Ship Sh!t Show show plan:

- a hard open
- clear sections
- a strong thesis
- fair setup, then sharper take
- clip-worthy lines called out explicitly
- concrete examples and stats

## Workflow

1. Ground in the house style.
   - Read [references/vault-talking-points-shape.md](references/vault-talking-points-shape.md).
   - Read [references/section-and-clip-patterns.md](references/section-and-clip-patterns.md).

2. Resolve the content mode.
   - `livestream` should be the most detailed and segment-driven.
   - `long-form video` should be tighter and less rundown-heavy.
   - `short` should be hook-first and payoff-fast.

3. Identify the argument.
   - What is the claim?
   - What is the conflict?
   - What changed this week?
   - Why should a developer, builder, or founder care?

4. Build the structure.
   - Intro with a direct thesis and stakes.
   - 3-5 main sections.
   - Conclusion with the punchline.
   - Sources, stats, clips, and distribution when useful.

5. Make it clip-aware.
   - Mark standout moments with `✂️ CLIP`.
   - Every major section should contain at least one line that could survive as a short or social cut.

6. Use real evidence.
   - If the user provided links or stats, anchor the outline to them.
   - If evidence is thin, say so and avoid fake certainty.

## Output Contract

Return one structured plan using this shape:

### Title

- one working title for the segment or stream

### Format

- livestream, long-form video, or short

### Core Thesis

- one short paragraph

### Rundown

- `INTRO`
- `SECTION 1`
- `SECTION 2`
- additional sections as needed
- `CONCLUSION`

Each section should include:

- time estimate when relevant
- what to say
- what to show
- the strongest argument or example

### Clips

- explicit `✂️ CLIP` callouts with rough duration and hook line

### Sources

- flat list of links or references

### Key Stats

- flat list, only when relevant

### Distribution

- only when useful
- note likely cuts, short ideas, or platform angle

## Guardrails

- Do not sound like a corporate script.
- Do not pad with generic filler like `engage the audience here`.
- Do not write fake timestamps or fake stats.
- If the source material is weak, keep the structure but state the uncertainty.
- If the topic is conflict-heavy, be fair first, then make the stronger argument.
- If the format is a short, compress the output hard and prioritize hook, turn, and payoff.

## Reading Order

- Read [references/vault-talking-points-shape.md](references/vault-talking-points-shape.md) first.
- Read [references/section-and-clip-patterns.md](references/section-and-clip-patterns.md) second.
- Read [references/output-template.md](references/output-template.md) before formatting the final result.
