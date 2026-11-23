# FORKED TONGUE — design analysis (draft, November 2026)

*State at this vetting pass: **In development** (old vocabulary); since v1.2 the game is **Untested** · physically unplayed. This is the vetting pass the game record's `next_step` asked for. Verdict: **not ready to promote** — the v1.1 rules read cleanly, but simulation finds a termination problem and an honesty-dominance problem that need a design decision first.*

Sim: [forked_tongue_sim.py](forked_tongue_sim.py). Rules: [FORKED_TONGUE_rulebook.md](FORKED_TONGUE_rulebook.md) v1.1.

## The questions

1. Does a game end? The rulebook's own FAQ admits *"Can the game stall? … If a table circles…"* with no rule that stops a circle.
2. Does skilled play beat random (≥ ~1.5× fair)?
3. Seat fairness at 3–6 players.
4. Does the strategy note *"lie early, truth late"* hold — is lying a real tool?
5. The recorded first-playtest question: is a one-card decline too cheap (watch the decline rate)?

## Method

- Ruleset modelled exactly as v1.1: deals 8/7/6/5 at 3/4/5/6P, registry 12/8/6/6; the ledger as a stack of (card, shown, claim); play-and-claim showing the owed symbol; decline takes the newest card and rewinds one link; challenges with closest-to-left priority, loser takes the whole ledger, the player after the claimant opens fresh; the final card wins if it survives the window.
- **RandomBot**: plays a random legal card 85% of the time when able, claims the truth half the time, challenges 15% of claims and 50% of final-card claims.
- **SkilledBot**: always sheds when able; claims the scarcest symbol (fewest cards it can't locate) to force declines; lies only with ≥ 4 cards in hand, half the time, never on its last card, and only with a pair nobody else can disprove (one it holds itself, or one it can't locate); challenges any claim it can prove false from the registry or known card locations; challenges every final-card claim. **Honest** = the same bot with lying switched off.
- 1,000 games per row, 4 player counts × 6 tables = 24,000 games, seed 1, turn cap 600 (a "turn" is one play or one decline). Skilled seat rotates independently of the first seat.
- Not modelled: table talk, tells, reading confidence, memory errors. The skilled bot counts only certain locations — a floor.

## Results

```
 P table            stall  turns  p90 focus win x fair  decl%  lie% chal/g caught
 3 random            6.3%  194.0  388      -       -      24%   44%   47.2    44%
 3 skilled           4.8%  114.7  212      -       -      30%   33%   13.2    93%
 3 honest           37.2%   55.1   89      -       -      47%    0%    0.6     0%
 3 mixed             0.0%   59.9  101     96.0%   2.88    21%   39%   16.2    61%
 3 honest-mixed      0.0%   52.8   88     98.3%   2.95    21%   31%   14.0    54%
 3 liar-vs-honest   17.8%   79.6  138     14.9%   0.45    42%    9%    2.7    70%
 4 random            1.5%  160.7  322      -       -      22%   44%   51.6    44%
 4 skilled           0.4%  122.6  236      -       -      30%   39%   18.8    95%
 4 honest           78.7%   58.4   91      -       -      49%    0%    0.2     0%
 4 mixed             0.0%   67.7  110     90.4%   3.62    20%   41%   23.0    54%
 4 honest-mixed      0.0%   54.7   92     96.4%   3.86    20%   33%   18.4    47%
 4 liar-vs-honest   37.6%  133.6  266      1.1%   0.04    45%    7%    4.4    86%
 5 random            0.0%  113.9  213      -       -      19%   44%   44.9    44%
 5 skilled           0.0%   74.7  122      -       -      26%   38%   13.1    92%
 5 honest            3.3%   83.1  146      -       -      41%    0%    1.0     0%
 5 mixed             0.0%   60.1   99     83.8%   4.19    18%   41%   25.0    50%
 5 honest-mixed      0.0%   50.9   79     90.7%   4.54    18%   35%   20.7    44%
 5 liar-vs-honest    0.4%   82.9  140      6.8%   0.34    36%   10%    3.1    68%
 6 random            0.0%   80.0  140      -       -      18%   44%   37.3    44%
 6 skilled           0.0%   59.9  101      -       -      30%   35%   10.1    90%
 6 honest           17.7%  131.5  270      -       -      47%    0%    0.8     0%
 6 mixed             0.0%   49.5   80     71.5%   4.29    17%   41%   24.0    48%
 6 honest-mixed      0.0%   44.0   71     85.2%   5.11    17%   37%   21.3    44%
 6 liar-vs-honest    2.4%   94.0  182      5.7%   0.34    42%    6%    3.0    67%
```

