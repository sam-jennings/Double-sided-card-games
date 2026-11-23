---
record_type: game
game: "CROSSROADS"
state: Rough edges
players: [2]
player_count: "2"
duration: "~20 min"
genre: "Abstract route duel"
complexity: Medium
min_players: 2
max_players: 2
min_minutes: 20
max_minutes: 20
physically_playtested: true
public_document: "Crossroads/CROSSROADS_rulebook.md"
next_step: "Run a proper 2-player Signal Fires test and probe pass-to-win."
catalog_order: 7
---
# CROSSROADS

*A route duel for 2 players · ~20 minutes · ages 10+*

> **Known issue:** The game ends on two passes in a row, which has felt unfair twice, and passing every turn once won outright. The Toll scoring meant to stop that has not been played yet.

> **⚠️ Two decisions still open (v1.2).** The deal-9, Toll and layout changes are now written in. Still open: the **end-of-game trigger** (this book still ends on two consecutive passes; the candidate is "the game ends when the eighth city dims"), and official **2–4P support** on one ruleset (not yet written in — this book covers 2 players). See `CROSSROADS_design_analysis.md` §6–§7 and `Crossroads/CROSSROADS_tasks.md` Phases 3–6.

Eight cities, twenty-eight roads — and every road exists exactly once. The roads you build are one-way; the roads you *keep in hand* are your secret — and with ten roads set aside unseen, your rival can only read your hand from what you build. CROSSROADS is the collection's chess: two players, a shared map, and the slow horror of watching someone redirect traffic away from a city you needed.

---

## Components

The **36-card** master deck builds its own board:

- The **8 cards carrying symbol 9** become the **cities**. Place them in a ring, symbol-9 face *down*, so each shows one of symbols 1–8 — eight cities, in pip order clockwise, all upright: every city starts **lit**. *(Every city lies on the hidden face of the ninth symbol; remove the capital and the map appears.)*
- The remaining **28 cards** are the **roads** — each the only road between its two cities.

## Setup

Shuffle the 28 roads, flipping chunks. Deal **9 each**, one card at a time. **Hands must be equal:** before anyone looks, count both hands to 9 aloud. Examine your hand freely, both sides, all game.

Set the other **10 roads aside, out of play** — never built, never contracts. Keep them squared, rotated 90° sideways and apart from the ring, and don't look through them. So you know your own 9 roads, but not which of the other 19 your rival holds. Builds are public; every build narrows it down.

Compare hand pip totals (both faces of every card count). **The player with the higher total decides who goes first.** You know your own hand; whatever moving first is worth, here it is chosen, never dealt.

## How roads work

A road card is **built** from the city it leaves: place it **touching its source city's card**, angled roughly toward the other city, with the **destination city's face showing** — a road always shows where it leads. Traffic flows one way: **toward the city its face names**.

A **route** from city A to city B is a chain of built roads, each one entered at the city where the previous road ended, each travelled *in its pointing direction*. 

**Flipping a built road** turns it over and points it at its other city — same road, reversed. Anyone may flip any road: the network belongs to nobody. But the map holds only **eight flips, shared between you** — see *Signal fires* below.

## Your turn — one action

1. **Build** a road from your hand (point it at either of its two cities — your choice of facing).
2. **Flip** any one built road, and **dim a city**: rotate any one still-lit city card sideways. No lit cities, no flip. **Ko rule:** you may not flip the road your opponent flipped on their last turn.
3. **Pass.**

If both players pass consecutively, the game ends.

## Signal fires — the eight flips

The duel contains exactly **eight flips**, drawn from a shared pool and paid for in cities: each flip, by either player, dims one lit city (rotate it 90° — the card never moves from the ring, it just goes dark). When the eighth city dims, the network's facings are final except by builds. The pool is the tempo war made visible: every flip you spend now is a flip you cannot answer with later, and both of you can count the remaining light at a glance.

## Contracts — the cards you never play

Every card still in your hand at game end is a **contract**: a demand that its two cities be connected. A contract is **fulfilled** if a route exists between its two cities **in either direction** — using the built roads, as they finally point.

