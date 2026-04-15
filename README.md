# Ship Sh!t Show Skills

This repo contains a small [`skills.sh`](https://skills.sh) skill pack built around the public [`shipshitshow/vault`](https://github.com/shipshitshow/vault) structure.

## Install

Install directly from GitHub with `npx`:

```bash
npx skills install shipshitshow/skills
```

## Included skills

### `talking-points`

Generates:

- livestream talking points
- long-form video rundowns
- section-by-section outlines
- clip callouts
- source and stats sections

It is tuned to the real Ship Sh!t Show `notes.md` structure from the vault, not generic bullet-list outlines.

### `youtube-metadata`

Generates:

- title candidates
- one recommended title
- a YouTube description draft
- `youtube_tags`
- a short performance rationale

It includes a bundled analyzer script that reads a local vault path or falls back to a GitHub repo.

### `thumbnail-prompt-variations`

Generates 4-6 thumbnail prompt variants plus one recommended winner, using:

- vault episode context
- saved thumbnail language
- pasted creative briefs

The prompts are optimized for:

- high contrast
- dark background or dark edge treatment
- clear center object
- host readability on outer edges
- thumbnail readability at small size

### `finding-channel-fit-trends`

Researches live trends from:

- Reddit
- Hacker News
- YouTube
- X

Then ranks them by Ship Sh!t Show fit first, not hype first, and turns them into content briefs with:

- source links
- recommended angle
- recommended format
- title hooks
- thumbnail idea seeds

## Repo layout

Each skill is publish-ready as its own folder:

```text
<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
└── scripts/        # only when needed
```

## Validation

The metadata skill includes a working analyzer:

```bash
node ./youtube-metadata/scripts/analyze-vault-performance.js --vault shipshitshow/vault --channel all --format pretty
```

Local vault example:

```bash
node ./youtube-metadata/scripts/analyze-vault-performance.js --vault /path/to/vault --channel videos --format json
```

## Notes

- Historical performance defaults to `view_count`.
- Long-form videos and shorts are ranked separately.
- Vault-facing metadata should always use `youtube_tags`, never Obsidian `tags`.
