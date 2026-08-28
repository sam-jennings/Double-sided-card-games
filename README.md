# Double-Sided Card Games

This is the project home for a 36-card, double-faced deck and the **34 games** currently designed for it.

## Start here

- **Choosing or filtering games in Obsidian:** open [Game Catalog](GAME_CATALOG.md). Start with all games and combine player count, time, state, whether it has been physically played, depth, or genre filters.
- **Reading the collection as a document:** [Collection Overview](COLLECTION_OVERVIEW.md) contains the complete catalogue, the state narrative, and next steps.
- **Using the public site:** open [the site](index.html), or go straight to [the game picker](games.html). It has exact player-count, state, played/never-played, time, and depth filters.
- **Printing a copy:** the site's [Print & Play section](index.html#print) serves `Print and Play/FLIP_DECK_print_and_play_Nine_Signs.pdf` — nine A4 pages, duplex on the long edge, 36 cards.
- **Working on the project:** [Project files](Project/README.md) explains which cross-game documents are current.
- **Adding a title:** [Adding a Game](Project/ADDING_A_GAME.md) is the short workflow and links to the reusable record template.
- **Looking for old decisions or ideas:** [Archive](Archive/README.md) contains historical material that should not be treated as current guidance.
- **Publishing work:** [Later](Later/README.md) keeps publication planning out of the active design workspace.

## The system in one line

Every game has a **state** — **In development** (needs design work), **Ready to test** (playable now), **Proven** (played and working), or **Shelved** (inactive) — plus a **physically played** flag recording whether humans have ever played it. 12 of the 34 have.

The structured source of truth is the frontmatter on each game's game record. `GAME_CATALOG.base` reads it directly; `COLLECTION_OVERVIEW.md` and `games.html` are synchronized catalogue views.
