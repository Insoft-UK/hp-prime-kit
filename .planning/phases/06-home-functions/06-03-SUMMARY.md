---
phase: 06-home-functions
plan: 03
status: complete
completed: 2026-09-13
key_files:
  - docs/commands/probability/*.md
  - docs/commands/results.tsv
commits: ["The 28 probability functions, and two commands that take no parentheses"]
---

# Plan 03 summary: the probability functions

## What was built

- All 28 probability functions. None was covered by the interpreter and none
  had an HP worked example with a result, so every entry here is written from
  what the calculator answered.

## What this turned up

**Seeding works, and that is the finding a program can act on.**
`RANDSEED(1); A := RANDOM(); RANDSEED(1); RETURN A - RANDOM();` answers 0, so
the same seed gives the same sequence. A program that uses randomness can be
made testable.

The probe was built to answer itself in one call, and that shape is worth
keeping. Two separate draws would have been two rows whose equality nobody
could check afterwards, because a stored random number is a value no second
run reproduces. Subtracting inside the call turns the question into a number
that means the same thing every time. For the same reason `RANDOM`, `RANDINT`
and `RANDNORM` are documented by their `TYPE` rather than their value, as
`RANDMAT` already was.

**`!` is postfix.** `5!` answers 120. That makes it the second name this phase
whose missing syntax string on HP's list turned out to mean "not called with
parentheses at all" -- `MOD` was the first, an infix operator. A name on the
list with no syntax is worth treating as a sign rather than a gap.

**μ and σ really are optional.** `NORMALD(0)` and `NORMALD(1,2,3)` both
compile and both answer, the first giving one over the square root of two pi,
the standard normal's peak.

**Six distributions share one naming pattern** -- bare for the density, `_CDF`
to accumulate, `_ICDF` to go back -- and `NORMALD` states it once so the other
seventeen link rather than repeat it. The rows check each other:
`NORMALD_CDF(0)` is 0.5 and `NORMALD_ICDF(0.5)` is 0, an exact round trip,
while the counted distributions do not invert exactly and `BINOMIAL_ICDF`
explains why. `CHISQUARE` and `FISHER` each agree with their own inverse
across two rows.

**`GEOMETRIC` carries a caution rather than a rule.** Its density at 3 and its
tail beyond 3 are both 0.125, but only because p is a half. With any other p
they differ, and it would be easy to read a relation into a coincidence.

## Deviations

- **Eight paragraphs went in without a readable label**, and the checker
  caught all eight. Six had none at all; two had one the format cannot parse
  -- a link inside the label's own parentheses, and a comma where the format
  wants the label alone or a colon. Writing many entries in one pass is where
  this keeps breaking, and it has now happened in every plan of this phase.
- **Three of the fixes left lines over 100 characters**, because a label was
  appended to text that was already wrapped. Re-wrapped afterwards. The same
  thing happened to `ROUND.md` in plan 01.
- `!` and `geometric_icdf` were held back into a batch of two, since HP gives
  neither a syntax string and a call that fails to compile takes the whole
  batch with it. Both compiled.

## Results

```
python tests/run_all.py     0 failed, across 13 suites
hpprime docs --check        214 entries, 111 facts: 0 problems
probability                 28 of 28
phase 6                     102 of 177
```
