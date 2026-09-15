---
phase: 08-app-variables
plan: 03
status: complete
completed: 2026-09-15
key_files:
  - docs/commands/inference/*.md
  - docs/topics/ppl.md
  - docs/commands/function/*.md
  - .planning/STATE.md
commits: []
---

# Plan 03 summary: the Inference app, and a name HP spelled wrong

## What was built

- **64 rows** from two batches with the Inference app selected by hand: a
  sweep of all 50 variables plus three controls, then eleven calls on the
  workflow. One further row was overwritten; see Deviations.
- **50 entries written**, the Inference app's whole variable group. The
  checker caught three errors of mine on the first run: `Alpha` citing a call
  text whose row held a refusal, `μ₀` citing a row stored under the other
  spelling's name, and the new fact declared as kind `trap`, which is not one
  of the two kinds the format allows. I fixed the first two and missed the
  third, because I read only the last eight lines of fourteen problems; it was
  fixed to `rule` by another agent while this session was interrupted, and
  that fix is kept.
- **One new fact**, `ppl.mu-zero-spelling`.
- **6 entries corrected**: `DoInference`, whose Phase 7 entry was wrong in
  four separate claims, and five Function app commands whose row references
  had shifted by one when a row was inserted above them.

## What this turned up

**49 of 50 answer with the app active, and the three controls refuse.**
`Root`, `AngleA` and `MeanX` -- one variable from each of three other apps --
were all refused with Inference active. The app rule came out as clean as it
has anywhere.

**The one refusal is a spelling, and the spelling is HP's.** `μ₀` is on the
list with GREEK SMALL LETTER MU, U+03BC, and the calculator refuses it in two
batches under two different apps. The same glyphs with MICRO SIGN, U+00B5,
answer 0.5. The other eleven Greek and subscripted names in the group -- `π₀`,
`σ₁`, `σ₂`, `n₁`, `n₂`, `s₁`, `s₂`, `x₁`, `x₂`, `Mean₁`, `Mean₂` -- all answer
as listed, so this is one name and not a rule about non-ASCII. Before calling
it HP's error the extractor was checked: it does not normalise, the other
twenty Greek names on the list kept their letters, and the Command Tree
spells this one with Greek mu. **The consequence reaches Milestone 2**: the
linter compares a program's names against the list, so it accepts the
spelling the calculator refuses and flags the one that works as invented.

**The app ships with a worked example loaded.** On a calculator the harness
had just reset, `n₁` and `n₂` read 50, `Mean₁` 0.461368, `Alpha` 0.05 and
`Conf` 0.99. That makes three apps with three conventions for a value nobody
has written: the Triangle Solver's −1, the Function app's 0, and here
somebody else's example. A program reading before writing cannot use one test
for all three.

**`DoInference` answers, and writes its results into the app.** It returned
1, and across that one call `TestScore`, `Prob`, `CritVal1` and `Result` all
moved off 0. Phase 7 recorded it refusing, and its entry gave the reasons as
the command's shape and an empty app. Both were wrong: the refusal was the
wrong app, and the app was not empty.

**That turns yesterday's "one app's habit" into a pattern with a reason.**
`DoSolve` and `DoInference` both write their app's variables; `ROOT`,
`SLOPE`, `ISECT` and `AREA` do not. A `Do` command runs over state the app
already holds and has nowhere to put its answer but back into that state; a
function takes arguments and returns. Two apps are not every app, and the
entries say so.

**A program can hand an app a whole data set.** `Ylist:={1,2,3}` answered the
list and a later read answered the same list. Everything set from a program
before this had been a single number.

**`DoSolve`'s bracket question got half an answer.** There, the bracketed
form ran second on a solved triangle and answered `{}`, so brackets and order
could not be separated. Here both forms returned 1, so for this command the
brackets make no difference. The entry for `DoSolve` is not changed on the
strength of another command.

**`Xlist` is still the only variable that answers with a foreign app active**,
now under three apps. None of the other lists were tried that way, so whether
it is alone is the cheapest open question in the phase.

## Deviations

- **A row was overwritten, and it was my doing.** `results.tsv` keys on the
  exact call text. Round 4 generated every call text against the stored keys
  and avoided the trap; round 5 was typed by hand and reused `(Alpha)`, which
  turned a refusal measured with the Function app active into 0.01 measured
  with Inference active. The row count gave it away -- 750 where the
  arithmetic said 751 -- and a diff against the last commit named it. The
  loss is redundant, since two other rows still carry that refusal and no
  entry lost its evidence, but it cannot be restored by hand, and it is
  exactly the failure this documentation warns about. From here every probe
  list is generated against the stored keys, and a guard in the harness is
  proposed in STATE.md as a decision rather than made.
- **Inserting a row shifted five entries' references by one.** The Function
  app commands gained a batch-reproduced row in position two, and their prose
  said "the second row" about what was now the third. The checker cannot see
  that -- the sentences were well-formed and correctly labelled -- so it was
  found by reading, and fixed in thirteen places.
- **The session broke between writing the last 36 entries and running the
  script that writes them.** Nothing was half-written: the script had not
  run, and it ran whole when the work resumed.
- **Another agent worked in that break, and my commit swept its changes in.**
  Between 00:08 and 00:14 on 2026-09-15, with nothing committed, it changed
  twelve files: it corrected the fact kind above; it turned links in nine
  Inference entries into plain text, because their targets did not exist yet;
  it created `.github/workflows/ci.yml`; and it rewrote `tests/test_lint.py`
  from the project's `PASS: N FAIL: M` style to `unittest`. `git add -A` took
  all of it into a commit carrying my message, and I did not look. I caught
  the CI file after committing; the user then pointed at the other agent, and
  the rest was found from there -- by file times, then proved by regenerating the entries from
  my own scripts and comparing byte for byte: the five written at 23:49:23
  were identical, the nine re-saved at 00:09 were not. The kind fix is kept;
  the links are back now that every target exists; the CI file is out at the
  user's word, with a copy kept outside the repository. The `test_lint.py`
  rewrite is left out of this commit and on disk for the user to decide:
  `tests/run_all.py` finds a suite's result by reading that line, so after the
  rewrite the linter's 39 checks count as zero, and nothing fails to say so.
  **From here nothing is committed with `git add -A`**; each commit stages the
  files its own work touched.

## Results

```
rows added                              63   (64 taken, 1 overwrote)
app variables with an entry             62 of 172
entries                                530
new facts                                1   (ppl.mu-zero-spelling)
entries corrected                        6
checker                                  0 problems
suite                                10611 passed, 0 failed  (39 of the
                                     linter's were not counted; see above)
```
