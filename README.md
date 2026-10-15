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
| `library` | Local edit folders, versions and final handoff |
| `recap` | Focused edit, cuts and final-timeline packaging |
| `dialogue` | Recording-specific audio treatment and review |
| `overlays` | Asset-sheet illustrations, motion graphics and overlays on a plain recording |

The four editing skills (`library`, `recap`, `dialogue`, `overlays`) are editor-neutral workflow rules. Each names its current editor, Tesseract, in a short closing section. They do not require a viewer to use Vincent's folders or copy the editor's changing API schema. A brief does not imply publication, paid generation, media upload or partner outreach.

Three of these were first published on 2 Oct 2026 as `tesseract-projects` (now `library`), `tesseract-recap` (now `recap`) and `tesseract-dialogue` (now `dialogue`). An existing install of an old name needs reinstalling under the new one.

## Channel context and maintenance

[Canonical Ship Sh!t Show profile](profiles/shipshitshow.md). Bundled copies are synchronized by `python3 scripts/sync-profiles.py`; `--check` reports drift. Update the canonical profile first. Descriptive historical channel patterns are not performance guarantees.

[The vault brand kit](https://github.com/shipshitshow/vault/tree/master/brand) owns the show's identity, tokens, asset inventory, layout boards and thumbnail/editing rules. Read the relevant guide and asset status before producing branded media. `SH*W` is the compact mark; **Ship Sh!t Show** remains the full name. Reference boards are not approved upload assets or actual episode footage. Update the vault first, then the canonical profile and its bundled copies. Other channels keep their own identity.

The metadata analyzer supports `--channel livestreams|videos|shorts|all` and a local vault or public GitHub repository:

```bash
node youtube-metadata/scripts/analyze-vault-performance.js --vault /path/to/vault --channel all --format pretty
```

Public episodes/transcripts: https://github.com/shipshitshow/vault. Public demonstration code: https://github.com/shipshitshow/examples. Producer Home: https://show.shipshit.dev/studio; sign-in: https://show.shipshit.dev/sign-in; public show: https://show.shipshit.dev.
