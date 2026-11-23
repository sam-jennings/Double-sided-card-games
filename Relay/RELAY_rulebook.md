# RELAY

*A route race for 2–4 players · ~20–25 minutes · ages 10+*

> **⚠️ Draft v0.1 (November 2026). Not yet playable at 4 players. RELAY stays In the workshop.** Written from the simulated goal-race rules in [relay_sim.py](relay_sim.py) ([RELAY_design_analysis.md](RELAY_design_analysis.md)). Where the concept sheet and the sim differ, this draft follows the sim, because the sim is the version that was validated. Decisions only the designer can make are listed in the **Design notes** at the end. The biggest is **how to mark the nine places at 4 players**: the deck has no spare cards to do it.

Nine signs, and every pair of them joined by exactly one road. Build roads into one shared web, aim them toward the places you need, and swing a rival's road around at the last moment. The first player to complete a route to a goal claims it, wherever the roads came from.

---

## Components

- The flip deck: **36 double-faced cards, 9 signs, every pair of signs on exactly one card, each sign on exactly 8 cards.** An index pip 1–9 is printed on both faces.
- **Flip counters:** 6 / 8 / 9 small objects from the house counter kit (any coins or beads) at 2 / 3 / 4 players.
- At 4 players only: **nine place markers.** *(Open: see Design notes.)*

The player count sets which signs you use:

| Players | Signs used | Remove every card showing… | Roads in play | Goals | Flip counters |
|---:|---|---|---:|---:|---:|
| 2 | Moon–Key (1–7) | Star or Crown | 21 | 5 | 6 |
| 3 | Moon–Star (1–8) | Crown | 28 | 6 | 8 |
| 4 | all nine | nothing | 36 | 7 | 9 |

## The places

Each sign in play is a **place**. Roads run between places, so the table needs a marker for each place:

- **2 players:** from the removed cards, take the seven that pair a sign 1–7 with **Star**. Lay them in a ring, Star face down, in pip order clockwise. Each shows one place, 1–7.
- **3 players:** take the eight removed **Crown** cards. Lay them in a ring, Crown face down, in pip order clockwise, exactly as in CROSSROADS. Each shows one place, 1–8.
- **4 players:** *not yet decided* (no cards are left over).

Put the other removed cards back in the box. Leave space inside the ring for roads and outside it for goals.

## Setup

1. Shuffle the cards in play, turning chunks over as you go so which face is up is random (there is no card back).
2. **Goals.** Deal 5 / 6 / 7 cards (by player count) into a squared, upright **goal stack**. Reveal three goals (see *Goals* below).
3. **Hands.** Self-deal: pass the squared deck round; each player takes 3 cards one at a time straight into hand. The face showing on the deck as each card is taken is seen by everyone, and that's fine. Hold your hand privately, tilted toward your chest. You may look at both faces of your own cards at any time.
4. **Market.** Lay the next 3 cards face up in a row: the **market**. Anyone may pick up and examine any market card, both sides, at any time. Return it as found.
5. **Stock.** The rest is the **stock**, a squared, upright stack beside the market. Its top face is public.
6. Put the **flip counters** in a shared pool.
7. The youngest player goes first. Play passes left.

## Goals

A **goal** is a card on the table that names a **destination** and an **origin**. To reveal one, take the top card of the goal stack *without turning it over*:

- The face that was **showing** is the **destination**.
- The face underneath is the **origin**.

Show both faces to the table. Then lay the goal **outside the ring, touching its origin place, showing its destination**. A goal always sits at the place you must start from, and shows where you must get to.

A goal is worth **both of its pips added together** (Moon–Crown is worth 10).

## How roads work

A road card is **built from one of its two places to the other**. Lay it inside the ring **touching its source place, showing the destination face** and angled toward the destination place. Traffic flows one way: toward the face it shows.

A **route** from place A to place B is a chain of built roads: the first leaves A, each next road leaves the place the previous one reached, and the last arrives at B. Every road is travelled in the direction it shows.

**Flipping a road** turns it over and moves it so it touches its new source, the place it used to point at. It's the same road, now pointing the other way. Anyone may flip any built road; nobody owns the web.

## Your turn

1. **Draft.** Take one card from the market into your hand. Refill the market from the stock, if any is left.
2. **Act.** Do exactly one of these:
   - **Build** a road from your hand, from either of its places toward the other. Its source doesn't have to touch any existing road.
   - **Flip** any one built road. Spend one flip counter to do it. When the pool is empty, no more flips.
   - **Pass.**
3. **Claim.** If your build or flip has made a route from any goal's origin to its destination, take that goal into your face-up **score pile**. Claim every goal it completes. Then reveal new goals until three are showing, or the goal stack is empty.

**Only the player who builds or flips claims.** Passing never claims.

