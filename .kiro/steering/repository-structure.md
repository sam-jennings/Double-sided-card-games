---
inclusion: always
---

# Repository and File Organisation

Kiro follows the shared instructions in [AGENTS.md](../../AGENTS.md). This file adds Kiro-specific detail; it does not define a separate project structure.

## Current layout

```text
Double-sided card games/
├── README.md                 # project home for Obsidian and GitHub
├── COLLECTION_OVERVIEW.md    # complete human-readable game catalogue
├── GAME_CATALOG.md           # Obsidian catalogue landing page and filter help
├── GAME_CATALOG.base         # Obsidian saved/filterable views
├── NEW_GAME_CONCEPTS.md      # design journal; not a current state index
├── index.html                # public/mobile landing page
├── games.html                # public/mobile game picker
├── <Game Name>/              # rules, concepts, analysis, sims, tests for one game
├── Project/                  # active cross-game standards, decisions, playtesting
├── Archive/                  # historical audits, prompts, and unadopted proposals
├── Later/Publishing/         # intentionally deferred publication work
├── Designs/                  # card layout, art scripts, and assets
├── Print and Play/           # printable prototype and generator
├── Reference/                # external learning and research
├── Templates/                # reusable playtest/design templates
└── .kiro/                    # Kiro-only steering, hooks, scripts, and old specs
```

CONCORD is a live game in `Concord/`; it is not an archived root-level proposal.

## The game record

Each game has one **game record**, identified by `record_type: game`. It may be a rulebook, concept, analysis, or proposal. Its YAML properties are the structured source of truth, while `public_document` points to the best current entry point:

- `record_type: game`
- `game`
- `state` — `In development`, `Ready to test`, `Proven`, or `Shelved`
- `physically_playtested` — true once humans have played it; never reverts
- `players` — exact supported counts
- `min_players` and `max_players` — derived bounds for broad filters
- `duration`
- `min_minutes` and `max_minutes` — numeric filter values when meaningful
- `complexity` — `Light` or `Medium`, aligned with the public picker
- `genre`
- `public_document`
- `next_step`
- `catalog_order`

Do not turn a discontinuous list into a range. `players: [3, 4, 6]` does not support five; MIRROR's `[2, 4]` does not support three.

## Catalogue sync rule

When any structured game property changes, update all three views in the same task:

1. the YAML properties on the game's game record;
2. the complete table and detailed entry in `COLLECTION_OVERVIEW.md`;
3. the matching object in `games.html`.

`GAME_CATALOG.base` reads the YAML properties automatically and normally needs no edit unless the property schema or saved views change. `NEW_GAME_CONCEPTS.md` is updated only when the design journal itself gains meaningful narrative; never use it as a second state ledger. `index.html` carries only the total game count (in its hero eyebrow and final-CTA stat) — update that count when the total changes, but its per-game data is not authoritative.

Before declaring a catalogue change complete, run `.kiro/scripts/check_catalog_sync.py`. It verifies every game record against `COLLECTION_OVERVIEW.md` and `games.html`, including exact player sets, bounds, duration, state, complexity, playtest history, and public document paths. It also checks the displayed game total on `index.html`. The checker deliberately has no fixed game count.

For a new title, follow `Project/ADDING_A_GAME.md` and copy `Templates/Game Record.md`. The record appears in Obsidian automatically; sync the overview and public picker from it in the same task.

## Per-game files

- `<GAME>_rulebook.md` — player-facing rules.
- `<GAME>_concept.md` — concept record before a rulebook exists.
- `<GAME>_design_analysis.md` or `<GAME>_design_proposal.md` — reasoning and evidence.
- `<GAME>_playtest_plan_NN.md` — pre-session plan.
- `<GAME>_playtest_NN.md` — report after a session.
- `<game>_sim.py` — simulation or solver when needed.

Keep all game-specific files in the game's root-level folder. Folder names use Title Case, including leading articles. File prefixes use UPPER_SNAKE and omit a leading article where existing convention does (`COUNCIL`, `ORRERY`, `UNPLAYED_PAIR`).

## File lifecycle

- `Project/` is live cross-game guidance.
- `Archive/` is history and provenance. It may explain why a decision was made but cannot override a current game record or `COLLECTION_OVERVIEW.md`.
- `Later/Publishing/` is valid deferred work. Do not use its schedules, Core Set choices, or publisher assumptions to set current priorities.
- `.kiro/specs/` records completed or historical Kiro work unless a current task explicitly reactivates a spec.

## Links and compatibility

Use relative Markdown links, not local absolute paths or Obsidian-only wikilinks, in shared documents. This keeps links working in Obsidian, GitHub, Claude Cowork, and Kiro. The single Base embed in `GAME_CATALOG.md` is the deliberate exception and is paired with ordinary links for other tools. After moving or renaming Markdown files, run `.kiro/scripts/check_md_links.py` with an available Python runtime and fix every broken reference before declaring the task complete.
