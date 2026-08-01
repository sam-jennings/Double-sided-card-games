# BRAVADO — Design Analysis

*v0.1, August 2026. Written when the game entered the collection from a standalone draft. Every number below is either an exact enumeration or a floor simulation from [bravado_sim.py](bravado_sim.py); the run output is quoted verbatim in §3. Rules: [BRAVADO_rulebook.md](BRAVADO_rulebook.md).*

**Summary.** BRAVADO clears both hard floors and has a healthy 1.88× skill gap with a genuinely non-obvious optimum. Its deck-necessity is real but thinner than the collection's best. Its *headline mechanic* — the Caller's one word — is worth almost nothing at equilibrium, which is a quantified risk, not a speculation, and the reason the game goes to a table rather than to more desk work. A repair is pre-designed in case the table confirms it.

---

## 1. Hard floors

### 1.1 Physical viability — pass

The [physical-handling](../.kiro/steering/physical-handling.md) checklist, answered explicitly:

| Question | Answer |
|---|---|
| What can each player see? | The active player sees one face of the presented card. Everyone else sees the other. The record row of resolved cards, and every banked streak, are face up and public. |
| What can each player inspect freely? | Every resolved card, both sides, at any time. Nothing is ever squared away. |
| What is supposed to be hidden, and is it? | Exactly one face, of exactly one card, for roughly ten seconds. The active player is forbidden to turn, tilt or touch it — and unlike a fan or a hand, a squared vertical card genuinely shows one face per side. |
| Is any required state buried? | No. This is the structural opposite of the OUROBOROS defect: nothing needed for play sits on a down-face, and the streak is a visible row. |
| Can the table verify legality? | Completely, and within seconds. The announcement in step 2 is audited by the reveal in step 5, and the reveal is public and re-inspectable. |

Memory load is **zero required**. The record row is a public oriented registry in the [FORKED TONGUE / UNPLAYED-PAIR mould](../COLLECTION_OVERVIEW.md), re-readable rather than memorised.

Two physical risks remain, both addressed in the rulebook and both first-table checks rather than design problems:

1. **Presentation geometry.** Prototype stock backlit by a lamp or window can read through, and the seats *beside* the active player have the shallowest angle on the far face — they need to see it, especially under the *Crowd* variant. The rulebook now requires the card squared, vertical, and angled away from light, with an explicit pre-game check.
2. **Well leakage.** The Caller may see what they draw at no cost — they are entitled to know the card. The active player must not, so the well is kept tilted away or the draw is made below the table line.

### 1.2 Deck necessity — pass, but qualified, and worth stating precisely

This is where the nearest relative in the project died, so it deserves care. [VERDICT](../Project/GATEWAY_GAME_CONCEPTS.md) §9 was a higher/lower betting game on the same `(9−S)/8` maths, refuted in §11 on four counts. BRAVADO's position against each:

| VERDICT's fatal flaw | BRAVADO |
|---|---|
| §11.1 Scoring parasitic on disagreement — everyone scores **0.00** at equilibrium | Doesn't apply. You score your own banked streak against the table's best; a round always has a winner. |
| §11.2 Optimal play is "randomise with probability (9−S)/8" — a die roll in a decision's clothes | Doesn't apply to the *game*, though it does apply to the advice (see §4). The live decision is **bank or push**, and it is neither random nor obvious: §3 shows banking at three is the worst option available. |
| §11.3 **Plays identically on a normal deck** | Partially applies. See below — this is the honest weak point. |
| §11.4 Players never touch cards | Doesn't apply. The Caller draws, presents and reveals, and the role rotates every single card, so everyone handles the deck. |

**On §11.3, the objection with teeth.** A normal 52-card deck can approximate the procedure: turn one card face up as the baseline, deal a second face down, let a peeker advise, call higher or lower. So the *arithmetic* of BRAVADO is close to deck-agnostic, and it would be dishonest to claim otherwise.

What does not survive the translation:

- **It is one card, not two.** The question and its answer are physically joined — the reveal is a flip of the same object, not the turning of a separate card. That is the deck's signature image and the game's whole staging.
- **The asymmetric split is free and simultaneous.** One card serves two audiences at once with no screen, no peeking and no trust. On a backed deck the "hidden" card shows nothing to anyone, so the active player has no baseline pip, and the entire odds structure — the thing that makes the decision interesting rather than blind — disappears.
- **Ties are structurally impossible**, because no card pairs a sign with itself. That is a property of K₉, not a patched rule. A normal deck needs an explicit tie clause.
- **The public record is a pair-registry**, not a rank count. Its information content is exact rather than statistical (see §5 for how little that turns out to be worth here).

