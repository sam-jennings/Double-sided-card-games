# TRIGON — Playtest Report 01

*Pairs with [TRIGON_playtest_plan_01.md](TRIGON_playtest_plan_01.md). Written per [playtesting.md](../.kiro/steering/playtesting.md). Part of the Lauren & Arran session, June 2026 — see the raw notes in [Lauren and Arran Playtest.md](../Lauren%20and%20Arran%20Playtest.md).*

## Setup

- **Game / version:** TRIGON v1.2 (sim-tuned over ~23k games; first ever table test).
- **Players:** 3 (Sam, Lauren, Arran — Lauren and Arran are regular board/card gamers; Lauren reads and parses rules well). Plan 01 anticipated a 2P first contact; in the event it was a 3P game (12 turns each).
- **Symbol subset:** all 9 signs / 36 cards.
- **Prototype:** first "good" PnP set — printed on card, cut, laminated, corners rounded.
- **Rules access:** rulebook open on a laptop, consulted live. **No Calm Signs variant** (the plan recommended starting with Star not-wild; in the event full v1.2 was played from the start).
- **First game taught cold.** This is the game's first human contact, so the questions are feel, handling, and teachability — not balance.

## Hypotheses

The plan's four predictions were largely **left open** because the session was dominated by reference-checking overhead (see Bug 2) — turns were too slow and too rules-focused for the intended feel questions to resolve. Recording them honestly:

| | Verdict | Notes |
|---|---|---|
| **H1 — capture cadence feels good, not exhausting** | **Open** | Turn pace was dominated by ability look-ups, not capture rhythm. Captures happened but cadence couldn't be judged on a first, slow game. |
| **H2 — no ability is dead weight** | **Open** | Abilities were activated, but often to "do something" rather than toward a plan (see Bug 5). Can't yet say all nine earn their place. (Note: the plan flagged "Aurora" as a stale legacy name — confirmed irrelevant; v1.2's nine signs are Moon/Leaf/Wave/Flame/Eye/Mask/Key/Star/Crown.) |
| **H3 — "active player captures everything" is dramatic, not theft** | **Open** | No clear read; the table was too busy parsing requirements to set up and react to stolen lines. |
| **H4 — charging vs re-charging teaches itself in one game** | **Open / leaning refuted** | Charge state was not internalised — players re-consulted the rules repeatedly (Bug 2). One game was not enough; may improve on a second play. |

The session was less a test of the hypotheses and more a discovery of the **handling and onboarding bugs that block them**. That is a useful first-contact outcome.

## Bugs found (severity-ranked)

### Bug 1 — The grid is not physically defined; play slips to an unfixed grid *(handling / setup — HIGH)*
Placing the first card, there was no way to tell whether a cell was a **centre, edge, or corner**. The rulebook says only "leave space for a 3×3 grid... it starts empty" — there is no frame, no board, and (this deck having no backs) nothing to anchor the nine positions. The table defaulted to a habit from *Instinkt* (a 4×4 adjacency-placement game where the grid floats and a "centre" card can end up a corner). 

This is serious because **five of the nine abilities are defined by grid position** — Moon (no orthogonal neighbours), Leaf (edge), Mask (central cross), Star (corner), Crown (full row/column). An unfixed grid makes those requirements unresolvable, which quietly undermines the whole activation engine. This is a true handling bug, not just a comprehension slip.

### Bug 2 — Reference overhead: every player checks both faces' requirements + abilities, every turn *(handling / teachability — HIGH)*
The dominant problem of the session. With nine signs each carrying a requirement *and* an ability, and every card showing two of them, **every turn every player was reading the rules** to recall what each face required and did. Turns were very slow. The mnemonics were read at the start but **not used** to recall requirements/abilities in play. Lauren proposed a per-player reference card; Sam is reluctant to add a component that only serves one game. This is the central tension to resolve: TRIGON's ability table is "the only thing you'll need mid-game" in theory, but in practice a single shared laptop reference throttled the whole table.

### Bug 3 — Ambiguity: is the symbol requirement needed to *place*, or only to *activate*? *(comprehension — MEDIUM)*
The table was unsure whether a card could only be placed where its requirement was met, or whether the requirement only gates the ability. They **played it correctly** (requirement gates the ability; placement is into any empty cell, any face) — but it cost discussion to get there. The rulebook is technically clear ("Place it in any empty cell" vs the separate Activations section) but the distinction is not stated emphatically enough up front for a first read.

