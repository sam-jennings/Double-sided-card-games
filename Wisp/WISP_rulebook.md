# WISP

*A hidden-movement pursuit for 2–3 players · ~20 minutes · ages 10+ · one Wisp vs. a side of one or two hunters*

> **⚠️ v0.1 — first-draft rulebook, unsimmed and untested (July 2026).** WISP was written to the wildcard-batch brief: *originality first, rubric waived, no simulation required* (see [WISP_concept.md](WISP_concept.md) and [NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §18). This document turns that concept into playable rules — it does **not** mean the balance is proven. The dials (hand 12 · raids 4 · escape 8 · sprints 2) are the concept's starting numbers, not tuned values. The one open handling question is physical: whether an eight-card overlapped trail plus a squared sprint packet excavates cleanly without slippage. Table this game to answer it. See the design footer for the fastest way to falsify it.

Every hidden-movement game — Scotland Yard, Fury of Dracula — needs a way to write a secret down: a notebook, a hidden track, a screen. This deck has none of those. It has something better. A card has two faces and no back, so the moment you lay it down it tells everyone one thing and hides exactly one other. WISP makes the trail itself the notebook: each card you drop announces the place you **just left** and presses the place you're **at now** to the table. The hunters always know where you *were*. They are always one move behind where you *are*. And when the chase ends, the whole trail is dug up in reverse and every card confirms every other — so the fugitive cannot have lied, ever, about anything. No board, no pencil, no trust.

---

## The signs are places

In WISP the nine signs are nine **places** — waypoints the Wisp drifts between. Nothing ranks above anything; **Crown** is just a place, **Moon** is just a place. The pip numbers (1–9) exist only to sort the atlas quickly. Every pair of places is joined by exactly one **road** — and that road *is* the single card carrying both their signs. Nine places, thirty-six roads: the map is the whole deck, so there is no board to print. It's already in the box.

## Components

- The full **36-card** master deck. That's every road: each of the 36 pairs of signs appears on exactly one card, and each sign sits on exactly 8 roads.
- Nothing else. No board, no pawns, no paper.

## Roles

- **The Wisp** — one player, the fugitive. Holds a hand of roads and drifts along the trail, trying to survive.
- **The hunters** — one player (2-player game) or two players sharing one side (3-player game). They see everything the table shows, deduce where the Wisp is, and spend a small budget of **Raids** trying to name the Wisp's current place.

In a match, rotate the Wisp role each game so everyone drifts and everyone hunts.

## Setup

1. Shuffle all 36 cards, flipping chunks as you go so faces are mixed.
2. Deal the **Wisp a hand of 12** cards. The Wisp holds these as a fan and may inspect **both faces** of every card freely — a held fan is genuinely private (nobody else may look at it), so this is the deck's one clean secret.
3. Spread the remaining **24 cards face-up as the atlas**, sorted by pip so any road is easy to find. The atlas is fully public: the hunters may pick up and read **both faces** of any atlas card at any time.

That spread is the engine of the whole game. Thirty-six roads exist; twenty-four are lying in the atlas; therefore **the Wisp's twelve are exactly the roads that are not**. The hunters know the Wisp's entire hand by subtraction — every road it could ever travel. What they do not know is the **order** it will travel them, and above all **where it is right now.**

## The one idea, in one turn

A road card names two places. When the Wisp travels it, the card goes onto the trail **showing the place left behind** and **pressing the place just arrived at** to the table.

- **Top (visible) face = where the Wisp *was*** — public.
- **Bottom (pressed) face = where the Wisp *is now*** — hidden.

Lay the trail as an **overlapping row** (the CROSSROADS technique), each new card set down to the right, half-covering the one before, so every card's top face reads at a glance and every card's pressed face stays flat against the table. **Never square the cards into a stack** (except a sprint — see below).

Now watch the chain. When the Wisp takes its *next* road, the new card's visible (departed) face **must be the place it's now leaving — which is exactly the place the previous card had pressed to the table.** So laying a new card silently reveals the previous card's hidden face. The trail confirms each position **one move after** the Wisp has already gone. That lag is the entire game.

### Worked example

- **Move 1.** The Wisp plays **Moon–Wave**, showing **Moon**, pressing **Wave**. Everyone now knows the chase *started* at Moon. Where is the Wisp? Somewhere hidden — the pressed face, Wave, but the hunters can't see that.
- **Move 2.** The Wisp plays **Wave–Flame**, showing **Wave**, pressing **Flame**. The new card shows Wave — which had to equal the previous card's pressed face. So the hunters *now* learn the Wisp was at **Wave** after move 1. But it has already left: it's at **Flame** now, hidden, and they're a step behind again.

The Wisp is never asked to flip a pressed card. If it forgets its own current place it may privately tip its top card to peek — its secret, its peek.

## Legal movement

- The road the Wisp plays **must contain its current place** on one face. It shows that place (departing it) and presses the road's other place (arriving). Because you can only travel a road you hold, you can only reach places your remaining hand connects to.
- **The first move** is free of the chain: the Wisp plays any hand card, showing one face (this publicly declares the start) and pressing the other (the first hidden place).
- **No road is ever travelled twice.** Each road exists on exactly one card, and playing it spends it — so the no-backtrack rule enforces itself with zero bookkeeping. (The Wisp may still *revisit a place* by arriving on a different road.)

## The hunters' turn — Raids

The hunters have a budget of **4 Raids for the entire game** — not per turn. After each Wisp move (once the card is down), the hunters may spend **one** Raid, or hold.

To Raid, the hunters **name one place aloud.**

- If it is the Wisp's **current** place (the pressed face of the top trail card), the Wisp is **caught** — hunters win. Flip the card to prove it.
- If not, it's a **miss.** The Wisp says "miss" and reveals nothing. The Raid is spent. (A miss still teaches the hunters something: the Wisp was *not* there this turn.)

The hunters cannot lie their way to information and the Wisp cannot lie its way out of a hit — the end-game excavation (below) reconstructs every position, so a Wisp who ever answered "miss" to a true hit is exposed and loses. **No trust is required from anyone.**

Two hunters (3-player game) are a single side: they confer openly and share the one 4-Raid budget.

## How the Wisp wins, loses, or slips away

- **Escape.** The instant the Wisp completes a turn that brings the trail to **8 cards** (a sprint may carry it to nine) *and* survives the hunters' Raid that turn, the Wisp has vanished into the dark. **Wisp wins.**
- **Caught.** A Raid names the Wisp's current place. **Hunters win.**
- **Cornered.** Movement is compulsory. If, at the start of its turn, the Wisp holds **no unplayed road containing its current place**, it cannot move and is run to ground by exhaustion. It reveals its current place and hand to confirm. **Hunters win.**

Cornering is a real danger, not a formality. The Wisp holds 12 roads spread across the nine places (about 2–3 roads touch any given place on average), and it must keep an onward road wherever it lands. Drifting into a place where it has already spent its only exits is how a careless Wisp traps itself.

## Sprints — buying ambiguity

**Twice per game**, instead of a normal move, the Wisp may **sprint**: announce it, then play **two roads at once as a single squared packet** rather than an overlapped step.

- The packet's top face still shows the place being departed (the chain holds), and its bottom face still presses the final place to the table. But the **intermediate place — where the two roads meet — is buried between the squared cards and is never shown.**
- The two roads inside a sprint chain to each other (the pressed face of the first is the shown face of the second), so the packet **audits perfectly at excavation** — it just stays silent until then.

A sprint's payoff is concealment: the intermediate place is never revealed one-move-late the way a normal step is, and — because a Raid can only ever name the place the Wisp *ends a turn* on — the hunters **never get a shot at the place a sprint passes through.** The cost is real: a sprint spends two hand roads and advances the trail by two cards, so it brings escape no closer in cards than two ordinary moves would. **A sprint buys ambiguity, not speed.** Spend one exactly when the hunters are about to squeeze your candidate places down to a single answer.

## The excavation — the end-game audit

However the game ends, **dig up the trail in reverse** to confirm the Wisp played honestly. Lift the last card laid, read its pressed face, then the next, and so on back to the start. Every card's pressed face must equal the next card's shown face (and each sprint packet's two cards must chain internally). If every link matches, the record is clean — which it always will be, because the cards physically cannot be placed any other way. The point of the excavation is not suspicion; it's that the possibility of the audit is what let the hunters trust every "miss" all game without ever seeing a hidden face.

## Edge cases & FAQ

**Can the hunters really deduce the Wisp's hand?** Yes — exactly. 24 roads are face-up in the atlas; the Wisp's 12 are the ones that aren't. That's not hidden information; it's arithmetic.

**Then what's actually hidden?** The Wisp's **current place** (one pressed face) and, during a sprint, the buried intermediate. That's all — and it's enough, because you can't Raid a place you can only narrow to a few candidates.

**How do the hunters narrow it?** The top trail card shows the place just departed, say Key. The Wisp's current place is the partner of Key on whichever Key-road it just played — and the hunters know every Key-road the Wisp holds. So the candidate set is "the partners of Key among the Wisp's still-plausible roads," usually two to four places. Each new move and each missed Raid trims that set further.

**Can the Wisp pass or stall?** No. Movement is compulsory every turn. If it can move, it must; if it can't, it's cornered.

**Can the Wisp revisit a place?** Yes, by a different road. It just can't reuse a road — there's only one card for each.

**What if the Wisp forgets where it is?** It may privately tip its own top card to look. The pressed face is the Wisp's own secret; peeking at it costs nothing.

**Does the Wisp have to reach 8 cards, or can it escape sooner?** Eight is the finish line. A shorter trail hasn't escaped — the Wisp must survive long enough to lay the eighth card.

**Two roads to the same place from where I am?** Fine — you choose which to spend. Spending the wrong one early is how you corner yourself later.

## Strategy notes (read after your first chase)

**For the Wisp**
- **Shape your route toward branchy places.** Aim for places where you still hold several onward roads: a place with four live exits gives the hunters four candidates; a place with one exit tells them exactly where you are *and* where you're going next.
- **Hoard exits, spend dead ends.** A road to a place you'll never need is fuel to burn early. A road that's your only way out of a place you plan to visit is sacred — losing it corners you.
- **Time your sprints to a collapse.** The moment the hunters can trim your candidates to one is the moment to sprint through it — bury that place forever and re-emerge two steps on with the chain reset in your favour.
- **Eight cards from twelve is slack, not comfort.** You'll leave four roads unplayed; make sure the four you keep are the ones that keep you connected, not the ones you couldn't offload.

**For the hunters**
- **Raids are precious — four of them, whole game.** Don't fire into a four-way candidate set early; wait for the trail's geometry (or a forced low-branch place) to squeeze the Wisp's options.
- **Read the hand, not just the trail.** You know all twelve roads. The Wisp's *future* is bounded by which roads remain unspent — corner-hunt: steer your guesses toward places where the Wisp is running out of exits.
- **A miss is data.** It deletes one place from this turn's candidates and, combined with the next one-move-late reveal, often pins the following position. Spend a Raid partly to *learn*, not only to *win*.
- **Watch the sprint tokens.** Two sprints exist. Once both are spent, the Wisp can never again hide an intermediate — the last stretch of the chase is your clearest read.

## Variants

- **Dark (chess → poker).** Square the 24 leftover roads away **unseen** instead of spreading them as an atlas. The hunters lose the complement read and no longer know the Wisp's hand — candidate sets balloon and the game turns from deduction to nerve. Recommended only after you've played the open game.
- **The dials.** Everything is tunable at the table: **hand size** (12), **Raid budget** (4), **escape length** (8 cards), **sprints** (2). If the Wisp escapes too easily, cut a Raid or lengthen the trail; if it's caught by move three every time, add a sprint or shorten the escape. These are starting numbers, not gospel.
- **Long hunt (3-player fairness).** Play a full rotation so each player is the Wisp once; total each Wisp's surviving trail length (8 for a clean escape, the caught-at length otherwise). Highest total wins the match.

---

*Design v0.1 — drafted July 2026 from [WISP_concept.md](WISP_concept.md); unsimmed and untested by design (wildcard-batch brief). Design notes: the "no board" problem dissolves because K₉ needs no drawing — every pair of places is a card, and the card is the road. The "no way to record a secret move" problem inverts into the game's engine: a backless card records exactly one public fact and hides exactly one, so the trail is a self-writing, tamper-proof movement log that confirms position one step late. The atlas gives the hunters perfect knowledge of the Wisp's roads with zero memory load; the only secret is one pressed face, which is the Wisp's own committed move (no involuntary hidden-face bookkeeping anywhere). Sprints add a spend-to-conceal lever without adding speed. Open questions the table must answer: does the hunters' candidate arithmetic read as a tightening noose or as homework; is the base escape/Raid balance a chase or a coin-flip; and — the one genuine handling risk — does an eight-card overlapped trail plus a squared sprint packet excavate cleanly without card slippage?*
