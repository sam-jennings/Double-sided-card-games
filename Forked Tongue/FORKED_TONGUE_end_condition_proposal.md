# FORKED TONGUE — end-condition proposal (November 2026)

*A proposal only. Nothing in the [rulebook](FORKED_TONGUE_rulebook.md), the game record, the catalogue or the public picker has been changed. The designer chooses.*

Evidence: [forked_tongue_end_sim.py](forked_tongue_end_sim.py) (a copy of [forked_tongue_sim.py](forked_tongue_sim.py) with the candidate rules as options; the original is untouched). Background: [FORKED_TONGUE_design_analysis.md](FORKED_TONGUE_design_analysis.md).

## Recommendation in one paragraph

Adopt two small rules together: **Swear on it** (once the ledger holds 4 or more cards, a claimant who survives the challenge window may flip their own card; if true, the whole ledger is retired face-up to the registry) and a **decline fuse** (each decline burns the registry once; when it is fully burnt the game ends and the fewest cards in hand wins). Across 2,000 games per row at 3, 4, 5 and 6 players, this pair took the stall rate to **0.0% for every table, honest tables included**, cut skilled games to a mean of 36–60 turns (p90 45–80), kept skilled play at 2.9–4.1× fair against random and kept seat spread within 4–10 points. If only one rule is wanted, the fuse alone also gives 0.0% stalls, but ends 52–74% of games on the clock rather than by shedding. Neither rule makes lying profitable for the bots; that is a separate problem (see the end).

Player counts: the task asked for 2/3/4P, but FORKED TONGUE is 3–6P and has no 2P deal, so every run is 3/4/5/6P.

## 1. Reproduction

Command: `python forked_tongue_sim.py --games 2000 --seed 1` (v1.1 rules, turn cap 600, 48,000 games, 87 s). Selected rows, copied from the output:

| P | table | stall | mean turns (finished games) | p90 |
|---:|---|---:|---:|---:|
| 3 | random | 5.8% | 196.4 | 396 |
| 3 | skilled | 4.2% | 114.7 | 214 |
| 3 | honest | **36.4%** | 56.0 | 90 |
| 4 | random | 1.3% | 159.3 | 322 |
| 4 | skilled | 0.4% | 124.4 | 241 |
| 4 | honest | **79.0%** | 58.5 | 98 |
| 5 | honest | 2.9% | 83.7 | 146 |
| 6 | honest | 18.1% | 125.8 | 269 |

This matches the earlier 1,000-game pass (3P honest 37.2%, 4P 78.7%). The new bench's "no rule" row reproduces these figures exactly, which confirms the copy plays v1.1 unchanged.

## 2. Root cause

I traced individual stalled honest games (400 per count, scratch diagnostic). The stall is not a slow drift. It is an **exact cycle**. At 4P, the last 12 events of a stalled game read: four plays (ledger 11 → 14), then four declines (ledger 14 → 10), then the same four plays again, with hand sizes returning to `[4, 4, 4, 4]` / `[5, 4, 4, 5]` each lap. Three rule facts combine to make that cycle possible and stable:

1. **No card ever leaves play unless someone lies.** Cards move between hands and the ledger, and only a challenge moves a block of them. With honest claims nobody challenges (0.2–1.0 challenges per honest game), so the cards in hands plus the ledger stay constant: 24 at 3P, 28 at 4P.
2. **The claimant sets the next requirement, and steering works best in small hands.** A player with 2–4 cards holds 4–8 of the 9 symbols. The strategy notes say to claim a scarce symbol, so the next player usually can't show it and declines.
3. **A decline is reversible.** It takes the newest card and rewinds the requirement one link, which restores the position from one play earlier. A lap of n plays followed by n declines returns the table to its starting state, apart from who holds which card.

So the game's only forward move (a successful challenge on a lie) is absent from honest play, and the honest strategy (true claims that steer) is exactly what produces the cycle. Under a row cap the cycle simply moves to short ledgers: 3P honest stalls under cap 6 finish with an **empty** ledger and level hands (`4,4,4` with 24 cards in the registry). Each player opens fresh, the next declines the single card, and so on. That is why any rule that only removes cards when the ledger is long can't guarantee an end. Only a rule that counts declines can.

## 3. Candidates

Each candidate passes the [physical-handling](../.kiro/steering/physical-handling.md) checklist as follows.

### A. Row cap (cap = 6 / 8 / 10)

*When a play survives the challenge window and the ledger now holds L cards, the whole ledger is retired face-up to the registry; the next player opens fresh.*

