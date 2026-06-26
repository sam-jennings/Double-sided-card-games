# JANUS — Playtest Plan 01

*Pairs with the report `JANUS_playtest_01.md` (write after the session).*

## Setup under test

- **Game / version:** JANUS v1.1 (untested at the table — this is the first table test).
- **Mode:** **Apprentice** — 3 gates, 4 omens (2 in play + 2 reserve as written), 3 strikes.
- **Player count:** 3 players (fans of 4 each). If only 2 are available, run 2P (fans of 6); avoid 4P for a first session — smaller fans keep the deduction legible.
- **Symbol subset:** the 7-symbol sub-deck (remove every card showing Star (8) or Crown (9) on either face → 21 cards). Validate gates per the setup cap: no symbol on ≥4 keystones; reshuffle if violated.
- **Why Apprentice:** the rulebook's own teaching ramp, and table-talk is fully open (still never describe a visible face), which isolates the *omen and deduction* learning from the harder communication discipline.

## Hypotheses (framed as falsifiable predictions)

1. **Hint grammar is graspable in one game.** *Prediction:* by the second or third omen reading, players read and act on a "these show X to us" pointing without re-explanation, and correctly infer that *un*-pointed cards are now known *not* to be X. *Refuted if* players still need the omen mechanic re-explained late, or routinely miss the negative inference.
2. **The omen economy paces rather than starves.** *Prediction:* the team is never hard-stuck (the archive-as-pressure-valve keeps it moving), but omens feel scarce enough that spending one is a real decision — expect roughly 3–6 readings across an Apprentice game, and at least one moment of "can we afford this?". *Refuted if* omens feel irrelevant (always plenty) or the team grinds to repeated archive-dumping just to function.
3. **Locking a gate produces a genuine deduction payoff.** *Prediction:* at least one lock is achieved by reasoning/memory about a buried face rather than a coin-flip "your face" gamble, and it lands as a satisfying team moment. *Refuted if* every lock is either a safe "my face" placement only, or a blind gamble — i.e. the deduction layer never bites.
4. **The game ends cleanly within range.** *Prediction:* one Apprentice game runs ~15–20 min and resolves as a clear win or loss (3 strikes / deck-out), not a confusing end-state. *Refuted if* the final-round timing causes argument, or the game drags well past 25 min.

## What to watch (handling + the JANUS-specific risks)

- **The sacred rule (no self-inspection).** This is JANUS's exceptional handling bet (`physical-handling.md`). Watch for accidental outward-face glimpses when picking up the fan, refilling, or fanning cards. **Count every accidental peek** — frequency and how disruptive. If it's constant, the whole concealment model is in question.
- **The communication wall.** The single biggest fragility. Watch for *quarterbacking* and leak-by-tone: wincing, hesitating, "are you sure?", steering a teammate's hand. Note every illegal-leak incident, whether the table caught it themselves, and whether it changed an outcome.
- **Refill / deal handling.** Does the "slide flat, outward face to the table, lift seeing only your side" protocol actually work physically with real cards, or do people fumble and flash a face?
- **Lock-check & returned pillars.** Is flipping both pillars to check the buried match clean? Does returning mismatched pillars to fans (v1.1 rule) get handled correctly, or do players try to archive them?
- **Comprehension.** Which rules needed re-explaining; where the rulebook was silent. Especially: "my face" vs "your face", and that a failed lock returns cards (no refill) vs a fumble (archive).
- **Pacing & downtime.** Turn length and dead time while one player computes deductions for the table.
- **Fun.** Where the table leaned in or agonised — particularly around omen spends and "your face" gambles.

## Observable success / failure signals

| | Looks like success | Looks like failure |
|---|---|---|
| Hint grammar | omen readings flow without re-teaching; negative inference used | readings keep needing explanation; pointing misread |
| Omen economy | spends feel weighty; no hard stalls | omens trivial *or* constant forced archive-dumps |
| Deduction payoff | ≥1 reasoned lock; audible "ahh" moment | all locks safe-only or blind gambles |
| Handling | ≤1–2 accidental peeks, non-disruptive | frequent peeks; concealment breaks down |
| Communication | leaks rare and self-policed | persistent quarterbacking; tone-leaks decide plays |
| Termination | clean win/loss, ~15–20 min | end-timing argument; drags past ~25 min |

## Teaching plan

Teachability is itself under test — teach it cold and watch where it snags.

1. **The hook first:** "Every card has two faces. You see your side; the table sees the other. You may *never* look at your own outward face. That asymmetry is the whole game."
2. **Goal:** "Together we lock 3 gates. A gate is a public pair; lock it by adding two pillars whose *buried* faces match each other — forming a symbol triangle."
3. **The one sacred rule**, demonstrated: pick up a fan without turning it; show how the table sees the backs.
4. **The three actions**, in this order: raise a pillar ("my face" = safe, "your face" = a bet), read an omen (the only legal channel for hidden-face info — demo one pointing), consult the archive (always legal, pays an omen, breaks ties).
5. **The communication wall:** give one legal example ("by my count every Moon foundation except Crown is dead") and one illegal ("don't play that one"). State the rule of thumb: *if the sentence would change meaning based on a face only you can see, don't say it — pay an omen.*
6. Defer all strategy notes until after game one.

**Watch during teaching:** does the "my face / your face" distinction land first try? Do players instinctively try to peek or quarterback before the rule sinks in? Time-to-first-action is a teachability signal.

## After the session

Write `JANUS_playtest_01.md`: setup, each hypothesis (confirmed / refuted / open), bugs categorised and severity-ranked (handling bugs first), concrete rule-change candidates each tied to an observation, and a verdict (iterate / park / cut). Per the rulebook, the live tuning candidates are starting omens (4), strike count (3), and fan sizes — tie any change to what you actually saw.
