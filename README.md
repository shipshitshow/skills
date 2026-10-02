# Ship Sh!t Show viewer skills

Reusable production skills for builders making AI videos and livestreams. Supply your own channel profile, source transcript and brand references; the bundled Ship Sh!t Show profile is optional context.

## Install and use

Install with your agent's skill installer from `shipshitshow/skills`, or copy the desired complete skill folder into its skill directory. Each folder includes its own instructions and references, so it works independently of this repository's siblings. Existing names remain compatible.

| Skill | Output |
| --- | --- |
| `talking-points` | Source board and run of show for natural discussion |
| `finding-channel-fit-trends` | Evidence-backed pitches and source clusters |
| `youtube-metadata` | Titles, description, chapters and focused tags |
| `thumbnail-prompt-variations` | Exactly three thumbnail test hypotheses/prompts |
| `youtube-channel-branding` | PFP/banner brief, assets and crop checks |
| `restream-layouts` | Scene map and usable broadcast graphics |
| `partner-ad-script` | Supported, disclosed host-read partner script |
| `transcript-archive` | Provenance, separate clocks and coverage ledger |
| `tesseract-projects` | Local project folders, versions and final handoff |
| `tesseract-recap` | Focused edit, cuts and final-timeline packaging |
| `tesseract-dialogue` | Recording-specific audio treatment and review |

These skills support the installed Tesseract plugin for editing. They do not require a viewer to use Vincent's folders or copy the plugin's changing API schema. A brief does not imply publication, paid generation, media upload or partner outreach.

## Channel context and maintenance

[Canonical Ship Sh!t Show profile](profiles/shipshitshow.md). Bundled copies are synchronized by `python3 scripts/sync-profiles.py`; `--check` reports drift. Update the canonical profile first. Descriptive historical channel patterns are not performance guarantees.

The metadata analyzer supports `--channel livestreams|videos|shorts|all` and a local vault or public GitHub repository:

```bash
node youtube-metadata/scripts/analyze-vault-performance.js --vault /path/to/vault --channel all --format pretty
```

Public episodes/transcripts: https://github.com/shipshitshow/vault. Public demonstration code: https://github.com/shipshitshow/examples. Producer: https://send.shipshit.dev; show: https://show.shipshit.dev.
