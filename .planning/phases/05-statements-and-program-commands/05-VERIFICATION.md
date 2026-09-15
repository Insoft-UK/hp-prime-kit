---
phase: 05-statements-and-program-commands
verified: 2026-09-12
status: approved
---

# Phase 5 verification: Statements and program commands

## Success criteria

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| 1 | Every name the inventory files under statements and program commands has an entry in the fixed format | VERIFIED | 112 names in scope on `names.tsv` -- 14 of kind `statement`, 98 of kind `command` -- and 112 have an entry, none missing. `hpprime docs --check` holds all 113 entries in the documentation to the format and reports 0 problems |
| 2 | Every example in those entries has a Virtual Calculator result on file, or says why it cannot have one | VERIFIED | 178 example rows across those entries: 163 have a stored answer in `results.tsv`, 15 are `*no value*`, and **0 are neither**. `*no value*` is the form the phase added for a call whose result is a screen or a keypress; the checker refuses an example labelled `emulator` with no stored answer, so the 163 are enforced rather than claimed |
| 3 | The tests pass with the new entries included | VERIFIED | `python tests/run_all.py`: 2533 passed, 0 failed, across 13 suites. `test_docs.py` alone walks 1,990 links and identifiers |

## Requirements

| ID | Status | Evidence |
|---|---|---|
| CMD-08 | VERIFIED | criterion 1: every statement and program command has an entry -- blocks, branches, loops, variables, functions, strings, drawing, matrices, input and output, app control |

CHECK-04 is Phase 4's and stays as it was: every lint rule is tied to a fact
or says what it comes from, and the audit of which facts a PC could catch and
no rule does is still open. This phase made that audit larger and more worth
doing: 108 facts now, and 113 entries to read them against.

## Tests

```
python tests/run_all.py     2533 passed, 0 failed, across 13 suites
hpprime docs --check        113 entries, 108 facts, 60 examples run: 0 problems
docs/commands/results.tsv   176 rows, all from Virtual Calculator 2.4, build 2025-09-15
```

## What this phase changed about the documentation

Writing 108 entries against a calculator rather than against HP's help turned
up things no amount of reading would have:

- **The factor of ten is explained.** `GROBW` answered 10 where `GROBW_P`
  answered 100, and four entries were deferring the question to each other.
  A drawing unit is ten pixels and the view's origin is the middle of the
  screen, `px = 160 + 10x`. It is now the fact `interface.draw-units`, and
  `DIMGROB`'s "probably" became a measurement.
- **A lint rule was wrong and is gone.** `equality` called a bare `=` in a
  condition an error; the calculator compiles it and compares. A linter that
  flags legal code is worse than no linter.
- **Three lint rules could not read a name with an arrow.** `C→PX(0,0)` was
  read as an index 0 into a variable `PX`, and the harness refused to send
  the batch that would have answered the unit question. One shared pattern
  fixed all three, with a control in the table for code that must not be
  flagged.
- **A fact claimed more than its own body.** `ppl.one-based` was titled
  "Everything is indexed from 1" while four drawing commands take a 0
  coordinate. Its body always said lists, strings and matrices; the title now
  agrees with it, and the screen exception is measured.
- **`TYPE` 8 stopped being hearsay.** It was one of the codes taken from HP's
  help and never measured. `CAS` answers with it -- and HP's help calls 8 a
  function while keeping 14.x for a CAS object, so the two namings do not
  agree and `ppl.type-codes` now says so instead of repeating the help.
- **The format gained a third kind of Result.** `*no value*` exists because
  15 commands have nothing an answer could hold, and inventing one, or
  writing `*error*`, would both have been false.

## What is measured as open, and stays that way

The phase did not close these, and the documentation says so rather than
guessing. Each names the probe that would settle it:

- `GETPIX`, `PIXON` and `PIXOFF` without `_P` answer `#FF000000h` whatever the
  picture holds, including a grob filled red. Paint with `PIXON` and read back
  with `GETPIX_P`, which does not share the mistake
- `SUBGROB` without `_P` is refused where `SUBGROB_P` cuts and allocates
- `ADDCOL` and `ADDROW` refuse nine forms, and the explanation both entries
  named as likeliest -- that they change a variable rather than answering a
  copy -- was tested and refuted
- `HMS→` answers its argument unchanged while `→HMS` converts. The round trip
  `HMS→(→HMS(1.5))` is the probe
- `TEXTOUT` answers 182 where `TEXTOUT_P` answers 19, and the factor of ten
  does not explain it: 182/19 is about 9.6
- whether the drawing unit follows a view the program sets itself; everything
  measured is the view before anything changes it
- `ppl.locals-initialised-one-line`, filed as a refuted hypothesis while still
  labelled `unverified`

## Human approval

- [x] Phase 5 approved to close — the user, 2026-09-12
