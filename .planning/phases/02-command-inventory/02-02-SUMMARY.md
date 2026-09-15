---
phase: 02-command-inventory
plan: 02
status: complete
completed: 2026-09-11
key_files:
  - hpkit/lint.py
  - hpkit/names.py
  - tests/test_lint.py
  - tests/test_compare.py
  - docs/tools.md
  - README.md
commits: [8b97ae3, 0dec929, 26d1ec0]
---

# Plan 02 summary: the linter that reads the list

## What was built

- The rule `unknown-name` in `hpkit/lint.py`: a call to a name that is
  neither on the list nor defined by the program. It knows the program's
  functions and parameters, locals, exported variables and forward
  declarations, and the calculator's own variables; it skips `#pragma` lines,
  block comments and strings. A warning for a file alone, an error with
  `--set`.
- The hand-kept `BUILTINS` set is gone; the `one-based` rule reads the list.
- `lint_files()` returns the findings and `check_files()` prints them, so a
  set of files can be tested.
- Names are compared without regard to case. Whether the calculator ignores
  case in its own names has not been measured, and the code and
  `docs/tools.md` say so.

## Results

```
python tests/test_lint.py      38 passed, 0 failed
python tests/run_all.py        606 passed, 0 failed (612 after groups.md)
hpprime lint LEN.txt           WARN unknown-name: STRLEN ...     exit 0
hpprime lint LEN.txt --set     ERROR unknown-name: STRLEN ...    exit 1
```

## Deviations

- `tests/test_compare.py` renamed its library function from `AREA` to
  `ZAREA`. Its case shows that the linter cannot tell `NAME(0)` from an
  index, which stopped being true of `AREA` once the list knew it as one of
  HP's names.

## For later phases

- The kit's starter program exports a function called `AREA`, which is also
  the name of a Function app function. What the calculator does with a
  program's `EXPORT AREA` has not been measured. It belongs to the starter
  and to the entry for `AREA` (Phase 7).
