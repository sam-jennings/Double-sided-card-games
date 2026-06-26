# Game Naming

> One deck runs the whole collection, so a game's **title is its primary handle** —
> what players say to choose it ("let's play ___"), what they scan for in a
> contents page, and how they ask for the rules. When titles collide or say
> nothing about play, the friction lands at the table, not on the page. Titles
> are a usability surface, not just flavour.

This governs the **game title** (the name in CAPS in prose, and the folder/file
prefix). For file and folder *spelling* conventions see `repository-structure.md`;
this file is about choosing the name itself.

## Two tests every title must pass

1. **Distinctness** — it must not be confusable with another collection title by
   *sound, shape, or shared key word*. The risk is highest between games that are
   already similar (same genre, shared engine, adjacent player counts): those need
   the *most* distinct names, not the least.
2. **Association** — a player who knows nothing should be able to guess *something*
   true about the game from the title, or learn it in one breath ("BLIGHT — the
   rot one"). A purely abstract or obscure word is acceptable only when it earns a
   strong, teachable one-line hook.

A title that passes neither is a bug to fix (rename), the same way a handling
defect is.

## Concrete naming rules

- **No shared key word between two games.** Don't reuse a distinctive noun across
  titles (e.g. two titles both built on FACE, or both on TURN). The shared word
  becomes the thing players *can't* use to tell them apart.
- **Spread the first letter / first sound.** Avoid piling titles under one initial.
  When alphabetised or read aloud in sequence they should not bunch. Watch the
  "T / THE ___" cluster especially.
- **Reserve near-identical names for things that are genuinely the same.** Sibling
  games that share an engine (e.g. an accumulation/avoidance pair) need *more*
  contrast in their names to signal they play differently, not matching names that
  imply they're interchangeable.
- **Prefer a concrete image over an abstract label.** A title that names a thing or
  action in the game (a route, a betrayal, a rot) beats one that names a category.
- **Obscure words must pay rent.** A rare word (ORRERY, CAIRN, JANUS, OUROBOROS) is
  fine *if* its meaning maps cleanly onto the core mechanic and the rulebook opens
  with the connection. If it's just atmosphere, pick something that also teaches.
- **Keep the article rule consistent** with `repository-structure.md` (the folder
  includes the article: `The Council/`).

## Naming checklist (run before naming or renaming a game)

- [ ] Does any existing title share a distinctive key word with this one?
- [ ] Said aloud back-to-back with its nearest sibling, are they easy to tell apart?
- [ ] Does it bunch under an already-crowded initial?
- [ ] Can a stranger guess one true thing about the game, or get it in one line?
- [ ] If the word is obscure, does the mechanic justify it and does the rulebook
      open on that link?

## Resolved conflicts (applied June 2026)

The collection-wide review in [`NAMING_REVIEW.md`](../../NAMING_REVIEW.md) was
applied across the repository (folders, files, prose, and the canonical index).
Renames made:

| Was | Now | Reason |
|---|---|---|
| FALSE FACE | **FORKED TONGUE** | broke the three-way FACE collision; "forked tongue" says *liar* and fits the game's forgery theme |
| TWO-FACED | **SLEEPER** | broke the FACE collision and the betrayal-theme overlap with TURNCOAT (a sleeper hides; a turncoat switches in the open) |
| TURNOVER | **WILDFIRE** | broke the TURN- collision; fire = the match-and-chain cascade. Its old chain-3 variant was renamed **INFERNO** to free the word |
| CABAL *(concept)* | **SNARE** | "cabal" read as a hidden-role social game; it's a silent 2P geometric trap |
| MERIDIAN *(concept)* | **RELAY** | "meridian" evoked nothing about routes; "relay" gives the route-race its energy |

Kept deliberately: **FACE VALUE** (now the sole FACE title — the pun earns it),
**TURNCOAT**, **TRIGON**, **GLEAN** (the gather/rot harvest pair with BLIGHT), and
the obscure-but-apt **THE ORRERY / CAIRN / JANUS / OUROBOROS**.

Still on watch (no rename, lower priority):

- **THE ORRERY** — a playtester misread "orbit"; revisit only if it recurs.
- The **"THE ___"** cluster (THE ORRERY, THE COUNCIL, THE UNPLAYED PAIR) — stop
  adding more; dropping the articles is a purely cosmetic future option.

When any future name changes, update this section and `COLLECTION_OVERVIEW.md`
together.