- **See / inspect:** row length is visible; retired cards join the registry and are examinable like any registry card.
- **Hidden:** nothing new. A lie buried in a retired ledger escapes punishment but becomes public as a pair, which shrinks the lie-space (on theme).
- **Verify:** count the row. No memory needed.

### B. Swear on it (ledger ≥ 4 / ≥ 6)

*After a play survives the challenge window, if the ledger holds N or more cards, the claimant may flip their own card. True: the ledger retires to the registry and the next player opens fresh. A lie: the claimant takes the ledger.*

- **See / inspect:** the flip is public. Retired cards go to the registry.
- **Hidden:** the claimant knows their own card, so the risk is only theirs to take. A liar simply doesn't swear, and *not swearing* is itself a readable tell, which is good social texture.
- **Verify:** the flip settles it immediately.

### C. Decline fuse (20 fixed, or 2 burns per registry card)

*Each decline burns the fuse once. When the fuse is spent, the game ends at once: fewest cards in hand wins. Tie: the first tied player clockwise after the player whose decline burnt the fuse.*

- **Physical fuse with no extra components:** the setup registry (12 / 8 / 6 / 6 cards). The first burn turns a registry card sideways; the second moves it to a spent row. That gives 24 / 16 / 12 / 12 declines at 3 / 4 / 5 / 6P. The cards stay public and examinable, so their deduction value is unchanged. Retired ledger cards (from A or B) go to a separate pile and never count toward the fuse.
- **Verify:** the count is the visible state of the registry row. Hand sizes are public at the end.

### D. Last word

*A player holding exactly one card may play it showing either face, ignoring the requirement (they still claim, and the challenge window applies).*

- **See / inspect:** hand size is public. Nothing hidden changes.
- **Verify:** trivial.

## 4. Results

Command: `python forked_tongue_end_sim.py --games 2000 --seed 1` (13 rule sets × 4 player counts × 6 tables, 2,000 games per row, turn cap 600, seed 1, about 160 s across all cores). Columns:

- **stall** is for random / skilled / honest tables.
- **turns** is mean / median / p90 on the all-skilled table. A turn is one play or one decline; the design analysis assumes about 8 s per turn, so 75 turns is about 10 minutes.
- **skill** is one skilled seat among random bots, as a multiple of a fair win rate.
- **liar** is one lying skilled seat among honest skilled bots, as a multiple of fair; above 1.00 would mean lying pays.
- **spread** is the gap between the best and worst seat on the skilled table.
- **lies/g** and **caught** are lies per skilled game, and the share of those lies that are caught (by a challenge or a failed swear).
- **fuse** is the share of skilled games ended by the clock.

### v1.1, no rule (baseline)

| P | stall | turns | skill | liar | spread | lies/g | caught |
|---:|---|---|---:|---:|---:|---:|---:|
| 3 | 5.8 / 4.2 / **36.4%** | 114.7 / 96 / 214 | 2.90 | 0.43 | 2.8% | 32.3 | 39% |
| 4 | 1.3 / 0.4 / **79.0%** | 124.4 / 99 / 241 | 3.62 | 0.06 | 4.0% | 34.1 | 52% |
| 5 | 0.1 / 0.0 / 2.9% | 75.2 / 66 / 126 | 4.21 | 0.36 | 3.8% | 21.2 | 57% |
| 6 | 0.0 / 0.0 / 18.1% | 60.0 / 52 / 103 | 4.43 | 0.32 | 6.0% | 14.7 | 63% |

### A. Row cap

| rule | P | stall | turns | skill | liar | spread | lies/g | caught |
|---|---:|---|---|---:|---:|---:|---:|---:|
| cap 6 | 3 | 0.0 / 2.9 / **25.1%** | 77.0 / 70 / 125 | 2.87 | 0.64 | 2.7% | 18.9 | 38% |
| cap 6 | 4 | 0.1 / 0.4 / 4.5% | 73.1 / 63 / 126 | 3.61 | 0.23 | 9.3% | 19.6 | 53% |
| cap 6 | 5 | 0.1 / 0.1 / 3.1% | 66.5 / 60 / 106 | 4.22 | 0.52 | 8.0% | 18.1 | 58% |
| cap 6 | 6 | 0.0 / 0.0 / 0.1% | 49.7 / 43 / 79 | 4.47 | 0.40 | 9.1% | 12.5 | 64% |
| cap 8 | 3 | 1.3 / 3.2 / 20.2% | 86.7 / 77 / 144 | 2.92 | 0.62 | 2.9% | 22.3 | 40% |
| cap 8 | 4 | 1.2 / 0.4 / 16.2% | 92.1 / 77 / 166 | 3.58 | 0.21 | 6.5% | 24.8 | 52% |
| cap 10 | 3 | 3.5 / 4.5 / 28.3% | 96.5 / 84 / 164 | 2.90 | 0.49 | 4.5% | 26.3 | 40% |
| cap 10 | 4 | 1.4 / 0.3 / 37.9% | 106.7 / 87 / 205 | 3.62 | 0.16 | 3.9% | 29.1 | 52% |

