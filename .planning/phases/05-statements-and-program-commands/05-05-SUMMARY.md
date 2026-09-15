---
phase: 05-statements-and-program-commands
plan: 05
status: complete
completed: 2026-09-12
key_files:
  - docs/commands/drawing/*.md
  - docs/topics/interface.md
  - docs/topics/ppl.md
  - docs/commands/results.tsv
  - hpkit/lint.py
  - tests/test_lint.py
commits: ["Sixteen drawing entries, and a probe that asked the wrong question", "Three lint rules could not read a name with an arrow in it", "Thirteen entries, and the factor of ten explained"]
---

# Plan 05 summary: the 35 that paint

## What was built

- All 35 drawing entries, `ARC` through `TRIANGLE_P`.
- A new fact, `interface.draw-units`, and a correction to `ppl.one-based`.

## What this turned up

**The factor of ten is explained.** `GROBW` answered 10 where `GROBW_P`
answered 100 for the same grob, and four entries were deferring the question
to each other. `C→PX(0,0)` answers `{160,109}` and `C→PX(1,1)` answers
`{170,99}`: the origin of the default view is the middle of the screen and one
drawing unit is ten pixels, `px = 160 + 10x` and `py = 109 - 10y`. `PX→C`
agrees from the other side, and a grob made `DIMGROB(G4,10,5,0)` measures 100
through `GROBW_P`. `DIMGROB` said its grob was "probably" the same size as the
`_P` one; it is now measured.

**A fact was titled more broadly than its own body.** `ppl.one-based` read
"Everything is indexed from 1" while four drawing commands take a 0
coordinate. Its body always said "lists, strings and matrices"; the title now
says the same, and the screen exception is measured rather than asserted.

**Three probes measured nothing, and are written as such.** `GETPIX`, `PIXON`
and `PIXOFF` answered `#FF000000h` all three times, including a read of a grob
filled red. An answer that does not move when the picture underneath changes
is not measuring the picture. The three entries carry the non-finding, the
hypothesis and the probe that would separate it, not a claim that the commands
work.

**The linter could not read a name with an arrow in it**, in three separate
rules. `C→PX(0,0)` was read as an index 0 into a variable `PX`, and the
harness refused to send the batch that would have answered the unit question.
One shared pattern fixed all three, with a control in the table for code that
compiles and must not be flagged.

## Deviations

- The plan said the phase closes here. It does not: `CAS` and `EXECON` have no
  entry, and plan 03's summary says why and what they need.
- The plan expected 117 entries. There are 111, because the estimate counted
  names the inventory files elsewhere.
- Two corrections found while reading rather than while measuring: the
  `results.tsv` row filed under `RECT` was a `RECT_P` call, re-filed where its
  evidence is, and `GROBH` claimed `GROBH_P` had never been run when it had.

## Results

```
hpprime docs --check      111 entries, 108 facts: 0 problems
python tests/run_all.py   2493 passed, 0 failed, across 13 suites
drawing                   35 of 35
```
