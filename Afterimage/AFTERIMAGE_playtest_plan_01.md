# AFTERIMAGE — playtest plan 01

*First table test · pairs with a future `AFTERIMAGE_playtest_01.md` report*

## Setup

| | |
|---|---|
| **Game / version** | AFTERIMAGE, [rulebook](AFTERIMAGE_rulebook.md) design v0.1 (never played) |
| **Players** | 2 |
| **Deck** | Game 1: signs 1–7 (21 cards, 7 × 3 grid, the first-game variant). Games 2–3: full 36 cards, 6 × 6 grid |
| **Time** | About 40 minutes for three games plus discussion |
| **Record** | A tally of guesses per game, matches per player, whether each sweep succeeded, final scores, and who went first |

Play three games:

1. **Seven signs, base rules.** Teach the game.
2. **Full deck, base rules** (no sideways marking).
3. **Full deck, with Marked flips** (flipped cards turned sideways). Swap first player from game 2.

## Hypotheses

Taken from the open questions in [AFTERIMAGE_concept.md](AFTERIMAGE_concept.md) and the caveats in [AFTERIMAGE_design_analysis.md](AFTERIMAGE_design_analysis.md).

| # | Hypothesis | Holds if… | Fails if… |
|---|---|---|---|
| H1 | **Recall beats guessing.** People remember what flipped cards showed well enough that the full-deck game lands near the sim's weak-memory range (34–40 guesses), not near random play (~150). | A full-deck game ends within about 50 guesses, and most matches after the first few are taken on purpose ("that one was a Leaf"). | It drags past ~60 guesses, or players say they're guessing blind well into the game. |
| H2 | **Counting is a moment, not homework.** At least one player counts at least once to decide whether to sweep, and it feels like a satisfying "it's safe" call. | Someone counts unprompted in game 2 or 3, sweeps on the count, and the table reacts to it. | Nobody counts after it's explained, or the count stalls the game or causes groans. |
| H3 | **A stronger memory wins, but not every game.** | The weaker rememberer takes at least a third of the pairs in some game, or wins one of the three. | One player takes nearly everything every time and the other checks out. |
| H4 | **Marked flips help without breaking it.** | Game 3 is faster or clearer than game 2, and memory still decides it. | It's no different (drop it) or play becomes trivial because the seen cards are obvious. |
| H5 | **The opening isn't decided by luck.** | Any early lucky match is soon forgotten; the winner isn't simply who got the first blind match. | A first-turn match feels decisive, or the first player wins every game. |
| H6 | **Refusing to sweep doesn't feel like stalling.** | If it happens, it reads as a clever last try. | It feels petty or slows the end. |

## What to watch

- **Handling first:** do cards slide when flipped in place? Do cards get nudged out of the grid? Is a 6 × 6 grid of flat cards comfortable to reach across? Is the wash-shuffle enough that nobody knows the starting faces?
- **The sweep itself:** is flipping every remaining card, and flipping them all back after a failed sweep, quick and unambiguous? Do cards get turned back to the wrong face?
- **The no-memory-talk rule:** do players naturally say "that was a Moon" aloud? Does forbidding it feel natural?
- **Taken pairs:** does anyone actually inspect taken cards for counting?
- **Pacing:** guesses per minute, and any long pauses.

## Teaching plan

Teach in under two minutes, from the rulebook only:

1. "Every card shows a sign. Flip one, then another. If the two new signs match, take them and go again."
2. "If they don't, leave them. Each one now hides the sign it just showed. Remember it."
3. "Matches always run out before the table's empty. When you think none are left, sweep: flip everything. If nothing matches, you end it and score a point."

Hold back the counting rule until the end of game 1, then teach it with the example from the rulebook. Note whether either player discovered it themselves.

Watch whether "it hides what it just showed" lands at once or needs a demonstration. That sentence is the whole game.

## After the session

Write `AFTERIMAGE_playtest_01.md` with each hypothesis marked confirmed, refuted or open, bugs by category, and rule-change candidates tied to observations. Then set `physically_playtested: true` and choose the state per the playtesting steering.