Verdict: a genuine pass, but BRAVADO uses the deck as **staging and structure** rather than as a puzzle. It is nearer TURNCOAT's "invisible infrastructure" end of [design-principles](../.kiro/steering/design-principles.md) Layer 2 than DOWRY's or CROSSROADS's, and it should not be sold as a deep exploitation of K₉.

---

## 2. Exact deck facts

Enumerated over all 36 cards × 2 orientations, with the assertions in `bravado_sim.py` §1 failing the run if any of them breaks:

- **The pip you are shown is uniform.** Each sign occupies exactly 8 of the 72 face-slots, so P(shown any given sign) = 8/72 = 1/9.
- **The printed odds table is exact.** For every sign, its eight partners are every other sign exactly once, so P(higher | shown S) = (9 − S)/8 — confirmed by enumeration, not just by formula.

| You see | Moon | Leaf | Wave | Flame | **Eye** | Mask | Key | Star | Crown |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P(higher) | 100% | 87.5% | 75% | 62.5% | **50%** | 37.5% | 25% | 12.5% | 0% |

- **Ignoring the Caller entirely and calling the favourite side of the pip scores 77.78% per card.** This is the number every other strategy has to beat, and it is high. It matters more than it first appears: see §4.
- **Card supply.** A run resolves at most six cards, so the worst case is 18 / 24 / 30 / **36** cards at 3 / 4 / 5 / 6 players. At six players that is *exactly* the deck with zero slack, which is why the rulebook carries a well-empty clause — even though the sim never once hit it (§3).

---

## 3. Floor simulation

40,000 rounds per configuration. The Caller's advice is modelled as **noise**, which is its equilibrium content (§4). Seats rotate in every skill measurement so that skill and seat order are never confounded.

```
3a. Bank versus push. One bot commits to depth k; three push to 4.
     k   avg banked streak   round-win share (fair 25.00%)
     1             0.779   21.21%
     2             1.218   18.26%
     3             1.410   15.65%
     4             1.428   24.87%
     5             1.402   32.58%
     6             1.271   25.91%

3b. Seat fairness -- identical bots (pip, chase the leader).
    3P  s1 44.39%  s2 24.72%  s3 30.90%   spread 19.67pp (fair 33.33%)
    4P  s1 29.08%  s2 18.70%  s3 24.01%  s4 28.21%   spread 10.38pp (fair 25.00%)
    5P  s1 19.14%  s2 13.85%  s3 18.75%  s4 22.40%  s5 25.86%   spread 12.02pp (fair 20.00%)
    6P  s1 12.63%  s2 10.53%  s3 14.01%  s4 17.84%  s5 21.41%  s6 23.59%   spread 13.06pp (fair 16.67%)

3c. Skill gap -- 4P, seats rotated.
    pip + chase                  vs 3x coin + push-3    47.05%  = 1.88x fair
    count + chase                vs 3x coin + push-3    47.66%  = 1.91x fair
    count + chase                vs 3x pip + chase      26.09%  = 1.04x fair
    always follow the Caller     vs 3x pip + chase       8.88%  = 0.35x fair
    always contradict the Caller vs 3x pip + chase       8.73%  = 0.35x fair

3e. Termination and supply (pip + chase, all seats).
    3P  max cards used 15/36   box emptied 0.000% of rounds   busts/round 2.01
    4P  max cards used 21/36   box emptied 0.000% of rounds   busts/round 2.72
    5P  max cards used 27/36   box emptied 0.000% of rounds   busts/round 3.45
    6P  max cards used 33/36   box emptied 0.000% of rounds   busts/round 4.19
```

**Termination is certified.** No configuration ever emptied the well across 160,000 rounds, and the maximum draw was 33 of 36 at six players. Roughly 2–4 players bust per round, so the round always resolves.

**The skill gap is healthy: 1.88×**, comfortably above the collection's ~1.5× bar, and it comes almost entirely from *stopping* well rather than from calling well.

**Neither pure message-strategy works.** Always following the Caller and always contradicting them both collapse to 0.35× fair share. The design's claim that a Caller cannot simply lie every time holds — but the reason is not that the liar gets punished, it is that *any* fixed response to the message is worse than ignoring it (§4).

