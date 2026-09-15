---
phase: 03-evidence-on-the-emulator
verified: 2026-09-12
status: approved
---

# Phase 3 verification: Evidence on the Virtual Calculator

## Success criteria

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| 1 | `hpprime doctor` finds the Spanish Connectivity Kit (`Calculadoras`) and the Virtual Calculator, and says which folders it used | VERIFIED | `doctor` prints `...\HP Connectivity Kit\Calculadoras` (ten calculators) and `...\HP Prime\Calculators`; `tests/test_emulator.py` covers the localised name, a folder found by what it holds, a folder of apps that is not one, and `HPPRIME_CK_ROOT` |
| 2 | A batch of examples is sent, run with one keypress on the emulator and read back, strings, lists, matrices and errors included | VERIFIED | 27 calls in the first batch: numbers, strings (`"MOM"`), lists (`{1,3,5,7,9}`, `{2,3}`) and errors (*error* for `MID("abcdef", 0, 2)` and four more). A second batch of two calls brought back the matrix `[[1,2],[3,4]]` and `TYPE` of one, `4` |
| 3 | Each result is stored with the firmware it came from, and one that differs from HP's stated result is flagged | VERIFIED | every row of `docs/commands/results.tsv` says `Virtual Calculator 2.4, build 2025-09-15`; `LEFT("abcdef", -1)` came back *error* against HP's `"abcdef"`, was reported as DIFFERENT, and `hpprime docs` fails while an entry disagrees with a stored answer (`tests/test_reference.py`: "catches a stored answer that differs from the entry") |
| 4 | The reader's wrong pick between two source records ending at the same offset is reproduced in a test and fixed | VERIFIED | cd14080 (2026-09-10): `tests/test_program.py` writes the five sizes that used to trip it (32,726; 32,737; 32,784; 32,801; 32,848) every run |

## Requirements

| ID | Status | Evidence |
|---|---|---|
| EVID-01 | VERIFIED | `emulator.calculators_in()` and `find_ck_root()`; `doctor` names both folders |
| EVID-02 | VERIFIED | `hpprime examples`: one generated program, `HPKDOC`, three keypresses on the emulator, `M9.hpmat` read back |
| EVID-03 | VERIFIED | strings, lists, errors and a matrix have all come back, each as `STRING` of the answer with its `TYPE` beside it |
| EVID-04 | VERIFIED | `results.tsv` keeps the answer and the firmware; a difference is flagged and never replaced (`--relabel` only moves a label where the answers agree, and never a `G2` one) |
| TOOL-03 | VERIFIED | cd14080, with the test over the five sizes |

## Tests

```
python tests/run_all.py     727 passed, 0 failed, across 13 suites
hpprime docs --check        0 problem(s)
```

## The second batch, which closed the gap

The first batch answered no matrices, so criterion 2 and EVID-03 stood at
PARTLY until a second batch of two probes ran the same way, on the user's
keypresses:

| Probe | Answer | What it settles |
|---|---|---|
| `M1 := [[1,2],[3,4]]; RETURN M1;` | `[[1,2],[3,4]]` | a matrix comes back like any other answer |
| `TYPE([[1,2],[3,4]])` | `4` | HP's help says 4 for a matrix; now it is measured |

It also left an `M1.hpmat` the calculator wrote with known contents: rank 2,
2x2, type `0014`, which is one of the three high bytes `formats.md` records,
and the reader gives back `[[1,2],[3,4]]`.

## Human approval

- [x] Phase 3 approved to close — the user, 2026-09-12, after running both batches on the emulator