*Verdict:* it shortens games and helps at 4–6P, but it **doesn't end honest 3P games** (20–28% stalls) for the reason in §2. It isn't enough on its own.

### B. Swear on it

| rule | P | stall | turns | skill | liar | spread | lies/g | caught |
|---|---:|---|---|---:|---:|---:|---:|---:|
| swear 4 | 3 | 0.1 / 2.5 / **29.1%** | 67.5 / 61 / 103 | 2.85 | 0.69 | 3.8% | 16.0 | 37% |
| swear 4 | 4 | 0.1 / 0.0 / 0.1% | 53.9 / 50 / 83 | 3.57 | 0.39 | 6.8% | 14.6 | 53% |
| swear 4 | 5 | 0.0 / 0.1 / 6.1% | 59.4 / 55 / 92 | 4.09 | 0.61 | 5.8% | 15.6 | 59% |
| swear 4 | 6 | 0.0 / 0.0 / 0.0% | 43.2 / 40 / 65 | 4.41 | 0.49 | 10.0% | 10.9 | 65% |
| swear 6 | 3 | 1.5 / 3.4 / 25.1% | 77.6 / 71 / 125 | 2.90 | 0.62 | 2.7% | 19.6 | 39% |
| swear 6 | 4 | 0.9 / 0.1 / 4.5% | 76.2 / 66 / 131 | 3.59 | 0.31 | 6.7% | 20.4 | 52% |

*Verdict:* the best single card-removal rule (4P honest drops from 79.0% to 0.1%), and it gives the claimant a real choice and the table a tell. It still leaves the 3P short-ledger cycle (29.1%).

### C. Decline fuse

| rule | P | stall | turns | skill | liar | spread | lies/g | caught | fuse / tie |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| fuse 12 (ties share) | 3 | 0 / 0 / 0% | 50.0 / 49 / 64 | 2.76 | 0.53 | 3.4% | 16.0 | 43% | 82% / 13% |
| fuse 12 (ties share) | 6 | 0 / 0 / 0% | 37.0 / 37 / 47 | 4.02 | 0.63 | 9.3% | 10.1 | 64% | 64% / 24% |
| fuse 20, tie next | 3 | 0 / 0 / 0% | 70.7 / 72 / 94 | 2.83 | 0.54 | 4.0% | 21.5 | 42% | 61% / 9% |
| fuse 20, tie next | 4 | 0 / 0 / 0% | 62.3 / 63 / 81 | 3.41 | 0.41 | 3.6% | 18.4 | 53% | 66% / 12% |
| fuse 20, tie next | 5 | 0 / 0 / 0% | 59.4 / 61 / 79 | 3.92 | 0.43 | 5.9% | 17.4 | 59% | 39% / 10% |
| fuse 20, tie next | 6 | 0 / 0 / 0% | 48.6 / 51 / 66 | 4.28 | 0.53 | 8.0% | 12.4 | 63% | 36% / 12% |
| fuse 2× registry, tie next | 3 | 0 / 0 / 0% | 78.3 / 81.5 / 107 | 2.88 | 0.58 | 5.1% | 23.2 | 41% | 52% / 8% |
| fuse 2× registry, tie next | 4 | 0 / 0 / 0% | 53.5 / 54 / 68 | 3.27 | 0.40 | 3.9% | 15.9 | 53% | 74% / 14% |
| fuse 2× registry, tie next | 5 | 0 / 0 / 0% | 44.5 / 44 / 56 | 3.62 | 0.43 | 6.8% | 13.7 | 59% | 70% / 19% |
| fuse 2× registry, tie next | 6 | 0 / 0 / 0% | 37.0 / 37 / 47 | 4.00 | 0.60 | 10.8% | 10.1 | 64% | 64% / 24% |

