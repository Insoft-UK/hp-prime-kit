---
phase: 07-app-functions
plan: 07
status: complete
completed: 2026-09-14
key_files:
  - docs/commands/triangle-solver/*.md
  - docs/commands/spreadsheet/*.md
  - docs/commands/function/*.md
  - docs/commands/linear-solver/*.md
  - docs/commands/solve/Solve.md
  - docs/topics/apps.md
commits: []
---

# Plan 07 summary: the rounds run with the app active

## What was built

- **39 new rows** in `results.tsv`, from four batches launched after the user
  selected an app by hand: Triangle Solver, Spreadsheet, Function with `F1`
  filled in its own editor, Linear Solver, and Solve.
- **19 entries rewritten** with paired rows -- the refusal without the app and
  the answer with it, side by side in one table: `triangle-solver` 6,
  `spreadsheet` 4, `function` 5, `linear-solver` 3, `solve` 1.
- **17 sibling entries corrected** in `spreadsheet`, where a sentence had
  gone false.
- Two facts in `docs/topics/apps.md`:
  `apps.function-needs-active-app` and `apps.triangle-solver-degrees`.

## What this turned up

**The app rule survives inside a program, which is what made these rounds
possible.** The finding from the four keypresses was that a function answers
while its app is active. It was not obvious that this would still hold for a
call made from a batch: the harness resets the calculator, and the program
runs from Home. It holds. The user selects the app, the batch runs, and the
functions answer from inside it -- so everything the keypresses could reach
one call at a time, a batch can now reach forty at a time.

**The rule is necessary but not sufficient, and the Spreadsheet proves it.**
Four of its twenty-two names answer with the app active -- `SUM`, `AVERAGE`,
`CellHasData`, `ClearCell` -- and eighteen still refuse. Those eighteen are
mostly statistics names that want data in cells, which an empty spreadsheet
does not have. The fact says so rather than promising the rule unlocks a
group.

**`AAS` and `ASA` can now be told apart, and their entries had said nothing
could do it.** With the app active both answer, and the answers differ by
arithmetic rather than by wording: the two orderings of the same three
measurements produce different triangles. That is a claim retracted, not a
gap filled.

**The Triangle Solver answers in degrees.** `SSS(3,4,5)` gives
`{36.8698976458,53.1301023542,90}` -- degrees to ten figures, summing to 180
-- while every other measurement in this documentation is in radians. A
program chaining those angles into a trigonometric function is wrong by a
factor near 57 and nothing raises.

**`LinSolve` answers, and the group is no longer empty.**
`LinSolve([[2,1,5],[1,−1,1]])` gives `{2,1}`: the last column of the matrix is
the right-hand side, and the command takes one argument, not a matrix and a
list of unknowns. This documentation predicted `y = −1` before the row
arrived and was wrong -- the second wrong arithmetic prediction of the phase.

**The first was `ISECT`**, where this documentation predicted 2 and the
calculator answered 2.56155281281. Two is where `F1` crosses the axis; the
question was where it crosses `F2`, which is one plus the root of seventeen
over two. The calculator was right both times. Both misses are written into
the entries rather than quietly replaced by the measured value.

**Three names are now firm negatives rather than untested ones.** `Solve` was
refused in five forms, `Solve2×2` and `Solve3×3` in two each. One form of each
was measured with the Linear Solver or the Solve app selected; the rest
predate that round. What makes these negatives rather than silence is that
`LinSolve` answered from the same batch, with the same app open: the
conditions were demonstrably working when the refusals came. The empty-bracket
form was tried on all three, because three commands in this phase take no
arguments and read app state instead; none of them reached it that way.

**Assigning to `F1` through `EXPR` stores a number, not a function.**
`F1:=X^2-4` leaves `F1` holding −4, which is why three earlier rounds of this
group looked broken. The working rows needed `F1` filled in the app's own
editor by hand and the app left active -- two conditions at once, neither of
which a batch can arrange.

## Deviations

- **A sentence in 17 entries had gone false.** They said the refusal was
  shared by all twenty-two names of the group; four of those names now
  answer. Replaced everywhere with the measured count. This is the failure
  mode of a claim about a *set* written from one measurement, and it is worth
  noting that the checker cannot catch it: the sentence was well-formed and
  correctly labelled, and only wrong.
- **U+2212 had to be substituted by script again.** Four cells across `ROOT`
  and `AREA` carry the calculator's own minus sign; they were written with an
  ASCII placeholder and filled from the stored rows, the same way `affix` was
  handled in Phase 6.
- **This round, like the three before it, ran without a plan file of its
  own.** Four plan-less rounds in one phase is now a pattern rather than an
  exception, and Phase 8 should either write the plans or stop pretending the
  numbering means one.

## Results

```
names answering something              130 of 179   (was 120)
groups answering nothing                 1          (was 2)
rows in results.tsv                    623          (was 584)
entries                                468
checker                                  0 problems
suite                                 9098 passed, 0 failed
```
