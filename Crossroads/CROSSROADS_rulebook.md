# CROSSROADS

*A perfect-information route duel for 2 players · ~20 minutes · ages 10+*

Eight cities, twenty-eight roads — and every road exists exactly once. The roads you build are one-way; the roads you *keep in hand* are your secret… except nothing here is secret: from your own hand you can name every card in your rival's. CROSSROADS is the collection's chess: two players, the whole truth, and the slow horror of watching someone redirect traffic away from a city you needed.

---

## Components

The **36-card** master deck builds its own board:

- The **8 cards carrying symbol 9** become the **cities**. Place them in a ring, symbol-9 face *down*, so each shows one of symbols 1–8 — eight cities, in pip order clockwise, all upright: every city starts **lit**. *(Every city lies on the hidden face of the ninth symbol; remove the capital and the map appears.)*
- The remaining **28 cards** are the **roads** — each the only road between its two cities.

## Setup

Shuffle the 28 roads, flipping chunks. Deal **14 each**. Examine your hand freely, both sides, all game.

Do the arithmetic once and feel the cold: 28 roads exist, you hold 14 — **your rival's hand is exactly the rest.** Builds are public. From the first turn, both of you know everything.

Compare hand pip totals (both faces of every card count). **The player with the higher total decides who goes first.** You have seen everything; the choice is informed — whatever moving first is worth, here it is chosen, never dealt.

## How roads work

A road card is **built** into the middle of the ring, lying between its two cities, with its top edge **pointing at the city its visible face names** — a road always shows where it leads. Traffic flows one way: **toward the pointed city**.

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

Savour what keeping a card means: holding the Sun–Moon road *removes the only direct road between Sun and Moon from the world*, then demands those cities be connected anyway — by everyone else's roads, pointed the right way, at the final whistle.

## Scoring

Most fulfilled contracts wins. Tiebreak: highest pip-sum across your fulfilled contracts (both faces count). Still tied: shared — the cities prosper, the players seethe.

## Edge cases & FAQ

**Is there any hidden information at all?** None after the deal. Your rival's hand, and therefore their possible contracts, are computable. The skill is reading *which* of their holdings they're nursing — from which roads they build, and which they reverse.

**Can I build a road pointing at a city that helps my opponent?** Every build helps someone. The deck's cruelty: any road you build can be reversed next turn — while the cities still burn. Early on, permanence lies only in *which* roads exist; once the eighth city dims, where they point is permanent too. Builds made after the last flip land exactly as placed, forever.

**Ko exactly:** if your opponent's last action flipped road R, you may not flip R this turn. You may flip it on your next turn.

**Can I keep my whole hand?** You may build nothing, pass early, and hold 14 contracts across a road network of your opponent's making. They'll build sparsely and point everything away from you. Good luck.

**Does a route have to be efficient?** No. Any directed chain works, however scenic.

**A contract between adjacent ring cities?** Ring adjacency means nothing — only roads connect cities. The ring is just seating.

**When should we stop?** When neither player can improve: every build now fulfils more of the opponent's contracts than yours, and every flip breaks less than it fixes. Passing is a move, not a surrender.

## Strategy notes (read after your first duel)

- **Build even, point odd.** The direction of a road matters less than its existence — but the *parity* of flips available before game end decides final facings. Count tempo like a chess endgame: who will get the last flip?
- **Hub cities are traps.** A city where many roads converge is easy to reach and easy to redirect around. The valuable contracts touch quiet cities served by exactly one in-road.
- **Your discards are your tell.** Building the Sun–Key road says you don't need Sun–Key as a contract — says it to someone who knew you held it. Build your dead weight late, not early.
- **The ko rule is a weapon.** Flipping a road your opponent must immediately flip back wastes *their* turn — and *their* city. The flip war is won by whoever has spare flips, and the ring shows exactly how many remain.
- **The last flip is the largest.** With the pool empty, every facing is permanent. Forcing your opponent to spend the seventh flip so that you own the eighth is the endgame in miniature — count the dark cities the way a chess player counts tempo.

## Variants

- **Caravans (gentler):** routes may travel roads in either direction; flipping only matters for the Toll variant below. Pure network-building; good first game.
- **Toll Roads:** a fulfilled contract scores +1 extra for each of its route's roads that *you* built (trace the shortest fulfilled route). Rewards building your own infrastructure rather than parasitising.
- **The Long Haul:** play twice, swapping who goes first; sum fulfilled-contract pips across both games.

---

*Design v1.1 — simulation-tested (June 2026; see `CROSSROADS_design_analysis.md`), untested at the table. Design notes: the symbol-9 cards as self-supplied city markers resolve the "board with no board" problem; the point-at-what-you-show convention makes every road self-reading (visible face = destination — no memory, no ambiguity); contracts-as-kept-cards replace the unconcealable face-down contract of the original concept and create the pair-exhaustion tension (keeping a road deletes it from the world). Perfect information is embraced, not fought — this is the collection's abstract. The v1.0 open questions are closed: ko alone provably does NOT end the game (simulated duels flipped forever, 100% of 400-turn caps hit), so v1.1 adds the Signal Fires pool — eight shared flips, marked on the city cards themselves, which ends every simulated game in ~20 turns with zero loops; and the measured seat advantage favoured the SECOND player, so the start rule became a pie rule (higher pip total chooses) rather than a komi. Remaining table questions: does eight flips ache the way it should, and does dimming read at a glance?*
