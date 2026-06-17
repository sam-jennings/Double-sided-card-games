# Repository & File Organisation

> **Primacy.** This note is part of the project's binding steering set in
> `.kiro/steering/`. Treat these notes as the **primary reference** for all
> design decisions and defer to them over any other document. When you apply
> guidance from here, **cite the specific steering note** you are relying on.

This is a design repository, not a code repository. Most files are Markdown documents; Python exists only for simulation, solving, and print-and-play.

## Layout

```
Double-sided card games/
├── COLLECTION_OVERVIEW.md      # the index: selectors, status tiers, coverage tables
├── COLLECTION_AUDIT.md         # design-facing health check / rubric scores
├── flip_card_project_goals.md  # founding vision and goals
├── DECK_SIZE_DECISION.md       # why 9 symbols / 36 cards (settled)
├── NEW_GAME_CONCEPTS.md        # concept sheets + status of each
├── SYMBOL_SETS.md              # candidate symbol identities (open)
├── Print and Play/             # FLIP_DECK print-and-play PDF + generator
│   └── make_pnp.py
├── Designs/                    # card art generation scripts, layout spec, symbol assets
│   ├── CARD_LAYOUT.md           # physical card layout specification
│   ├── compose_cards.py
│   └── ...
├── Reference/                  # external learning, market research, one-off analyses
│   ├── Game Development Notes/  # course notes (not deck-specific)
│   ├── deck_mathematical_analysis.md
│   └── similar-product-market-survey.md
├── <GameName>/                 # one folder per game (Title Case, incl. article)
│   ├── <GAME>_rulebook.md       # player-facing rules (always)
│   ├── <GAME>_design_analysis.md# design reasoning / sim results (when it exists)
│   ├── <GAME>_playtest_NN.md    # playtest reports (numbered)
│   └── <game>_sim.py            # simulator / solver (when it exists)
└── .kiro/steering/             # these steering files
```

## Per-game folder conventions

- One folder per game, **Title Case** folder name including article (e.g. `Twelve Trials/`, `The Council/`, `The Unplayed Pair/`).
- **Rulebook**: `<GAME>_rulebook.md`, UPPER_SNAKE prefix. Every game has one once it reaches tier 3+.
- **Design analysis**: `<GAME>_design_analysis.md`. Explains reasoning, constraints, and simulation results. Present for sim-tuned/validated games.
- **Playtest reports**: `<GAME>_playtest_NN.md`. Numbered sequentially per game.
- **Simulator**: `<game>_sim.py`, lower_snake. Present where simulation was used.
- Not every game has all three. A tier-3 (untested) game may have only a rulebook.

## Document types and what belongs where

| Need | Goes in |
|---|---|
| How to play a game | that game's rulebook |
| Why a rule is the way it is, sim results | that game's design analysis |
| Playtest plans & reports | the game's folder (see `playtesting.md`) |
| Cross-game decisions, deck-wide maths | a top-level doc (e.g. `DECK_SIZE_DECISION.md`) |
| Collection status / what's next | `COLLECTION_OVERVIEW.md` |
| New game pitches | `NEW_GAME_CONCEPTS.md` |
| Card layout, art generation, symbol assets | `Designs/` |
| External learning, market research, historical analyses | `Reference/` |

## Naming & consistency rules

- Game names are written in **CAPS** in prose (TRIGON, THE COUNCIL) to match existing docs.
- Keep `COLLECTION_OVERVIEW.md` in sync when a game changes tier, gets renamed, or is cut. It is the canonical index.
- When a game is cut, **keep its folder** as an archive/design record (as with `Ouroboros/`); note the cut and its lessons in the overview and concepts docs.
- Folder names include the article when the game title has one: `The Council/`, `The Orrery/`, `The Unplayed Pair/`.
- Cross-reference rather than duplicate: link to the authoritative doc instead of restating maths or status in multiple places.
- Create new Markdown files only when a deliverable genuinely needs its own document; otherwise extend an existing one.
