# Adding a Game

Adding a game should start with **one game record**, not a collection-wide editing session.

## Normal process

1. Make a Title Case folder at the repository root, for example `Glass House/`.
2. Copy [Game Record](../Templates/Game%20Record.md) into it and rename it with the game's file prefix, for example `GLASS_HOUSE_concept.md`.
3. Change `record_type` from `game-template` to `game`, then fill in the YAML properties and short concept sections. Use `state: In the workshop` unless complete, playable rules already justify `Untested`.
4. Set `public_document` to this file. If a rulebook later becomes the best entry point, change this one property to the rulebook's path; the catalogue record itself can stay where it is.
5. Ask a repository-aware agent: **“Add GLASS HOUSE to the collection from its game record and sync the catalogue.”** The agent updates the complete overview, public webpage, and displayed collection totals; assigns the next catalogue order; creates the links; and runs the checks.

As soon as step 3 is complete, the game appears automatically in Obsidian's [Game Catalog](../GAME_CATALOG.md). Step 5 is what makes it appear on the public webpage and in the human-readable overview.

## What belongs in the record

- `players` is the exact supported set. Write `[3, 4, 6]`, not `[3, 4, 5, 6]`, unless five genuinely works.
- `min_players` and `max_players` are derived from that exact set and make broad filtering easier.
- `duration` is the readable label; `min_minutes` and `max_minutes` make time filters work. Omit the numeric fields for an asynchronous game with no meaningful session length.
- `state` is one of `Proven` (played and works), `Rough edges` (played, works in general, known bugs or open questions), `Untested` (complete rules, never played), `In the workshop` (not playable yet: an idea, or rules with a known problem to solve first), or `Shelved` (set aside, kept as a design record). A new game is almost always `In the workshop`. A `Rough edges` game also needs a one-line known issue on its `games.html` entry and at the top of its rules, and an `Untested` rulebook the designer has not reviewed carries the note "Rules not yet reviewed by the designer" on its `games.html` entry.
- `physically_playtested` is true only after humans have played it, and never goes back to false. It is independent of `state`, although the checker requires it to be true for `Proven` and `Rough edges` and false for `Untested`. A played game can still go back to `In the workshop` if it needs design work before another table.
- `complexity` is the public picker's broad `Light` or `Medium` depth label.
- `public_document` is the repo-relative file opened from the catalogue and webpage.

Update the record whenever one of these facts changes. The other catalogue views should be synced from it rather than becoming independent sources of truth.

## Promotion without relinking everything

When a concept becomes a rulebook, keep the record properties on the existing concept file and point `public_document` at the new rulebook. This preserves the stable Obsidian record and avoids moving the catalogue metadata. The concept may then serve as the game's design history while the rulebook is the public entry point.