> **Example: a claim by flip.** A goal sits at Leaf showing Key: *reach Key from Leaf*. The web has a road from Leaf to Mask and a Mask–Key road pointing *at Mask*. Ben spends a flip counter, turns the Mask–Key road over and moves it so it touches Mask, now showing Key. The route Leaf → Mask → Key exists, and Ben claims the goal (2 + 7 = 9 points).

## Game end & scoring

The game ends at once when **the last goal is claimed**. It also ends if the stock and market are empty and **every player passes in a row**.

Add up the goal values in your score pile. **The highest total wins.** Tiebreak: most goals claimed. Still tied: shared.

## Edge cases & FAQ

**A goal is revealed and its route already exists.** Nobody claims it yet. The next player who builds or flips claims it, even if their action had nothing to do with it.

**Can I build a road that touches nothing else?** Yes. Isolated roads are legal; they just don't help until something joins them.

**Can I flip a road my rival just flipped?** Yes. The flip pool is the only limit, and it's shared, so every flip you make is one fewer for everybody.

**Is a goal card a road?** No. Goals never join the web.

**What's hidden?** Only your hand (three or four cards). The web, the goals, the market and every score pile are public.

**Must I draft?** Yes, while the market has cards. Your hand can grow past three if you pass.

**Can one road complete a goal?** Never. A goal *is* the only card for its pair, so there is no direct road between its origin and destination. Every route to a goal goes through at least one other place.

## Strategy notes *(read after your first game)*

- **Draft toward the goal row.** A market card whose signs touch a goal's origin or destination is worth more than a high-pip card that touches nothing.
- **Flips score.** About a quarter of simulated claims came from a flip, not a build. A rival's half-finished route, pointed the wrong way, is a gift.
- **Don't build the last step for someone else.** Since only the active player claims, a road that leaves a goal one flip from done hands it to the next player who has a counter.
- **Count the pool.** When the flip counters run out, every road points where it points forever. Late in the game, the player with the last flip often takes the last goal.

## Designer's variants

- **Open road (first game):** ignore flips entirely. It plays as a pure connection race and is good for learning route-reading.
- **Long haul:** reveal only two goals at a time. Fewer targets mean more contention and more denial.

---

## Design notes *(not player-facing)*

### Open decisions for the designer

1. **Place markers at 4 players (blocking at 4P).** A road shows only its destination; its source is the face pressed to the table. So a route can be read only if every road touches a visible marker for its source, as in CROSSROADS. The concept's "a node is simply where roads meet" doesn't work physically. At 2P and 3P, the removed Star or Crown cards make exact markers, deck-native and with no new components. At 4P all 36 cards are in play. Three costed options are in [RELAY_design_analysis.md](RELAY_design_analysis.md) under *4P place markers*, with sim evidence: (A) make RELAY 2–3P only, (B) play 4P on 8 signs with the Crown cards as markers, (C) nine external markers. This draft leaves 4P unplayable until you choose.
2. **Turn structure.** The concept says build, then optionally re-aim, in the same turn. The validated sim gives **one action** (build, flip or pass). This draft follows the sim. Changing it needs a re-sim.
3. **Build connectivity.** The concept says a road joins the web at a shared sign. The sim allows any build, anywhere. This draft follows the sim. A connectivity rule may improve legibility and is a table question.
4. **Flip counters vs dimming.** The sim's shared pool (6/8/9) is tracked with house-kit counters (convention C5). Dimming the place markers, as in CROSSROADS, would need one marker per flip; that fits 3P (8 and 8) but not 2P (7 places, 6 flips) or 4P.
5. **Goal handling.** Laying each goal touching its origin place is this draft's answer to "a goal's origin is its pressed face". Without that, players would have to remember origins, which would be involuntary hidden-face memory.

### Physical-handling checklist

- **What can each player see?** Every place marker, every built road (its destination face, and its source by what it touches), every goal (its destination face and origin place), the market, the stock top, all score piles.
- **What can each player inspect?** Their own hand; any market card; any goal (lift and return as found).
- **What is hidden, and is it really hidden?** Only hands, held tilted to the chest (the F8 fan leak is accepted as in SILK CUT and CARAVAN).
- **Is required state visible?** Yes, given place markers. The road's source is shown by position, not by its pressed face.
- **Can the table verify legality without memory?** Yes. A claim is checked by tracing the route on the table.

### What the sim covers and what it doesn't

The rules here are the sim's GOAL mode: subset by player count, goals 5/6/7 with 3 showing, value = both pips, hand 3, market 3, shared flip pool 6/8/9, one action per turn, and only the active player claims. The analysis reports (1,000 games per cell, November 2026): no turn-cap hits at 2–4P; one-ply skill gap 1.92 / 2.81 / 3.70× fair; a passer scores 0; ~23–27% of claims come by flip. Two draft rules aren't in the sim: ending at once when the last goal is claimed (score-equivalent, since nothing scores after it) and the shared-tie line. The sim doesn't model place markers, layout, or route-reading effort. Those are the main table risk.

*Design v0.1, draft. Structurally simulated (goal-race fork); never played; 4P blocked on place markers.*