**Bank-or-push is a real decision with a non-obvious answer, and this is the strongest finding.** The curve is not monotonic. Average banked streak peaks at four, but *round wins* peak at **five** — because matching the leader loses the tie, so you must beat them outright. And **three is the worst place to stop in the game** (15.65%, below even the trivial bank-at-one line at 21.21%): a banked three is a target for every seat behind you, and it costs you two-thirds of the pushes that would have made it a winner. The source draft asked whether players are "genuinely tempted to push from three to four and four to five." They should be, emphatically, and the fact that the tempting stopping point is the losing one is exactly the kind of discovery a push-your-luck game needs.

**Seat spread is 10–13pp at 4–6 players and 19.7pp at three**, from two opposing biases: *first to bank takes ties* favours early seats (seat 1 wins 44.39% at 3P against a fair 33.33%), while knowing the benchmark favours late seats (seat 6 wins 23.59% at 6P against a fair 16.67%). Seat 2 is consistently the worst chair. The rotating starting player and the race to three round wins wash this out over a match, but **a single round is not fair**, and the short game must keep the rotation for that reason. Worth watching, not worth fixing before evidence.

---

## 4. The central risk, quantified: the Caller's word may be worth nothing

The Caller knows the answer, has no stake in being believed, and pays nothing for lying. That is textbook **adversarial cheap talk**, whose equilibrium is babbling: the message carries no information, and the active player should ignore it and play the pip.

The sim measures the exact ceiling — the per-card accuracy of a player who knows the Caller tells the truth with probability *t* and plays the Bayesian posterior:

```
     t   accuracy   vs. ignoring the Caller
  0.00   100.00%   1.286x
  0.25    83.33%   1.071x
  0.40    78.89%   1.014x
  0.50    77.78%   1.000x   <- no read: the advice is worth nothing
  0.60    78.89%   1.014x
  0.75    83.33%   1.071x
  1.00   100.00%   1.286x
```

Read this honestly. The 77.78% baseline is *high*, so the advice has very little room to add value. A player who can tell when a Caller is lying **65% of the time** — which is a substantial read on a human being — gains **1.029×**. To reach even 1.07× you need to be right about their honesty three times in four.

So the game's headline mechanic, the thing the pitch is built on, is a **1–3% edge** under any plausible degree of human readability. Everything interesting about it is theatre: the pause, the audacity, the groan when the truth was sitting there in plain sight. That may well be enough — plenty of loved social games are theoretically babbling, and the [design-principles](../.kiro/steering/design-principles.md) instruction is to design to the table rather than to the rubric. But it must be said plainly rather than discovered later, and it sets the falsification test in §7.

**The pre-designed repair: *Accomplice*.** The fix is to give the Caller mixed motives, because partially aligned interests are what make cheap talk informative. Under *Accomplice*, when the active player follows the Caller's word and is correct, the Caller earns a favour (three favours buy one push past the cap). The Caller now sometimes *wants* to be trusted, so truth becomes a live strategy, so the message carries real information, so reading it becomes worth something. This is untested and deliberately kept out of the base game — but it is written into the rulebook so a session that finds the advice inert can switch to it immediately instead of ending inconclusively.

---

## 5. The counting layer is much thinner than it looks

The source draft claimed the deck "becomes increasingly readable" and that "players who pay attention gradually gain real information." Measured over every card resolved in a six-player round — the deepest case in the game — that claim is technically true and practically negligible:

```
    cards observed                       744,105
    avg partners already eliminated      1.85 of 8
    calls where counting differs from pip 11.58%
    accuracy, pip only                   77.42%
    accuracy, pip + registry             78.79%
```

**+1.4 percentage points.** The registry changes your call about one card in nine and is worth 1.04× fair share in round wins (§3c). The reason is structural: a round resolves only 15–33 cards, and the partners of any *particular* sign are eliminated at a trickle — 1.85 of 8 on average.

This is a much weaker counting layer than ICARUS's, where the Fallen field genuinely inverts the naive odds. The rulebook is right to keep it optional and right not to advertise it; **the corrected claim is that the record row exists so nothing has to be memorised, not so that counting wins games.**

---

## 6. Collection fit

**Distinctness.** Three neighbours, all clearly separated:

