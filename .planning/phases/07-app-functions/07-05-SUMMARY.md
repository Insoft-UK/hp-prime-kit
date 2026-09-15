---
phase: 07-app-functions
plan: 05
status: complete
completed: 2026-09-14
key_files:
  - docs/commands/geometry/*.md
  - docs/commands/results.tsv
commits: ["Geometry closes at 84 of 84, and a third plain name turns out to be broken"]
---

# Plan 05 summary: transform, plot, zoom, and the three with no menu

## What was built

- 26 entries: 8 `Transform`, 8 `Plot`, 7 `Zoom`, and `Apps`, `Instruction`
  and `DelInstruction`, which HP files with no menu path at all.
- **`geometry` is complete: 84 of 84.** Phase 7 stands at 144 of 179.

## What this turned up

**Four predictions in the transform family, four matches.**
`homothety(point(0,0),2,point(1,1))` is `point(2,2)`; `projection` of
`point(2,3)` onto the x axis is `point(2,0)`; `inversion` of `point(2,0)` in
the unit circle is `point(1/2,0)`; and `reflection` of `point(1,2)` in the x
axis is the point 1 across and 2 below. Each was worked out before the
calculator was asked, which is what separates computing from echoing.

**A third family has its plainest name broken.** `plotfunc` and `plotpolar`
both answer by building a `plotparam(...)` object -- and `plotparam` called
directly is refused. That follows `line`, refused while `segment` and
`half_line` answer, and `triangle`, refused while its eight polygon
neighbours answer. Three families, three gaps, each at the name a reader
reaches for first. It is now a pattern rather than a coincidence, and worth
carrying into Phase 8.

**The calculator corrected HP's syntax for the second time in this phase.**
`translation` given a point replies, in words, that its first argument must
not be a point: it wants a vector. `perpendicular` did the same in the first
geometry batch, replying that it expects three points where HP publishes a
point and a line.

**All seven zoom commands are refused**, with no type at all. They change a
view, and a batch evaluating a string from Home on a reset calculator has no
view to change. One entry carries the account and the other six point at it,
rather than six entries guessing separately.

**`Apps` answers the calculator's own app names, in Spanish**, as a list of
strings cut at the harness's 160 characters. That is worth more than a
curiosity: the names are data a program might compare against, and on an
English machine they would not match.

**`rotation` answers `e` raised to the imaginary unit** rather than a pair of
coordinates -- a turn of one radian written as a complex exponential, which
confirms the angle mode yet again and leaves a program to evaluate it.

**`plotimplicit` answered an empty list**, the third command in this group to
do so after `tangent` and `conic`: no error, no curve, nothing. A program
looping over the answer does nothing and reports nothing.

`plotlist` is the exception in its family: given a matrix of two rows it
answers a `segment`, an object the rest of the group understands.

## Deviations

- **This batch, like the one before it, ran without a plan file of its own.**
  It was prepared from the previous batch's coverage gap and launched.
  Writing a plan now would be back-dating the method rather than following
  it.
- **One missing label in 26 entries**, in `DelInstruction`, caught by the
  checker. The rate is improving across the project -- eight in twenty-seven
  in Phase 6, one in thirty-four in `finance`, one in twenty-six here -- but
  it remains the single defect this documentation produces most.
- **Seven Result cells were built from `results.tsv` by script**, not typed:
  `reflection`, `rotation`, `translation`, `Apps`, `plotfunc`, `plotpolar`
  and `plotseq` carry U+E003, U+2212 or Spanish accents, and two of them
  arrived cut.
- **The guard refused the first launch, correctly.** No emulator was running,
  so the next window would have opened the user's own calculator rather than
  the throwaway. The batch went out only after their calculator held the
  first window.

## Results

```
transform, plot, zoom, no-menu   26 of 26
geometry                         84 of 84  -- complete
phase 7                         144 of 179
entries                         433
checker                           0 problems
suite                          8386 passed, 0 failed
```