*Verdict:* the only candidate that **guarantees** an end (0.0% in every row; it can't cycle forever because each cycle burns the fuse). The cost is that it changes what usually decides the game: on its own, the clock, not shedding, ends 52–74% of games and needs a tie-break 8–24% of the time. The "tie next" break leaves seat spread at 3.6–10.8%.

### D. Last word

| rule | P | stall | turns | skill | liar | spread | lies/g | caught |
|---|---:|---|---|---:|---:|---:|---:|---:|
| last word | 3 | 0.2 / 0.4 / 10.9% | 70.4 / 59 / 124 | 2.88 | 0.52 | 8.2% | 21.9 | 42% |
| last word | 4 | 0.0 / 0.1 / **40.5%** | 76.7 / 64 / 138 | 3.50 | 0.22 | 7.3% | 22.4 | 53% |
| last word + cap 8 | 3 | 0.1 / 0.8 / 7.6% | 62.0 / 54 / 102 | 2.88 | 0.63 | 3.4% | 18.4 | 42% |
| last word + cap 8 | 4 | 0.0 / 0.1 / 7.6% | 66.6 / 56 / 120 | 3.57 | 0.28 | 7.7% | 19.5 | 53% |

*Verdict:* honest 4P tables still cycle at 3–5 cards (40.5%). Nobody gets down to one card, so the rule never fires. Rejected.

### Recommended: B + C (swear 4 + fuse 2× registry, tie next)

| P | stall | turns | skill | liar | spread | lies/g | caught | fuse / tie |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 3 | 0 / 0 / **0%** | 59.7 / 62 / 80 | 2.88 | 0.90 | 3.9% | 15.3 | 39% | 28% / 7% |
| 4 | 0 / 0 / **0%** | 45.8 / 46 / 61 | 3.42 | 0.38 | 5.6% | 13.1 | 54% | 35% / 8% |
| 5 | 0 / 0 / **0%** | 43.1 / 43 / 53 | 3.57 | 0.51 | 4.3% | 12.8 | 60% | 64% / 18% |
| 6 | 0 / 0 / **0%** | 35.6 / 36 / 45 | 4.07 | 0.55 | 10.3% | 9.4 | 65% | 42% / 16% |

Compared with the fuse alone, swearing lets most 3–4P games end the way the game intends, by shedding (the fuse decides 28% / 35% instead of 52% / 74%). It also shortens games by 8–19 turns. At about 8 s a turn, skilled games run 5–8 minutes of bot play, well inside the "~20 min" banner, which leaves room for human table talk. The trade-off is one more rule to teach. The fuse alone is the minimum fix if the designer would rather keep v1.1 nearly as written.

Proposed rulebook wording (not applied):

> **Swear on it.** If your play survives the challenge window and the ledger holds 4 or more cards, you may flip your own card. True: move the whole ledger face-up to the registry; the next player opens fresh. A lie: you take the ledger.
>
> **The fuse.** Each time anyone declines, burn the fuse: turn one upright registry card sideways or, if none is upright, slide one sideways card into the spent row. When the last registry card is spent, the game ends: fewest cards in hand wins. On a tie, the first tied player clockwise after the player who burnt the fuse wins. (Cards retired by swearing go beside the registry and are never burnt.)

## 5. What the sim can't settle (for the table)

- **Lying still doesn't pay for the bots** (liar 0.38–0.90× fair under the recommendation, 0.06–0.43× in v1.1). The end rules fix *termination*, not the honesty-dominance problem in the design analysis. Whether humans bluff profitably through tells and nerve is the first table question.
- **Gaming the fuse.** The bots never decline on purpose to burn the fuse while they lead. A human with the fewest cards may decline to end the game if they would still be fewest after taking a card, which would be a legitimate endgame play. Watch for it, and for whether it feels clever or cheap.
- **The 5–6P fuse is short** (12 declines; it decides 64% / 42% of games). If the table feels robbed, try 3 burns per registry card at 5–6P (18 declines).
- **Swear as a tell.** Does *not* swearing on a long ledger read as an admission? That is the point, but check that it doesn't make lies trivially readable.
- **Registry sprawl.** Retired ledgers can more than double the registry at 3P. Check that it stays examinable on a real table.
- Still open from the analysis: the Apprentice Forgers variant doesn't say what happens to the older ledger cards after a challenge. The rulebook's FAQ fallback ("if a table circles, play the Long Con") would be replaced by the fuse.

Re-run `python forked_tongue_end_sim.py --games 2000 --seed 1` after any change. The bots are a floor, not a ceiling; see the design analysis for what they don't model.
