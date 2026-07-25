# WILDFIRE — where the skill went, and how to get it back

*July 2026. Diagnosis of the "felt reactive" finding from [WILDFIRE_playtest_01.md](WILDFIRE_playtest_01.md), and a simulated fix. Simulation: [wildfire_decision_sim.py](wildfire_decision_sim.py). Companion to [WILDFIRE_design_analysis.md](WILDFIRE_design_analysis.md), which tuned the game's balance; this document is about its **decisions**.*

---

## 1. The contradiction

The v1.1 simulation measured a healthy **1.5–1.8× skill edge**. The first table test recorded the opposite:

> *"players did not feel there was much skill involved. The game felt reactive ('play whatever matches') rather than strategic."*

Both are true. This document explains how, because the explanation is a number and the number points straight at the fix.

## 2. Model validation

Before trusting any new metric, the model was checked against the published figures in `WILDFIRE_design_analysis.md` §3:

| Config | This model | Published |
|---|--:|--:|
| 3P chain 2 | 13.9 turns/player, 0% stalls | 11.1, 0% |
| 4P chain 2 | 10.3, 0% | 9.4, 0% |
| 5P chain 2 | 8.2, 0% | 7.9, 0% |
| 6P chain 2 | 6.5, 0% | 6.8, 0% |
| 3P chain 1 | 65.3 turns/player, 4% stalls | 81, 24% |

Close on every chain-2 configuration, and it reproduces the qualitative chain-1 result (a chainless game barely terminates). The random bot here is not identical to the published one, so treat the figures as faithful rather than exact.

## 3. The diagnosis — seven turns in ten contain no decision

A turn only *feels* like a decision if you have more than one legal card. It only *is* one if those cards lead somewhere different.

| Players | Deal | Avg legal plays | **No play — just draw 2** | **Exactly 1 legal card** | A real choice | Choice visibly mattered |
|--:|--:|--:|--:|--:|--:|--:|
| 3 | 9 | 1.11 | **34%** | **35%** | 31% | 14% |
| 4 | 7 | 1.04 | **35%** | **36%** | 29% | 14% |
| 5 | 6 | 1.00 | **36%** | **37%** | 27% | 14% |
| 6 | 5 | 0.94 | **38%** | **38%** | 24% | 13% |

**On roughly 70% of turns the player has no decision at all** — a third of the time they cannot play and simply draw two cards, and another third they hold exactly one card that fits. Of the ~28% of turns where a choice exists, only about half change anything the player can see, so **your choice visibly matters on about one turn in seven**.

The arithmetic behind it: a card carries 2 of the 9 signs, so any given card matches the target with probability 8/36 = 2/9. With a hand of 6, the expected number of legal plays is 1.3, and the chance of none is over a third.

**This is not a balance problem — the balance is fine.** It is a *decision-density* problem, and no amount of retuning the chain limit or refusal cost touches it.

### Why the sim's 1.5–1.8× edge is invisible at the table

The published skilled bot counts every face in the pile history, prefers exit signs the table is poorest in, and preserves pairs for guaranteed chains. Every one of those advantages is **delayed, diffuse and unverifiable**: you feel it several turns later, spread across all opponents, with no way to attribute it. A bot with perfect recall banks it. A human at a party cannot even perceive it. The same explains the refuted chaining hypothesis — chaining's cost (fragmenting your hand) is invisible, so shedding two cards is always obviously right.

## 4. The recommendation: two piles, and drop chaining

**Two changes, and one of them deletes a rule.**

1. Flip **two** cards to the middle instead of one. Both are live targets. Play a card matching **either** target onto that pile and turn it over, as before. Only if you can match neither do you draw two.
2. **No chaining.** One card per turn.

Teaching cost is *negative* — the rulebook gets shorter.

### Why the two changes belong together

`WILDFIRE_design_analysis.md` §3 established that chains are "the game's exhaust valve": at one pile, removing chaining stalled 24% of games, because refusals pump two cards into a hand and only multi-card turns shed fast enough to outrun the pump.

**Two piles removes the need for the valve.** Refusals fall from 34% of turns to 17%, so the pump is mostly switched off — and chaining becomes optional rather than load-bearing:

| Config | Stalls | Turns/player (3P) |
|---|--:|--:|
| 1 pile, chain 2 (shipped) | 0% | 13.7 |
| 1 pile, chain 1 | 1% | 66.7 — glacial |
| 2 piles, chain 2 | 0% | 6.6 — too fast |
| **2 piles, chain 1** | **0%** | **14.1** |

Better still, the two changes cancel each other's side-effects. Two piles alone halves the game (6.6 turns/player against 13.7); dropping chaining restores it almost exactly to the shipped pacing. **You keep the doubled decision density and lose nothing.**

### Everything gets better at once

| | Shipped | **Two piles, no chaining** |
|---|--:|--:|
| Avg legal plays per turn | 1.11 | **2.06** |
| Turns with no play (just draw 2) | 34% | **17%** |
| Turns offering a real choice | 31% | **59%** |
| Skill lift, 3P (fair share 33.3%) | 39.2% → 1.18× | **50.2% → 1.51×** |
| Skill lift, 4P (fair share 25.0%) | 28.1% → 1.12× | **37.1% → 1.48×** |
| Skill lift, 6P (fair share 16.7%) | — | **25.5% → 1.53×** |
| Turns per player (3P) | 13.7 | 14.1 |
| Stalls | 0% | **0%** |
| Rules to teach | chain limit | *one fewer* |

Strictly better on every axis, at the same length, with less to explain. The 1.48–1.53× skill lift also clears the collection's ~1.5× healthy bar — and unlike the published 1.5–1.8×, it is now attached to a choice the player actually *has* on 59% of turns rather than 31%.

