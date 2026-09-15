---
phase: 07-app-functions
plan: 04
status: complete
completed: 2026-09-14
key_files:
  - docs/commands/geometry/*.md
  - docs/commands/results.tsv
commits: ["The curve, polygon and test families of geometry, and three debts paid"]
---

# Plan 04 summary: curve, polygon and tests

## What was built

- 27 new entries: 9 `Curve`, 9 `Polygon`, 9 `Tests`.
- 4 entries rewritten -- `inter`, `parallel`, `equation` and `perimeter` --
  because the probe they each named has now run.
- `geometry` stands at 58 of 84, phase 7 at 118 of 179.

## What this turned up

**Three of the four debts are paid, and the hypothesis was right.**
`inter` answers `{point(2,0)}`, `parallel` answers `line(y=1)` and `equation`
answers `y=0`, all three when their argument is built by `segment` instead of
`line`. Each entry now carries both rows, the failing and the working, which
together say what neither says alone: the command is sound and the argument
was what broke it.

**The fourth debt explains itself.** `perimeter` was handed a `triangle`, and
`triangle` is refused, so nothing ever reached it.

**`triangle` is broken where its eight neighbours are not** -- `square`,
`rectangle`, `rhombus`, `parallelogram`, `quadrilateral`, `right_triangle`,
`isopolygon` and `polygon` all answered. That is the second family whose
plainest name is the broken one, after `line` among the line builders. Two
families, two gaps, both at the most obvious name.

**Two of the nine tests answer a code, not a truth.** `is_isosceles` answers
3 for a triangle that is isosceles and `is_parallelogram` answers 4 for a
square. `is_equilateral` answers 0 for a triangle that is not equilateral, so
0 is still the family's no and those numbers sit on a scale. A condition
testing the answer works; a comparison against 1 never fires. Both entries
carry a `Models get wrong` table.

**Every polygon normalises to `polygon(...)` and closes its ring**, repeating
the first vertex at the end. A triangle answers four points and a square
five, so counting vertices as given overstates every figure by one. The
constructor's name is lost in the value: `square` and `quadrilateral` gave
byte-identical answers for the same shape.

**`rectangle` with a ratio of 1 answered exactly what `square` did**,
character for character, which is what says its third argument is a ratio
rather than a length.

**`rhombus` takes an angle in radians where its neighbours take ratios.** The
answer carries `COS(1)` and `SIN(1)` rather than a number, so the 1 was read
as one radian. Three commands side by side take a third number and it means
something different in each, with nothing in the answer to warn a reader.

**The four circle commands all answered correctly and in one form.**
`circle` of a diameter, `circumcircle` and `incircle` of the 3-4-5 triangle,
`excircle` of the same: centre and radius every time, with `circumcircle`
giving three halves and five halves exactly rather than as decimals.

**`isopolygon` is the first answer in Phase 7 long enough to be cut**, at the
harness's 160 characters, because a pentagon's vertices arrive exact, with
the square root of five unevaluated.

**`conic` answered an empty list**, as `tangent` did in the previous batch:
not an error, not a curve, nothing at all.

## Deviations

- **This batch ran without a plan file of its own.** `07-03-PLAN.md` covers
  the first geometry batch; this one was prepared directly from its findings
  and launched. Writing a plan now, dated today, would be back-dating the
  method rather than following it, so this summary records the gap instead.
- **The shell could not carry this content.** Two attempts to write entries
  with heredocs died on `unexpected EOF looking for matching quote`, because
  the text is full of apostrophes and quotation marks. The work moved to
  direct file writes, which is what this project's own memory note already
  prescribed after three such failures in an earlier phase.
- **Five Result cells were built by script from `results.tsv`**, not typed:
  `ellipse`, `hyperbola`, `parabola`, `rhombus` and `isopolygon` carry
  U+E003, U+221A or U+2212. Typing those was proved impossible when `affix`
  was fixed, and the format already required building them from the row.
- **Nothing was caught by the checker this time.** The thirteen written first
  were verified before the remaining eighteen, and both halves came back
  clean: 0 problems in the entries and 0 mismatches across all 58 geometry
  examples.

## Results

```
curve, polygon, tests        27 of 27
geometry                     58 of 84
phase 7                     118 of 179
entries                     407
checker                       0 problems
suite                      7902 passed, 0 failed
```
