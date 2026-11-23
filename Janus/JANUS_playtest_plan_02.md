# JANUS — Playtest Plan 02

*Pairs with the forthcoming `JANUS_playtest_02.md`. Written per [playtesting.md](../.kiro/steering/playtesting.md). Hypotheses come from the "Next session must answer" list in [JANUS_playtest_01.md](JANUS_playtest_01.md), the known-issue banner at the top of [JANUS_rulebook.md](JANUS_rulebook.md), and open tension T1 in [DECK_CONVENTIONS.md](../Project/Deck/DECK_CONVENTIONS.md). The physical checks follow [physical-handling.md](../.kiro/steering/physical-handling.md).*

## Open before the session

- **The concealment model is still unresolved.** The rulebook's deal and refill need a "face-down stack". A backless deck can't make one: the top card always shows a face to the whole table (F7). A card dealt flat onto the table also shows its face to everyone, its future owner included (F3). No rule has been chosen to fix this (T1 options a–c are listed but not decided). **This plan adds no concealment rule.** Part B trials whatever method the table proposes and records how it goes. Nothing goes into the rulebook from this session.
- **"Open-information Apprentice" is not written down as a variant.** The rulebook's Apprentice variant is *3 gates, table-talk fully open (still never describe a visible face)*. That still assumes hidden fans. The open version the banner and `games.html` point to is what the first table actually played: every card's two faces visible to everyone, no "my face / your face" declaration. **Session convention for Part A:** play Apprentice exactly as written, except that fans are held open (cards laid face up in front of their owner, anyone may lift and check either face) and every pillar is placed showing the keystone's symbol with no declaration. Say this aloud before the deal. It is a session convention, not a rule. Whether to write it into the rulebook is for the designer to decide after the report.
- **Unchanged since playtest 01:** v1.1 rules, the setup cap (no symbol on 4+ keystones at 7 signs), failed locks return pillars to fans, exact final-round timing.

## Setup

- **Game:** JANUS
- **Version:** v1.1 rules, plus the Part A session convention above.
- **Players:** 3 (fans of 4) is preferred, to match playtest 01. 2 (fans of 6) is acceptable. Avoid 4P.
- **Symbol subset:** the 7-sign sub-deck. Remove every card showing Star (8) or Crown (9); 21 cards remain. Keep 1–2 spare Crown cards and something opaque (the deck box, a mug, an envelope) on the table in case Part B wants them.
- **Mode:** Apprentice — 3 gates, 4 omens in play plus 2 in reserve, 3 strikes. Deck after the deal: 6 cards.
- **Session shape:**
  1. **Part A — open baseline (required).** One Apprentice game under the open convention. About 15–20 minutes.
  2. **Part B — concealed trial (optional).** Only if the table wants it and has time. One Apprentice game played as written (sacred rule, my face / your face), using a concealment method the table proposes for the deal and refills. Stop the game the moment the method visibly fails. A failed attempt that is logged is still a useful result.
- **Why this session:** `next_step` is "choose and document a leak-free concealment model before retesting". The designer can't choose without knowing two things: is the open game worth keeping as a variant, and does any physical method actually stop the draw leaking a face? Part A answers the first, Part B the second.

## Hypotheses to test

### Part A — open baseline

- **A1 — The open game still has decisions.** Playtest 01 found locks were "bookkeeping, not deduction". *Prediction:* there is at least one turn where the table argues about which pillar to raise or which card to archive, because a foundation might be needed elsewhere. *Falsified if* every turn has one obvious best play and nobody debates. That is the flatness bug, and it would mean the open version is not a variant worth writing.
- **A2 — Stranded foundations are a player mistake, not a setup trap.** Playtest 01 Finding 3: two of three rounds ended needing a key that had already been used. *Prediction:* when the table knows this can happen, it routes around it. The game ends as a win, or as a loss the table can trace to a specific earlier play. *Falsified if* the game becomes unwinnable with no play anyone could have made differently. Then the dead-foundation safeguard is not enough, even with full information.
- **A3 — Omens have any job in the open game.** *Prediction:* omens are never read, because with every face visible there is nothing to learn. They act only as a strike buffer via the archive. *Falsified (in the interesting direction) if* the table finds a use for omen readings. Either way, record it: it decides whether an open variant would drop omens.
- **A4 — Clean end in range.** Playtest 01 H4, left open. *Prediction:* the game takes 15–20 minutes and ends as a clear win or loss. The final round causes no argument. *Falsified if* the final-round timing is disputed or the game runs past 25 minutes.

### Part B — concealed trial (if played)

These are playtest 01's three "next session must answer" questions, unchanged.

- **B1 — A real opaque-draw method stops the face leaks.** *Prediction:* with the table's method, no card's outward face is seen by its holder during the deal or any refill, and no card's holder-side face is seen by the table before it reaches a fan. *Falsified if* any deal or refill shows a face to the wrong person. Count each leak and say which step caused it.
- **B2 — The sacred rule holds for a whole game.** *Prediction:* the table keeps the rule all game, with **at most 2 accidental self-peeks per player**, and no peek changes a decision. *Falsified if* the rule is dropped again (as in playtest 01), or peeks are frequent enough that the table stops caring.
- **B3 — Concealed locks produce the deduction moment.** Playtest 01 H3. *Prediction:* at least one gate locks because someone reasoned out a buried face (from an omen, the archive or counting), and the table reacts to it. *Falsified if* every lock is a safe "my face" play or a blind "your face" gamble.

## Candidate concealment methods (to try and observe, not rules)

These are the only methods already on record. Let the table choose, or try its own. Write down exactly what was done.

