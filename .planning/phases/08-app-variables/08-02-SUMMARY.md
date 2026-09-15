---
phase: 08-app-variables
plan: 02
status: complete
completed: 2026-09-14
key_files:
  - docs/commands/function/*.md
  - .planning/STATE.md
commits: []
---

# Plan 02 summary: the Function app, and a debt paid by one quote mark

## What was built

- **16 rows** from one batch that needed no app selected, because a reset
  calculator already has the Function app active.
- **5 entries written**, the Function app's whole variable group, and the
  first use of the `-var` file suffix built in Phase 7 and never needed
  until now.
- **5 entries corrected**: the function commands gained a row each, and two
  of them had said something a batch has now disproved.

## What this turned up

**`F1:='X^2-4'` stores the expression. The quote is the whole difference.**
Phase 7 found that `F1:=X^2-4` stored the **number** −4, because `EXPR`
evaluates before it assigns, and concluded that a batch could not put a real
function into `F1` at all -- that a person had to type it into the app's own
editor. That was wrong. With the quote, `F1` comes back holding `X^2-4` as an
expression object, type 8. `F2:="X"` as a string does the same. The standing
question of Phase 7 is answered, and it cost one line.

**So the entire Function app group is measurable by a batch alone.** In one
run, with no keypresses beyond starting it: `ROOT(F1,1)` answered 2,
`EXTREMUM(F1,0)` 0, `SLOPE(F1,2)` 4, `AREA(F1,0,2)` −5.33333333333 and
`ISECT(F1,F2,2)` 2.56155281281. Every one matches the value taken by hand in
Phase 7, so this is a reproduction and not a new set of claims.

**Two entries had said a batch could arrange neither condition.** They now say
it can arrange both, and they say what was really missing: a quoting rule,
not an ability. The correction is in the entries rather than in a silent
rewrite of the rows.

**The commands do not write their own variables, and that kills a pattern.**
`ROOT` answered 2 and the very next call read `Root` as 0. `ISECT` answered
2.56155281281 and `Isect` read 0. `SLOPE` answered 4 and `Slope` read 0. In
the Triangle Solver, `DoSolve` *had* written its answers into `AngleA` and
its neighbours, and the obvious generalisation was that an app command fills
the variable of the same name. It does not. One app does it and one does not,
and each entry now says which.

**`Extremum` is the trap in that set.** It read 0, and `EXTREMUM(F1,0)`
answered 0, because `X^2-4` turns at zero. Read alone, that row says the
command stored its answer. Read beside the reading taken *before* the command
ran -- also 0 -- it says nothing of the kind. The entry keeps both rows for
that reason.

**The five variables all read 0 unset, where the Triangle Solver's read
−1.** So there is no shared convention for "not computed" across apps: one
marks absence visibly and the other cannot be distinguished from a real
answer of zero. A program cannot write one test that works on both.

## Deviations

- **A call of mine did not compile, and the line number paid for itself.**
  `EXPR("F2:="X"")` ended its own string early; PPL writes a quote inside a
  string by doubling it. The Check reported line 33, the harness line map put
  that at call 5, and call 5 was the one with the quotes. Nothing else in the
  batch had to be guessed at, which is what
  `ppl.check-last-error` is for.
- **A shell heredoc died on apostrophes for the third time in this project**,
  writing five entries at once. The files were checked, none had been
  written, and they went through the editing tool instead -- which is what
  this project's own note has said to do since Phase 5. Reaching for the
  heredoc again was the mistake, not the failure.

## Results

```
rows added                              16
app variables with an entry             12 of 172
entries                                480
entries corrected                        5
checker                                  0 problems
suite                                 9424 passed, 0 failed
```
