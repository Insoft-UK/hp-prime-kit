---
phase: 06-home-functions
verified: 2026-09-13
status: approved
---

# Phase 6 verification: Home functions

## Success criteria

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| 1 | Every name the inventory files under the Home functions has an entry in the fixed format | VERIFIED | 177 names of kind `function` on `names.tsv`, and 177 have an entry, none missing. `catalog` was the last group and is 48 of 48. `docs.check` holds all 289 entries in the documentation to the format and reports 0 problems |
| 2 | Every example in those entries has a Virtual Calculator result on file, or says why it cannot have one | VERIFIED | 212 example rows across the 177 entries: 211 have a stored answer in `results.tsv` and 1 is `*no value*`, which is `DEBUG` and says in words why it was never run. **0 are neither.** The checker refuses an example labelled `emulator` with no stored answer, so the 211 are enforced rather than claimed |
| 3 | Where HP's stated result and the emulator's answer differ, the entry says so | VERIFIED, with a stated limit | 27 of the 177 entries discuss what HP states; 10 word an actual disagreement -- `CEILING`, `EQ`, `FISHER`, `Heaviside`, `INVERSE`, `MIN`, `MOD`, `RANDMAT`, `RANDOM`, `SIZE`. A further 5 record the *interpreter* answering differently from the calculator: `DET`, `EXP`, `INVERSE`, `NTHROOT`, `RREF`. **The limit:** that count is of wording, found by pattern. It shows the entries say so where they say so; it is not proof that every difference HP's help contains was noticed |

## Requirements

| ID | Status | Evidence |
|---|---|---|
| CMD-09 | VERIFIED | criterion 1: every Home function has an entry -- mathematics, lists, matrices, probability, statistics, integers and bits, and the machine names HP files with them |

CHECK-04 stays open, as it has since Phase 4: every lint rule is tied to a
fact, and the audit of which facts a PC could catch and no rule does is not
done. This phase made that audit larger again -- 112 facts now, and 289
entries to read them against.

## Tests

```
python tests/run_all.py     5657 passed, 0 failed, across 13 suites
docs.check                  289 entries, 112 facts: 0 problems, 15 notes
docs/commands/results.tsv   390 rows, all from Virtual Calculator 2.4, build 2025-09-15
```

The 15 notes are examples the interpreter cannot run. They are notes and not
problems by design: the documentation does not require the PC to be able to
check what only the calculator can answer.

## The serial number

The phase's own must-have was that `SERIAL` gets an entry and no run of it
puts the calculator's serial number anywhere. Checked rather than assumed:

- `results.tsv` holds two rows reading `(not stored)`, for `SERIAL` and for
  `VERSION`, and nothing in the file has the shape of a serial number.
- A search of every committed file for a serial-shaped run of characters
  returns one hit, `0x0FFF000000000000` in `tests/test_numbers.py`, which is
  a hexadecimal literal in a test that rejects a non-BCD mantissa.

`VERSION` was the near miss. It answers the serial number the same way
`SERIAL` does, and the guard built in plan 01 covered only `SERIAL`. It was
caught while designing the batch, not while reading the file afterwards, and
the name went onto the guard before anything ran -- so there was nothing to
scrub.

## What this phase changed about the documentation

- **The compiler names the last bad line, not the first.** Now the fact
  `ppl.check-last-error`. Three refused batches each accused a call that the
  round before had appeared to clear, and the reasoning here had it exactly
  backwards: everything *below* a named line is clean, everything above it is
  still unknown.
- **A doubtful call belongs inside `EXPR`.** A string compiles whatever it
  holds, so a bad call becomes one row's error instead of a refusal of the
  whole program. Three batches carrying calls directly returned nothing at
  all; the wrapped ones returned every answer including the refusals. It is
  what made `NTHROOT`, `NEG`, `INVERSE` and the four upper-tail commands
  measurable.
- **`NTHROOT` is an infix operator**, the second after `MOD`. `3 NTHROOT 8`
  answers 2. HP gives neither name a syntax string, and that silence is now
  something to read rather than a gap.
- **Infinity is an ordinary real.** `Dirac(0)` is `+Inf` and `TYPE` answers 0
  for it, so nothing in the type marks it.
- **The angle mode was read rather than inferred**, closing half a question
  `ARC` and `ARG` had both left open, and type 9 was measured five times over
  on unit-carrying answers.
- **A false claim reached the repository and was withdrawn.** `STATE.md` said
  `NTHROOT` was refused in both forms, on a line-map formula that had never
  been checked. The correction came from decoding the `.hpprgm` actually sent
  and diffing it against a rebuild. Reconstructing what was sent is not the
  same as reading it.

## What is measured as open, and stays that way

Each names the probe that would settle it:

- `NEG` refuses both `NEG(5)` and `NEG 5`; the working form is unknown, and
  the remaining candidate is a character entered from a menu rather than typed
- `INVERSE` refuses both a number and a matrix, which kills the interpreter's
  lead that the argument merely wanted to be a matrix
- `UTPC`, `UTPF`, `UTPN` and `UTPT` are all refused, each written with HP's
  own argument list. All four were reached through `EXPR` on Home; the probe
  is one direct call inside a program
- `LineTan` answers a collapsed expression rather than a tangent, because what
  it is handed is evaluated before it sees it. The probe is `QUOTE` around it
- `GETBASE` answers a code rather than a base; the probe is `#12b`, `#12o` and
  `#12d`
- `MEMORY` answers two figures and which is which is not established
- `GF` answers a string describing the field, where every other constructor
  here answers an object
- `COLOR` hands its own name back, which an unknown symbol and a constant both
  do
- `DEBUG` was deliberately never run: it waits for a person, so in a batch it
  would hold the window open and cost a round for nothing
- `ppl.check-last-error` has no direct confirmation. One program carrying two
  deliberate errors far apart would give it one, and costs a single round
- Phase 5's open questions are unchanged: `ADDCOL` and `ADDROW`, `TEXTOUT`
  against `TEXTOUT_P`, `GETPIX` and `PIXON` without `_P`, `SUBGROB`, `HMS→`,
  whether the drawing unit follows a changed view, and
  `ppl.locals-initialised-one-line`

## Human approval

- [x] Phase 6 approved to close — the user, 2026-09-13
