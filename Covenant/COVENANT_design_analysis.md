# COVENANT (version A) — how a chapter actually works

*Design exploration, July 2026; rulebook simulation added November 2026. The July sections below are kept as written: they explore four chapter models and recommend one (Model 3). The [trial-engine draft](COVENANT_trial_engine.md) later rejected that and proposed an open-information engine. **The November section at the end records what the v0.1 rulebook actually adopted, and the simulation of it.** Companions: [COVENANT_concept.md](COVENANT_concept.md), [COVENANT_rulebook.md](COVENANT_rulebook.md), [covenant_sim.py](covenant_sim.py) (the July scoping model is `--scoping`).*

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

---

## November 2026 — the v0.1 rulebook and its simulation

### What the rulebook adopted, and why it differs from the July recommendation

The July scoping model was right about its own premise. A claim that answers only yes or no rules out one (stranger, sign) pair, and against that the full deducer is no better than guessing: C(k,2)/2 misses either way. Re-run with `--scoping`, it still gives 2.99 / 5.00 / 7.47 / 10.49 / 13.99 misses for k = 4..8. **But that premise is not the physical game.** At the table you verify a claim by flipping the stranger. A miss therefore *shows* its true sign. It does not just say "no".

The [v0.1 rulebook](COVENANT_rulebook.md) keeps version A as the concept describes it and makes that flip honest:

- The row is uniform, and each stranger is secretly bound to one covenant sign.
- You claim with a hand card bearing the sign you name.
- A **miss unmasks** the stranger, ashes the claim card, and the stranger strikes back, ashing the top card of the reserve.
- A **hit** turns the stranger and returns the claim card.

Your hand (one card per stranger, no automatic draw) is your strength, and nothing in it is hidden. The decisions are:

- **Card stewardship:** which card to risk, given that every card names two signs.
- **When to spend cards on powers:** Leaf, Wave, Moon, Eye and Key, with Mask and Star always on.
- **Whether to burn with Flame** and take a grudge.

Memory is not the spine (Model 3 becomes a variant). The open-information Turning engine stays on file as the alternative if this engine fails at the table. The rulebook's closing note lists all 15 designer decisions.

### The questions

1. Does chapter one (no powers) contain any real decision, or is it only a tutorial?
2. Per chapter (k = 3..8 strangers): average cards lost, failure rate, stall rate.
3. Skill gap: skilled vs random, and skilled vs the *obvious* line (the OUROBOROS lesson).
4. Does a failure ever block the campaign, and are grudges a live choice?
5. Which hand size and miss penalty give a sensible difficulty ramp?

### Method

- **Ruleset:** [covenant_sim.py](covenant_sim.py) models the v0.1 rules exactly as written: the uniform row, hand claims, unmask on a miss, strike-back, all nine power rules, Flame grudges, the grudge toll and free retries. Retries are capped at 2 in the campaign model; after that the newcomer joins as a grudge.
- **Not modelled:**
  - assistants;
  - concession timing, beyond "concede when no useful action is left";
  - the honour of the wash (the sim assumes a perfect shuffle).
- **Bots** (public information only):
  - **Random:** uniform over every legal action, including silly claims. This is the mechanics floor.
  - **Greedy:** the obvious line. Claim unmasked strangers it can match, otherwise guess a still-possible sign with a random card, and use powers only when stuck.
  - **Skilled:** a one-ply heuristic. It risks the card whose loss hurts coverage least, Leafs for card advantage, uses Eye before a blind guess into three or more masked strangers, uses Key/Moon/Wave to fix coverage, and burns with Flame only as a last resort on the final hearing.
- **Exact solve:** chapter one by expectimax over information states (masked strangers are interchangeable, so the state is hand × unmasked signs × unaccounted signs).
- **Volume:** 2,000 hearings per chapter per bot (36,000); 1,000 campaigns per bot; a hand-size × strike sweep at 1,000 hearings per cell (80,000). About 145,000 hearings in total. The turn cap is 600 actions. Main seed 2026, repeated with seed 7: every headline figure moved by ≤ 2 points.

### Results (hand = one card per stranger, strike-back on — the adopted rules)

