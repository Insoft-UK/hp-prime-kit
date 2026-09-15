---
phase: 03-evidence-on-the-emulator
plan: 03
status: complete
completed: 2026-09-12
key_files:
  - docs/commands/results.tsv
  - docs/commands/strings/LEFT.md
  - docs/commands/strings/RIGHT.md
  - docs/commands/list/SIZE.md
  - hpkit/interp.py
  - hpkit/numbers.py
  - hpkit/examples.py
  - docs/reference/deploy.md
  - docs/reference/formats.md
commits: ["The batch runs on Prime_1", "The first batch's answers", "A negative count is an error", "SIZE of a matrix is a list", "A vector in .hpmat is rank 1 and one row", "The breaks follow the labels the batch changed"]
---

# Plan 03 summary: the first real batch

27 calls on the Virtual Calculator 2.4, build 2025-09-15: the 23 examples of
the five entries, and four probes for questions the entries left open. The
user pressed the keys; the answers are in `docs/commands/results.tsv`.

## What the calculator said

26 of the 27 agreed with their entry. The one that did not:

| Call | The entry said | The calculator |
|---|---|---|
| `LEFT("abcdef", -1)` | `"abcdef"` (HP help) | *error* |

The probes:

| Probe | Answer | What it settles |
|---|---|---|
| `RIGHT("abcdef", -1)` | *error* | the same refusal, never measured before |
| `TYPE(SIZE([[1,2,3],[4,5,6]]))` | `6` | the dimensions are a list, not a vector |
| `M1 := [1,2,3]; RETURN SIZE(M1);` | `{3}` | and `M1.hpmat` gave the vector's layout |
| `LEFT(42, 2)` | *error* | the interpreter's refusal was not invented |

## What changed because of it

- `LEFT` and `RIGHT`: a negative count is an error (emulator), and both
  entries keep HP's wording on the record beside it. The interpreter raised
  the whole string for `LEFT` and `Unsupported` for `RIGHT`; both now raise.
- `SIZE`: the dimensions are `{2,3}`, a list. The `TYPE` call stays in a
  paragraph, not an example: the interpreter has no `TYPE` and does not grow
  in this milestone.
- Eight examples taken from HP's help came back exactly as stated and were
  relabelled `emulator` by `--relabel`.
- `.hpmat`: rank 1 is a vector, one row of `n` elements (40 bytes for
  `[1,2,3]`, the words after the rank 1 and 3). The reader reads them now,
  `formats.md` says so, and the two files the suite used to skip are read.
- `deploy.md` section 1: a new window opens `Prime`, `Prime_1`, `Prime_2`...
  by the locks they hold, never a calculator with another name.

## Deviations

- **The throwaway calculator is `Prime_1`, not `DOCS`.** The first launch, with
  `Prime` open, made an empty `Prime_1` and opened that, leaving `DOCS`
  untouched. `emulator.next_opens()` now reads the lock files before
  launching, and the command refuses unless the next window will be the batch's
  calculator. `DOCS` and the empty `Prime_1` were moved into the kit's folder,
  not deleted.
- **`VERSION` carries the calculator's serial number**, and `results.tsv` is
  committed. `firmware()` keeps the version number and the build date and
  nothing else. The first write of `results.tsv` held the raw block; it was
  rewritten from `M9` before anything was committed, and the serial has never
  been in a commit.
- The `calc.hpsettings` of an open calculator moved three times without the
  window closing, so the wait is on the process and the file only says which
  calculator a window had. Written into `deploy.md`.
- No answer in the first batch was a matrix, so that part of EVID-03 stood
  open until a second batch of two probes closed it the same night.

## The second batch

Two probes, run the same way, for the one kind of answer the first batch had
not produced:

| Probe | Answer | What it settles |
|---|---|---|
| `M1 := [[1,2],[3,4]]; RETURN M1;` | `[[1,2],[3,4]]` | a matrix comes back like anything else |
| `TYPE([[1,2],[3,4]])` | `4` | HP's help says 4 for a matrix; now it is measured |

So `TYPE` is measured for a number (0), a string (2), a matrix (4) and a list
(6), all of them by the harness itself, which calls `TYPE` on every answer it
brings back. The 2x2 `M1.hpmat` the calculator left is rank 2, type `0014`,
and reads back as `[[1,2],[3,4]]`.

## Results

```
python tests/run_all.py        727 passed, 0 failed, across 13 suites
hpprime docs --check           5 entries, 3 facts, 25 examples run: 0 problems
docs/commands/results.tsv      29 rows, all on Virtual Calculator 2.4,
                               build 2025-09-15
```

## Open

- Whether `agrees()` should treat `[2 3]` and `{2,3}` as the same value, which
  it does today.
- What the header words at 20 and 44 of an `.hpprgm` mean.
