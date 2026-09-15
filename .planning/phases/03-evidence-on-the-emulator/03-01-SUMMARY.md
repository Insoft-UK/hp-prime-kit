---
phase: 03-evidence-on-the-emulator
plan: 01
status: complete
completed: 2026-09-11
key_files:
  - hpkit/emulator.py
  - hpkit/cli.py
  - hpkit/numbers.py
  - tests/test_emulator.py
  - tests/test_program.py
  - tests/test_numbers.py
  - docs/reference/formats.md
commits: ["Find the Connectivity Kit's folder by what it holds", "What the real mirror showed"]
---

# Plan 01 summary: the localised folders, and the reader's case

## What was built

- `emulator.calculators_in()`, `find_ck_root()` and a fallback in
  `find_root()`: the calculators folder is found by a known name
  (`Calculators`, `Calculadoras`) or by what it holds, and a folder of apps
  is not taken for it. `HPPRIME_CK_ROOT` overrides.
- `hpprime doctor` names both folders: on this machine
  `...\HP Connectivity Kit\Calculadoras` (ten calculators) and
  `...\HP Prime\Calculators`.
- `test_program` and `test_numbers` use the same function, and so read this
  machine's own binaries for the first time.

## TOOL-03

Already done before this phase: cd14080 (2026-09-10), "The reader could hand
back the wrapper instead of the source", with `tests/test_program.py`
writing the five edge lengths (32,726, 32,737, 32,784, 32,801, 32,848) every
run. No change was needed. `PROJECT.md` had said it was not reproduced; it
was corrected.

## Deviations, all found by reading the real mirror

- `doctor` crashed on calculator names with characters the Windows console
  cannot encode. Every command now reconfigures stdout to replace them.
- Two header words (offsets 20 and 44) vary between real programs and are
  not lengths. The cross-build reports them instead of failing;
  `formats.md` records them as seen in twelve programs, meaning unverified.
- `M1` and `M2` on two calculators are vectors (rank 1). The reader refused
  them as "not a matrix"; it now says their layout is not measured, and the
  suite lists them as not covered.
- `VaporHP`'s block holds a plain global and a forward-declared function;
  the check that counted only `EXPORT`s called them missing. It now uses
  `lint.scan_names`.

## Results

```
python tests/run_all.py     655 passed, 0 failed, across 12 suites
hpprime doctor              both folders named
```

## For later phases

- The layout of a vector longer than one element: the first batch can store
  `[1,2,3]` in `M1` and read the file back.
- What the header words at 20 and 44 mean.
