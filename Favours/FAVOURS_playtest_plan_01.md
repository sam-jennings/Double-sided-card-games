# FAVOURS — Playtest Plan 01

*Pairs with the forthcoming `FAVOURS_playtest_01.md`. Written per `.kiro/steering/playtesting.md`. Hypotheses come from the first-table questions in `COLLECTION_OVERVIEW.md`, the rulebook's "Design intent, and what is being tested" section, and [favours_sim.py](favours_sim.py) (re-run for this plan, seed 2026).*

## Open before the session

No rule gap blocks a session. Three things to settle:

- **5P instead of 7P.** `next_step` and the rulebook's falsification test both ask for a 7-player evening. This plan runs 5, the smallest supported count. That matters: at 5P each player holds **2 cards for 2 rounds**, and the sim's forced-play rate (cards carrying your own sign, so with only one legal recipient) is **40%**, against 29% at 7P. A quiet 5P table is **weaker evidence** against the social premise than a quiet 7P table. The 7P test carries forward whatever happens.
- **Play the two-deal variant.** The rulebook recommends it at 5–6P. Re-run for this plan (20,000 random-play games each): one deal leaves **55%** of games tied at the top and **28%** still shared after the tiebreak; two deals cut that to **41%** and **15%**.
- **Simultaneous giving has no commitment step.** "On a count of three, give it" relies on everyone moving at once. Nothing stops a slow hand from watching where others go. **Session convention:** before the count, everyone holds their chosen card **pinched against their chest**, hand closed, so it's hidden from everyone (including which face is up) and you can't keep looking at the table while choosing. On "three", everyone places together. Record any late or changed placement. This is the THE COUNCIL palms-commit technique; the rules stay as written.

## Setup

- **Game:** FAVOURS
- **Version:** v0.1 (sim-checked: spoiling priced at 1.00 for 1.00, even-count removal fair; never tabled).
- **Players:** 5.
- **Symbol subset:** signs **1–5 (Moon–Eye)**: the **10** cards pairing two of them. No removal at 5P. 2 cards each, 2 rounds per deal.
- **Components:** the 10-card sub-deck, a bowl of counters (about 20).
- **Seating:** count off clockwise Moon, Leaf, Wave, Flame, Eye. Seat = sign.
- **Session shape:** about 25 minutes.
  1. **Teaching deal, Open hands** (rulebook variant): hands face-up on the table, one deal, not scored. It teaches the resolution once.
  2. **Games 1–3, base rules, two deals each** (4 rounds per game). Talking allowed. Rotate who counts "three".
  3. **Game 4, Silent FAVOURS** (if time allows): the same structure with no talking, as a direct contrast for H1.
- **Why this session:** `next_step` is "check whether the giving is lobbied aloud or computed in silence". The rulebook calls that the falsification test.

## Hypotheses to test

- **H1 — The table lobbies (the falsification test).** *Prediction:* in every talking game, at least two players openly claim a target, warn someone off, or plead ("don't give to Wave, I'm giving to Wave"). The Silent game then feels clearly different. *Falsified if* talking games play as quietly as the Silent one, with everyone silently working out the least-crowded recipient. Per the rulebook: "If it plays in silence, the social premise is wrong and this is an anti-coordination puzzle wearing a party game's clothes." At 5P, record a failure as *provisional* (see above).
- **H2 — There are still real choices at 5P.** Sim: **40%** of cards dealt at 5P carry the holder's own sign, so they have only one legal recipient. *Prediction:* each player feels they made a genuine choice at least once per deal (which card to play this round, or which of two recipients). *Falsified if* players say "there was nothing to decide", or most rounds play themselves.
- **H3 — The obvious heuristic collides.** Sim: "give to whoever has received least" loses to random play (**0.76–0.84×**), because everyone reasons the same way. *Prediction:* at least one round has a visible pile-up on the obvious "quiet" player, and someone remarks on it ("being popular is a curse"). *Falsified if* the obvious play works reliably.
- **H4 — Ties don't spoil the ending.** Sim (two deals): **41%** of games tied at the top, **15%** shared after the tiebreak. *Prediction:* ties are resolved by "most cards received" without argument, and nobody calls a shared win unsatisfying. *Falsified if* a shared win draws visible disappointment or a call to change scoring.
- **H5 — The snub face gets used.** The pressed face of a received card names the person passed over. *Prediction:* someone turns over a received card to see who was snubbed and comments on it, at least once. *Falsified if* nobody ever looks: the theme isn't landing.
- **H6 — One-minute teach.** *Prediction:* after the Open-hands deal, no rules questions in game 1 about who can receive a card or how resolution works. *Falsified if* resolution needs re-explaining.

