---
phase: 07-app-functions
plan: 02
status: complete
completed: 2026-09-13
key_files:
  - docs/commands/explorer/*.md
  - docs/commands/spreadsheet/*.md
  - docs/commands/results.tsv
commits: ["Explorer computes from Home and spreadsheet does not, whatever it is given"]
---

# Plan 02 summary: spreadsheet and explorer

## What was built

- All 26 names: 4 `explorer` and 22 `spreadsheet`, covering both groups
  exactly.
- Phase 7 stands at 60 of 179.

## What this turned up

**The four `explorer` names answered, and every one matched a value worked
out before the calculator was asked.** `LinearSlope(0,0,2,1)` is 0.5,
`LinearYIntercept(2,3,1)` is 1, `QuadDelta(1,-3,2)` is 1 and
`QuadSolve(1,-3,2)` is `{1,2}`. Four predictions, four matches: that is the
difference between a command computing and a command handing something back,
and it is why the calls were chosen with known answers.

**Every one of the 22 `spreadsheet` names was refused.** Not some of them,
and not the ones needing a cell: all of them, including `AVERAGE({1,2,3})`
and `SUM({1,2,3})`, which take a plain list and need no cell, no range and no
app state.

**That refutes this plan's own design.** It said three shapes lived in
`spreadsheet` and would be measured differently -- argument-taking, range and
model, and the two that read the current cell. The shapes make no difference:
a plain list, four separate numbers, a range and no arguments at all were all
refused identically. The boundary is the group, not the argument.

**The obvious explanation was tested and refuted too.** HP files these names
under `Toolbox App Spreadsheet`, which suggests they only live inside the
app. But HP files the four `explorer` names under `Toolbox App Explorer` in
exactly the same way, and those four answered from Home in the same batch. So
belonging to an app's menu is not what separates the two groups, and the
entries say the cause is not established rather than inventing one.

**`ConfZ2prop` was deliberately sent in its own published shape** -- four
separate numbers, not a list -- so that the group's refusal could not be
blamed on a wrong argument. It was refused like the rest.

**What is measured is narrow and the entries state it exactly**: these names
are not reachable by evaluating a string from Home on a calculator reset
before the run. Two probes would settle the rest, one batch each: the same
call written straight into a program instead of inside `EXPR`, and the same
call made from inside the Spreadsheet app with a sheet open.

## What this batch did NOT settle

No name in this plan came near the harness's 160-character width: the four
that might have -- `STAT1`, `STAT2`, `REGRS` and `AMORT` -- are all in the
refused group, and the longest answer here was 7 characters.

**Corrected 2026-09-13.** This section first called the width question
untested. It was answered in Phase 6, where `SVD([[1,2],[3,4]])` was
truncated and its row records it, and `matrix/SVD.md` and `matrix/SVL.md`
write it up. The narrow truth is that phase 7 has not produced an answer long
enough to reach the limit, which is a statement about these batches and not
about the harness.

## Deviations

- **The plan's design section was wrong**, and it is recorded as refuted
  above rather than quietly rewritten. The batch was worth running for that
  alone: it cost one round and removed a false premise from three later
  plans.
- **One missing label in 26 entries**, in `SUM`, caught by the checker at
  seven entries rather than at twenty-six. The nineteen that followed were
  written only after the shape was verified.
- **A verification script of mine reported three false failures.** It
  compared an example's `result` field against the stored answer, but the
  loader represents an `*error*` result as `None`, so three correct entries
  looked wrong. The script was at fault, not the entries, and the kit's own
  checker was quiet about them throughout. A check that fails correct files
  is as dangerous as a missing one, which is why this is written down rather
  than fixed in silence.

## Results

```
explorer                     4 of 4
spreadsheet                 22 of 22
phase 7                     60 of 179
checker                     0 problems
suite                       6710 passed, 0 failed
```
