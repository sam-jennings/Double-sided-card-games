# Focus & Prioritisation

> **Primacy.** This note is part of the project's binding steering set in
> `.kiro/steering/`. Treat these notes as the **primary reference** for all
> design decisions and defer to them over any other document. When you apply
> guidance from here, **cite the specific steering note** you are relying on.

The collection has eleven games, one designer, and limited table-testing
opportunities. This note exists to answer: **"what should I work on next?"**
and to resist the gravitational pull of new concepts and whichever game feels
interesting in the moment.

## The core rule

> **Advance the highest-priority game that you can actually test right now.**

"Can actually test" means: you can sit down today (or this week) and run a
session with the players you have access to. That makes **player count the
dominant logistical constraint** — solo and 2P games are always testable;
3–4P games need one or two willing friends; 5–6P games are event-dependent.

## Priority ladder

Work the ladder top-down. Only move to a lower rung when every game above it
is either blocked (waiting on a partner, awaiting materials, parked by
decision) or has no actionable next step you haven't already completed.

### Rung 1 — Iterate on table-tested games (with open questions)

These have been played and produced concrete findings. The next step is
always recorded in `COLLECTION_OVERVIEW.md`. Finish the iteration before
starting something new.

| Game | Players | Current next step |
|---|---|---|
| TWELVE TRIALS | 1–2 | Alt flip-tracking method; re-test with scoring |
| THE ORRERY | 1–3 | Fix terminology; test with random deals (9-sym) |
| CROSSROADS | 2 | Test Signal Fires flip economy (v1.1) |

**Why these first:** they already have momentum and specific, falsifiable
questions. Iterating is cheaper than starting from scratch.

### Rung 2 — First table test for sim-validated games

These are analytically complete but have never been touched by human hands.
A single session answers more than another thousand simulated games.

| Game | Players | Testability | Blocking question |
|---|---|---|---|
| TRIGON | 2–4 | 2P possible | Does a capture every ~5 turns feel right? |
| TURNCOAT | 2–4 | 2P possible | Is one activation/turn exciting over 18 turns? |
| TURNOVER | 3–6 | Needs 3+ | Announce-rule policing fun? |

**Priority within rung 2:** TRIGON and TURNCOAT are testable at 2P (you +
one person), so they jump ahead of TURNOVER which needs 3+.

### Rung 3 — First table test for rulebook-complete games

Full rules, zero plays. Ordered by testability (fewest players needed first).

| Game | Players | Testability | Key question |
|---|---|---|---|
| FACE VALUE | 2 | Solo-simulable, 2P test | Fold frequency; cold-read timing |
| JANUS | 2–4 | 2P possible | Omen economy pacing |
| THE UNPLAYED PAIR | 3–5 | Needs 3+ | Hidden-face rank simplicity |
| FALSE FACE | 3–6 | Needs 3+ | Can first-gamers price a lie? |
| THE COUNCIL | 3–6 | Needs 3+ | Kingmaking at 5–6P |

### Rung 4 — New game concepts

**Only enter this rung when:**
1. Every rung-1 game has been iterated past its current open question, AND
2. You have run at least one first-table session from rung 2 or 3 since the
   last time you designed something new, AND
3. The new concept fills a gap visible in the coverage tables (player count,
   genre, mood, complexity) that no existing game already fills.

If you catch yourself reaching for a new concept, ask: *"Have I read through
the existing games' open questions first?"* If not, do that. The answer to
"what should I work on?" is almost always already written down.

## Testability tiers (for scheduling)

| Available players | Games you can advance |
|---|---|
| Just me (solo) | TWELVE TRIALS, THE ORRERY |
| Me + 1 | CROSSROADS, TRIGON, TURNCOAT, FACE VALUE, JANUS |
| Me + 2 | All above + TURNOVER, THE UNPLAYED PAIR, FALSE FACE, THE COUNCIL |
| Me + 3–5 | All above at full count |

**Use this table when planning a session.** If a friend is coming over,
look up which rung-1 or rung-2 games you can run at that player count, pick
the highest-priority one, and prep a playtest plan for it.

## The "shiny new idea" circuit breaker

When a new game idea arrives (and it will), before writing anything:

1. **Write one sentence:** what deck property does it exploit?
2. **Check the coverage table:** does an existing game already cover that
   property × genre × player count?
3. **Check the ladder:** is there a higher-priority game you could advance
   with the same time investment?
4. If yes to 2 or 3 → **log the idea in one line** at the bottom of
   `NEW_GAME_CONCEPTS.md` (under a "Parking Lot" heading) and return to
   the ladder.
5. If genuinely novel and gap-filling → write a short concept sheet, but
   **do not develop a full rulebook** until at least one rung-2 or rung-3
   game has been first-tested.

## Session planning checklist

Before sitting down to work on any game:

- [ ] Read that game's entry in `COLLECTION_OVERVIEW.md` (current status,
      open questions).
- [ ] Read its most recent playtest report or design analysis (if any).
- [ ] Identify the single most important question this session should answer.
- [ ] If it's a table test: write a short playtest plan (per `playtesting.md`).
- [ ] If it's design/iteration work: tie any proposed change to a specific
      observed problem from a prior test.

## Keeping this file current

When a game changes rung (e.g. TRIGON gets its first table test → moves to
rung 1), update both this file and `COLLECTION_OVERVIEW.md`. When all rung-1
games are resolved or parked, promote the next rung-2 games up.
