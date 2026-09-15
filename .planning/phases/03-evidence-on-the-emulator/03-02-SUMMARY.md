---
phase: 03-evidence-on-the-emulator
plan: 02
status: complete
completed: 2026-09-11
key_files:
  - hpkit/examples.py
  - hpkit/docs.py
  - hpkit/cli.py
  - docs/format.md
  - docs/tools.md
  - tests/test_examples_run.py
  - tests/test_reference.py
commits: ["hpprime examples: the documentation's examples on the Virtual Calculator", "The documentation answers to what the emulator said"]
---

# Plan 02 summary: the batch runner, and results.tsv

## What was built

- `hpkit/examples.py` and `hpprime examples NAMES... | --all [--probe E=CALL]
  [--no-wait] [--collect] [--relabel]`.
- The program, `HPKDOC`: every call inside `IFERR`; a call with a `;` becomes
  a function of its own; each answer written into a row of `M9` by `ZENC`
  (answered, `TYPE`, the number, the length of `STRING` of the answer, then
  its character codes from `ASC`); row 1 is `VERSION`. It goes through the
  linter before it is written.
- The run: `DOCS` is cloned from `Prime` the first time and reset before
  every batch; the program is written there; an emulator is launched; the
  keys are printed; nothing is read unless `DOCS`'s `calc.hpsettings` moved.
  What to collect is kept in the kit's state folder, so `--collect` works
  after `--no-wait`.
- `docs/commands/results.tsv`: entry, call, answer, type, firmware, date,
  merged by (entry, call).
- `hpkit/docs.py`, `results_check`: a stored answer that differs from the
  entry is a problem; an `emulator` label with no stored answer is a problem.
- `--relabel`: `HP help` becomes an `emulator` label linking to results.tsv
  where the stored answer agrees, and each change is printed. `G2` is never
  touched.
- `docs/format.md` (what results.tsv is), `docs/tools.md` (the command, the
  suite, the module), `README.md` (the command, thirteen suites).

## Deviations

- `results.tsv` does not exist yet. Its first rows come from the real batch,
  plan 03.
- The program is not removed from `DOCS` after collecting. `DOCS` is reset
  before every batch, which clears it; deleting only the file would leave
  the calculator's own record of a program whose file is gone.
- `M9` is always the matrix: `DOCS` is reset, so nothing of the user's is in
  it.
- The names `TYPE` gives its numbers are HP help's and unverified;
  `results.tsv` keeps the number, not the name.

## Results

```
python tests/test_examples_run.py   20 passed
python tests/test_reference.py      25 passed (two new breaks)
python tests/run_all.py             678 passed, 0 failed, across 13 suites
hpprime docs --check                0 problem(s)
```
