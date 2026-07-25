# Gateway Game Concepts — a livelier opener than WILDFIRE

*Design-selection document, July 2026. Cross-game, so it lives in `Project/` rather than any game folder. Once one concept is chosen, it graduates to its own root-level folder with a proper game record per [ADDING_A_GAME.md](ADDING_A_GAME.md). Nothing here is in the catalogue yet.*

> **Status: the gateway role is filled for 3-5 players by WILDFIRE v1.2; the 8-10 player brief remains open.**
>
> **Part One (§1–§7)** proposed CLAMOUR, CAULDRON, HUSH and SALVO, all built on private three-card hands — refuted for deal-locked ceilings and computable best moves (§7). **Part Two (§8–§9)** proposed VERDICT, built on the opposite assumption that nobody is dealt anything — refuted for having no decision content and no dependence on the deck (§11).
>
> **Part Three (§13)** scores the eventual answer - repairing WILDFIRE rather than replacing it - against the original six requirements: three passes, two partials, one outright failure.
>
> **Before writing another candidate, read §11.5** (the gate both failed attempts skipped) and **§13.5** (the gateway teaches no rank, which is the collection's most actionable open gap).

---

## 1. The brief

A game whose **only job** is to introduce a group of new players to the deck and send them hungry for the rest of the collection. Requirements, in Sam's words:

1. Quick to explain.
2. Easy to remember.
3. **No awkward hand or card management.**
4. Easily adaptive to higher player counts.
5. More exciting than WILDFIRE.

WILDFIRE currently holds this seat and half-works. Its first table test ([WILDFIRE_playtest_01.md](../Wildfire/WILDFIRE_playtest_01.md)) recorded the best possible teaching result — *zero rule clarifications* — alongside the finding that kills it for repeat use: **"players did not feel there was much skill involved… the game felt reactive rather than strategic."** It also generated the collection's worst ergonomics finding, [F1](Playtesting/DECK_PLAYTEST_FINDINGS.md) (nine-card hands with no sort axis, re-scanned every turn).

So the replacement must fix two things at once: **excitement** and **hand load**.

### The four design commitments

Chosen before any mechanism, and shared by all three concepts below:

| Commitment | Why |
|---|---|
| **Simultaneous reveal** | Zero downtime, no turn order to track, and player count becomes a free parameter — the single cheapest route to requirement 4. It is also the most reliable excitement generator: everyone commits blind, everyone reacts together. |
| **Three cards, face up in a row in front of you** | Kills F1 outright. Nothing is held, nothing is fanned, nothing is sorted, nothing is concealed. Public rows also mean new players can *see* what everyone else is working with, which removes "am I doing this right?" anxiety and teaches the deck faster. |
| **Cards never leave; they flip** | You play a card by pushing it forward; afterwards it turns over and returns to your row showing its partner sign. No drawing, no discarding, no deck management. Every card is a **two-stroke engine** — spend the Crown now and that card owes you its partner next time. This is the deck's signature move applied to the player's own resources. |
| **Nothing to memorise** | All state is on the table, face up. Per [design-principles.md](../.kiro/steering/design-principles.md) lesson 1, the deliberate-memory genre is a *separate* design target (STRATA), not a gateway feature. |

### Card economy — all three fit

Hand of 3, persistent, no draw deck needed:

| Players | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cards in rows | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 |
| Cards spare | 27 | 24 | 21 | 18 | 15 | 12 | 9 | 6 | 3 | 0 |

The 36-card deck supports **up to 12 players** with no rule changes at all. Set-up is "deal three each, lay them face up, go" at every count.

---

## 2. CLAMOUR — the loudest voice nobody else is using ⭐ recommended

*3–10 players (best at 5+) · ~5 minutes · simultaneous anti-coordination · full 36*

> **If two of you shout the same thing, you drown each other out.**

### The whole game

1. Deal **3 cards** to each player. Lay them face up in a row in front of you. Everyone can see everyone's row all game.
2. Each round, on a count of **"one — two — three — CLAMOUR!"**, every player pushes **one card** from their row forward. All at once.
3. **Every player whose shown sign is unique scores its pip.** Anyone who shares their sign with another player scores **nothing**.
4. Turn every pushed card over and slide it back into your row. It now shows its partner sign.
5. Play **nine rounds**. Highest total wins.

That is the complete ruleset. There is no deck, no discard, no draw, no turn order, no hand.

### Teaching script (~30 seconds, timed)

> "Every card has two signs, one per side, and each sign is worth its number — Moon 1 up to Crown 9. You've got three cards face up; that's everything you'll ever have. On three, we all push one card forward at the same time. **You score the number you showed — unless somebody else showed the same one, and then you both get nothing.** Then your card flips over and you get its other side back. Nine rounds. Ready? One, two, three — CLAMOUR."

### Why it's exciting

The tension is entirely social and entirely legible. Crown is worth 9 and everyone can see who's holding one — which is exactly why showing it is dangerous. A quiet 4 that nobody else picked beats a Crown that two people reached for. Every round is a simultaneous read of the room, and the payoff lands as one collective noise.

**The pigeonhole moment:** at ten players there are only nine signs, so *somebody must clash, every single round*. The game gets crueller and funnier as the table grows — the deck's own arithmetic doing the work.

### What it teaches about the deck

This is the strongest gateway argument. Every round, played cards flip in full view, so the table watches pairs reveal themselves continuously: *that Crown was a Crown/Wave; that Star was a Star/Moon*. By round three, players have internalised "each card is a pair, and every pair exists once" without anyone explaining it — which is exactly the understanding GLEAN, BLIGHT and ICARUS all assume on arrival.

### Floor simulation (`gateway_concepts_sim.py`, 8,000 games per configuration)

| Players | Skilled vs. random | **Room-reader vs. a greedy table** | Clash rate | Avg score / 9 rounds |
|--:|--:|--:|--:|--:|
| 3 | 1.33× | 1.07× | 24% | 43 |
| 4 | 1.32× | 1.17× | 35% | 36 |
| 5 | 1.32× | **1.25×** | 43% | 31 |
| 6 | 1.33× | **1.35×** | 51% | 26 |
| 8 | 1.34× | **1.60×** | 63% | 19 |
| 10 | 1.32× | **1.78×** | 73% | 14 |

*Clash rate and average score are measured on an all-greedy table — everyone reaching for their best front, which is how a first-time table will play.*

The load-bearing column is the third one: **the advantage of reading the room grows from 1.08× at three players to 1.80× at ten.** The bigger the table, the more everyone piles onto the high signs, and the more the player paying attention profits. This is the opposite of the usual party-game curve, and it is a direct hit on requirement 4 — CLAMOUR doesn't merely *tolerate* higher counts, it gets better at them.

**Honest caveat:** at 3P the mind-game is thin (only 32% of rounds even have a contested top sign) and the reader's edge is a negligible 1.08×. CLAMOUR should be sold as a **4+ game, ideally 5–10**. Also note 1.33× against random play is below the ~1.5× bar the collection uses for strategy games — appropriate for a five-minute opener, but it should be quoted honestly rather than dressed up.

### Falsification test

One 6-player session, three games. **It fails if:** players show their highest available sign every round without deliberating (the read isn't happening — same failure mode as WILDFIRE's refuted chaining hypothesis), *or* nobody notices the pigeonhole squeeze at high counts, *or* the simultaneous push doesn't stay simultaneous (players visibly waiting to see hands move before committing).

---

## 3. CAULDRON — don't be the one who tips it

*4–10 players · ~10 minutes · collective push-your-luck · full 36*

> **The table gambles together. Only the greediest gets burned.**

Same three-card public rows, same simultaneous push, but the drama is **shared fate**.

1. The **Brim** is **6 per player** (5 players = 30). Say it once; it never changes.
2. Everyone pushes a card. **Add up every shown pip.**
3. **At or under the Brim:** the round holds. Everyone scores the pip they showed.
4. **Over the Brim:** it **boils**. Nobody scores — and the player who showed the **highest** pip turns their card over and **loses its hidden pip**. Ties all pay.
5. Flip and return as usual.

The second reveal is the engine. When it boils, one card turns over in front of the whole table and everyone finds out what the loudest player was actually risking. Sometimes it's a 1 and they laugh; sometimes it's a Crown and the table howls. **Every card is a public number hiding a private one**, which is the deck's whole premise dramatised in a single beat.

### Floor simulation

Brim = 6 per player is the right dial — it boils **9–22%** of rounds on an undirected table and **59–73%** once everyone gets greedy. That band is exactly the tragedy-of-the-commons shape you want: restraint is stable but exploitable, and collective greed is visibly ruinous (average scores collapse from ~58 in a timid field to ~14 in a greedy one).

**But it has a real flaw, and it should not be built without fixing it.** In the first version I tried, a boil punished *everyone* equally, which meant your shown pip had no bearing on your punishment and **"always show your highest" was strictly dominant at 1.80×**. Moving the penalty onto the loudest player alone helps but doesn't cure it: greedy play still leads at **1.30–1.42×** against a random field, and at **1.77–1.81×** against a cautious one. The brake isn't strong enough yet.

Candidate fixes, none tested:

- The loudest player loses their hidden pip **and** the second-loudest scores nothing.
- A **ratchet**: each boil lowers the Brim by 1 for the rest of the game, so a greedy table strangles itself faster and faster.
- On a boil, everyone who showed **above the table average** pays.

CAULDRON is the most *fun-looking* of the three and the least *finished*. It needs a proper simulation pass before a rulebook, not just a floor probe.

---

## 4. HUSH — the sibling that inverts CLAMOUR

*4–10 players · ~5 minutes · simultaneous reveal, hidden-face scoring · full 36*

> **CLAMOUR pays the front of the card. HUSH pays the back.**

Everyone pushes a card simultaneously. Sort the shown pips: the **quieter half of the table** score their card's **hidden** pip; the louder half score nothing. So the face you show is pure exposure and the face you hide is the entire payoff — you want the low front concealing the high back, and pair-uniqueness means there is exactly **one** Moon/Crown card in the deck.

The two-beat reveal is lovely (beat one: who was quiet enough; beat two: everyone flips and the payoffs land). The collection likes declared sibling pairs — GLEAN/BLIGHT already work this way — and CLAMOUR/HUSH would be a natural second pair, same rows, same push, opposite economy.

**Verdict: works, but shallow.** The floor sim gives the best simple policy (just play your lowest front) only **1.13–1.19×** over random, and chasing the fat hidden pip regardless of exposure is properly punished at **0.79–0.80×**, so it is non-degenerate — but a 1.15× skill gap is thin even for a five-minute game. Best filed as a **variant of CLAMOUR** printed at the bottom of its rulebook rather than as its own title.

---

## 5. Cut during design: SALVO

A prize row of four face-up cards; simultaneously commit a card **showing that prize's sign** to claim it; sole claimant takes the prize and scores its hidden pip; contested prizes bounce and flip.

**Killed by its own numbers.** Requiring the shown sign to match a prize means players frequently have no legal target at all: **44–66% of player-turns were dead** with a four-card row, still 29–44% with a six-card row. A gateway game cannot have half the table sitting out. Skill gap was also negligible (1.00–1.15×). Recorded here so the idea isn't re-derived.

---

## 6. Recommendation — SUPERSEDED

> **This section recommended CLAMOUR v1. Sam refuted it before it reached a table; see §7.** The reasoning below is kept because the *error* is the useful part: every figure in §2 was true, and the design was still broken. The floor sim measured whether a skilled bot beat a random one, and never asked the prior question — whether the best play was obvious. It was.

**Build CLAMOUR.** It is the only one of the four that is simultaneously (a) explicable in thirty seconds, (b) immune to F1 by construction, (c) better at ten players than at four, and (d) actively teaching the pair structure while it plays. Its skill gap is modest but honest, and modest is correct for a five-minute opener whose real job is to make the table curious about BLIGHT.

Suggested route: draft the CLAMOUR rulebook with HUSH printed as its inversion variant, run the 6P falsification session, and hold CAULDRON back until someone has simulated a working brake.

**Lesson for the next floor sim in this collection:** a skill-gap number is meaningless until you have checked that a *pure* strategy doesn't dominate. Add an obviousness test — fictitious play, or simply "can a bot compute a risk-free move, and how often?" — before quoting any bot-vs-bot ratio.

---

## 7. REFUTED — Sam's critique of CLAMOUR, and the repair (July 2026)

Sam rejected CLAMOUR v1 on three grounds before it reached a table. All three are confirmed by simulation (`gateway_concepts_sim.py` → critique mode), and the third is fatal.

### 7.1 The critique, measured

**"If you only have low symbols it's impossible to score."** Confirmed. A 3-card row contains 3–6 distinct signs, and its best sign is your ceiling for all nine rounds:

| Your best sign | 4 | 5 | 6 | 7 | 8 | 9 |
|---|--:|--:|--:|--:|--:|--:|
| Share of deals | 0.3% | 1.4% | 4.7% | 12.2% | 27.0% | 54.3% |

**18.6% of players can never show an 8 or 9. 6.4% are capped at 6 or below for the whole game.** Roughly one player in five is structurally locked out of the top scores at the deal.

**"It wouldn't be strange for only one player to have a Crown."** Confirmed at low counts. Exactly one player holds Crown access in **36% of 3P games and 20% of 4P games** — and because a played card flips and can be flipped back, that player has a free 9 every other round with no counterplay.

**"The obvious strategy is playing the highest value card nobody else has — there is no tension."** Confirmed, and this is the fatal one. With rows public, a sign no opponent can show is risk-free money, and it exists this often:

| Players | 3 | 4 | 5 | 6 | 8 | 10 |
|---|--:|--:|--:|--:|--:|--:|
| A safe sign exists | **88%** | **73%** | **56%** | 41% | 19% | 8% |

At 3–5 players the round is a lookup, not a read.

### 7.2 Worse than stated: there is no good window

The obvious defence would be "it's fine at higher counts, where safe signs are rare." It isn't. At 8–10 players nobody has a safe sign, so everybody reaches high, everybody clashes, and the correlation between deal quality and final score falls to **r² = 0%** — not because skill took over, but because *nothing* did. CLAMOUR v1 is **a computation at 3–5 players and noise at 8–10**. There is no count at which it is a game.

### 7.3 Root cause — a self-inflicted wound

Three faults, and every concept in this document carries at least one:

| | Fault | CLAMOUR | CAULDRON | HUSH |
|---|---|:-:|:-:|:-:|
| **A** | **Fixed pool.** Your three cards never change, so your ceiling is set at the deal and a bad deal never recovers. | ✗ | ✗ | ✗ |
| **B** | **Public rows.** Everyone's option set is known, so safe plays are computable rather than read. | ✗ | | ✗ |
| **C** | **Absolute pip scoring.** High signs are strictly better, so Crown is always the right answer. | ✗ | ✗ | ✗ |

Fault B was self-inflicted. I made the rows public to defeat [F1](Playtesting/DECK_PLAYTEST_FINDINGS.md) — but F1 is a finding about **9–14 card hands with no sort axis**. Three cards need no sorting and no fanning. The ergonomic problem I was solving does not exist at this hand size, so I traded the game's entire tension for nothing.

### 7.4 The repair — *show one face to survive, score the other*

One structural change kills all three faults:

1. **Hidden hand of three.** Costs nothing at this size, and restores the uncertainty that a simultaneous-reveal game runs on. *(kills B)*
2. **You choose the card *and which way round to play it*.** The face you **show** settles the clash; the face you **hid** is what you score. Showing Crown now earns you only its low partner — the loudest voice is the cheapest payoff. *(kills C)*
3. **Unique shown sign → score your hidden face. Clashed → nothing.**
4. **Pass the played card to your left afterwards.** Cards circulate, ceilings move, and you choose what to arm your neighbour with. *(kills A)*

**Evidence it works.** Fictitious play over the shown-sign distribution converges to a **mixed strategy at every player count** — no sign is chosen more than 13–14% of the time:

| Players | Most-played sign | Verdict |
|---|--:|---|
| 3 | 14% | mixed |
| 5 | 14% | mixed |
| 10 | 13% | mixed |

A pure strategy would show one sign near 100%. There is no obvious play left to compute. Note the shape: signs 7–9 are shown *least* (3–11%), because showing a high sign means banking a low one — exactly the inversion fault C needed.

Passing closes the deal-determined score gap by **59–80%**:

| Players | Best/worst final score, keeping your cards | Passing left | Gap closed |
|---|--:|--:|--:|
| 4 | 78 / 37 | 67 / 59 | 80% |
| 6 | 79 / 13 | 63 / 45 | 72% |
| 8 | 79 / 1 | 58 / 32 | 66% |
| 10 | 79 / 0 | 52 / 20 | 59% |

The two-beat reveal also falls out for free: push forward (*who got drowned out?*), then everyone flips at once (*and here's what it was worth*).

**Still unverified:** whether "show one face, score the other" survives contact with a first-time player's brain. It is one more idea than v1 had, and the brief's first requirement is a thirty-second teach. That is the falsification test now.

---

---

# Part Two — the second attempt (July 2026)

## 8. What the first attempt got wrong at the root

The whole of Part One shares one assumption: **each player is dealt a small private endowment and plays out of it.** That is what produced every fault in §7.3 — a fixed pool means a fixed ceiling, private pools mean asymmetric ceilings, and asymmetric ceilings mean a deal can decide the game before anyone makes a decision.

So the second attempt inverts the assumption:

> **Nobody is dealt anything. Nobody holds a card at any point. Every player faces the identical question every round.**

Under perfect symmetry a bad deal cannot exist, because there is no deal. Requirement 3 (no card management) is satisfied absolutely rather than approximately, and requirement 4 (higher player counts) becomes free — headcount stops touching the card economy entirely.

The remaining question is what players *do*, if not play cards. The answer this deck supplies better than any other: **they bet on what's on the other side.**

---

## 9. VERDICT — REFUTED (see §11) — the table passes judgement on a hidden face

*3–10+ players · ~5 minutes · simultaneous odds-betting · full 36 · no components beyond the deck*

> **Higher or lower? Thumbs on three. Then we turn it over.**

### The whole game

1. Shuffle. Deal nothing. Nobody holds a card at any point in this game.
2. Turn the top card face up in the middle — the **Accused**. Its visible sign is the **Charge**.
3. On a count of three, everyone commits at once: **thumb up** if the hidden face is *higher* than the Charge, **thumb down** if *lower*.
4. **Turn the Accused over.**
5. Everyone who was right scores **one point for every player who was wrong**. Everyone who was wrong scores nothing.
6. Lay the card aside face up and turn up the next. Play **twelve rounds**; highest total wins.

One rule to remember beyond that: **if the Charge is Moon or Crown, turn the card over and use the other face** — a Moon can only be hiding something higher and a Crown something lower, so there is no question to answer.

### Teaching script (~20 seconds)

> "Every card has two signs, one on each side, numbered 1 for Moon up to 9 for Crown. I turn one up — this one's Wave, that's a 3. The other side is one of the eight signs it *isn't*. So: higher, or lower? Thumb up or thumb down, everyone together, on three. Then I flip it. If you're right, you score a point for every person who got it wrong. Twelve rounds."

### The odds are printed on the card

Because every pair of signs appears exactly once, a card showing sign **S** has its hidden face spread evenly across the other eight signs. So:

> **P(higher) = (9 − S) ÷ 8**

| Charge | Moon | Leaf | Wave | Flame | **Eye** | Mask | Key | Star | Crown |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P(higher) | *turn it* | 87.5% | 75% | 62.5% | **50%** | 37.5% | 25% | 12.5% | *turn it* |

Nothing to memorise, nothing to consult — the pip **is** the odds table. A new player can compute their bet correctly on the first round of their first game by counting how many signs sit above the one they can see. Eye is a perfect coin flip, which makes it the round the table dreads.

### Why it's exciting

The payoff is **the size of the table's mistake**. Being right when nine people were wrong is worth nine points in a single gesture — so the drama isn't the bet, it's watching the thumbs come up and realising you're alone. And because piling onto the favourite destroys the favourite's payoff, the obvious answer is never safe: a Leaf is 87.5% to go higher, and precisely because everyone knows that, the four people who called lower and hit will lap the table.

### Simulation (`verdict_sim.py`)

**Obviousness test, run first this time.** Fictitious play on the fraction of the table calling higher converges on the **true odds** at every player count — 85% where the odds are 87.5%, 52% where they are 50%, 15% where they are 12.5%. It does not converge on a fixed answer. There is no pure strategy to look up, which is exactly the check CLAMOUR v1 failed.

**Skill gap, three tiers:**

| | 4P | 6P | 10P |
|---|--:|--:|--:|
| Reading the pip, vs. guessers | 1.54× | 1.44× | 1.39× |
| Playing contrarian, vs. a table that all reads the pip | 1.44× | 2.47× | **4.39×** |
| Anything, vs. the mixed equilibrium | 1.11× | 1.04× | **1.00×** |

That is the gradient a gateway wants: a beginner who just reads the pip immediately beats a guesser and *feels competent*; a table that all plays the obvious line is savagely exploitable; and at equilibrium nothing dominates, so the game is **playable on sight but not solvable**.

**Skill survives the length.** An odds-reader against a table of guessers wins far more than their fair share, and more so the longer the game:

| Players | Fair share | 9 rounds | 12 rounds | 16 rounds |
|---|--:|--:|--:|--:|
| 4 | 25% | 53.7% | 60.5% | 66.4% |
| 6 | 16.7% | 42.8% | 50.2% | 56.2% |
| 10 | 10% | 32.1% | 37.3% | 44.3% |

Twelve rounds is the sweet spot for a five-minute game; sixteen if the table wants a firmer result.

### What it teaches

Everything the rest of the collection assumes on arrival, in one loop: that a card is a **pair**, that signs carry a **fixed rank**, that flipping is how a face is **revealed**, and that the every-pair-once registry makes hidden information **countable rather than mysterious**. A player who has finished twelve rounds of VERDICT has been *using* the deck's mathematics, not merely watching it.

### Deck-nativeness

"What's on the other side?" is the one question that exists only because of this deck — an ordinary card has a blank back, so the question has no content and no odds. Here it has both, exactly.

### Optional layers (keep out of the base game)

- **Counting the record.** Resolved cards are laid face up, and each one seen removes a candidate — a Wave can't be hiding Crown if the Wave/Crown card is already down. Worth **1.39–1.54×** over guessing on top of the printed odds. Deliberately optional: requiring it would violate "easy to remember."
- **The Herald.** The previous round's winner chooses the next Accused from a row of four face-up cards, and can hand the table a nasty Eye.

### Honest risks

1. **A binary thumb may be too thin a decision** across twelve rounds. This is the real falsification question, not the maths.
2. **The signature moment thins out at high counts** — one player against the whole table happens 16.4% of rounds at 4P but only 4.5% at 10P (about once every two games), though it pays 9 when it lands.
3. **Adjacency.** FACE VALUE (2P hidden-pip betting) and FORKED TONGUE (claims about hidden faces) occupy neighbouring ground. VERDICT is distinct — mass simultaneous betting on honest public odds, with no bluffing and no hands — but the family resemblance should be acknowledged rather than discovered later.
4. **Runaway leader** untested; scores compound and nothing catches up.

### Falsification test

One 6-player session, twelve rounds, then ask whether they want a second game. **It fails if:** the table stops deliberating and just thumbs the favourite every round (the decision isn't real), *or* players can't compute the odds off the pip unaided by round three (the teach failed), *or* the whole thing reads as a coin-flip guessing game despite the numbers saying otherwise.

---

## 11. REFUTED — VERDICT, and the failure mode behind both attempts (July 2026)

Sam rejected VERDICT on sight. All four objections hold.

### 11.1 "Everyone would do exactly the same thing"

Worse than stated. Score is *1 point per player who was wrong*, so if the table agrees, the wrong-count is either zero or everyone — and either way **nobody scores anything at all**:

| Players | Final score after 12 rounds, everyone playing the obvious read | Unanimous rounds |
|---|--:|--:|
| 4 | **0.00** | 67% |
| 6 | **0.00** | 67% |
| 10 | **0.00** | 67% |

The scoring is entirely parasitic on disagreement, and the odds are public and trivially computable, so the table converges immediately. The game pays out only when players are confused.

### 11.2 "I can't see how contrarian beats the obvious read"

Correct — it doesn't. The 4.39× figure in §9 is an artifact of a **frozen opponent model**: a bot that keeps making the same call while one player exploits it. The edge evaporates the moment anyone copies it:

| Contrarians at a 10P table | Their pts/round | Obvious-read pts/round |
|--:|--:|--:|
| 1 | 2.94 | 0.67 |
| 2 | 2.61 | 1.35 |
| 3 | 2.30 | 2.01 |
| 4 | 1.96 | 2.70 |
| 5 | 1.64 | 3.36 |

What survives at equilibrium is not a read but an instruction to **randomise with probability (9−S)/8**. That is a die roll wearing a decision's clothes. My "obviousness test" checked that no *pure* strategy dominates and I wrongly treated that as proof a decision exists — a mixed equilibrium with no private information and no tells has no decision content whatsoever.

### 11.3 "You could play this with a normal deck"

Decisive, and it should have been checked first:

| | Double-faced deck | Normal 52-card deck |
|---|---|---|
| Player's procedure | read pip → P(higher) = (9−S)/8 → call | read rank → P(higher) = (13−R)/12 → call |

Structurally identical. Pairing, flipping and the every-pair-once registry change **not one decision**. VERDICT fails [PROJECT_GOALS.md](PROJECT_GOALS.md) evaluation criterion #1 — *"Does the game need this deck?"* — and criterion #2, *"Is flipping meaningful?"*

### 11.4 "Players aren't even interacting with the cards"

Also correct, and self-inflicted. §8 concluded that private endowments caused the deal-locked ceilings, and I over-corrected from *"players shouldn't own cards"* to *"players shouldn't touch cards."* For a game whose entire purpose is to introduce a **deck**, hands that never touch a card is a contradiction in terms.

### 11.5 The actual failure mode — twice now

| | Metric it passed | What it actually was |
|---|---|---|
| CLAMOUR | 1.33× skill gap vs. random | Best move computable; free money 88% of turns at 3P |
| VERDICT | No pure strategy dominates | Optimal play is a die roll; deck irrelevant |

Both times the simulation **proposed** the design and I optimised toward a measurable property instead of designing for a decision a human wants to make. Simulation is a filter, not a generator — it can refute, but it cannot invent, and a design tuned to satisfy it will satisfy it while being unplayable.

**Gate to apply before any future candidate is written up, in this order:**

1. **Deck-necessity.** Describe the player's procedure. Would it change at all on a normal deck? If not, stop. *(criteria #1 and #2)*
2. **Hands on cards.** Do players physically pick up, place, or flip cards? If not, it is not introducing this deck.
3. **Ten-second read.** Say the core decision aloud. Does an obvious answer appear immediately? If so, stop.
4. **Convergence.** If the whole table plays well, does anything still happen? *(VERDICT scored 0.00.)*
5. *Only then* simulate — and simulate to refute, not to justify.

---

---

# Part Three — does WILDFIRE v1.2 actually meet the brief? (July 2026)

The gateway search ended by abandoning new designs and repairing WILDFIRE instead ([WILDFIRE_excitement_diagnosis.md](../Wildfire/WILDFIRE_excitement_diagnosis.md), rulebook v1.2). This section scores the result against Sam's original six requirements rather than against itself. **It passes three, partially meets two, and fails one outright.**

| # | Requirement | Verdict |
|--:|---|---|
| 1 | Quick to explain | ⚠️ **Slightly worse than v1.1** |
| 2 | Easy to remember | ⚠️ **One fragile clause** |
| 3 | No awkward hand/card management | ❌ **Worse, and unfixable without giving back the decisions** |
| 4 | Easily adaptive to higher player counts | ❌ **Fails — it is a 3–5 game** |
| 5 | More exciting than v1.1 | ✅ **Clear pass** |
| 6 | Introduces the deck, excites for other games | ⚠️ **Teaches flipping and pairs, teaches rank not at all** |

## 13. Scoring v1.2 against the six requirements

### 13.1 Requirement 5 — excitement: passes

The thing Sam originally complained about is fixed. No-decision turns fall from **70% to ~40%**, legal plays per turn from 1.11 to 2.06, and the Mirror fires on **6.4–6.8% of turns — about 2.2–2.6 skips per game**, which is frequent enough to be a feature of every session and rare enough to stay an event. This is the requirement the work was aimed at and it lands.

### 13.2 Requirement 3 — hand management: v1.2 makes it *worse*

[F1](Playtesting/DECK_PLAYTEST_FINDINGS.md) is explicit that the pain is a **per-turn re-scan**, not a one-time sort: "every time a sign is led, each follower must check *both faces* of every card." **Two targets doubles what you are scanning for.** Every turn, against every card, against two symbols instead of one.

Cutting the deal to compensate immediately gives back the decisions it was meant to buy:

| 3P deal | Avg hand in play | Legal plays | Turns with a choice |
|--:|--:|--:|--:|
| 9 (shipped) | 4.8 | 2.04 | **58%** |
| 7 | 4.1 | 1.73 | 51% |
| 5 | 3.5 | 1.46 | **43%** |

**Hand size *is* the option supply.** Requirements 3 and 5 are in direct opposition in this design — not a tuning problem, a structural one. v1.2 chose excitement; it did not solve hand management and cannot without reversing itself.

*(One consolation: average hand held during play is 3.5–4.8, not 9. The pain is front-loaded at the deal and after refusals, not constant.)*

### 13.3 Requirement 4 — higher player counts: fails

Sam asked for **8–10 players**. WILDFIRE runs at those counts without stalling, but the experience collapses:

| Players | Deal | Legal plays | No play | Turns each, whole game | Turns you wait |
|--:|--:|--:|--:|--:|--:|
| 6 | 5 | 1.58 | 19% | 5.7 | 5 |
| 8 | 3 | 1.21 | 27% | 2.9 | 7 |
| 10 | 3 | **1.20** | **26%** | **2.6** | **9** |

At ten players you take **under three turns all game**, wait nine turns between them, and hold ~1.2 legal plays when your go arrives — back to the v1.1 decision drought the whole exercise was meant to cure. The cause is the 36-card economy: more players means smaller hands means fewer options, and no rule change escapes it.

**WILDFIRE v1.2 is a 3–5 player game** (6 is acceptable). It is not, and cannot become, the 8–10 player opener from the brief.

### 13.4 Requirements 1 and 2 — teaching: a small regression and one fragile rule

Counting rule beats in the teach:

| v1.1 | v1.2 |
|---|---|
| match the target · flip it · chain up to 2 · can't match → draw 2 · announce at one card | match **either** target · flip it · can't match → draw 2 · **Mirror skips the next player** · **the skipped player flips a pile** · announce at one card |
| **5 beats** | **6 beats** |

Dropping chaining removed a rule, but Mirror added two. The June session's best result was *zero rule clarifications*, and that is now at risk.

The weak point is **"the skipped player turns over a pile."** It is an exception attached to an exception, the least memorable thing in the rulebook — and forgetting it is not harmless: without it the mirrored targets persist and dead turns rise from 17% to 25%. A rule that is easy to forget and damaging when forgotten is the one to watch at the table.

### 13.5 Requirement 6 — the gap nobody has flagged: WILDFIRE teaches no rank

WILDFIRE uses the nine signs purely as **symbols**. It never reads a pip. Moon is not 1 and Crown is not 9 in this game — they are just two of nine shapes.

But [F4](Playtesting/DECK_PLAYTEST_FINDINGS.md) records that after the June session a player carried a misunderstanding of *sign = rank* through an entire GLEAN game, "which materially affected their play." And rank is load-bearing in **BLIGHT, GLEAN, FACE VALUE, DOWRY, ICARUS and THE UNPLAYED PAIR** — most of the collection's strongest titles.

**So the gateway game omits precisely the concept whose absence damaged the follow-on session.** It hands players three of the deck's four ideas — two faces per card, flipping as the action, every pair exactly once (which the Mirror teaches beautifully: *only one card in the deck can do that to you*) — and silently skips the fourth.

This is the most actionable finding in the evaluation, and it is cheap to address: a scoring variant that reads pips (**Last Light** already scores minus-1 per card and could score minus-pip instead), or simply a line in the teaching script. Neither has been tested.

### 13.6 Verdict

**v1.2 fixes the problem Sam named but does not satisfy the brief he set.** As a 3–5 player opener it is now materially better than v1.1 and worth putting on a table. As *the* introduction for a group of new players it has two real gaps: it does not go to 8–10, and it does not teach rank.

Whether that matters depends on the actual use case. If new players usually arrive in threes and fours, v1.2 is the answer and only the rank gap needs closing. If the target is a party of eight, WILDFIRE is structurally the wrong vehicle and Part One's brief is still open — with §11.5's gate now available to stop the next attempt failing the same way.

---

## 14. Open questions for the table

1. Does the simultaneous push **stay** simultaneous, or do players hedge on each other's hand movements? (If it drifts, the fix is a spoken count everyone commits on.)
2. Are three cards enough choice, or does the round feel forced? (Dial: four cards, still trivially manageable, still fits 9 players.)
3. Do **public rows** make the read richer, or does perfect information flatten it into arithmetic? (Dial: hold the three cards instead — still no sorting problem at that size.)
4. Does a five-minute game read as "let's go again" or as "was that it?"
5. Does CLAMOUR actually hand players off to the rest of the collection better than WILDFIRE did — i.e. after playing it, do they understand pairs, pips and flipping well enough to start BLIGHT cold?

---

*Simulation code: [gateway_concepts_sim.py](gateway_concepts_sim.py). All figures are floor simulations with simple bots — they certify that the rules terminate, scale and are non-degenerate. They say nothing about whether the table laughs, which is what the falsification session is for.*
