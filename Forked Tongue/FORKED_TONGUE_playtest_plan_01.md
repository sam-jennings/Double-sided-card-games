# FORKED TONGUE — Playtest Plan 01

*Pairs with the forthcoming `FORKED_TONGUE_playtest_01.md`. Written per `.kiro/steering/playtesting.md`. The hypotheses come from the game record's `next_step`, the open questions in the [rulebook](FORKED_TONGUE_rulebook.md)'s design notes, the [design analysis](FORKED_TONGUE_design_analysis.md) and the [end-condition proposal](FORKED_TONGUE_end_condition_proposal.md).*

## Open before the session

No rule gap blocks a base-game session. The Apprentice Forgers variant still doesn't say what happens to ledger cards older than the three newest after a challenge, so **don't use Apprentice Forgers** this session.

## Setup

- **Game:** FORKED TONGUE
- **Version:** v1.2 (Swear on it and the fuse added November 2026; never played).
- **Players:** 3 or 4. 4P is the count where honest tables used to stall worst (79%), and 3P is the count where only the fuse fixes it. Prefer 4P if you can field it.
- **Symbol subset:** all 9 signs / 36 cards. Hands 8 (3P) or 7 (4P); registry 12 or 8, which gives a fuse of 24 or 16 declines.
- **Session shape:** two base games. Swap the first seat between them. Use a spare card or a coin to mark who opened.
- **Why this session:** the bots say lying never pays (a lying bot wins 0.38–0.90 of a fair share). In a bluffing game that is the deciding question, and only people can answer it.

## Hypotheses to test

- **H1 — People bluff profitably.** *Prediction:* each player lies at least twice a game, and at least one lie per game survives to the player's benefit (unchallenged and never exposed, or it sheds the winning card). *Falsified if* the table stops lying after the first caught forgery and plays honestly for the rest of the game. That is the honesty-dominance problem the sim found, and the most serious result this session could produce.
- **H2 — Every game ends, mostly by shedding.** The sim puts the fuse ending 28% (3P) / 35% (4P) of skilled games. *Prediction:* both games end; at most one of the two ends on the fuse. *Falsified if* both end on the fuse, or anyone says the fuse "stole" the game.
- **H3 — Swearing is a real choice and a readable tell.** *Prediction:* players swear at least once per game on a long ledger, and someone remarks on a claimant who *didn't* swear. *Falsified if* nobody swears (dead rule), or if not swearing makes every lie obvious (lying becomes pointless).
- **H4 — Length fits the banner.** Skilled bot games run 36–60 turns. *Prediction:* each game takes 12–25 minutes. *Falsified if* a game runs past 30 minutes.
- **H5 — The deck earns its place.** *Prediction:* at least one challenge per game is called from the registry, the sworn pile or the ledger ("that pair is already dead"), not from a hunch. *Falsified if* every challenge is a gut call. That would mean pair uniqueness isn't doing the work.
- **H6 — Declining is a decision, not a dodge.** *Prediction:* declines happen for both reasons (can't show it, won't show it), and at least once someone declines on purpose to run down the fuse while holding the fewest cards. Note whether that feels clever or cheap.

## What to watch

Handling first:

- **The claim in the air.** Only the newest claim is remembered. Watch how often someone asks the claimant to repeat it, and whether anyone disputes what was claimed.
- **Challenge flips.** Watch that the flipped card goes with the ledger and that nobody accidentally exposes another ledger card's pressed face.
- **The fuse.** Turning registry cards sideways, then into the spent row. Watch that everyone can still pick up and examine registry cards, and that nobody loses count of what's left.
- **The sworn pile.** Keep it beside the registry, separate from the fuse. Watch that it stays examinable and doesn't sprawl.
- **Hand inspection.** Players see both faces of their own cards; watch nobody tilts a card so the table sees its other face.

Then:

- **Lies attempted and caught**, per player per game (tally marks).
- **Declines**, and whether each was forced or chosen (ask afterwards).
- **How the game ended:** shed, or fuse. If the fuse, the hand sizes.
- **Time** per game.

## Success and failure signals

- **Success:** the table lies, laughs at caught forgeries, groans at a well-timed swear, and wants a rematch. Both games end inside 25 minutes.
- **Failure:** the table settles into honest play, or treats the fuse as an arbitrary clock. Either one sends the game back to In the workshop.

## Teaching plan

Teach in this order: the ledger and the claim (one example play), declining, challenging, then Swear on it and the fuse together, framed as "how the game ends if nobody gets caught". Skip the variants. Point at the registry and say that every card in it is a pair nobody can be holding. **Watch:** whether the rewind on a decline is understood first time; whether players grasp that sworn cards count for deduction.

## After the session

Write `FORKED_TONGUE_playtest_01.md`. Set `physically_playtested: true` on the game record, then set `state` from the verdict per the playtesting guide.
