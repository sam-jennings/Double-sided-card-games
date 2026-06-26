# WILDFIRE

*A shedding race for 3–6 players · ~10 minutes · ages 8+*

*(Developed from the concept formerly called HOT POTATO PAIRS.)*

Match the symbol, slap the card down — then **turn it over**. Whatever appears on the other side is the next player's problem. Empty your hand first; leave the wreckage to the table.

---

## Components

The **36-card** master deck. Your own hand may be examined (both sides) at any time.

## Setup

1. Shuffle thoroughly, flipping random chunks.
2. Flip one card to the middle as the **pile**. Its visible symbol is the first **target**.
3. Deal hands: **3P: 9 · 4P: 7 · 5P: 6 · 6P: 5**.
4. Stack the leftovers face-up beside the pile as the **well** (3P: 8 · 4P: 7 · 5P/6P: 5).
5. Left of dealer starts. Play clockwise.

## Your turn — match and turn

The pile's visible symbol is the **target**.

1. **Match:** play a card from your hand onto the pile **showing the target symbol** — either side of any card can do the showing; flipping a hand card around to match is the whole point. The table verifies the match at a glance.
2. **Turn:** immediately turn your played card over where it lies. Its other symbol now shows — that's the **new target**.

You may chain **up to two cards** in one turn (match-and-turn, then match-and-turn the new target — both from your own hand).

**Can't match — or won't?** Take the top **2 cards of the well** into your hand instead; turn over. (Well empty? Lift the pile's top card and set it aside, flip the rest of the pile over to form a fresh well, then set the top card back down — the target doesn't change. Draw your 2 cards from the new well.)

## Going out

When you're down to **one card**, announce **"Wildfire!"** as you end that turn. Forget, get caught before your next turn, and you take 2 from the well.

Play your last card (match and turn, as ever) and you **win**. The rest may keep playing for the silver medals; the well and pile hold out for a while.

## Edge cases & FAQ

**The same symbol can't chain twice, right?** Right — you match the target, then the card turns to its *other* symbol. Each play changes the target, always. (Each card's two faces always differ; that's the deck.)

**Do I choose which face to play?** No choice needed: the face you show *must* be the target. The decision is *which card* — i.e. which **new** target you leave behind. That's the game: every card in your hand is an exit door from the current symbol to one specific other.

**Two-card chains seem strong.** They are — they're also how you strand yourself. Chaining burns the exact bridges you'll wish you had two turns later.

**What's in the well is public.** The well sits face-up; the top card is visible. You always know what a refusal will cost you.

**Someone took the cards under the pile's top — what's the target?** Unchanged: the top card never moved. (If the well had run dry, the top card is lifted, the rest of the pile is flipped into a new well, and the top card returns — same target, replenished well.)

**Can I count cards?** Please do. Eight cards carry each symbol; the pile shows the whole history of play, face by face, and the well is public. There is nothing to memorise — only things to notice.

## Strategy notes (read after your first race)

- **Leave targets the table is poor in.** If five Moon-carrying cards are visibly spent, turning the pile to Moon taxes everyone after you 2 cards each. Cruelty is just counting.
- **Hold your doubles apart.** Two cards sharing a symbol give you a guaranteed chain later. Spending one early for tempo is usually a mistake.
- **The well is a clock.** When it runs dry, refusals start eating the pile — and the pile's history is everyone's card-count. The endgame is faster and meaner than the start.
- **Watch who refuses what.** A refusal on Flame means no card of theirs carries Flame — eight cards just got easier to place around the table.

## Variants

- **Salvage** (softer refusals, sim-checked): when you are *forced* to refuse (no card matches the target), after taking your 2 cards you may immediately play **one** card matching the target — match and turn, no chain. A drawn card that fits can leave again at once, so a bad draw stings less. Simulation (`wildfire_drawplay_sim.py`, 4,000 games/config) shows it keeps games the same length, holds seats flat and stalls at zero, and *raises* the skill edge slightly (3P 1.46×→1.56×, 4P 1.60×→1.68×) — it rewards attention a little more, not less. Born from the first table test, where plain refusal felt purely punishing. Recommended at 3–4P.
- **Slow Match** (with younger players): no chains — one card per turn — **and refusals take 1**. The two changes belong together: chains are the game's exhaust valve, and without them the standard refusal cost pumps cards in faster than they can leave (simulated chainless games at cost 2 frequently never ended).
- **Inferno** (once the table knows the deck): chains of up to **three** cards. Measurably faster and meaner — about three minutes a race — and it rewards the sharpest counter at the table even harder. The right answer for a 6-player table that wants more bite.
- **Last Light** (scored match): when someone goes out, others score minus-1 per card in hand; play rounds equal to the player count, rotating dealer. Least negative total wins.

---

*Design v1.1 — simulation-tuned (~60,000 games, June 2026; see `WILDFIRE_design_analysis.md`), untested at the table. The original concept tracked the pile's buried faces from memory (the rule died with OUROBOROS — see the project's post-mortem lessons). The match-and-turn action replaces it: every constraint lives on the visible top face, every play is publicly verified at a glance, the turn IS the deck's signature flip, and the pile's visible history makes card-counting a skill of attention, never recall. The v1.0 open questions are closed: chain limit 2 and refusal cost 2 confirmed (zero stalls, flat seats, 1.5–1.8× skill edge, ~5-minute races at every count); the old Hot Well variant was cut because raising the refusal cost made games 20–60% LONGER, not shorter — Inferno delivers what Hot Well promised; Slow Match gained its refusal-cost errata because the chainless game otherwise fails to terminate.*
