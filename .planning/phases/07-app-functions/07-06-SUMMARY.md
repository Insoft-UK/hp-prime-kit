---
phase: 07-app-functions
plan: 06
status: complete
completed: 2026-09-14
key_files:
  - docs/commands/function/*.md
  - docs/commands/inference/*.md
  - docs/commands/statistics-1var/*.md
  - docs/commands/statistics-2var/*.md
  - docs/commands/triangle-solver/*.md
  - docs/commands/linear-solver/*.md
  - docs/commands/solve/*.md
commits: ["The seven small groups, and a wrong conclusion about function overturned"]
---

# Plan 06 summary: the seven small groups

## What was built

- 35 entries across `inference` 9, `statistics-1var` 6, `statistics-2var` 5,
  `triangle-solver` 6, `function` 5, `linear-solver` 3 and `solve` 1.
- **Phase 7 is covered: 179 of 179.**

## What this turned up

**The `function` group does compute, and this documentation had said
otherwise.** That correction is the most valuable thing in the batch, and it
came from paying a debt rather than from new ground.

An earlier probe had set `F1` and called `ROOT` on it, seen a refusal, and
recorded the group as unreachable. It never checked whether the assignment
worked. This batch made the assignment its own row: `F1:=X^2-4` answers −4,
and reading `F1` back answers −4. The expression was evaluated with `X`
standing at zero and the **number** was stored, so `F1` never held a function.

With that known, the rest reads correctly. `SLOPE(F1,1)` answers 0 and
`AREA(F1,0,1)` answers −4 -- exactly the slope and the signed area of the
constant −4 over one unit. Both commands compute, from Home, with no app
open. `ROOT`, `EXTREMUM` and `ISECT` refuse because a constant has no root,
no extremum and no crossing with itself. The group works; the setup was what
failed.

**A clean division runs through these groups: commands that receive their
data answer, commands that read their app's state do not.** `DoInference()`,
`DoSolve()` and `Do1VStats(H1)` take nothing or take an empty data set, and
all three refuse. The `inference` commands that are handed two lists all
answer. It holds in every group here.

**`S1` cannot be assigned at all**, where `F1` could. Assigning a matrix to it
is refused and reading it back is refused, so `statistics-2var` stays blocked
for a reason that is now visible rather than guessed.

**`statistics-1var` splits three and three**: the names taking a plain number
answer -- `CHECK`, `UNCHECK`, `ISCHECK` -- and the three naming a data set
refuse.

**Three whole groups refused everything**: `triangle-solver` on four
different argument shapes, `linear-solver` on two matrix shapes, `solve` on
two forms. Several shapes each, which is what makes those findings about the
groups rather than about one guess.

**A fourth pair could not be told apart.** `LinRegrTMeanResp` and
`LinRegrTPredInt` answered identical lists, because the data lay exactly on a
line and both intervals collapse to no width. Recorded as agreement with the
probe named, after the same situation with two unit commands in Phase 6,
`CashFlowMIRR` beside `CashFlowFMRR`, and `is_orthogonal` beside
`is_perpendicular`.

## Deviations

- **One missing label in 35 entries**, in `Resid`, caught by the checker. The
  rate keeps falling but it remains the defect this documentation produces
  most often.
- **Two file names carry U+00D7** -- `Solve2×2` and `Solve3×3` -- and they
  wrote correctly by hand, unlike U+E003, which had to be substituted by
  script when `affix` was written. So the limit found earlier is the
  private-use range, not non-ASCII in general.
- **This batch, like the two before it, ran without a plan file of its own.**

## Results

```
inference, statistics, solvers, function   35 of 35
phase 7                                   179 of 179
entries                                   468
checker                                     0 problems
suite                                    8970 passed, 0 failed
```
