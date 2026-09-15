---
phase: 08-app-variables
plan: 01
status: complete
completed: 2026-09-14
key_files:
  - docs/topics/apps.md
  - docs/commands/triangle-solver/*.md
  - docs/commands/explorer/*.md
  - docs/commands/statistics-1var/CHECK.md
  - docs/commands/solve/Solve.md
  - docs/commands/linear-solver/*.md
commits: []
---

# Plan 01 summary: the probe, and what it cost the entries already written

## What was built

- **48 rows** from two batches: 28 with nothing selected, 20 with the
  Triangle Solver selected by hand.
- **One new fact**,
  `apps.reset-leaves-function-active`.
- **7 entries written**, the whole `triangle-solver` variable group and the
  first app variables this documentation has.
- **8 entries corrected**, seven of which claimed a condition that does not
  exist, plus `DoSolve`, whose measured refusal has become a measured answer.

## What this turned up

**There is no "no app open" on the Prime, and eleven documents said there
was.** A reset calculator has the **Function** app active. The proof is a
reversal, not an assertion: with nothing selected, the Function app's
variables answered -- `Root`, `Slope`, `SignedArea` all 0 -- and the Triangle
Solver's refused. With the Triangle Solver selected and nothing else changed,
that reversed exactly, `AngleA` and its five neighbours answering and `Root`
refused. A name does not stop working because another app was chosen unless
the first app was what made it work.

Seven entries had written "it answered from Home, with no app open" as
though that were the neutral condition it was measured under. It was not
neutral; it was the Function app. For names outside that app the reading
still stands, which is why those entries are corrected rather than
withdrawn -- but the phrase was wrong and it was wrong in the same words
seven times.

**The app rule reaches variables, not only functions.** `AngleA` refused both
reading and assignment with another app active, and did both with its own.
That decides the shape of this phase: most of the 172 names need the user to
select an app before a batch can touch them, so this is a phase of rounds,
not of one big unattended run.

**A program can set an app variable, and the value stays.** `SideA:=3`
answered 3 and a later read in the same pass answered 3. That is the success
criterion of this phase -- whether a program can set it -- answered with rows
rather than with HP's word, for the first time.

**The working shape of an app from a program is now measured end to end.**
Set `SideA`, `SideB`, `SideC` to 3, 4 and 5; call `DoSolve`; read `AngleA`,
`AngleB`, `AngleC` and get 36.8698976458, 53.1301023542 and 90. **`DoSolve`
answered where Phase 7 recorded it refusing**, and the difference is that the
app now had a triangle. Phase 7's entry had named exactly this probe and
called it unverified; it was right to.

**An unset side reads −1, not 0.** A program testing for 0 to find out
whether a side is known is wrong on every fresh app. `TriType` is the
exception at 0, and it is also the one variable `DoSolve` did not write.

**`SOLVE` is not the callable form `Solve` lacked.** All four forms refused,
the bare read included, with the Solve app's variable name carrying a
function's syntax in HP's list. Phase 7's one silent group stays silent, and
the likeliest explanation on the table is now gone.

**One result is not explained by any of this**: `Xlist`, of the Inference
app, answered `{}` with the Function app active and again with the Triangle
Solver active. Whether other variables ignore the rule the same way is
untested, and the fact says so instead of rounding it off.

## Decisions

- **App variables use the entry format unchanged.** `Syntax` takes a row per
  form, so a variable gets its read form and its `:=` form; `Group` is its
  app; whether a program can set it is a Behaviour paragraph paid for with
  rows. No format change, no new field, one format across the documentation.

## Deviations

- **Three rows were spent on a question already answered.** The probe asked
  whether the calculator's channel carries U+03A3, and `results.tsv` already
  held `ΣLIST({1,2,3,4})` answering 10 from Phase 6. Checking the
  file before designing the batch would have cost nothing. Worse, the three
  calls were confounded anyway: every ASCII name in the same groups refused
  too, so they could not have separated the character from the condition.
- **One finding was spoiled by the order of my own calls.** `DoSolve`
  answered the triangle and `DoSolve( )` answered `{}`, but the bracketed one
  ran second, on an already-solved triangle. Whether the brackets or the
  order caused it is not separated, and the entry says so.
- **The phase's first plan did get written first**, which the last four
  rounds of Phase 7 did not.

## Results

```
rows added                              48
app variables with an entry              7 of 172
entries                                475
new facts                                1  (apps.reset-leaves-function-active)
entries corrected                        8
checker                                  0 problems
suite                                 9284 passed, 0 failed
```
