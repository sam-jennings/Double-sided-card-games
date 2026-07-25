---
record_type: game
game: "WILDFIRE"
state: Ready to test
players: [3, 4, 5, 6]
player_count: "3, 4, 5, 6"
duration: "~10 min"
genre: "Party shedding"
complexity: Light
min_players: 3
max_players: 6
min_minutes: 10
max_minutes: 10
physically_playtested: true
public_document: "Wildfire/WILDFIRE_rulebook.md"
next_step: "Table-test v1.2 — two piles, no chaining, Mirror."
catalog_order: 5
---
# WILDFIRE

*A shedding race for 3–6 players · ~10 minutes · ages 8+*

*(Developed from the concept formerly called HOT POTATO PAIRS.)*

Two fires burn in the middle of the table. Match either one, slap your card down — then **turn it over**, and whatever appears is the next player's problem. Empty your hand first; leave the wreckage to the table.

And if you can make both fires show the same sign, the player on your left doesn't get a turn at all.

---

## Components

The **36-card** master deck. Your own hand may be examined (both sides) at any time.

## Setup

1. Shuffle thoroughly, flipping random chunks.
2. Flip **two** cards to the middle as the two **piles**. Each pile's visible symbol is a **target** — there are always two live targets. Each pile grows as a **loosely overlapping line** (every play covering only part of the card before), so past faces stay visible: the piles *are* the game's public history, and that only works if they aren't squared into stacks.
3. Deal hands: **3P: 9 · 4P: 7 · 5P: 6 · 6P: 5**.
4. Stack the leftovers face-up beside the piles as the **well** (3P: 7 · 4P: 6 · 5P/6P: 4).
5. Left of dealer starts. Play clockwise.

## Your turn — match and turn

Both piles show a target. **One card per turn.**

1. **Match:** play a card from your hand onto **either** pile, showing that pile's target symbol — either side of any card can do the showing, and flipping a hand card around to match is the whole point.
2. **Turn:** immediately turn your played card over where it lies. Its other symbol now shows — that pile has a new target.

**Can't match either — or won't?** Take the top **2 cards of the well** into your hand instead. (Well empty? Lift the newest card off the taller pile and set it aside, gather the rest of that line into a stack, flip it over and square it as a fresh well, then lay the newest card back down — targets don't change. Draw your 2 from the new well.)

## Mirror

If, when your turn ends, **both piles show the same symbol**, you have set a **Mirror** — and the next player **misses their go**.

They aren't quite helpless: as they skip, they **turn over the top card of either pile**, which breaks the Mirror and leaves a new target of their choosing. Then play passes on.

Only one card in the whole deck can ever do this. If the piles show Moon and Crown, the Moon/Crown card is the only card carrying both — play it on either pile and it turns to face its twin. Watch what the fires are showing, and check whether you're holding the key.

## Going out

When you're down to **one card**, announce **"Wildfire!"** as you end that turn. Forget, get caught before your next turn, and you take 2 from the well.

Play your last card (match and turn, as ever) and you **win**. The rest may keep playing for the silver medals.

## Edge cases & FAQ

**Do I choose which face to play?** No choice needed: the face you show *must* be that pile's target. The decision is *which card, onto which pile* — i.e. which new target you leave behind. That's the game: every card in your hand is an exit door from one symbol to one specific other.

**Can I play one card onto both piles?** No — one card, one pile, one turn.

**What if both piles show the same symbol at setup?** Turn one of them over and start.

**Can a Mirror skip someone twice running?** No. The skipped player breaks it by turning a pile over, so the next player always faces two different targets.

**What if I make a Mirror by accident?** It still counts. The fires don't care what you meant, and neither does the player on your left.

**Can refusing make a Mirror?** No — taking cards from the well doesn't change either target.

**What's in the well is public.** The well sits face-up; the top card is visible. You always know what a refusal will cost you.

**Can I count cards?** Please do. Eight cards carry each symbol; the piles show the whole history of play, face by face, and the well is public. There is nothing to memorise — only things to notice.

## Strategy notes (read after your first race)

- **Check for the key every turn.** Look at the two targets and ask whether you hold the one card carrying both. It's the only free hit in the game.
- **Two fires, two exits.** Your real choice is which pile to feed, because that decides which of the two targets survives. Leave a symbol the table is visibly short of and you tax everyone after you.
- **Don't hand them the key.** The target you leave, paired with the other pile's target, names exactly one card. If it hasn't been played yet, you may just have armed your left-hand neighbour.
- **The well is a clock.** When it runs dry, refusals start eating the piles — and the piles' history is everyone's card count. The endgame is faster and meaner than the start.
- **Watch who refuses what.** A refusal means *neither* target is in their hand — sixteen cards just got easier to place around the table.

## Variants

- **Inferno** (once the table knows the deck): chain up to **two** cards per turn, matching and turning each. Roughly halves the race — about three minutes — and rewards the sharpest player harder. The right answer for a six-player table that wants more bite.
- **Slow Match** (with younger players): refusals take **1** card instead of 2. Gentler, and slightly quicker. Drop Mirror as well for the very youngest — it costs about a turn and a half per player and it's the one rule that punishes someone who did nothing wrong.
- **Salvage** (softer refusals): when you are *forced* to refuse, after taking your 2 cards you may immediately play **one** card matching either target. A bad draw stings less. Recommended 3–4P.
- **Last Light** (scored match): when someone goes out, others score minus-1 per card in hand; play rounds equal to the player count, rotating dealer. Least negative total wins.
- **Classic** (the v1.1 game): one pile, chain up to two, no Mirror. Faster and flatter — kept because it is what the June 2026 table actually played.

*All five simulated at 3P/4P/6P: zero stalls, dead turns 15–23%.*

---

*Design v1.2 (July 2026). Two structural changes and one rule addition, all driven by the first table test's verdict that the game "felt reactive rather than strategic" — see [WILDFIRE_excitement_diagnosis.md](WILDFIRE_excitement_diagnosis.md) and [wildfire_decision_sim.py](wildfire_decision_sim.py).*

*The diagnosis: at one pile, a card matched the target only 2/9 of the time, so a player averaged **1.11 legal plays per turn** — on about a third of turns they could not play at all, and on another third exactly one card fitted. **Roughly 70% of turns contained no decision.** The v1.1 balance was sound; there was simply nothing to decide.*

***Two piles** doubles legal plays to 2.12 and cuts do-nothing turns from 34% to 17%. **Dropping chaining** is possible only because of that: chains existed as the exhaust valve for a refusal pump that two piles largely switches off, and removing them restores the pacing that two piles alone would have halved (12.8 turns per player at 3P, against v1.1's 13.7). One rule fewer, twice the choices, the same length, zero stalls at every count.*

***Mirror** was adopted on design judgement against a metric, and the disagreement is recorded rather than hidden. It lowers the simulated skill gap from ~1.46× to ~1.30×, because the chance to mirror is gated by holding one specific card and so pays out on luck. It is in the game anyway: it is the only immediate, visible, aimed consequence in a design whose every other lever is delayed and diffuse, and a player who feels they influenced the table is most of what a party game is for. The figure it costs is measured against a bot that reads everyone's hand — see [Project/SKILL_GAP_METHOD.md](../Project/SKILL_GAP_METHOD.md) for why that number should not be deciding games.*

*Still untested at a table. The question for the first session: does anyone choose a card **because of the target it leaves**, unprompted?*
