---
phase: 08-app-variables
plan: 05
status: complete
completed: 2026-09-25
key_files:
  - docs/topics/apps.md
  - docs/commands/statistics-1var/*.md
  - docs/commands/statistics-2var/*.md
  - docs/commands/advanced-graphing/*.md
  - docs/commands/spreadsheet/*.md
  - docs/commands/linear-solver/*.md
  - docs/commands/sequence/SeqPlot.md
  - docs/commands/solve/SOLVE-var.md
  - hpkit/interp.py
  - hpkit/docs.py
  - docs/tools.md
  - README.md
---

# Plan 05 summary: every app variable, through its app's name

## What was built

- **165 rows** from two batches, neither with an app selected: 116, then
  47 calls and two programs checked for compiling beside the two controls.
  Both controls came out right. None overwrote a stored row.
- **42 entries written**, the last app variables: 172 of 172, and with them
  706 of the 706 names that get an entry.
- **One new fact**, `apps.qualified-names`, and two corrected:
  `apps.function-needs-active-app` says the name in front lifts it, and
  `apps.triangle-solver-degrees` is retitled "while it is active".
- **15 entries corrected**: `Do1VStats` and `Do2VStats` rewritten, since
  both blamed their data for a refusal that was the app; `AngleA`, `Alpha`,
  `PV`, `Xmin`, `SSS`, `SUM` and `Solve` gained their qualified row;
  `AVERAGE` and four Finance entries point at the new form; `Xlist`'s summary
  line still called it the only variable of its kind, which 08-04 had
  disproved in its body.
- **Three interpreter fixes**, found by running the new fact's programs
  through `hpprime run`; see Deviations.

## What this turned up

**A program reaches another app's variables and functions by writing the
app's name in front, and the bare name does not.** With the Function app
active, `Triangle_Solver.AngleA`, `Inference.Alpha` and `Finance.PV`
answered, all three refused bare under the same condition in earlier
batches; `Function.Xmin` answered as `Xmin` does. A space in the app's name
becomes an underscore. The two programs showed it is not an `EXPR` effect:
written in a program's source, it compiled and answered.

**So the rule the phase was built around has a way round it.** Phase 8's
first plan found that the app rule reaches variables, and concluded that
most of the 172 names needed the person to select an app before each batch.
Seven such rounds were planned for the last 42. Probing the qualified form
first, at the user's choice, made them two unattended batches.

**Every statistic matched the hand computation.** With `{1,2,2,3,7}` the
mean came out 3 and the median 2; the quartiles 1.5 and 5 say which method:
the halves without the median. `ssX` is the sum of squared deviations, 22;
`serrX` is the sample deviation over the square root of the count. For the
pairs, `Corr` 0.959166304663 and `CoefDet` its square, 0.92.

**The name in front picks the app, not only the permission.**
`Statistics_1Var.MeanX` answered 3 and `Statistics_2Var.MeanX` 2.5 in the
same batch: two values under one name.

**The active app's settings still apply.** `Triangle_Solver.SSS(3,4,5)`
answered in radians from the Function app, where the same call with the
Triangle Solver active answers degrees. The unit follows the active app, as
`apps.app-mode-overrides-home` found for Home's settings.

**Empty looks different in each app.** The Statistics 1Var results read 0
with no data; the Statistics 2Var results and `LSolution` refuse. A program
reading either kind needs a different test.

**`SOLVE` is the Solve app's solver, and `Solve` is still nothing.**
`Solve.SOLVE(X^2-4=0,X,1)` answered 2; `Solve.Solve` with the same arguments
was refused. HP's list files `SOLVE` as a variable with a function's syntax,
and the syntax was right.

**What a program can set**: the settings, twelve of them, `LSystem`
included, which solves the system at once. The computed results refuse,
and so do `Col` and `Row`. `SeqPlot` took 1 without an error and still read
0.

## Deviations

- **I miscounted the first batch, and said so to the user.** The plan's
  second section and my report said 39 of the 42 answered qualified at once;
  it was 28, the other 14 answering once their app had data or, for
  `SOLVE`, when called. Found while writing the fact's evidence, corrected
  in the plan and in the chat.
- **`hpprime run` called the calculator wrong three ways, all fixed.**
  `Statistics_1Var.MeanX` was a syntax error at load, "unexpected character
  '.'", about a program the calculator had just compiled. A name starting
  with a letter outside ASCII, `ΣLIST` or `σX`, ended in a Python traceback,
  which Phase 9.1 promised never happens. And a name the calculator has,
  `Xmin` or `SSS`, was "undefined variable" or "no such", an error the
  calculator does not raise. Now the first two are one token each, the
  qualified one a case not covered, and a name on HP's list that the
  interpreter lacks raises "not covered". A test holds all three, and
  `tools.md` states the rule.
- **Two pairs of names fold together on this filesystem**: `ΣX` and `σX`,
  `ΣY` and `σY`, capital and small sigma. The small sigma takes the `-var`
  suffix built for `ROOT` and `Root`, and the comment that declares the
  suffix now says so.
- **The row that assigns `SOLVE` cannot say whether the assignment was
  refused**, because the read after it is refused anyway. The entry says
  that instead of "a program cannot set it".

## Results

```
rows added                             165   (none overwritten)
app variables with an entry            172 of 172
entries                                706 of 706
new facts                                1   (apps.qualified-names)
facts corrected                          2
entries corrected                       15
docs/llms.txt                       91,328 bytes of 100,000
suite                               14,713 passed, 0 failed
```