| Ch | Newcomer | k | Bot | Clear | Grudge-clear | Fail | Cards lost | Misses | Actions |
|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Flame | 3 | Random | 19.6% | 0% | 80.5% | 2.65 | 2.65 | 3.9 |
| | | | Greedy | 72.7% | 0% | 27.4% | 1.17 | 1.17 | 3.9 |
| | | | Skilled | 84.5% | 0% | 15.4% | 1.16 | 1.16 | 4.0 |
| 2 | Eye | 4 | Random | 1.4% | 9.8% | 88.8% | 4.03 | 3.06 | 5.8 |
| | | | Greedy | 75.4% | 14.3% | 10.2% | 3.07 | 1.91 | 6.3 |
| | | | Skilled | 90.3% | 2.1% | 7.6% | 3.25 | 1.90 | 6.1 |
| 3 | Mask | 5 | Random | 0.4% | 2.6% | 97.0% | 6.60 | 3.79 | 7.2 |
| | | | Greedy | 81.9% | 7.6% | 10.5% | 5.11 | 2.72 | 8.9 |
| | | | Skilled | 96.0% | 1.3% | 2.8% | 4.23 | 2.28 | 9.1 |
| 4 | Key | 6 | Random | 0.1% | 1.2% | 98.7% | 9.15 | 4.90 | 8.3 |
| | | | Greedy | 87.8% | 4.7% | 7.5% | 6.75 | 3.51 | 11.3 |
| | | | Skilled | 96.5% | 1.1% | 2.5% | 5.27 | 2.77 | 11.7 |
| 5 | Star | 7 | Random | 0.0% | 0.6% | 99.4% | 10.54 | 5.55 | 9.0 |
| | | | Greedy | 85.9% | 2.5% | 11.7% | 8.43 | 4.39 | 13.5 |
| | | | Skilled | 90.8% | 1.5% | 7.8% | 6.92 | 3.54 | 13.6 |
| 6 | Crown | 8 | Random | 0.0% | 0.1% | 99.9% | 12.99 | 6.79 | 9.9 |
| | | | Greedy | 88.3% | 1.5% | 10.2% | 10.34 | 5.29 | 14.8 |
| | | | Skilled | 96.5% | 0.4% | 3.1% | 9.19 | 4.62 | 14.5 |

Stall rate is 0.0% in every configuration.

**Skill gap.** Cards-lost ratios understate it against Random, because Random dies early and so loses fewer cards. Clear rate is the clearer measure.

| Ch | Random ÷ Skilled (cards lost) | Greedy ÷ Skilled (cards lost) | Clear: Random / Greedy / Skilled |
|---:|---:|---:|---|
| 1 | 2.29× | 1.01× | 20% / 73% / 85% |
| 2 | 1.24× | 0.95× | 1% / 75% / 90% |
| 3 | 1.56× | 1.21× | 0% / 82% / 96% |
| 4 | 1.74× | 1.28× | 0% / 88% / 97% |
| 5 | 1.52× | 1.22× | 0% / 86% / 91% |
| 6 | 1.41× | 1.12× | 0% / 88% / 97% |

**Chapter one, solved exactly.**

