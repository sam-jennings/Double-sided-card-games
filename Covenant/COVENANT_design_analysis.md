# COVENANT (version A) — how a chapter actually works

*Design exploration, July 2026. Early stage: no rulebook yet. This document proposes four concrete ways a chapter could play, grounds them in a scoping computation, evaluates them against the house standards, and recommends one. Companion to [COVENANT_concept.md](COVENANT_concept.md) and the model in [covenant_sim.py](covenant_sim.py).*

The concept fixes the fiction (you are the Tenth; the sub-deck is the save; a new sign joins each chapter) but leaves the chapter loop as a sketch — "a blind-matching permutation puzzle." The job here is to turn that sketch into a loop with real decisions, and to find out whether the obvious version is even a game.

---

## The problem the concept walked into

In the chapter that admits sign *S*, the attackers are the cards pairing *S* with each already-won sign. Laid *S*-face up they are **visually identical**; their hidden faces are a permutation of the won signs. Taken literally, "claim each attacker" is: identify a hidden permutation by naming (attacker, sign) and flipping to check, paying one card of health per wrong guess.

I modelled that literal loop ([covenant_sim.py](covenant_sim.py), 200k trials per row size) to ask the only question that matters first: **is there skill in it?**

| Attackers *k* | permutations *k!* | health = deck C(k,2) | random guessing — misses | full deducer — misses | skill gap |
|---:|---:|---:|---:|---:|---:|
| 4 (ch. 2) | 24 | 6 | 3.00 | 3.00 | **1.00x** |
| 5 (ch. 3) | 120 | 10 | 5.00 | 5.00 | **1.00x** |
| 6 (ch. 4) | 720 | 15 | 7.50 | 7.50 | **1.00x** |
| 7 (ch. 5) | 5,040 | 21 | 10.50 | 10.51 | **1.00x** |
| 8 (ch. 6) | 40,320 | 28 | 13.99 | 14.01 | **1.00x** |

The "full deducer" runs complete constraint propagation — it places any attacker with one candidate left, and any sign with one possible home, and only gambles when nothing is forced. **It does no better than guessing at random.** The closed form confirms it: expected wrong guesses are exactly C(k,2)/2 regardless of strategy.

The reason is structural, and it's worth stating because it constrains every design below. A wrong claim (a NO) only excludes *one* (attacker, sign) pair — it tells you nothing about the other attackers. A right claim (a YES) removes that sign from the rest, but every strategy is forced into the same YESes eventually, and the last attacker is always free. There is simply nothing for deduction to bite on. **The blind match is a slot machine.** It also barely threatens you — with health equal to the deck you clear ~100% of the time, just poorer.

So the concept's own "fastest falsification" question ("is chapter one a game?") has an answer for the literal reading: **no.** A chapter becomes a game only if it adds an information source the blind match lacks. There are exactly three honest ones on this deck:

- **Memory** — let the player see the faces once; the skill is recall (perfect recall wins with zero misses).
- **Paid information** — let the player buy certainty (a peek reveals a face; deduce the last for free at cost *k*-1).
- **Imposed structure** — add deducible clues or an oracle so reasoning has something to chew.

Every model below is really a choice of which of these to build on.

---

## Model 1 — The Blind Rite (press-your-luck)

*Information source: none. Tension source: the health economy.*

