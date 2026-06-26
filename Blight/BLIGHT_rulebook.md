# BLIGHT

*A trick-taking game of dodging the rot for 3, 4, or 6 players · ~25 minutes · ages 10+*

Every card hides a sign — and in BLIGHT, the hidden sign is the rot. Win a trick and you don't gather a prize; you swallow everything the table was concealing. The card that *looks* harmless — a quiet Moon showing — may hide a Crown that costs you nine. Take as little rot as you can. Or, if you're bold and the cards are with you, swallow it **all** and walk away clean while everyone else chokes.

*BLIGHT is the dark sibling of **GLEAN** — the same trick engine, the opposite goal. In GLEAN you fight to win tricks; here you fight not to.*

---

## Components

- The **36-card** master deck (9 signs; every pair on exactly one card). The corner **index pips (1–9)** are the ranks: Moon 1, Leaf 2, Wave 3, Flame 4, Eye 5, Mask 6, Key 7, Star 8, Crown 9.

## Setup

1. Shuffle thoroughly, **flipping random chunks**.
2. Deal the **entire deck** out evenly:
   - **3 players:** 12 each. · **4 players:** 9 each. · **6 players:** 6 each.
   - *(5 players: set one card aside face-up as a dead card and deal 7 each.)*
3. Examine your hand freely, **both sides**, all game.
4. BLIGHT is played as a **match of one round per player**, rotating the first lead clockwise each round. **Lowest total penalty across the match wins.**

## How a trick works

*(Identical to GLEAN — the goal is what differs.)*

The leader plays any card, choosing **which face shows**; that sign is the **led sign**. Each other player must **follow** — play a card carrying the led sign on either face, flipping if necessary to show it. If you can't, **slough** any card, any face. *(Sloughs can't win.)*

**The reveal.** Flip every card in the trick. Among the followers, the **highest revealed (hidden) pip wins** — ties impossible. The winner takes the trick.

> What wins is the strength you hid. In BLIGHT, winning is exactly what you're trying to avoid.

## Taking the rot

When you win a trick, gather its cards into your **rot pile** — but **flip each captured card to its hidden (penalty) face up**. Your rot pile always shows the poison faces, so your penalty is simply the **sum of the pips showing in your pile**. Nothing to remember: the orientation records the rot.

The winner leads the next trick.

## Scoring a round

Each player's penalty for the round is the **total of the pips in their rot pile** (the hidden faces of every card they captured). **Lower is better.**

### Shoot the rot

If a single player **wins every trick in the round**, they have *shot the rot*: they score **0**, and **every other player scores the round's entire penalty total**. A desperate, glorious gamble — rarely on, never forgotten. *(The simulation confirms it: even a player actively trying succeeds in only about 1% of rounds. Treat it as a legend you occasionally chase, not a plan.)*

Add up penalties across the match. **Lowest total wins.** Tiebreak: fewest tricks won; then earliest in turn order.

## Edge cases & FAQ

**Must I follow if I can?** Yes — any card carrying the led sign on either face obliges you to follow, showing that sign. An illegal slough is exposed at the reveal.

**Which follower should I play?** The craft of BLIGHT. To lose safely, play a card whose hidden pip is below whatever's already winning the trick — and shed your *most dangerous* card while you're at it. If you can't lose, lose as cheaply as you can.

**I'm void — what do I slough?** Your worst poison. Show a card's **low** face so its **high** face (the penalty) lands in the winner's pile. Handing a rival your hidden Crown is the game's quiet knife.

**Why is winning bad?** The trick winner swallows every hidden face in the trick, including their own high card. You score by *not* winning — or by winning only cheap, low-rot tricks.

**The Moon/Crown card.** It shows a harmless Moon (1) so it ducks tricks easily — but if you ever get stuck winning with it, its hidden Crown costs you 9. The lowest-looking card hides the worst rot.

**Can the rot pile be inspected?** Yes — all rot piles are public and examinable, both sides, any time. (The penalty faces are already up.)

## Strategy notes (read after your first game)

- **Lose on purpose, but shed while you do it.** A trick you can't win is a chance to dump your highest hidden pip safely. Wasting a safe loss on a low card is a mistake.
- **Lead low-hidden.** Lead by showing a card's **high** face so its hidden pip is small — you probably won't win your own lead, and you set the sign.
- **Track the Crowns.** Eight cards hide big pips. Knowing who still holds rot — and forcing them to eat it — is the whole late game. Everything is public; count, don't remember.
- **The shoot lurks.** If one player keeps winning, they may be going for the rot — and one trick handed to someone else ruins it. Break a shoot the moment you smell it.
- **Voids are weapons and traps.** Being void lets you dump poison — but it also means you can't steer that sign's tricks. Engineer your own voids early.

## Variants

- **Only Crowns Bite (first game):** penalty is just the **number of Crown faces** you capture on hidden faces (8 in the deck), like Hearts' "only the Queen." Add full hidden-pip scoring once the dodging rhythm clicks. *(Teaching scaffold; the full hidden-pip game is the simulation-validated one.)*
- **The Passing:** pass 3 cards left each round before play to soften unlucky hands.
- **Partners (4P/6P):** fixed teams sitting alternately; combine penalties (lowest team total wins). Shooting the rot scores 0 for the *team*.

---

*Design v1.0 — simulation-validated (`blight_sim.py`; ~4,000 rounds per player count, seed 42), untested at the table. Skilled play beats random by **2.02× (3P) / 1.91× (4P) / 1.41× (6P)** — the steepest skill gap of the trick-taking siblings at 3–4P, thinner at 6P (the lighter, higher-variance option). Seat fairness is excellent (near-flat across seats). Shoot-the-rot occurs in ~0% of skilled games and ~1% even when attempted — a live but rare gambit. The hidden-face-is-penalty design means the rot pile must be stored **penalty-face-up** (orientation as state) so nothing is remembered — a deliberate fix for the deck's hidden-face memory trap. **Caveats for the first table test:** does ducking create satisfying agony or passive low-card-dumping? Does eating a surprise hidden 9 read as drama or a gotcha? Is the shoot threat exciting even at ~1% realisation? Sibling: **GLEAN** (same engine, accumulation goal).*
