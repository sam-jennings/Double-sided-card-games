# Game Catalog

This is the detailed Obsidian view of the whole collection. Start with **All games**, then use the filter button in the table toolbar to combine any properties you need.

Outside Obsidian, the underlying [Base file](GAME_CATALOG.base) remains available, while the [public game picker](games.html) provides the portable interface.

![[GAME_CATALOG.base#All games]]

## How games are classified

Two fields carry the whole system.

**State** — what to do with the game next:

| State | Meaning |
|---|---|
| **In development** | No usable rules yet, or rules that still need design work before they are worth tabling. |
| **Ready to test** | You could physically play it now without further design work. |
| **Proven** | Played, works, and has no known blocking problem. |
| **Shelved** | Deliberately inactive. |

**Physically played** — true once humans have played it on a table. This never reverts. A game can be physically played and still **In development**, as JANUS is; that is the honest description of a game that was tested and found to need rework.

`next_step` says what specifically needs doing. Playtest reports hold the detailed verdicts.

## Useful filters

Filters can be combined with **and** / **or**. For example:

| Question | Filter |
|---|---|
| What can I put on the table tonight? | `State is Ready to test` |
| What have I never actually played? | `Physically played is false` |
| Tested games that still need work | `Physically played is true` **and** `State is In development` |
| Untested games that are ready to go | `State is Ready to test` **and** `Physically played is false` |
| Ready games that support four players | `State is Ready to test` **and** `Exact players contains 4` |
| Ready games with a four-or-more-player option | `State is Ready to test` **and** `Max players is at least 4` |
| Games shorter than 20 minutes | `Max minutes is less than 20` |

The player list is exact. GLEAN's `3, 4, 6` does not include five, and MIRROR's `2, 4` does not include three. The numeric minimum and maximum fields are only for broader questions; use **Exact players contains** when choosing for a specific group size.

The other tabs are saved starting points, not a fixed classification system. You can add a temporary filter without changing the underlying game files.

## Maintaining the catalogue

Each game has one Markdown file carrying its catalogue properties. The Base reads those properties automatically. For a new title, follow [Adding a Game](Project/ADDING_A_GAME.md); you should not need to hand-build links in several places.
