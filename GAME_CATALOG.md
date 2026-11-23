# Game Catalog

This is the detailed Obsidian view of the whole collection. Start with **All games**, then use the filter button in the table toolbar to combine any properties you need.

Outside Obsidian, the underlying [Base file](GAME_CATALOG.base) remains available, while the [public game picker](games.html) provides the portable interface.

![[GAME_CATALOG.base#All games]]

## How games are classified

Two fields carry the whole system.

**State** — what a player can expect:

| State | Meaning |
|---|---|
| **Proven** | Played and works. Just play it. |
| **Rough edges** | Has been played; works in general but has known bugs or open questions. Feedback helps — a table may even find the fix. |
| **Untested** | Complete rules, never played. The first table should expect surprises. |
| **In the workshop** | Not playable yet: an idea only, or rules with a known problem to solve first. |
| **Shelved** | Set aside, kept as a design record. |

**Physically played** — true once humans have played it on a table. This never reverts, even if a game later goes back to **In the workshop**.

`next_step` says what specifically needs doing. Playtest reports hold the detailed verdicts.

## Useful filters

Filters can be combined with **and** / **or**. For example:

| Question | Filter |
|---|---|
| What can I put on the table tonight? | `State is Proven` **or** `State is Rough edges` **or** `State is Untested` |
| What have I never actually played? | `Physically played is false` |
| Played games with known issues to chase | `State is Rough edges` |
| Complete rules waiting for a first table | `State is Untested` |
| Playable games that support four players | (`State is Proven` **or** `Rough edges` **or** `Untested`) **and** `Exact players contains 4` |
| Untested games with a four-or-more-player option | `State is Untested` **and** `Max players is at least 4` |
| Games shorter than 20 minutes | `Max minutes is less than 20` |

The player list is exact. GLEAN's `3, 4, 6` does not include five, and MIRROR's `2, 4` does not include three. The numeric minimum and maximum fields are only for broader questions; use **Exact players contains** when choosing for a specific group size.

The other tabs are saved starting points, not a fixed classification system. You can add a temporary filter without changing the underlying game files.

## Maintaining the catalogue

Each game has one Markdown file carrying its catalogue properties. The Base reads those properties automatically. For a new title, follow [Adding a Game](Project/ADDING_A_GAME.md); you should not need to hand-build links in several places.