## What to watch

Handling first:

- **Placement orientation.** A gift is placed **in front of its recipient, showing their sign**. Watch for cards placed showing the wrong face, or in front of the wrong person (seat counting).
- **Simultaneous reveal.** Late hands, changed minds after the count, someone holding back to watch. (Convention above; record breaches.)
- **Refused row.** Refused cards leave the game into a shared overlapping row. Do the givers move them promptly, and does the row stay readable?
- **Reach.** At 5P every recipient should be within arm's reach. Note if anyone needs a passer.
- **Score piles.** Received cards are face-up nameplates. Check scoring (cards plus counters) is a quick count at the end.

Then:

- **Seat-to-sign lookup.** Trivial at 5P, but time any pause before giving spent counting seats. It is the 9P risk in miniature.
- **Spite.** Does anyone deliberately crowd someone else's gift? Spite is priced (1 for 1) in the sim. Note whether it happens and how the table reacts.
- **Length.** A two-deal game should take about 5 minutes. Note whether the table wants another game straight away.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Open claims, warnings and pleas every talking game; Silent feels different | Talking games as quiet as Silent (**provisional fail at 5P**) |
| H2 | Each player names a real choice per deal | "Nothing to decide" |
| H3 | A visible pile-up on the "quiet" player | The obvious play works every time |
| H4 | Tiebreaks accepted; no complaints about a shared win | Disappointment at shared wins |
| H5 | A received card turned over to see the snub | Nobody looks |
| H6 | No resolution questions in game 1 | Resolution re-explained |
| Handling | Gifts placed correctly, all at once | Wrong face, wrong recipient, late placement |

## Teaching plan

- Seat everyone, count off signs aloud, then say the sentence the rulebook asks for: *"Every card in this deck names two of us, and every pair of us is on exactly one card."*
- Explain one round in three lines: choose a card; on three, give it to one of the two people on it, showing their sign; alone = kept, plus a counter for the giver; crowded = all refused.
- Play the **Open-hands** teaching deal and talk through each resolution.
- Explain the commit convention (card pinched to chest) and that talk is free and not binding.
- **Don't** teach strategy (popularity is a curse, read the refused row). H3 tests whether those surface on their own.
- **Watch during teaching:** whether "you can't give to yourself, so own-sign cards are forced" lands first time.

## Record sheet

Per round:

| Game | Deal | Round | Gifts kept | Gifts refused (crowded recipients) | Forced plays | Lobbying heard? (claims / warnings / pleas) | Late or changed placements |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | | | | | |
| 1 | 1 | 2 | | | | | |
| 1 | 2 | 1 | | | | | |
| 1 | 2 | 2 | | | | | |
| 2 | 1 | 1 | | | | | |
| 2 | 1 | 2 | | | | | |
| 2 | 2 | 1 | | | | | |
| 2 | 2 | 2 | | | | | |
| 3 | 1 | 1 | | | | | |
| 3 | 1 | 2 | | | | | |
| 3 | 2 | 1 | | | | | |
| 3 | 2 | 2 | | | | | |

Per game:

| | Moon | Leaf | Wave | Flame | Eye |
|---|---|---|---|---|---|
| Game 1 score (cards + counters) | | | | | |
| Game 2 score | | | | | |
| Game 3 score | | | | | |
| Game 4 (Silent) score | | | | | |

- Ties at the top (games): ____ Still shared after the tiebreak: ____
- Snub faces turned over (who, when): ____
- Silent game vs talking games, in one sentence: ____
- Teach time: ____ Time per game: ____
- Surprises / quotes:

## Out of scope

- **7P** (the `next_step` count) and the 8–9P seat-lookup and reach questions: a later event.
- **Snubs** (counter-free) variant. The sim has 37% of players finishing below zero at 5P; not needed while counters are on hand.
- Point-value changes for ties. Only if H4 fails.