- **Start.** Shuffle the *k* attackers, lay them *S*-up in a row. Your covenant deck is your health.
- **Turns.** On your turn, either **claim** (name an attacker's hidden sign, flip to check — hit banks it, miss discards one health card) or **spend a power** (discard a won-sign card for its verb: Eye peek, Wave rearrange, Moon recover, etc.).
- **Decisions.** Which attacker to gamble on; whether to blow a card on an Eye-peek instead of guessing; when to Flame-remove a stranger you can't crack and eat the grudge.
- **Win / lose.** Clear the row → the matched cards flip friend-side and join the deck. Health gone → the sign joins as a grudge; retry or carry it.
- **Verdict.** The measurements above are exactly this model. Its base loop is a 1.00x slot machine, and only the powers inject decisions — but the powers are themselves just "buy information" (Model 2) bolted onto luck. Honest, cleanest handling, playable from chapter one, but thin. Keep it only as the *fallback* difficulty when a player has no useful powers.

## Model 2 — The Reading (peek-and-commit / information economy)

*Information source: paid peeks. Tension source: spend efficiency.*

- **Start.** Same row, but **blind claims are banned** — you may only commit a claim you have earned.
- **Turns.** Either **peek** a hidden face (tilt, look, set back *S*-up) at a cost of one health card, or **commit** a claim you know (free, and correct commits are safe). Won signs cheapen peeking: Eye peeks free, etc.
- **Decisions.** How many faces to buy before the rest fall out by elimination; peek order (buying *k*-1 deduces the last for free); which powers lower the information price.
- **Win / lose.** All committed correctly → win. Out of cards → grudge.
- **Verdict.** Converts luck into optimization and handles cleanly, but the optimum is nearly a script — "peek all but one" costs a flat *k*-1 with no gamble — so the decision space is shallow and can feel like paperwork. Also weak exactly where it's needed: chapters one and two have no Eye, so peeking is pure health-burn. A supporting economy, not a spine.

## Model 3 — The Remembering (deliberate hidden-face memory)  ← recommended

*Information source: memory. Tension source: recall under a growing load, backed by elimination.*

This is the blind match turned inside out: instead of hiding the faces and making you gamble, it **shows** you the faces once and makes you remember.

- **Start — "The Approach."** Lay the *k* attackers **partner-face up**: you see the whole permutation (Moon here, Flame there, Leaf there...). Study as long as you like. Then **seal** the row — flip every card in place to its identical *S*-face. One clean gesture, no lingering hidden state; now the row is uniform and the only handle on each stranger is *where it stood*.
- **Turns.** **Claim** by naming a position's hidden sign and flipping it to verify. A hit banks the friend (flip stays, card joins the deck). A **miss** costs a health card *and* the strangers **shuffle** — slide the unclaimed cards around, scrambling your positional memory. Powers become memory tools: Eye = re-study one face without penalty; Moon = recover a spent card; Flame = send an unplaceable stranger away as a grudge; Wave = freeze the row against one shuffle.
- **Decisions.** What to prioritise memorising when *k* reaches 7–8; **claim order** — bank the certain ones first, because every correct claim shrinks the set of remaining signs, so the last few are *logically forced* even after memory fades (memory and counting hand off to each other); and the push-your-luck call, claim now from fuzzy memory and risk the shuffle, or spend to re-study first.
- **Win / lose.** Clear the sealed row → the sign joins. Health gone → grudge.
- **Why it fixes the skill gap.** Perfect recall wins with **zero** misses; a player who remembers nothing is back at the 1.00x slot machine. That whole gap — 0 up to ~14 misses at k=8 — is now *skill*, not luck. The difficulty ramp is free: 4 faces is a gentle rite, 8 faces is a real feat, which is exactly the campaign arc.
- **Handling.** Self-enforcing and clean. There is no ongoing hidden-state to police (physical-handling's chief fear): the seal is a single flip, the faces are identical so you *cannot* peek without a visible, committing flip, and the shuffle penalty is just sliding cards. It is the deliberate, verifiable, roughly-symmetric memory game that `physical-handling.md` and `product-vision.md` both flag as an **under-served gap worth filling** — the collection has deduction, bluff, and trick-taking but engineers memory *out* of almost everything.
- **Bootstrap bonus.** Claiming is "name and flip," so it needs no card in hand — which quietly solves the chapter-one problem of a signless player having nothing to play. The covenant deck is purely the health/power reserve.

## Model 4 — The Trial of Witnesses (imposed deduction / oracle)

*Information source: added clues. Tension source: pure logic, no luck.*

- **Start.** The row is blind, but the chapter also deals a few face-up **witness** constraints, or an assisting player who saw the deal answers "how many of your claims are correct" each round (Mastermind).
- **Turns.** Propose an assignment; read the feedback; reason to the solution.
- **Decisions.** Classic logical inference — the deepest of the four.
- **Win / lose.** Solve it; wrong rounds cost health.
- **Verdict.** The most *game* on paper and zero luck, but it fights the concept. Solo needs an oracle substitute (a booklet or a fiddly self-check), and physically, flipping to verify reveals identity, breaking the "how many" abstraction. It shines only with assistants — which makes it a good **multiplayer layer** (the assistant becomes the trial-master), not the solo spine.

---

## Evaluation

| | M1 Blind Rite | M2 Reading | **M3 Remembering** | M4 Witnesses |
|---|:---:|:---:|:---:|:---:|
| Handling floor (clean, no policed hidden state) | Pass | Pass | **Pass** | Risk (oracle/flip-reveal) |
| Deck necessity | Pass | Pass | **Pass (uses the flagged pressed-face property)** | Pass |
| Skill gap (design-principles lesson 6) | **1.00x — fails** | Shallow (near-script) | **Full: 0→~14 misses is skill** | Deep |
| Real decisions | Powers only | Efficiency only | Recall + claim-order + risk | Inference |
| Playable at chapter one (no powers) | Yes | Poor (no Eye) | **Yes** | Needs oracle |
| Solo-first, assists optional | Yes | Yes | **Yes** | Assist-dependent |
| Collection fit | Overlaps luck fillers | — | **Fills the memory gap** | Overlaps JANUS-style deduction |

**Recommendation: build Model 3 (The Remembering) as the chapter spine**, and fold the others in as texture rather than alternatives:

- **Model 1's health economy** stays — the covenant deck is health, misses cost cards, grudges are the failure state. It just sits *under* a memory game instead of a slot machine.
- **Model 2's paid peeks** become the *powers* (Eye = re-study), so buying information is a costed option, not the whole game.
- **Model 4** becomes the **assistant mode**: an assisting player who saw the Approach can be the trial-master and withhold or dole out a re-study, turning the solo memory game into a light co-op deduction at 2–4 players.

This gives one engine that scales: chapter one is a 4-face memory rite that teaches "name and flip," and chapter six is an 8-face feat of recall with five sign-powers as memory tools — the same loop, harder, which is what a campaign wants.

---

## What this changes in the concept

- The line "claim by playing a card of its hidden sign from your covenant hand" should soften to **"name the hidden sign and flip to verify"**; the hand is health and powers, not the claim token. (This also fixes the signless-chapter-one bootstrap.)
- "Wrong claims leak information for the next guess" is **false** in the blind reading (proven above) — drop it. Under Model 3 the honest tension is memory disruption, not information gain.
- Keep every-pair-once doing real work: it guarantees the hidden faces are exactly one-of-each-won-sign, which is what lets late claims be *deduced* once memory has banked the earlier ones.

## Open questions (for the first table test)

- **Is 4-face memory too easy and 8-face too punishing?** The ramp may need the shuffle penalty tuned (shuffle all unclaimed, or only two neighbours?).
- **Does the shuffle-on-miss feel fair or infuriating?** It is the whole tension; if it reads as "the game erased my progress," soften to a single-swap.
- **Do permanent card losses spiral the campaign?** If misses permanently shrink the deck, an early bad chapter may doom later ones. Likely fix: spent cards return between chapters; only *grudges* persist.
- **Are the sign-powers real choices or auto-plays?** Especially Eye (re-study) — if it's always right to use, it isn't a decision.

## Fastest falsification

Two solo sittings on the printed Set D deck: play the Approach at **k=4** (founders) and at **k=8** (Crown) back to back. Watch one thing — does recall create the tension, or do players just flip blindly and treat misses as noise? If even k=8 collapses into shrug-and-guess, memory is not carrying the game and Model 3 is wrong. If k=8 makes the table lean in and groan at a shuffle, the spine is proven and the next step is a chapter-one-through-six rulebook.

## Next step

Draft a one-page **Model 3 chapter rulebook** — Approach, seal, claim, miss/shuffle, win, grudge — and run the k=4 / k=8 falsification before writing the campaign frame around it.
