# THE COUNCIL — design analysis (vetting pass, November 2026)

*State: **Untested** (promoted from design work to playable after this pass) · physically unplayed. Rules: [COUNCIL_rulebook.md](COUNCIL_rulebook.md) v1.0a. Sim: [council_sim.py](council_sim.py).*

## 1. Read-through against the physical-handling checklist

| Question | v1.0 answer | Problem? | v1.0a fix |
|---|---|---|---|
| What can each player see? | Tabled issue stacks, committed cards' shown faces, the discard row, the issue deck's top face | **Yes.** The rulebook says three times that everyone can read a committed card's alternative (*"everyone can read both options off your card"*, *"the threat was public the moment you slapped it down"*, *"your treachery is printed on your card"*). But a committed card lies with its other face pressed to the table, so nobody can see it. | **Show your alternative:** after the slap, each player tips their card up to show its other face, then lays it back as committed, and may be asked again. This makes the written intent physically true; it adds no new decision. |
| What can each player inspect freely? | Own hand; tabled issues; discard row | Hands were "dealt", and a held fan shows its outer faces to the table (F8) | Self-deal (house convention C2, rung 2, already listed for THE COUNCIL); hold the hand tilted to the chest |
| What is supposed to be hidden, and is it? | Your hand; which card and face you commit | Hidden by the hand convention and the palms commit | — |
| Is required state visible? | Stack value = sum of pips | **Yes.** "Stack any new issue on other tabled cards" reads as a squared pile, which shows only its top card, so the stack's size is hidden (C3) | Lay stacks as an overlapping cascade; the value is stated as the pip sum |
| Can the table verify legality without memory? | Supporters, deadlocks and lone winners are all on the table | — | — |

Other gaps found:

- **Which face becomes the issue?** "Flip 3 cards from the issue deck" didn't say whether the issue is the face that was showing on the deck or the face underneath. **v1.0a takes the literal reading of "flip":** turn the card over, and the underside is the issue. This keeps the FAQ's "half-preview" true: you see the partner, not the issue. *Designer may prefer the opposite (the showing face is the issue, so the next issue is fully previewed). It doesn't change balance, because faces are random either way.*
- **Final tie.** The tiebreak list had no last line. v1.0a: still tied, shared.
- **Rank canon.** C7 lists THE COUNCIL as a rank-sensitive game; the callout is now printed in Components.

No issue-stack rule was ambiguous beyond the two above. Same-symbol issues tabled in one round merge (FAQ), rolled-over stacks stay open, and deadlocked or unsupported stacks persist to the end and then rot.

## 2. Floor simulation

**Questions:** does it terminate; does skilled card play beat random without any negotiation; are seats and turncoat order fair; how often do stacks roll over (a recorded playtest question).

**Method:** v1.0a rules. **RandomBot**: random card and face, flips 30% of the time. **SkilledBot**: commits the card and face whose stack is biggest after discounting how many rivals could reach it by either face. In the turncoat phase it compares its two faces, simulating later seats as greedy one-step players. 5,000 games per row, 3 tables × 4 player counts = 60,000 games, seed 1. Skilled seat rotates independently of the first Speaker. Talk is not modelled.

```
 P table     S win x fair  S pts  R pts carries/rd rollover stacks/rd flips/g rotted pips  seat wins (0 = first Speaker)
 3 random      -      -      -     9.8       1.11               3.16     3.6        30.4  33% 34% 33%
 3 skilled     -      -    12.7     -        1.62               1.99     0.9        21.9  33% 33% 34%
 3 mixed     69.3%   2.08   18.4    8.2       1.36               2.57     2.7        25.2  33% 33% 34%
 4 random      -      -      -     8.5       1.28               2.81     4.8        25.9  24% 25% 25% 26%
 4 skilled     -      -    10.1     -        1.65               2.02     1.1        19.8  25% 24% 25% 26%
 4 mixed     58.6%   2.34   16.6    7.1       1.47               2.36     3.9        22.1  26% 25% 24% 25%
 5 random      -      -      -     7.4       1.40               2.61     5.9        23.3  20% 20% 20% 20% 20%
 5 skilled     -      -     8.0     -        1.59               2.16     1.0        19.6  19% 20% 21% 20% 20%
 5 mixed     50.7%   2.53   15.0    6.3       1.56               2.21     5.1        19.8  21% 20% 20% 20% 19%
 6 random      -      -      -     6.4       1.49               2.43     7.3        21.2  17% 17% 17% 16% 17% 17%
 6 skilled     -      -     6.6     -        1.52               2.33     0.9        20.8  16% 16% 17% 18% 17% 16%
 6 mixed     44.3%   2.66   13.4    5.6       1.62               2.15     6.3        18.5  17% 16% 17% 17% 17% 16%
```

*"rollover stacks/rd" = open stacks left on the table after each round's resolution.*

## 3. Health checks

| Check | Result |
|---|---|
| Termination | **Structural:** exactly 4 rounds. Cannot stall. |
| Skill gap | **Healthy:** 2.1–2.7× fair from card play alone, before any negotiation. |
| Seat / flip-order fairness | **Flat:** within ±2 points at every count, including 5–6P, where the Speaker doesn't reach every seat in 4 rounds. For the bots, later flipping doesn't buy a measurable edge. Humans who read the table may get more from it, which is the playtest question. |
| Rollover | **Frequent:** about 2–3 open stacks after each round; skilled tables carry ~1.6 stacks a round and leave ~20 pips to rot (roughly a third of the ~60 issue pips). Deadlocks matter, as intended. Whether a third rotting feels wasteful is a table question. |
| 3P collusion | Not modelled (no talk). Skilled 3P tables carry only 1.62 of the ~3.6 open stacks per round, so the "everyone takes one" line isn't arising by itself, but deliberate collusion needs a table. |

## 4. Changes adopted

v1.0 → v1.0a: the handling clarifications in §1. No mechanic was added or retuned; the sim shows no balance problem to tune.

## 5. Caveats for the first table

- Everything that makes the game the game is talk: promises, lies, threats. The sim says only that the card skeleton is sound.
- Watch whether **show your alternative** feels natural, and whether players ever forget a rival's alternative (they may ask again).
- Watch kingmaking at 5–6P and whether rotted stacks feel like waste.