### Bug 4 — Chaining order/limits unclear when multiple cards are charged *(rules ambiguity — MEDIUM)*
With two independently charged cards A and B, the table wasn't sure of the protocol: resolve A's whole chain before B, or interleave freely? And: if you use one face's ability, can you flip the card and use the other face's ability the same turn? 

The rulebook *does* answer both — you choose the order and may interleave (continuous alignment checks; "you choose the order"), and **each card activates at most once per turn** regardless of face, so you cannot use both faces of the same card in one turn. But these answers are buried; players couldn't find them mid-turn. The table also under-used chaining generally — felt like a first-game artefact that would improve on replay, but they flagged a worry that **multi-chaining could become overwhelming** once they do use it.

### Bug 5 — Aimless placement: weak sense of strategy on a first game *(engagement — MEDIUM, likely first-game)*
Sam reported that, outside an obvious direct capture, he was placing cards "arbitrarily" or just to fire an ability with no goal. The strategy notes (decline ~3/4 of activations; "showing a sign feeds it"; pairs are bait) were not yet internalised. Plausibly a first-game effect — but worth re-checking on a second play, because a near-random *obvious* line that masks the real skill is exactly the OUROBOROS onboarding trap (see [design-principles.md](../.kiro/steering/design-principles.md) lesson 6a).

### Bug 6 — Draw deck vs removed/discard pile not visually distinguishable *(handling — LOW, cross-game)*
Recorded as a generic note: hard to tell the draw deck from the removed pile (and discard piles generally). Promoted to a deck-wide finding — see DECK_PLAYTEST_FINDINGS F9.

## Rule-change candidates (each tied to an observation)

1. **Fix the grid with no new components (Bug 1).** Make the **first card placed the centre cell**, and define the 3×3 as extending one cell in each direction from it. Positions become fixed and unambiguous from turn one, killing the *Instinkt* drift, with zero extra components. *Alternative:* place the first card as a *corner* and grow inward — but centre-first is the most intuitive and keeps the central-cross/corner geometry legible. **Test next session.**
2. **Resolve the reference-overhead tension (Bug 2).** Options, cheapest first: (a) **stage the teach** — play the first game with Calm Signs *and* only the position-free abilities, adding the positional ones once the grid is internalised; (b) a **single shared reference sheet** in the rulebook/centre of table rather than per-player cards (one component, all games could share a generic "sign reference"); (c) reconsider Lauren's **per-player reference cards** — the resistance is that they're game-specific, but a *generic* nine-sign quick-reference card could serve TRIGON, TURNCOAT, and others. This is a design decision, not a settled fix — flagged for the designer.
3. **Front-load the requirement-vs-ability distinction (Bug 3).** Add a one-line statement at the top of Activations: *"Requirements never restrict where you place a card — you may place any card in any empty cell. A requirement only decides whether that card's ability may fire."*
4. **Add an explicit chaining FAQ (Bug 4).** State plainly: *"Resolve activations in any order you like; you may switch between independent chains freely. Each card may activate at most once per turn — flipping a card to its other face does not give it a second activation."*
5. **Surface the real skill in the rulebook (Bug 5).** If a second game still feels aimless, treat it as a teaching problem, not a balance one: lead the strategy notes with "decline is usually right; don't start lines you can't finish."

## Verdict: **ITERATE**

TRIGON's first contact was bottlenecked by **handling and onboarding**, not by its core engine, which never got a fair test. The two HIGH bugs (undefined grid, reference overhead) are both addressable and are the priority before any feel/balance question can be answered. Nothing here challenges the simulation work — it challenges how the game is set up, taught, and referenced at the table.

**This keeps TRIGON in the pipeline at Stage 3 (table-tested). It is not yet a candidate for promotion** — the flagship needs at least one session where the engine actually breathes.

### Next session should answer
1. Does **centre-first grid definition** eliminate the unfixed-grid drift? (Bug 1 fix.)
2. With grid and references sorted, does the **capture cadence (H1)** and the **"active player captures everything" swing (H3)** finally read as drama? 
3. Does a **second game** lift play out of aimless placement (Bug 5), or is the skill genuinely hidden behind a near-random obvious line?
4. Re-test at **2P** as originally planned, to isolate the engine from multi-player downtime.