Savour what keeping a card means: holding the Crown–Moon road *removes the only direct road between Crown and Moon from the world*, then demands those cities be connected anyway — by everyone else's roads, pointed the right way, at the final whistle.

## Scoring

Each fulfilled contract scores **1**, plus **1 Toll** for each road on its route that *you* built (trace the shortest fulfilled route). A player who builds nothing collects no Toll. Most points wins. Tiebreak: highest pip-sum across your fulfilled contracts (both faces count). Still tied: shared — the cities prosper, the players seethe.

## Edge cases & FAQ

**Is there any hidden information?** Some. You see your own 9 roads; your rival's 9 are mixed in among the 19 you don't hold, and the 10 set aside stay unseen all game. The skill is reading *which* roads they're nursing — from which roads they build, and which they reverse.

**Can I build a road pointing at a city that helps my opponent?** Every build helps someone. The deck's cruelty: any road you build can be reversed next turn — while the cities still burn. Early on, permanence lies only in *which* roads exist; once the eighth city dims, where they point is permanent too. Builds made after the last flip land exactly as placed, forever.

**Ko exactly:** if your opponent's last action flipped road R, you may not flip R this turn. You may flip it on your next turn.

**Can I keep my whole hand?** You may build nothing, pass early, and hold 9 contracts across a road network of your opponent's making. You'll collect no Toll, and they'll build sparsely and point everything away from you. Good luck.

**Does a route have to be efficient?** No. Any directed chain works, however scenic.

**A contract between adjacent ring cities?** Ring adjacency means nothing — only roads connect cities. The ring is just seating.

**When should we stop?** When neither player can improve: every build now fulfils more of the opponent's contracts than yours, and every flip breaks less than it fixes. Passing is a move, not a surrender.

## Strategy notes (read after your first duel)

- **Build even, point odd.** The direction of a road matters less than its existence — but the *parity* of flips available before game end decides final facings. Count tempo like a chess endgame: who will get the last flip?
- **Hub cities are traps.** A city where many roads converge is easy to reach and easy to redirect around. The valuable contracts touch quiet cities served by exactly one in-road.
- **Your discards are your tell.** Building the Crown–Key road says you don't need Crown–Key as a contract — and every build tells your rival something about the hand they can't see. Build your dead weight late, not early.
- **The ko rule is a weapon.** Flipping a road your opponent must immediately flip back wastes *their* turn — and *their* city. The flip war is won by whoever has spare flips, and the ring shows exactly how many remain.
- **The last flip is the largest.** With the pool empty, every facing is permanent. Forcing your opponent to spend the seventh flip so that you own the eighth is the endgame in miniature — count the dark cities the way a chess player counts tempo.

## Variants

- **Caravans (gentler):** routes may travel roads in either direction, so a flip never breaks a contract. Pure network-building; good first game.
- **The Long Haul:** play twice, swapping who goes first; sum fulfilled-contract pips across both games.

---

*Design v1.2 — v1.2 (playtests 01–02; design analysis §6–§7): deal 9 each with 10 set aside, Toll scoring in the base game (closes pass-to-win), roads built touching their source city, and a counted equal deal. Simulation-tested (June 2026; see `CROSSROADS_design_analysis.md`); table-tested twice, with the Signal Fires flip economy not yet exercised at the table. Design notes: the symbol-9 cards as self-supplied city markers resolve the "board with no board" problem; the point-at-what-you-show convention makes every road self-reading (visible face = destination — no memory, no ambiguity); contracts-as-kept-cards replace the unconcealable face-down contract of the original concept and create the pair-exhaustion tension (keeping a road deletes it from the world). The v1.0 open questions are closed: ko alone provably does NOT end the game (simulated duels flipped forever, 100% of 400-turn caps hit), so v1.1 adds the Signal Fires pool — eight shared flips, marked on the city cards themselves, which ends every simulated game in ~20 turns with zero loops; and the measured seat advantage favoured the SECOND player, so the start rule became a pie rule (higher pip total chooses) rather than a komi. Remaining table questions: does eight flips ache the way it should, and does dimming read at a glance?*