*"focus win" = win rate of the one rotating focus seat (skilled in `mixed`/`honest-mixed`, the liar in `liar-vs-honest`); "× fair" = that rate × player count. "turns" counts finished games only.*

Seat spread among finished games is within ±5 points of fair at every count (e.g. 4P skilled 25/27/24/25%), except 6P honest (last seat 9%) on a table that also stalls.

## Health checks

| Check | Result |
|---|---|
| **Termination** | **Fails.** Non-zero stall at the 600-turn cap at 3P for every bot mix (random 6.3%, skilled 4.8%) and at 4P (1.5% / 0.4%). Tables of honest players stall **37% (3P), 79% (4P), 3% (5P), 18% (6P).** |
| **Skill gap** | **Healthy against random:** one skilled seat wins 96 / 90 / 84 / 72% at 3 / 4 / 5 / 6P (2.9–4.3× fair). |
| **Seat fairness** | Fine where games finish. |
| **Length** | **Too long for the banner.** Skilled tables average 115 / 123 / 75 / 60 turns (p90 212 / 236 / 122 / 101) at 3–6P. At ~8 s a turn, a 3–4P game is ~15–16 min on average with a tail past 30 min; the "~20 min" banner holds only at 5–6P. |
| **Lying** | **Not a winning tool for these bots.** A lying skilled bot loses to honest skilled bots (focus win 0.04–0.45× fair) and does worse than an honest one against random (e.g. 4P 90% vs 96%). |

## Reading — the root cause

The stalls and the honesty result are the same structural fact.

1. **Every pair is held by somebody.** At 5–6P all 36 cards are dealt or in the registry; at 3–4P the registry is public. So a forged pair {shown, claim} is almost always sitting in a rival's hand or the registry, and **its holder can prove the lie with certainty** — the deck's pair-uniqueness makes the lie-space small from turn one, not "a coin in a fountain" early. The only safe lie is forging a pair you hold yourself.
2. **Only challenges reset the ledger.** A play adds one card, a decline removes one. With nobody lying, no challenge ever wins, so the ledger is a random walk with no reset. The stalled positions confirm it: in honest tables hands sit at 2–5 cards while the ledger holds 10–18. Players steer claims to the scarcest symbols (as the strategy notes advise), the next player declines, the requirement rewinds, someone replays the card, and the table circles. Nobody empties a hand because nobody's last card matches the owed symbol.
3. So the game **needs lies to finish, but punishes the liar**. Honest play is close to dominant, and a table of careful, honest players is the table most likely to never end. Humans may lie more freely than these bots, but the rulebook's own fallback (*"If a table circles, play the Long Con"*) scores a round. It doesn't end one.

The decline rate (20–30% of all turns with bots that lie, 41–49% with honest bots) supports the recorded worry that a one-card decline is too cheap a dodge. In the honest stalls it's the mechanism of the circle.

## What this does not decide

The sim floor can't tell whether human bluffing (tells, reads, nerve) makes lying pay where these bots can't. A thoughtful liar who only forges pairs in their own hand is already modelled. A deeper "lie to bait a wrong challenge" line isn't.

## Decision needed from the designer (no rule changed here)

Termination needs a rule, and every candidate is a new mechanic or changes a recorded choice, so none is adopted in this draft:

- **A hard clock** — e.g. the round ends after a fixed number of ledger pick-ups or laps; fewest cards in hand wins (the Long Con scoring then works per round).
- **A dearer decline** — the open first-playtest question. The v1.0 two-card decline was dropped because it corrupted the self-recording ledger, so any new cost must keep v1.1's "shorten only from the newest end" property (for example, the decliner also *pays* a hand card to a side pile).
- **Shrink the knowable lie-space less** — fewer dealt cards / a bigger unseen remainder at 5–6P, so a forged pair isn't always in a rival's hand. This reopens the deal table and the "deck as public registry" premise.

Re-run `forked_tongue_sim.py` after any change. Target 0% stall at 3–6P with honest tables included, and a lying skilled bot that at least matches an honest one.

## Rules read-through (ambiguities)

The core turn, decline-rewind, challenge and final-card rules are unambiguous and were modelled without guesswork. One gap: **Apprentice Forgers** says a challenge costs or awards only the 3 newest ledger cards, but it doesn't say what happens to the older ones (do they stay as the ledger, and if so, who opens and what is owed?). That needs a one-line answer before the variant is tabled.

## Caveats for the first table (once the above is fixed)

- Watch the decline rate and whether a circle forms at 3P.
- Watch whether anyone lies at all after the first caught forgery.
- Time a 3P game against the banner.