### The gate

| Test | Result |
|---|---|
| Would the procedure change on a normal deck? | **No — it couldn't run at all.** The played card's *other* face becoming the next target is untouched. |
| Do players' hands touch cards? | Yes. |
| Does an obvious answer appear immediately? | No — you weigh two targets and which one you leave. Residual risk that a first-time table still plays whatever fits; that's the table question. |
| If everyone plays well, does anything still happen? | Yes — 0% stalls, skilled play pays 1.5×. |

### Honest limits

1. **Visibility is still unsolved.** "Choice visibly mattered" stays ~15%. More options don't make blocking easier, so the consequence of a good play remains delayed and diffuse. §5 is about this.
2. **Untested at a table**, and the entire point of this document is that a table found something the simulation missed.

## 5. Tested and rejected: the mirror rule

*Sam's proposal (July 2026): if your play leaves the **same sign showing on both piles**, the next player misses their go.*

The intent is right — immediate, visible, aimed at a named person — and it is **profoundly deck-native**: if the piles show X and Y, the only card in the whole deck that can mirror them is the X–Y card, and there is exactly one. It could not exist on any other deck. The rule also got a jam-clearing repair, since two identical targets would otherwise halve everyone's options: the penalised player flips a pile. That repair works, holding dead turns at 17% rather than the 25% the raw rule produced.

**A mirror is a fact lying face up on the table in front of the person who just played it.** Everyone can see it; the cards cannot tell intent from accident; it always fires. Testing has to model it as mandatory, and the analysis has to separate two questions that are easy to conflate:

- **A vs B — does the *rule* dilute skill?** Same bot, rule off then on.
- **B vs C — is *mirroring* a skill worth having?** Rule on, bot ignoring mirrors vs bot chasing them.

**15,000 games per arm, matched seeds, Wilson 95% intervals** on the skilled seat:

| | 3P (fair 33.3%) | 4P (fair 25.0%) | 6P (fair 16.7%) |
|---|--:|--:|--:|
| **A** rule off, cruel play | **48.2% [47.4–49.0] — 1.45×** | **36.8% [36.0–37.5] — 1.47×** | **25.4% [24.7–26.1] — 1.52×** |
| **B** rule on, cruel play (ignores mirrors) | 44.5% [43.7–45.3] — 1.33× | 32.1% [31.4–32.9] — 1.29× | 23.8% [23.1–24.5] — 1.43× |
| **C** rule on, actively seeking mirrors | 45.3% [44.5–46.1] — 1.36× | 32.4% [31.6–33.1] — 1.29× | 23.0% [22.3–23.7] — 1.38× |
| **D** rule on as proposed (miss a turn), seeking | 43.1% [42.3–43.9] — 1.29× | 31.2% [30.4–31.9] — 1.25× | 22.6% [21.9–23.2] — 1.35× |

**A vs B: the rule measurably dilutes skill at every player count**, intervals clear at 3P and 4P. Two piles land on the same sign **by chance about 1 turn in 9**, so the penalty is mostly an accident tax landing on whoever happens to be sitting next. That variance washes out the positional play the two-pile change was introduced to create.

**B vs C: chasing mirrors is worth essentially nothing** — +0.8 points at 3P, +0.3 at 4P, and *negative* at 6P. The X–Y key card is in hand only 7–11% of turns, and playing it forfeits the strangle play, so the trade nets to zero.

**Recommendation: two piles, no chaining, no mirror rule.**

The X–Y key card remains a lovely piece of deck structure and is worth keeping on file — but for a game where *making the connection is the goal*, not a detour from it.

> ### Correction notice
>
> An earlier version of this section reported the mirror rule as skill-neutral or better, on the strength of a variant where it fired "only when the player calls it aloud." That variant was a bug in the simulation, not a rule: the `deliberate` flag was set only inside the mirror-seeking bot's branch, so the test seat's mirrors fired and the opponents' never did — a privilege granted to one player. Sam identified the flaw on sight: *the cards can't tell whether you mirrored on purpose, and you'll see it either way the moment you put the card down.* There is no honest version of the called variant, so it has been removed from the simulation rather than fixed. The table above supersedes it.

## 6. Suggested next step

Run one 4P session on **two piles, no chaining, shipped deal sizes**, and watch one thing: does anyone ever choose a card *because of the target it leaves*, unprompted? If yes, decision density was the whole problem and this is done. If no, the problem is visibility, and the next candidate has to make the consequence land on a named person without costing the player their best play — which §5 shows is harder than it looks.

## 7. A note on how this document was produced

Three of the findings above were wrong before they were right, and the pattern is worth recording because it will recur:

| Claim | What was wrong | How it was caught |
|---|---|---|
| Two piles roughly triples the skill payoff | The first loop double-drew and ran games to 215 turns against a published 33 | Validating the model against `WILDFIRE_design_analysis.md` §3 before trusting it |
| Mirror rule rejected in all eight configurations | Underpowered arms; differences were inside the noise | Re-running with 12,000 games and confidence intervals |
| Mirror rule is skill-neutral if called aloud | The "called" arm fired one seat's mirrors and never the opponents' | Sam reading the *rule*, not the numbers, and seeing it was unimplementable |

The common factor: a simulation will answer whatever question its code actually encodes, which is not always the question in the design. **Before quoting a figure, state the rule in plain language and check that a person could execute it at a table.** The third row was invisible to every statistical check available and obvious in one sentence of English.

*The game record's `next_step` currently reads "Retest whether experienced players ever choose not to chain." On this evidence that question is moot — the recommendation is to delete chaining — and the field should be replaced once the above has seen a table.*
