---
phase: 05-statements-and-program-commands
plan: 03
status: complete but for two entries
completed: 2026-09-12
key_files:
  - docs/commands/matrix/*.md
  - docs/commands/more/*.md
  - docs/commands/results.tsv
commits: ["Twelve entries from the third batch, and a question left open on purpose", "Thirteen entries, and the factor of ten explained"]
---

# Plan 03 summary: matrices, and the mixed bag under `more`

## What was built

- The 12 matrix entries: `ADDCOL` through `SWAPROW`.
- 12 of the 14 in `more`, including `HMS→` and `→HMS`, whose names carry an
  arrow.

## What this turned up

**`ADDCOL` and `ADDROW` refuse every form tried, and the best explanation is
now refuted.** Three shapes were refused at first: the column as a list at
position 3, the same at position 2, and as a one-column matrix. Both entries
said the likeliest explanation was that the command changes a variable rather
than answering a copy, which would explain a refusal on a literal. Run on a
matrix held in `M1`, they are refused too, and so is the form with the
arguments reversed. Nine forms, none working, and the entries say that rather
than guessing a tenth.

**`→HMS` converts and `HMS→` does not.** `→HMS(1.5)` answers `1°30′00″`, and
its `TYPE` is 0: a number whose *display* carries the degree and prime signs,
not a string. `HMS→(1.3)` answers `1.3`, its argument unchanged. The round
trip `HMS→(→HMS(1.5))` is the probe that would explain the difference and has
not been run.

## Deviations

- **Two of the fourteen `more` names have no entry: `CAS` and `EXECON`.**
  They were held out of every batch because they may change the evaluation
  mode, which would quietly affect the rows after them in the same program.
  They cannot be written without running them: the format admits three kinds
  of Result cell -- PPL in backticks, `*error*`, `*no value*` -- and all three
  would be false for a command whose answer nobody has seen. HP's own example
  set is no help either; it leaves CAS objects out on purpose.

  What they need is one batch of their own, two calls long, which is also the
  reason holding them back was right: alone, there is no later row for them to
  disturb. Until then this plan, and criterion 1 of the phase, are two names
  short.

## Results

```
hpprime docs --check      0 problems
matrix                    12 of 12
more                      12 of 14
```
