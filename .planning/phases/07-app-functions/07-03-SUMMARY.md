---
phase: 07-app-functions
plan: 03
status: complete
completed: 2026-09-14
key_files:
  - docs/commands/geometry/*.md
  - docs/commands/results.tsv
commits: ["The first geometry batch, and a claim from yesterday that it overturned"]
---

# Plan 03 summary: point, line, measure and cartesian

## What was built

- All 31 names of the four families, covering them exactly: none missing and
  none written that the list does not carry.
- Phase 7 stands at 91 of 179.

## What this turned up

**Seven predictions, seven matches.** `center` of the circle through the
origin and 2,0 is `point(1,0)`; `element` of a segment at 0.5 is its
midpoint; `radius` is `1/2`; `angle` of three points on the axes is half of
pi; `abscissa` and `ordinate` of `point(3,4)` are 3 and 4; and
`polar_coordinates` is `[5,0.927295218002]`, the arc tangent of four thirds
to twelve figures. Calls chosen so arithmetic knew the answer first are what
separate a command computing from a command echoing.

**`circle` takes its two points as a diameter, now confirmed three ways**:
`center` gives the midpoint of them, `radius` gives half their separation,
and `area` gives a quarter of pi. Three names agreeing is worth more than the
one row that first suggested it.

**Seven answers carried their failure as data rather than raising it**, in
three different types: as strings from `perimeter`, `parameq`, `equation`,
`single_inter` and `perpendicular`; as a list holding one from `inter`; and
worst, from `parallel` as a type 8 object with the message built in --
`line(y="Error: entrada no válida")`. A program checking that it received a
line receives one. A program checking for an error finds none. Only reading
inside the object shows anything is wrong.

**That overturned a claim committed the day before**, which had said
reporting a failure as text was `residue`'s own behaviour, closed in the
negative because `Chi2GOF` and `LinRegrTTest` answer a plain error. Those two
do refuse; plenty of others do not. The bullet was corrected rather than
deleted.

**`arcLen(X^2,0,1)` answers 1 and the arc is 1.4789428575**, checked here two
ways that agree to twelve places. A third short, from a call that succeeded
and raised nothing, which is the same shape of trap as `LineTan` collapsing
its expression in Phase 6. It has a `Models get wrong` table.

**`perpendicular` replies that it expects three points**, while HP publishes
`perpendicular(Point, Line)` and was given exactly that. The machine and the
help disagree and the machine is the one that runs.

**`line` was refused where `segment` and `half_line` answered**, from the
same two points in the same batch. Two of the three ways to join two points
work and the plainest does not.

**`tangent` answered an empty list** -- a third way of reporting trouble,
after a refusal and a message carried as data. A program looping over the
answer does nothing, silently.

Smaller ones: `coordinates` and `polar_coordinates` are type 4, a matrix, not
the list their braces-free look suggests; the error text is Spanish because
this machine is, so no entry quotes it as a property of a command.

## Deviations

- **The one checker problem in 31 entries was predicted before running it.**
  `affix.md` carried a Result cell deliberately left short of the imaginary
  unit, and the checker caught the mismatch exactly where it was expected.
- **U+E003 cannot be typed through the editing channel.** The hand edit came
  back byte-identical to the original -- a no-op -- because the private-use
  codepoint does not survive it. The cell had to be rebuilt by reading
  `results.tsv` and substituting programmatically, which is what the entry
  format already required. The accented U+00E1 in the Spanish error strings
  does survive and matched its stored row first time, so the limit is
  private-use characters and not non-ASCII in general.
- **A display of the fixed file still showed the cell truncated**, disagreeing
  with the script that had just written and re-read it. Settled by the
  checker, which reads from disk and was silent, rather than by preferring
  the more convenient view.
- **The rows are dated a day before the measurements.** The batch was prepared
  before midnight and run after it, and `collect()` stamps rows with the
  preparation date. Recorded in `STATE.md` as a question for the tool.

## What this did NOT settle

`line`'s refusal leaves six rows weak as evidence about themselves:
`inter`, `single_inter`, `parallel`, `equation`, `parameq` and `perimeter`
were all given arguments built by `line` or by `triangle`, which this batch
never tested alone. Each entry says so and names the cheap probe -- rebuild
the argument with `segment`, or wait for the polygon family in the next
batch.

## Results

```
point, line, measure, cartesian   31 of 31
geometry                          31 of 84
phase 7                           91 of 179
checker                           0 problems
suite                             7340 passed, 0 failed
```