- **ICARUS** (2–4, push-your-luck) is *solitary and countable* — you flip your own tower and the maths is the whole opponent. BRAVADO is *social and advised* — the maths is a baseline and a rival's word is the drama. Different player counts, different genres of tension, and the two read as a deliberate pair rather than a duplication.
- **FACE VALUE** (2, bluffing duel) is a heads-up betting game about your *own* hidden pip, with folding and stake-raising. BRAVADO has no hand, no stakes and no fold.
- **FORKED TONGUE** (3–6, bluffing) is the closest on player count, but its lie is a *claim about your own card* that a challenge can punish. BRAVADO's lie is *advice about someone else's card* and is never punished — which is precisely the asymmetry §4 identifies as the risk.

**Gap-filling.** A 3–6 player, 15–25 minute, Light social game. That slot currently holds WILDFIRE (~10 min, and per [GATEWAY_GAME_CONCEPTS.md](../Project/GATEWAY_GAME_CONCEPTS.md) §13 a 3–5 game in practice), FORKED TONGUE and THE COUNCIL (both unvetted). BRAVADO is the only *vetted, table-ready* game in that space, and unlike WILDFIRE it genuinely runs at six.

**It closes the flagged rank-teaching gap.** §13.5 of the gateway evaluation records the collection's "most actionable open gap": WILDFIRE, the gateway, never reads a pip, and a player carried a sign-equals-rank misunderstanding through an entire GLEAN game as a result — while rank is load-bearing in BLIGHT, GLEAN, FACE VALUE, DOWRY and ICARUS. BRAVADO cannot be played at all without the rank canon; the pip *is* the odds table. It is a strong candidate to sit before the rank-sensitive games in the learning order, pending its first test.

**Component consequence worth noting.** BRAVADO is the **second** game to need [DECK_CONVENTIONS](../Project/Deck/DECK_CONVENTIONS.md) rung 4, the box base as an opaque draw well. The [house-kit decision](../Project/Decisions/HOUSE_KIT_DECISION_2026-07.md) explicitly noted that the container was "only load-bearing for JANUS," accepted because the box ships regardless. A second user strengthens that decision at zero cost and reinforces the two-piece-box production note.

**Naming** ([naming.md](../.kiro/steering/naming.md) checklist): no shared key word with any existing title; B held only BLIGHT, and *blight* and *bravado* are unmistakable read aloud (one syllable versus three, no shared sound); it does not bunch under the crowded T or S initials; a stranger correctly guesses "the daring, bluffing one"; and the word is common, so the obscure-word rent clause does not apply. Passes.

---

## 7. What the table has to decide

Ranked. The first question outranks all the others combined, and no further simulation can touch any of them.

1. **Does the room become invested when someone risks a strong streak?** The source draft's own gate, and correct: if the table doesn't lean in, the design lacks the emotional response a push-your-luck game needs and should be abandoned rather than mathematically repaired.
2. **Does the Caller's word carry any read at all?** §4 puts the honest ceiling at 1–3% for a strong human read. Watch whether players actually try to read the Caller, or quietly settle into playing the pip. If they settle, switch to *Accomplice* in the same session and compare.
3. **Is banking at three the trap the sim says it is, and does the table feel it?** The push-to-five optimum is the game's real strategic content. If players find it, there's a discovery curve; if the tie rule reads as arbitrary, the pressure structure isn't landing.
4. **Does the held card hold up physically?** Does the active player ever glimpse the far face; can the seats beside them read it; does the well leak.
5. **Does rotating the Caller add variety or cut the duel short?** The draft raises this as a genuine tension and it can only be answered by comparison — try a round of *Personal Challenge* against the rotating default.
6. **Does the seat spread show up over a three-win match**, or does the rotating start absorb it as §3b predicts?

**Verdict framing for the report.** Per [playtesting.md](../.kiro/steering/playtesting.md): *iterate → Proven* if the room lights up and only polish remains; *iterate → Ready to test* if the advice needs the *Accomplice* switch but the game plainly works; *iterate → In development* if the higher/lower call turns out to be too thin to carry 15–25 minutes; *cut → Shelved* if question 1 fails, since that is the one thing no rule change repairs.

---

*Simulation and enumeration: [bravado_sim.py](bravado_sim.py) (Python 3.13, no dependencies). Original standalone draft: [BRAVADO_source.docx](BRAVADO_source.docx).*
