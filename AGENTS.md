# Project Instructions

These instructions are shared project guidance for Codex, Claude Cowork, and other repository-aware agents. Kiro-specific automation remains in `.kiro/`, but it must follow the same catalogue and file-status rules.

## Where to start

1. Read `README.md` for the repository map.
2. Read `COLLECTION_OVERVIEW.md` for the current collection-level picture.
3. For a specific game, find the one file with `record_type: game`, then follow its `public_document` property to the current rules or concept entry point.

## Sources of truth

- A game's single game record owns its structured metadata: `state`, `physically_playtested`, exact `players`, player bounds, readable and numeric duration, `complexity`, `genre`, `public_document`, and `next_step`.
- `GAME_CATALOG.base` reads game records directly and is the detailed arbitrary-filter interface. `GAME_CATALOG.md` is its Obsidian landing page.
- `COLLECTION_OVERVIEW.md` is the complete human-readable catalogue and detailed status narrative.
- `index.html` is the public landing page; `games.html` is the public catalogue. Keep `games.html`'s game data aligned with the main-file metadata.
- `NEW_GAME_CONCEPTS.md` is a design journal and historical concept archive, not a current status index.
- `Archive/` is historical. Never treat it as current guidance without checking a live source.
- `Later/Publishing/` is deferred. Do not introduce publishing priorities into ordinary design work.

## Classification: two fields

**`state`** — exactly one of `In development`, `Ready to test`, `Proven`, or `Shelved`. It answers *what do I do with this next*:

- `In development` — no usable rules yet, or rules that still need design work before the game is worth tabling.
- `Ready to test` — it could be physically played now without further design work.
- `Proven` — played, works, and has no known blocking problem.
- `Shelved` — deliberately inactive, retained as a design record.

**`physically_playtested`** — `true` once humans have played the game on a table. This is independent of `state` and **never reverts to false**. A game can be `physically_playtested: true` and still `In development` (JANUS is), which is the honest description of a game that was tested and found to need rework.

Do not reintroduce derived flags. "Can I play it tonight?" is `state == "Ready to test"`; "have I tested it?" is `physically_playtested`. Detailed verdicts belong in playtest reports, and the single next action belongs in `next_step`.

Simulation and version numbers are evidence, not states.

## Compatibility

- Use ordinary relative Markdown links so files work in Obsidian and on GitHub.
- `GAME_CATALOG.md` may additionally use one Obsidian Base embed, provided it also includes ordinary links for other tools.
- After moving or renaming a Markdown file, update links and run `.kiro/scripts/check_md_links.py` with an available Python runtime.
- After changing game metadata or either catalogue view, run `.kiro/scripts/check_catalog_sync.py`.
- Keep exact player sets. Do not turn `3, 4, 6` into `3–6`, and do not infer that `2 or 4` supports 3.
- Keep game-specific material together in the game's root-level folder.
- Put active cross-game documents in `Project/`, historical records in `Archive/`, and publication work in `Later/Publishing/`.

## Adding a game

Follow `Project/ADDING_A_GAME.md` and start from `Templates/Game Record.md`. Create one record first; do not manually invent several competing indexes. Then sync `COLLECTION_OVERVIEW.md`, `games.html`, and their displayed collection totals from that record and run both validation scripts. Validators compare totals with the discovered records rather than assuming the collection will always contain a fixed number of games.