| Method | Source | What to watch |
|---|---|---|
| Deck inside the **box base, a mug or an envelope**; draw blind from inside | T1 option (a) | Can the holder bring the card into the fan without seeing its outward face? Does the deal also work this way, or does it still leak? |
| **Cloth bag** | T1 option (b) | As above; note any fumbling with a fan in the other hand. |
| **Spare Crown card laid over the deck top** | Playtest 01 Bug 1 (the table's own hack) | Does the cover hide the top face *and* the new top face after each draw? How is the card moved into the fan? |
| Drawing from the **bottom** | Playtest 01 Bug 1 | Already failed (hard one-handed, and still exposes the new top). Only retry if the table insists, and log it as a repeat. |

T1 option (c), redesigning JANUS with no draw deck, can't be played tonight because no rules exist for it. It is out of scope.

## What to watch

Handling first, per the [physical-handling.md](../.kiro/steering/physical-handling.md) checklist:

- **What each player can see.** In Part B, log every moment a player sees a face they shouldn't: own outward face (holder), or a holder-side face before the fan (table). Note the step: deal, refill, raising a pillar, a pillar returned after a failed lock, or rearranging a fan.
- **The deal.** The rulebook deals cards flat "outward face down against the table". A card on the table shows its upper face to everyone, so this leaks the holder's face to the table. Watch whether the table's method fixes the deal, the refills, or both.
- **Buried pillar faces.** After a "my face" pillar is placed, its owner can't see its buried face but the table remembers it. The rulebook doesn't say whether the owner may lift the pillar. Note whether anyone does, and whether the table treats it as legal. This is where Bug 3 ("gates constantly checked on the down face") will show up under concealment.
- **Returned pillars.** After a failed lock, both pillars go back to their owners' fans. Is that handled without the owner seeing the outward face?
- **The communication wall (Part B).** Count tone leaks, quarterbacking and reactions. Note whether the table caught them itself.
- **Memory load (both parts).** Is anyone tracking buried faces? Is that a chosen effort or a strain?

Then:

- **Terminology.** Playtest 01's players called gates "locks", pillars "keys" and omens "clues". Note which words this table reaches for unprompted. "Key" collides with the Key sign; record it, don't adopt it.
- **Pacing.** Turn length and dead time while one player works out a deduction for the table.
- **Fun.** Where the table leaned in or went flat, in each part.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| A1 | At least one real debate about a play | Every turn obvious; nobody debates |
| A2 | Win, or a loss traceable to a play | Unwinnable with no avoidable play |
| A3 | Omens unused, or used for a reason the table explains | (record either way) |
| A4 | 15–20 min, clean end | End-timing argument; > 25 min |
| B1 | Zero face leaks at deal and refill | Any leak; name the step |
| B2 | Rule kept all game; ≤ 2 peeks per player, none decisive | Rule dropped; frequent or decisive peeks |
| B3 | At least one reasoned lock with a reaction | All locks safe or blind |

**Verdict framing:** A1–A4 decide whether the open game is worth writing up as a variant (a designer call). B1 is the gate for everything else. If no method passes B1, B2 and B3 can't be judged, and the report should say the concealed game is still untested. If B1 passes, the method used is evidence for T1. Choosing it is still the designer's decision.

## Teaching plan

- **Part A:** Teach the skeleton: gates (pairs shown openly), pillars, the lock-check (buried faces must match, forming a triangle), strikes, the archive, the final round. State the open convention at the start: "Everything is visible; lift anything." Skip the sacred rule and the communication wall. Mention that a foundation can be used up, without giving advice on avoiding it (A2 tests whether the table notices).
- **Part B:** Re-teach in plan 01's order. Start with the hook ("you see your side; the table sees the other"), then demonstrate the sacred rule, then the three actions, then the communication wall with one legal and one illegal example. Then **ask the table how it wants to deal and refill without leaking a face.** Show the candidate table above only if they ask for ideas. Record what they choose and why.
- **Watch during teaching:** time to first action. Does "my face / your face" land first time? Does anyone object to the sacred rule before play starts? That would suggest a group verdict on fragility, not a teaching gap (the open question from playtest 01 Bug 2).
- Don't read the strategy notes before either game.

## Record sheet

| | Part A (open) | Part B (concealed) |
|---|---|---|
| Players / fan size | | |
| Concealment method (exact procedure) | open convention | |
| Result (win / strikes / deck-out) | | |
| Gates locked / strikes taken | | |
| Omen readings (count) / omens left | | |
| Debated plays (count) | | |
| Stranded-foundation moment? Traceable to which play? | | |
| Face leaks at deal / refill (count, step) | — | |
| Accidental self-peeks (per player) | — | |
| Communication-wall incidents (caught by table?) | — | |
| Reasoned locks (count) | | |
| Owner lifted own pillar? Treated as legal? | | |
| Time | | |
| Game abandoned? At which step? | | |

- Words the table used for gates / pillars / omens: ____
- Did the table propose its own concealment idea? Exact wording: ____
- Surprises / quotes:

## After the session

Write `JANUS_playtest_02.md`: setup, each hypothesis (confirmed / refuted / open), bugs ranked by severity with handling bugs first, rule-change candidates each tied to an observation, and a verdict (iterate / park / cut). Set `physically_playtested: true` (it already is) and choose the `state` per the playtesting table. If Part A is still the only playable form, JANUS stays Rough edges. Update `next_step` and the known issue in all three catalogue views. Record any concealment method as evidence for T1, not as an adopted rule.

## Out of scope

- Writing or adopting a concealment rule. That decision is T1's.
- The no-draw redesign (T1 option c). No rules exist yet.
- Masters, Oracle and Ninefold Temple variants.
- Tuning starting omens, strike count or fan sizes. The rulebook defers tuning until concealment is fixed.
- The lock/key/clue rename.
