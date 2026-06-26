# BLIGHT — Playtest Report 01

*Written per [playtesting.md](../.kiro/steering/playtesting.md). Part of the Lauren & Arran session, June 2026 — raw notes in [Lauren and Arran Playtest.md](../Lauren%20and%20Arran%20Playtest.md). (No prior plan doc; BLIGHT was played opportunistically in the session.)*

## Setup

- **Game / version:** BLIGHT v1.0 (sim-validated; first table test).
- **Players:** 3 (Sam, Lauren, Arran) → **12 cards each**, full 36-card deck.
- **Rounds:** one round (not the full match-of-one-round-per-player).
- **Symbol subset:** all 9 signs / 36 cards.
- **Teach:** Lauren read the rules herself and reported them **clear and easy to understand** — and that BLIGHT was **more the kind of game she expected** from this deck than TRIGON, JANUS, or CROSSROADS.

## Hypotheses (from the rulebook's first-table caveats)

| | Verdict | Notes |
|---|---|---|
| **Does ducking create satisfying agony, or passive low-card dumping?** | **Open / leaning positive** | The interesting line (Arran's crown-dumping, below) was active, not passive — but one round at 3P is thin evidence. |
| **Does a surprise hidden 9 read as drama or gotcha?** | **Confirmed-ish (drama)** | The crown faces drove the round's defining swing and were understood as the point of the game, not a gotcha — though see Finding 2 on the *fun* split. |
| **Is the ~1% shoot threat exciting?** | **Not tested** | No shoot attempt arose in a single round. |

## What happened — the defining outcome

Arran held **~6 of the 8 Crown (9) cards**. He ended the round with **by far the lowest penalty (i.e. winning)** — because he could rarely follow suit and so **sloughed** most of those Crowns away, dumping their hidden 9-pips into other players' rot piles. 

**This is BLIGHT working exactly as designed.** The strategy notes say it outright: "Show a card's low face so its high face lands in the winner's pile — handing a rival your hidden Crown is the game's quiet knife," and "voids are weapons." The player who *looked* doomed (a fistful of Crowns) won by weaponising voids to offload rot. That the table found this **surprising** is the headline: the design's central skill expression is counter-intuitive on a first play — a good sign for depth, and a teaching note (it parallels the OUROBOROS "real skill hidden behind the obvious line" lesson, [design-principles.md](../.kiro/steering/design-principles.md) lesson 6a, but here in the *player's favour*).

Play otherwise **went through without any rules issues** — clean comprehension, no handling disputes over the trick/reveal/rot-pile mechanics. The penalty-face-up rot pile (orientation-as-state) did its job: nothing needed remembering.

## Bugs & findings (severity-ranked)

### Finding 1 — Large hand handling: 12 cards, both faces, no natural sort, realign every trick *(handling — HIGH, cross-game)*
The one real handling complaint. With 12 cards (3P), each turn a follower must: check **both faces** of every card for the led sign, **rotate them to face the same way**, *then* choose. Because the deck has **no natural ordering** (every card belongs to two signs at once), this re-scan happens **every single trick** — it can't be solved by sorting once. Example given: leader plays Moon → everyone hunts both faces of all cards for a Moon, aligns them, then decides. This is the deck-wide hand-management problem, felt hard at 12 cards. Promoted to DECK_PLAYTEST_FINDINGS (extends F1). **3P (12 cards) is the heaviest BLIGHT configuration — 4P (9) and 6P (6) will be lighter.**

### Finding 2 — "Bad hand, can't recover" — a fun split *(engagement — MEDIUM, divisive)*
Lauren **did not enjoy** the round: she felt she'd been dealt a bad hand with no way to climb back. Sam and Arran disagreed — this is typical of trick-takers, and BLIGHT actually gives *more* recovery than most because **every card offers two playable faces**. Both positions are legitimate:
- It's a real trick-taking-genre objection (hand luck), valid for some players.
- BLIGHT's two-faced cards and the slough-as-weapon line (Finding above) genuinely do offer agency that single-faced trick-takers lack — Lauren may not have seen it on a first play, which loops back to the teaching point.

This is a **fun/feel question only more table time (and more players) can settle**, not a clear bug. The existing **"The Passing"** variant (pass 3 cards each round) directly targets unlucky hands and is the obvious lever if this recurs.

### Finding 3 — Single round, off the intended match structure *(method — note)*
BLIGHT is designed as a **match of one round per player** (rotating lead, lowest total across the match) precisely to wash out per-deal luck — exactly Lauren's complaint. Playing a **single round** maximises the felt unfairness. The next test should run the **full 3-round match** so deal variance averages out as intended.

## Rule-change candidates (each tied to an observation)

1. **No rules change yet** — the round played clean and the surprising outcome was the design functioning, not a defect.
2. **Address hand-handling via the cross-game track (Finding 1)**, not a BLIGHT-specific rule — see DECK_PLAYTEST_FINDINGS F1. Prefer testing **4P/6P** (smaller hands) before concluding 12 cards is too many.
3. **If the hand-luck complaint recurs (Finding 2)**, promote **The Passing** from variant to default, or trial it as the standard rule — but only after a full match, since the match structure is itself the primary mitigation.
4. **Run the full match next time (Finding 3)** to test the intended luck-smoothing.

## Verdict: **ITERATE** — the most promising of the four games this session

BLIGHT was the session's standout: rules praised as clear, play clean, and it delivered the deck-native experience Lauren expected (the hidden face as the poison). Its central skill — weaponising voids to dump rot — surfaced naturally and decided the round. The two open issues are a **deck-wide handling problem** (large hands) and a **genre-inherent fun split** (hand luck), both with known levers (player count, The Passing, the match structure).

**Stays in the pipeline at Stage 3 (table-tested). Strong promotion candidate** once it has (a) a full-match test, (b) a test at 4P or 6P to check the lighter hand sizes, and (c) a read on whether the hand-luck complaint survives the match structure.

### Next session should answer
1. At **4P (9 cards) / 6P (6 cards)**, does the large-hand handling load (Finding 1) drop to comfortable?
2. Over a **full match**, does the hand-luck complaint (Finding 2) wash out — and does Lauren's view change once she's seen the slough-as-weapon line?
3. Does the **shoot-the-rot** threat ever light up the table?
