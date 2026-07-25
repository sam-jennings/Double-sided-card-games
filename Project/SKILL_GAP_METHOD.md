# The skill-gap metric is broken

*July 2026. Cross-game methodology note. Raised by Sam after the WILDFIRE Mirror analysis: "the difference in some arbitrary skill gap against a bot that is cheating shouldn't be a deciding factor for any game."*

---

## 1. What the number currently is

Almost every design analysis in this collection quotes a **skill gap** or **skill edge**: BLIGHT 2.02×, GLEAN 1.74×, OUROBOROS 1.74×, WILDFIRE 1.5–1.8×, ICARUS 1.55–1.61×, DOWRY ~3.6×, CROSSROADS, TRIGON and TURNCOAT similar. A **~1.5× bar** has been treated as the threshold for a healthy game.

In every case the figure is:

> the win rate (or score) of a **skilled bot** seated among **randomly-playing bots**, divided by its fair share.

Three things are wrong with it, in ascending order of seriousness.

## 2. Fault A — the skilled bot cheats

The bots read hidden information no player has. WILDFIRE's "cruel" bot inspects the next player's entire hand before choosing which target to leave. The GLEAN and BLIGHT bots count every face in the pile history perfectly. DOWRY's cutter evaluates the exact contents of a lot.

This does not merely inflate the number, it **measures the wrong skill**. A bot that sees hidden hands is rewarded for exploiting information; a human is rewarded for inference, memory and reading people. The two can move in opposite directions — WILDFIRE's published 1.5–1.8× was real *and* the table correctly reported no skill, because the bot's entire advantage was perceptual access a person doesn't have.

**Rule going forward:** if the skilled bot uses information a player at the table cannot see, the figure is void. State the bot's information set alongside any number quoted.

## 3. Fault B — the baseline is meaningless

"Beats a bot playing uniformly at random" is an extraordinarily low bar. It answers *is this better than flailing?* — a question with no design content, because the answer is yes for almost any ruleset.

The question that matters is **whether two thoughtful players have anything to decide between**. That requires comparing two *plausible* strategies, not a strategy against noise.

The WILDFIRE Mirror analysis shows the difference starkly. Skilled-vs-random said the rule was harmful (1.46× → 1.30×). The comparison that actually informs play — a bot that values the mirror against one that ignores it, both otherwise competent — showed the mirror-valuer **ahead**. The two comparisons disagree, and only the second describes a decision a real player faces.

**Rule going forward:** the headline comparison is **thoughtful line vs. naive-but-sensible line**, both playing legally and with the same information. Skilled-vs-random may be reported as a floor, clearly labelled as such.

## 4. Fault C — a high skill gap does not mean the game has decisions

This is the fault that cost the most time. A game can post a healthy skill gap while its best move is completely obvious, because a bot will happily execute an obvious move very reliably.

The gateway-concept search ([GATEWAY_GAME_CONCEPTS.md](GATEWAY_GAME_CONCEPTS.md)) produced CLAMOUR at a respectable 1.33× — in a game where a risk-free move was computable on **88% of player-turns at 3P**. The metric could not see it. WILDFIRE posted 1.5–1.8× with **~70% of turns containing no decision at all**.

The metric measures *how well a decision, once made, is converted into wins*. It says nothing about **whether a decision exists**.

**Rule going forward:** report decision density *before* any skill figure:

| Measure | What it asks |
|---|---|
| **Legal options per turn** | Does the player have anything to choose between? |
| **% turns with ≥2 options** | How often is there a choice at all? |
| **% turns where the choice changes the visible outcome** | Does the choice matter, and can the player *see* that it did? |
| **Obviousness** | Can a risk-free or dominant move be computed? On what share of turns? |

For CLAMOUR that would have been a one-line kill. For WILDFIRE it was the diagnosis the balance simulation had missed for a year.

## 5. Fault D — it silently penalises the things party games are made of

The metric rewards low variance, because variance decouples good play from winning. So it will always argue against catch-up mechanics, random events, direct-attack rules and swingy moments — the exact ingredients that make a light game fun at a table.

WILDFIRE's Mirror is the worked example. It lowers the skill gap ~0.15× because the chance to mirror is gated by holding one particular card. It is also the only immediate, visible, aimed consequence in the entire design. Optimising the metric would have deleted it; the design judgement was to keep it, and that judgement is recorded in the rulebook footnote rather than buried.

**Rule going forward:** a skill figure is **evidence, never a gate**. A party game and a two-player abstract should not be judged against the same bar, and no rule should be cut for costing skill gap alone. State what the game is *for* before quoting what it scores.

## 6. What replaces the ~1.5× bar

Nothing, as a single number. The health check becomes a short ordered list:

1. **Does it terminate?** Stall rate, length, seat fairness. *(This part was always sound and stays unchanged.)*
2. **Is there a decision?** Decision density and obviousness, per §4. A game failing here is dead regardless of anything below.
3. **Does the decision reward thought?** Thoughtful line vs. naive line, same information, no cheating. Per §3.
4. **Can a player perceive that it did?** The visible-consequence share. A skill nobody can feel is not a skill at the table — WILDFIRE's central lesson.
5. **Is the variance right for what this game is for?** A judgement, stated as one.

## 7. What this means for the existing analyses

Every quoted skill gap in the collection was produced under §2 and §3, so **none of them should be read as evidence that a game has decisions**. They are not necessarily wrong — most probably do measure something real — but they are unaudited.

The affected files: `BLIGHT_design_analysis.md`, `GLEAN_design_analysis.md`, `OUROBOROS_design_analysis.md`, `WILDFIRE_design_analysis.md`, `ICARUS_design_analysis.md`, `DOWRY_design_analysis.md`, `TRIGON`/`TURNCOAT`/`CROSSROADS` analyses, `CAIRN_design_analysis.md`, `RELAY_design_analysis.md`.

Suggested triage, cheapest first:

- **Annotate, don't re-run.** Add one line to each analysis stating the bot's information set and that the baseline is random play. Cheap, and it stops the numbers being over-read.
- **Re-run decision density** for the games that have already been table-tested, where a "felt reactive" style complaint exists or might. BLIGHT, GLEAN and TRIGON are the candidates — TRIGON's first test reported turns bottlenecked on reference-checking, which is a decision-cost signal.
- **Leave the pre-table games alone** until they've been played. Their numbers cost nothing while nobody is relying on them.

Nothing here invalidates the *termination* and *seat-fairness* work, which is the majority of what those simulations did and remains the thing simulation is genuinely good at.

---

*Origin: the WILDFIRE v1.2 Mirror decision — [Wildfire/WILDFIRE_excitement_diagnosis.md](../Wildfire/WILDFIRE_excitement_diagnosis.md) §5.*
