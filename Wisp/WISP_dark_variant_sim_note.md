# WISP — Dark variant sim note (option c, November 2026)

*Measures option (c) from [WISP_design_analysis.md](WISP_design_analysis.md) §4: the rulebook's **Dark** variant, where the 24 leftover roads are set aside unseen and the hunters do not know the Wisp's hand. No rules, dials, record or state were changed; the dial choice is the designer's.*

## Method

`python wisp_sim.py --dark --games 2000 --seed 1` (new `--dark` mode in [wisp_sim.py](wisp_sim.py); the default open-game output is unchanged and reproduces the analysis table exactly). Same bots as the open sim. What changes is what the hunters know:

- **Worlds.** Hunters track every history consistent with the trail using *any* unplayed road (36 minus those played), not just the Wisp's known hand. Missed Raids still delete a place for that turn.
- **Weights, exact over hands.** Every world at a given moment has the same number *k* of played roads, so every world is consistent with the same C(36−k, hand−k) hands. Worlds differ only in how many of those hands keep the Wisp alive, which plays the part of the open sim's "a careful Wisp isn't cornered" pruning. Two ways of counting that:
  - **exit1** (`--prune exit1`, the default): the exact share of consistent hands holding at least one onward road from the world's current place (hypergeometric). This is exact, but it only looks one step ahead.
  - **full** (`--prune mc --mc-samples 300`): the share of consistent hands that still hold a *complete* escape route, the same test the open sim uses. Counting every hand exactly is too slow (C(35,11) ≈ 4×10⁸ hands after move 1), so it's a Monte Carlo estimate from 300 sampled hands per world. It has converged: at 12/4/8/2 over 200 games, 300 samples gave 53.0% escapes and 1,000 samples gave 52.0%. It's slow (~0.6 s per game), so it was run for Skilled v Skilled only.
- The skilled Wisp uses the same hunter model to judge how exposed it is, so both sides change together.

## Results (2,000 games per row, seed 1)

| Dials (hand / raids / escape / sprints) | S v S escapes (full) | S v S escapes (exit1) | S Wisp v random hunters | Random Wisp v S hunters | Random v random | Mean trail when caught, S v S (full / exit1) |
|---|---:|---:|---:|---:|---:|---:|
| **12 / 4 / 8 / 2 (v0.1)** | **56.1%** | **46.0%** | 67.3% | 26.6% | 31.1% | 6.6 / 6.3 |
| 12 / 3 / 8 / 2 | 61.3% | 56.4% | 73.0% | 29.8% | 31.3% | 7.0 / 6.9 |
| 12 / 3 / 7 / 3 | 68.3% | 57.1% | 71.9% | 40.4% | 43.9% | 6.1 / 5.9 |
| 12 / 2 / 8 / 2 | 70.8% | 67.8% | 79.0% | 33.7% | 38.0% | 7.5 / 7.4 |
| 12 / 1 / 8 / 2 | 82.2% | 83.6% | 88.3% | 39.1% | 41.0% | 8.0 / 8.0 |
| *12 / 5 / 8 / 2 (exit1 only)* | — | 39.6% | — | — | — | — / 5.8 |
| *12 / 4 / 7 / 2 (exit1 only)* | — | 51.8% | — | — | — | — / 5.4 |

The S v R, R v S and R v R columns use exit1. Random v random is the same as in the open game, as it should be (31.1% at v0.1), because neither random bot uses information. The skilled Wisp is cornered ≤ 0.1% of the time; the random Wisp is cornered 36–53%. For comparison, the open game at v0.1 dials gives 0.2% S v S escapes (analysis §2).

## Reading

- **Dark turns the v0.1 dials from a certain catch into a chase.** At 12/4/8/2, Skilled v Skilled escapes are 46% (exit1) to 56% (full), against 0.2% in the open game. Catches come late, at trail 6.3–6.6 of 8. Not knowing the hand lets a missed Raid delete one place from a set of up to eight (every unplayed road at the shown place) instead of ~2–3.
- **Of the measured rows, only the v0.1 dials land in or near 40–55% with a late catch.** Exit1 puts 12/4/8/2 at 46.0% (catch at 6.3), which is inside the target. The full model puts it at 56.1% (6.6), just over. Every lower-Raid row is Wisp-favoured under both models: 12/3/8/2 is 56–61%, 12/3/7/3 is 57–68%, 12/2/8/2 is 68–71%, and 12/1/8/2 is 82–84%, with that last row's one catch coming at trail 8.0, the forced final shot. If the table plays like the full model, 12/5/8/2 (39.6% under exit1) or 12/4/7/2 (51.8% exit1, but an earlier catch at 5.4) are the nearest neighbours, but neither was run under the full model.
- **Skill still matters, but the hunters' edge is thin.** On the Wisp side, at v0.1 the skilled Wisp escapes 46.0% against skilled hunters and the random Wisp 26.6%, a 1.7× gap. Much of that gap is the random Wisp cornering itself (45.6%). On the hunter side, skilled hunters cut the skilled Wisp from 67.3% (random hunters) to 46.0%, catching 1.66× as often. But against a random Wisp, skilled hunters barely beat random hunters (26.6% v 31.1% escapes). This matches the rulebook's "deduction to nerve". The hunters' arithmetic gets simpler (candidates are the partners of the shown place among unplayed roads, minus misses), so there is less for hunter skill to work on. This is a discovery-curve risk to watch at the table.
- **Nothing else has to change.** Dark keeps the 12-card hand and uses the rulebook's own Raid count. It avoids the trade made by options (a) (one Raid, a short chase) and (b) (a 14–16-card hand). What it gives up is the open game's perfect-information deduction.

## Physical-handling check (Dark)

| Question | Answer | Problem? |
|---|---|---|
| What can hunters see? | The trail's shown faces, the top faces of sprint packets, and the Wisp's hand count. No atlas. | — |
| Is the Wisp's hand private? | It is during play, with the v0.1a handling: hold the hand to the chest and choose each road below the table edge. **It isn't during setup.** The open rules shuffle by "flipping chunks" and deal openly, so the hunters see one face of every card the Wisp is dealt. In the open game that doesn't matter, because the atlas gives away the hand anyway. In Dark it leaks one face of each of the 12 hand cards. The leftover stack also has no back, so a squared pile shows a face on its top and bottom cards. | **Yes, a setup leak (not modelled; the sim assumes hunters know nothing).** Fix if Dark is adopted: the hunters look away while the Wisp shuffles, takes 12, and puts the other 24 straight back in the box. |
| Is legality verifiable at game end? | Mostly. The reverse excavation still checks every link, every sprint packet and every Raid answer, and a cornering claim is checked by showing the hand. **New gap:** with no atlas, nothing at the table shows that the Wisp played only its dealt 12. A swap with the boxed cards keeps the hand count right and passes the excavation. | A trust gap, not an ambiguity. Keep the box closed and out of the Wisp's reach. Optional end check: the trail plus the unplayed hand must be 12 cards. That catches miscounts, not swaps. |
| Hidden-face memory? | None added. The Wisp's only secret is still its own pressed face. | — |

## Caveats

- The hunter models weight histories by how many hands are consistent with them. They don't model the Wisp's policy, and neither does the open sim. The two hunter models bracket the effect of how careful the Wisp is assumed to be: exit1 is a weaker assumption, the full model a stronger one. Human hunters are probably weaker than both.
- Single seed. With 2,000 games, a row's standard error is about ±1.1 points.
- Tells and nerve aren't modelled. Dark puts more weight on both.