- Optimal play wins **83.3%** (5/6) with 1.33 expected misses.
- The worst *sensible* play (never naming an impossible sign) wins **66.7%**; uniform random wins 19.1%.
- The optimal path has 17 decision states. In **2** of them a sensible choice changes the odds, by a **50-point swing**: after a miss, which card you risk next (the rulebook's worked example).

**Campaign** (1,000 per bot; retries ≤ 2, then grudge):

| Bot | Grudges | Hearings (min 6) | Cards lost (all hearings) | Campaigns with 0 grudges |
|---|---:|---:|---:|---:|
| Random | 5.51 | 17.1 | 82.4 | 0% |
| Greedy | 0.07 | 7.4 | 41.3 | 94% |
| Skilled | 0.00 | 6.5 | 32.0 | 100% |

**Sweep** (Skilled / Greedy: % of hearings not cleanly cleared, and cards lost; 1,000 per cell):

| Hand | Strike | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Ch 6 |
|---|---|---|---|---|---|---|
| k | off | 0.7/0.8 · 1.86/1.87 | 0.7/3.8 · 2.21/2.56 | 2.8/8.9 · 2.73/3.29 | 9.6/13.6 · 3.54/4.07 | 4.0/9.6 · 4.59/5.05 |
| **k** | **on** | **7.3/24.4 · 3.21/3.10** | **4.0/15.0 · 4.12/5.01** | **3.1/13.9 · 5.23/6.81** | **9.6/12.3 · 7.08/8.38** | **4.0/11.0 · 9.11/10.35** |
| 4 | on | 7.3/24.4 · 3.21/3.10 | 23.0/32.8 · 4.58/5.23 | 49.1/59.1 · 5.64/6.37 | 87.5/85.2 · 6.20/7.20 | 92.0/93.3 · 7.17/7.67 |
| 5 | on | 0.0/6.1 · 2.88/2.63 | 4.0/15.0 · 4.12/5.01 | 20.5/34.2 · 5.76/6.71 | 66.8/62.7 · 7.07/7.95 | 76.8/79.5 · 8.59/8.96 |
| 6 | on | 0.0/1.0 · 1.92/1.90 | 0.7/14.6 · 3.49/4.97 | 3.1/13.9 · 5.23/6.81 | 35.9/38.8 · 7.31/8.29 | 49.3/56.5 · 9.36/9.82 |

(The strike-off rows for hands 4–6 are in the script output and follow the same pattern.)

### Health checks

- **Termination:** no stalls anywhere. Every action either turns a stranger or moves a card out of play for good; Moon only reaches into Ash, and Moon's own card is spent.
- **Skill vs the floor:** healthy. Random clears almost nothing from chapter two on, while Skilled clears 90–97%. On cards lost, Skilled beats Random 1.4–2.3× in five of six chapters (1.24× in chapter two, where Random's early deaths flatter it).
- **Skill vs the obvious line: thin, and the honest weak spot.** Skilled loses 1.1–1.3× fewer cards than Greedy from chapter three on, and clears 5–15 points more often. In chapters one and two the cards-lost gap is nil (0.95–1.01×). The edge there is entirely in clear rate (+12 and +15 points): the stewardship decision and not wasting cards on silly powers. This is a one-ply bot, so it is a floor, not a ceiling (design-principles lesson 6b). Still, the table must find out whether "risk the redundant card" and "Leaf early" feel like decisions or like chores.
- **Ramp:** with a fixed hand, the game is backwards. Hand 5 is easy in chapter two and 67–77% failure in chapters five and six, and Skilled is no better than Greedy there. One card per stranger gives a flat, forgiving ramp: Skilled fails 3–10% per chapter. Difficulty shows up as rising Ash (1.2 → 9.2 per chapter), not as failure.
- **Progress is never blocked:** with free retries, a Skilled campaign takes 6.5 hearings on average and gets no grudges. Even Greedy averages 7.4 hearings.
- **Strike-back earns its place:** it is what makes Eye worth spending, and it opens the Greedy–Skilled gap. With strike-back off, the two bots are within 3 points in chapters two and three. With it on, the gap is 24% vs 7% and 15% vs 4%.
- **Estimated time:** 4–15 actions per chapter. That is roughly 2 minutes for chapter one and 10–15 for the finale, including setup and the wash.

### Changes adopted (v0.1)

- **Opening hand = one card per stranger,** not a fixed 5. With 5, chapters five and six were near-unwinnable for both bots.
- **Strike-back on** as standard. Off becomes the *Gentle rite* variant.
- **Standing bands** set from the simulated per-chapter Ash. The sum of the six won-chapter averages is about 30 for Skilled and 35 for Greedy, which gives bands of ≤ 24 / 25–32 / 33–40 / 41+.
- **Chapter one is labelled a teaching rite** in the rulebook, with its single decision named and worked through.

### Verdict on the blocking questions

- **Chapter one is a tutorial, honestly framed.** It is not inert (one 50-point decision, 83% vs 67%), but it is not a game you would replay. The rulebook says so.
- **No blocking defect** in the floor: it terminates, nothing blocks progress, the skill gap against the random floor is healthy, and the difficulty ramp is sane.
- **Two soft risks need the table, not more simulation:**
  - **Flatness.** The edge over the obvious line is thin, and failure is rare once you play carefully.
  - **Grudges are near-irrelevant.** With free retries, a careful player never takes one. The *Strict hearings* variant is the ready fix if grudges should matter.

### Caveats for the first table test

- **The wash.** Can a human really lose track of 4–8 identical strangers by sliding them? And does lining them up without lifting work?
- **Do the decisions feel like decisions?** Watch for "risk the redundant card" being spotted, or missed, without the strategy notes.
- **Flatness.** Is the rising Ash count enough tension when failure is rare, or does the campaign need *Strict hearings* by default?
- **Power use.** Measured separately (1,000 Skilled hearings per chapter, seed 99+ch), per hearing: Leaf 0.15–1.9, Eye 0.6–1.0, Wave 0.06–0.21, Moon 0.04–0.20, Key 0.08–0.24, Flame ≤ 0.04. Leaf and Eye carry the play; Wave, Moon, Key and Flame barely fire for the bot. Does a human ever reach for them? If not, they are dead text to cut or rework.
- **Chapter six.** Is the 8-stranger finale a climax, or just a longer chapter five?
- **Assistants** are completely unsimulated.
