# TURNOVER — Design Analysis

*How the party game was tuned by simulation, v1.0 → v1.1. Companion to the rulebook; sibling to the SYZYGY and TURNCOAT analyses.*

---

## 1. The questions

The v1.0 rulebook shipped with three open questions in its design footnote: is the chain limit right at 2 (or should it be 3)? Is the refusal cost right at 2 cards (or 3)? And does 6P need the Hot Well rule (refusals take 3) by default? A fourth question emerged in testing the variants: does Slow Match (no chains, for younger players) even terminate?

## 2. Method

The full ruleset as a simulator (`turnover_sim.py`, included): exact deal sizes per player count, face-up well with the under-pile fallback, the announce rule treated as always observed. Two bots — RandomBot (uniform legal play, 50% chain rate) as the mechanics floor, and a SkilledBot that plays the public-information game the strategy notes describe: it counts every face in the pile history (both faces of a played card are public once turned), prefers exit symbols the table is poorest in, refuses to break its last guaranteed-chain pair while its hand is large, and chains only when that doesn't fragment its hand. **1,200 games per configuration** across all four player counts and a 3×2 grid of chain limits (1/2/3) × refusal costs (2/3), plus seat-randomised skill-gap arms — roughly **60,000 games** total, with a 600-turn cap to catch non-terminating rules.

## 3. Results

### Chain limit (the 2-vs-3 question)

| 3P, refusal 2 | chain 1 | chain 2 | chain 3 |
|---|---|---|---|
| Stalls (no winner by turn 600) | 24% | **0%** | 0% |
| Avg turns/player | 81 | 11.1 | 7.1 |
| Skill edge (skilled vs random, ×baseline) | — | 1.50× | 1.64× |
| Seat 1 vs last seat win | — | 36/31 | 34/34 |

The pattern holds at every player count. **Chains are not a luxury — they are the game's exhaust valve.** Refusals pump cards into hands two at a time; only multi-card turns shed fast enough to outrun the pump. At chain 1 the race literally never finishes in a quarter of games. Chain 2 (the v1.0 default) is confirmed: ~4.5–5.5 minutes of real play at every count, seats near-flat, healthy 1.5–1.8× skill edge. Chain 3 is *also* sound — faster (~3 min), slightly more skilled (up to 2.1× at 5–6P), seats still flat. It is too brutal a pace for a first game but too good to discard: v1.1 keeps 2 as the default and adds chain 3 as the **Wildfire** variant.

### Refusal cost (the Hot Well question)

The v1.0 text sold Hot Well as "sharper, shorter, crueller." The simulation says the middle word is exactly backwards:

| Avg turns/player, chain 2 | refusal 2 | refusal 3 |
|---|---|---|
| 3P | 11.1 | 17.5 (+58%) |
| 4P | 9.4 | 15.0 (+60%) |
| 5P | 7.9 | 11.2 (+42%) |
| 6P | 6.8 | 8.2 (+21%) |

Taking three cards instead of two doesn't make refusal scarier — it makes hands fatter, and fat hands take longer to empty than the extra threat saves. Crueller, yes; shorter, no. The skill edge barely moves. And the question "does 6P need Hot Well by default?" answers itself: 6P at the standard cost is already the fastest, flattest configuration in the matrix. **v1.1 cuts Hot Well entirely.** A table that wants more bite should reach for Wildfire, which actually delivers shorter-and-sharper instead of promising it.

### Slow Match (the variant nobody checked)

No chains at the standard refusal cost is the chain-1 row above: 24–73% of games never end, depending on player count. The variant as written was broken for precisely the audience it serves. One knob fixes it: **refusals take 1 card** in Slow Match. Stall rate drops to 0.0% at every count (800 games each), with games running a leisurely 14–21 turns per player — long for adults, right for the eight-year-old it exists for.

### Health checks

Zero stalls in 4,800+ games at the shipped configuration; seat spread within 5 points at every count; the skilled bot's edge (1.5–1.8× at default, rising with player count) clears the OUROBOROS lesson — random-vs-skilled gaps this wide predict a table where attention is rewarded. Estimated length at 8 s/turn: 4.5–5.5 min average, p90 ≤ 10 min — comfortably inside the "~10 minutes" box on the tin.

## 4. Changes adopted in v1.1

1. Chain limit **stays 2**; refusal cost **stays 2**. The defaults were right.
2. **Hot Well deleted** (its one claim was false; its job is done better by Wildfire).
3. **Wildfire** added: chains of up to 3 — measurably faster and more skill-rewarding, recommended once the table knows the deck.
4. **Slow Match** errata: refusals take 1 card. Without it the variant frequently cannot end.
5. Design footnote updated: the three open questions are closed, with numbers.

## 5. Caveats for the first table test

Bots don't laugh, and TURNOVER is a party game — pacing and table feel still need humans. The sim also treats the announce rule as automatic; the catch-the-forgetter mini-game is untested by construction. What simulation *can* certify is now certified: the race ends, the defaults are sound, the variants do what they claim.
