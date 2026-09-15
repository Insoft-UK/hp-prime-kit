---
phase: 06-home-functions
plan: 01
status: complete
completed: 2026-09-13
key_files:
  - docs/commands/arithmetic/*.md
  - docs/commands/list/*.md
  - docs/commands/numbers/*.md
  - docs/topics/ppl.md
  - hpkit/examples.py
  - tests/test_examples_run.py
commits: ["Ten Home functions, and a guard for the one answer we must not keep", "Regenerate the page the re-wrap left stale", "Fifteen more Home functions, measured before they were written"]
---

# Plan 01 summary: arithmetic, list and numbers, and the guard

## What was built

- All 34 names of the block: 13 `arithmetic`, 13 `list`, 8 `numbers`.
  `SIZE` already had an entry from Phase 1 and kept it.
- `NEVER_STORED` in `hpkit/examples.py`, holding `SERIAL`, with a test that
  fails if a guarded answer reaches `results.tsv` **or** the report.
- Two facts: `ppl.imaginary-unit`, and `ppl.type-codes` gained a measured
  code 3.

## What this turned up

**The guard needed to cover two paths, not one.** `collect()` builds a row for
every case and hands the same `Answer` object to `_report`, and `displayed` is
a read-only property. A guard on the stored file alone would still have put
the calculator's serial number on screen and into a session transcript.
Replacing the object's text closes both with one line. The test checks both,
and checks that a name *not* on the list keeps its answer, so the guard cannot
quietly discard measurements.

**`MOD` is the finding of the plan.** The calculator refuses `MOD(9,4)` at
compile time -- a batch carrying it was rejected at that line and never ran --
and answers `9 MOD 4` as 1. This kit's interpreter is the exact inverse: the
builtin `_b_mod` is correct and answers `MOD(9,4)` as 1, while the parser has
no infix `MOD` at all, so `9 MOD 4` comes back as 9 and `9 MOD 4 + 100` comes
back as 9 as well, the rest of the expression dropped with no error. **Neither
spelling works on both machines**, and only measuring both sides showed it.
The parser defect is written down in `STATE.md`; fixing it is a change to the
tool and goes through its own decision.

**`TYPE` 3 is measured for the first time**, on what `CONJ` answers. That is
the second code this session to move from HP's help to measured, after 8 from
`CAS` in Phase 5.

**The imaginary unit goes in as ASCII and comes back as a private-use glyph.**
`3+4*i` and `(3,4)` are both accepted, and the answer carries U+E003. Nothing
in the kit normalises it, unlike the minus sign, so `results.tsv` holds the
glyph literally and a program comparing against its own text will not match.

**`DIFFERENCE` is the symmetric difference**, not a subtraction: `{1,2,3}`
against `{2,3,4}` is `{1,4}`, not `{1}`. The name reads like subtraction in
every other library, which is exactly why it is worth an entry.

**The interpreter raises Python tracebacks on legal PPL.** Eight of HP's own
worked examples for this block hit it -- `CONCAT` with a list, the list forms
of `CEILING`, `FLOOR`, `FP` and `IP`, `ROUND` with a list of places. The
checker classifies them as *uncovered*, which is a note, so the documentation
pipeline tolerates what the command line crashes on. Also in `STATE.md`.

## Deviations

- The plan said eleven entries could be drafted before the batch. It was ten:
  `MOD` is implemented by the interpreter but HP's list gives it neither a
  syntax string nor an example, so its Result column would have been invented.
- The plan expected one batch. It took three. The first was refused at line 95
  -- `MOD(9,4)` -- and since a refusal stops the compiler at the first error,
  the relaunch kept what had already compiled and moved the genuinely
  uncertain probes into a small batch of their own, so that one refusal could
  not cost another round of keypresses for the other 45 calls.
- **Seven entries were written with a label I invented**, "(emulator: not this
  one -- measured on the PC)". It passes the format check because it contains
  the word `emulator`, and it was wrong: it claimed a calculator had run what
  the interpreter ran. Corrected to `unverified`, which is what the house has
  always used for that. The checker cannot catch this class, and that is worth
  knowing.
- **One commit went in on a red tree.** Re-wrapping a paragraph staled a
  generated page; the guard meant to stop the commit was a shell `&&` chain
  whose steps ended in a pipe to `tail`, and a pipeline's status is the last
  command's, so it never blocked. Repaired in the next commit, and the checks
  now run from a driver that reads return codes.

## Results

```
python tests/run_all.py     3070 passed, 0 failed, across 13 suites
hpprime docs --check        146 entries, 109 facts: 0 problems
plan 06-01                  34 of 34 names
phase 6                     34 of 177
```
