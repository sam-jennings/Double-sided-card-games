---
inclusion: always
---

# Agent Working Discipline

> **Why this exists.** Adapted from the one part of the "run Opus like Fable"
> experiments that actually transfers. Controlled testing (the `fablize`
> comparison) found Fable's edge was *model capability* — it could not be moved
> by any prompt or harness. What *did* transfer was **procedure**: running what
> you build, seeing tasks through, investigating systematically, and refusing a
> groundless "done." So this file ports only those procedures. It deliberately
> does **not** copy any "Fable system prompt" — those are consumer-chat product
> wrappers, unverified, and would fight Kiro's own tooling. Capability is a
> model-choice question, not something a steering file can grant.

These are procedures, not suggestions. The goal is to reliably hit the model's
own ceiling, not to fake a higher one.

## 1. Verification grounding

Before claiming any task is done, run the thing that proves it — don't reason
about what the result *should* be and present that as the result.

- Combinatorial / structural claim → compute it (`itertools`, `math.comb`, an
  explicit witness), per `simulation-standards.md` ("Verifying combinatorial
  claims"). Show the computed value.
- Balance-sensitive rule change → re-run the relevant sim and cite the numbers
  (stall rate, skill gap, seat spread), per `simulation-standards.md`.
- Edited a sim or script → actually run it; paste the real output, not the
  expected output.
- A claim about a file's contents → read the file first; don't assert from
  memory.
- A **collection-wide or "absence" claim** ("no game uses X", "every rulebook
  says Y", "this is the only game that…") → verify against the canonical source
  (the **Component inventory** and coverage tables in
  [`COLLECTION_OVERVIEW.md`](../../COLLECTION_OVERVIEW.md)) or by reading *every*
  relevant file. **Truncated tool output is never evidence of absence** — a
  `grep`/`file_search` capped at N results, or a result line cut off mid-text,
  can hide the very counterexample you are claiming doesn't exist. If a search
  reports truncation or a cap, narrow it or open the sources before asserting,
  and prefer the canonical doc over re-deriving the fact.

Never present "expected" as "observed." If something could not be run, say so
and say why.

## 2. Completion + evidence gate

- Decompose a multi-part request into explicit sub-tasks before starting.
- A sub-task is "done" only with evidence: a command's output, a computed
  number, or a quoted line from the file. No evidence → it is not done, and the
  reply says which parts remain open.
- End multi-part work by stating what is verified versus still open. Don't round
  "mostly there" up to "done."

## 3. Investigation protocol (bugs and "why" questions)

For a defect or a "why is this happening" question (rules ambiguity, a stall in
a sim, a degenerate line of play — see the bug list in `design-principles.md`):
reproduce it first, list competing hypotheses, trace the causal chain to the
root cause, *then* propose a fix. No incremental patching of symptoms before the
cause is understood.

## 4. No early stop

Don't say "I'll run the sim" or "next I'll check X" and then stop the turn.
Either do it now, in the same turn, or phrase it as an explicit question for the
designer to answer. A stated intention is not a completed action.

## Escalate instead of pretending

Some work needs genuine open-ended creative depth or out-of-spec discovery — the
part no procedure transfers. When a task hits that ceiling (a novel mechanic that
needs invention, a fun/feel judgment that only the table can answer, a design
call with real trade-offs), say so plainly and put the decision to the designer.
Flagging the ceiling honestly beats a confident, groundless answer.

## Relationship to the rest of steering

This file governs *how work is done*. It sits under the domain rules, not over
them: where it touches simulation, `simulation-standards.md` is authoritative;
where it touches what counts as a defect or a sound design, `design-principles.md`
and `physical-handling.md` win. It adds no new design constraints — only the
discipline of verifying and finishing the ones already there.
