---
phase: 05-statements-and-program-commands
plan: 01
status: complete
completed: 2026-09-12
key_files:
  - docs/commands/block/*.md
  - docs/commands/branch/*.md
  - docs/commands/loop/*.md
  - docs/commands/variable/*.md
  - docs/commands/function/KEY.md
  - hpkit/docs.py
  - hpkit/interp.py
commits: ["The 14 statements, and a result that says there is nothing to record", "The four probes the next batch carries, written down"]
---

# Plan 01 summary: the language itself

## What was built

- The 14 statements: `BEGIN`, `KILL`, `RETURN`; `CASE`, `IF`, `IFERR`;
  `BREAK`, `CONTINUE`, `REPEAT`, `WHILE` beside the `FOR` that already
  existed; `EXPORT`, `LOCAL`; `KEY`.
- A third form of Result cell, `*no value*`, for an example that runs
  nowhere: the command's result is a screen or a keypress, and there is no
  answer a batch could store. The user chose extending the format over the
  three alternatives.

## What this turned up

**The format had a gap, and the statements are where it showed.** `KILL;`,
`BEGIN commands; END;` and `VIEW "Text" Function()` have nothing to put in a
Result column. Writing `*error*` would be false and inventing a value worse,
so the format gained a form that says so and that neither the interpreter nor
a batch tries to run.

**My own example was illegal PPL.** The first batch of the phase was refused
at line 3, and the line was the `BEGIN` entry's example: a `BEGIN` block
nested inside the program's own. Isolated later with a hand-written program,
it is a syntax error on the calculator. `hpkit/interp.py` now refuses a nested
`BEGIN` too, so the PC and the calculator agree about it.

Three divergences between this kit's interpreter and the calculator came out
of the same batch and were settled in the interpreter's favour only where the
calculator agreed: a list renders as `{a,b}`, `STRING` of a string keeps its
quotes, and `LEFT`/`RIGHT` with a negative count is an error rather than the
whole string.

## Deviations

- The plan expected 19 entries in the documentation at the end; there are 19,
  but the four probes it promised did not all land here. `BREAK 2` and
  `LOCAL za := 2, zb := 3` ran; `IF a = 1 THEN` and the bare `END` needed
  hand-written programs, because the harness lints what it sends and refused
  to send a probe its own rules called an error. They were measured in plan
  02's window and are recorded there.

## Results

```
hpprime docs --check      19 entries: 0 problems
python tests/run_all.py    passed, 0 failed, across 13 suites
```
