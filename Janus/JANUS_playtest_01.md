# JANUS — Playtest Report 01

*Pairs with [JANUS_playtest_plan_01.md](JANUS_playtest_plan_01.md). Written per [playtesting.md](../.kiro/steering/playtesting.md). Part of the Lauren & Arran session, June 2026 — raw notes in [Lauren and Arran Playtest.md](../Lauren%20and%20Arran%20Playtest.md).*

## Setup

- **Game / version:** JANUS v1.1 (first table test).
- **Mode:** Apprentice — **3 gates**, played as written otherwise. Three rounds played.
- **Players:** 3 (Sam, Lauren, Arran), fans of 4 as specified.
- **Symbol subset:** 7-symbol sub-deck (21 cards). Spare Crown (symbol-9) cards were on hand and got used as an improvised deck cover (see Bug 1).
- **Critical deviation:** the table **did not play the fan-asymmetry concealment**. Cards were placed beside gates and **everyone freely examined both faces at any time**; "my face / your face" was never declared. So this session tested an *open-information* variant of JANUS, **not JANUS as designed.**

## Hypotheses

Because the core concealment was abandoned, the plan's hypotheses about hint grammar, the omen economy as deduction-under-uncertainty, and reasoned (vs blind) locks **could not be tested** — there was no hidden information to deduce. Recording honestly:

| | Verdict | Notes |
|---|---|---|
| **H1 — hint grammar graspable in one game** | **Not tested** | Omens were used as "clues" but against open information, so the "these show X to us" deduction payoff never bit. |
| **H2 — omen economy paces rather than starves** | **Not tested** | Without hidden faces, omens weren't load-bearing. |
| **H3 — locking a gate is a genuine deduction payoff** | **Refuted in spirit** | With full visibility, locks were bookkeeping, not deduction. The intended "ahh" moment can't exist in the open variant. |
| **H4 — clean end within range** | **Open** | Three rounds completed; two ended needing an already-played key (see Finding 3). No end-timing argument noted. |

The session's real value was a **handling discovery that blocks JANUS as written** (Bug 1) and useful **terminology data** (Finding 2).

## Bugs found (severity-ranked)

### Bug 1 — A concealed draw deck is physically impossible with backless cards *(handling — CRITICAL / blocking)*
This is the headline. JANUS v1.1 explicitly tried to fix the v1.0 public-deck-top leak by specifying a **"face-down stack"** drawn without looking. **That fix does not survive contact with the physical deck**: a stack of double-faced cards *always* exposes one face of the top card to the whole table — there is no back to turn down. The players hit exactly the leak v1.1 claimed to close: everyone had seen one symbol of the top card before it was drawn.

Their attempted fixes both failed:
- **Drawing from the bottom** — physically very hard while holding a fan in one hand (one face to you, the other to the table) and secretly taking the bottom card; and it *still* exposed one face of the new bottom (now top) card.
- **Covering the deck with a spare Crown card** — a working *hack*, and the strongest clue to the real fix: JANUS needs a genuine **deck cover / opaque draw method** as a component or convention, because "face-down stack" is not a thing this deck can do.

Until this is resolved, the asymmetric-information game cannot actually be played as written. **This is the blocker.**

### Bug 2 — The sacred no-self-inspection rule + my-face/your-face was dropped entirely *(handling / teachability — HIGH)*
The table never adopted the one sacred rule (never look at your own outward face) or the my-face/your-face declaration; they just let everyone see everything. Whether this was a teaching failure, a handling-friction avoidance, or a quiet verdict that the discipline is too fragile to sustain is **unknown** — but it means JANUS's central conceit got no test at all. The fan-asymmetry bet (flagged in [physical-handling.md](../.kiro/steering/physical-handling.md) as JANUS's exceptional, policed exception) remains **completely unvalidated at the table.**

### Bug 3 — Gates "constantly checked on the down face" *(handling — MEDIUM)*
The buried (table-facing) side of the gate/keystone cards was repeatedly re-checked by everyone. In the open variant this was free; under proper play it points at a memory-load and verification question the concealed game will have to answer.

## Findings (not bugs)

### Finding 1 — Three rounds completed without the game breaking
Even as an open-information variant, the structure (raise pillars, lock matching foundations) functioned and the group played three rounds — so the *skeleton* is sound. The problem is that the skeleton without concealment isn't really JANUS.

### Finding 2 — Players' instinctive terminology beat the rulebook's
The table spontaneously renamed the components: gates/keystones → **"locks,"** the pillar-pairs that lock them → **"keys,"** omens → **"clues."** "Unlock the lock with a connected key" was how they actually described play. This lock-and-key language is arguably more intuitive than gate/keystone/pillar and is worth considering as a rename — it maps cleanly to the mechanic (a two-card key opens a lock) and players reached for it unprompted. *Caveat:* "key" collides with the Key sign in the 9-symbol games and the shared deck vocabulary; weigh that before adopting.

### Finding 3 — Two of three rounds ended needing an already-spent key
The first two rounds stalled because a needed foundation card had already been played (as a starting lock or a key elsewhere). The table read this as **their own careless play, not a game bug** — and noted it would have been far harder, *possibly impossible*, under the proper hidden-information rules. This points squarely at the v1.1 dead-card safeguard and setup validation: with full visibility they could route around it, but the concealed game may need stronger protection (or the deduction *is* "don't strand your own foundations," which is fine — but it needs testing under real concealment to know).

## Rule-change candidates (each tied to an observation)

1. **Solve the concealed draw (Bug 1) before anything else.** Candidates: a dedicated **opaque deck cover / sleeve** the deck sits in (drawn blind from the top); drawing from a **cloth bag**; or restructuring so there is **no draw deck at all** (deal the whole sub-deck into fans + a face-up archive, no refills). The last is the most deck-honest — it removes the only physically impossible component — but changes the game's pacing and must be designed and re-simmed. **This is the priority design decision.**
2. **Decide the fate of the sacred rule (Bug 2).** Either commit to teaching/policing it hard next session and measure accidental peeks (the plan's metric), or accept that fan-asymmetry is too fragile for this group and pivot JANUS toward a deliberately *open* deduction game. Don't leave it untested twice.
3. **Consider the lock/key/clue rename (Finding 2)** — pending the Key-sign collision check.
4. **Re-examine the dead-foundation safeguard under concealment (Finding 3).**

## Verdict: **ITERATE** (but note: JANUS-as-designed was not actually tested)

The session was valuable precisely because it exposed a **blocking handling bug**: v1.1's "face-down stack" is physically unsound on a backless deck, and the group abandoned the concealment that defines the game. JANUS keeps its place in the pipeline, but it **regresses to "needs a sound concealment model"** before its real hypotheses (hint grammar, omen economy, deduction payoff) can be tested at all.

**Stays at Stage 1–2 in the pipeline — not promotable.** The next session must play it *concealed* with a working draw method, or the game's core premise stays unproven.

### Next session must answer
1. With a real opaque-draw method (cover, bag, or no-deck deal), does the concealed game run without face leaks?
2. Can the group **sustain the sacred rule** for a whole game — how many accidental peeks, and are they disruptive?
3. Under genuine concealment, does locking a gate finally produce the deduction "ahh" (H3)?
