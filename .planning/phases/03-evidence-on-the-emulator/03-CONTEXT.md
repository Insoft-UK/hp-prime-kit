# Phase 3: Evidence on the Virtual Calculator — Context

**Gathered:** 2026-09-11
**Status:** Ready for planning

## Phase Boundary

This phase delivers:

- the kit finding a localised Connectivity Kit, and saying which folders it
  used;
- the documentation's examples run in batches on the Virtual Calculator, every
  kind of answer brought back and stored with the firmware that gave it;
- an answer that differs from what an entry states, flagged;
- the container reader's wrong pick, reproduced and fixed.

It writes no new entries; those are Phases 5 to 8. It does run the examples of
the five sample entries, as the first real batch.

Requirements: EVID-01, EVID-02, EVID-03, EVID-04, TOOL-03.

The roadmap's second criterion says "one keypress". A program copied into the
emulator's folder has to be compiled once before its name works on Home
(measured on 2026-09-06), so a batch is one short manual pass: compile, run,
close. The criterion is read that way.

## Decisions

Locked by the user on 2026-09-11.

- **The user presses the keys.** The kit installs the batch, prints the exact
  keys, waits for the emulator to close, and collects the results. Few
  batches: one per group or per phase, each with as many examples as it needs.
- **A throwaway calculator.** The examples run on a calculator called `DOCS`,
  cloned from `Prime` and reset before each batch. `Prime` is not touched.
- **Labels follow the evidence.** When the emulator confirms an example
  labelled `HP help`, its label becomes `emulator`, and the stored result
  keeps that HP's help said the same. When the two differ, nothing is
  replaced: the difference is flagged for a person to decide.

## Claude's Discretion

Decided here, open to the user's review.

- **How an answer comes back.** One generated program per batch. Each example
  is either an expression or a function body of its own, and the harness calls
  it inside `IFERR`. Its answer becomes one row of a real matrix: whether it
  answered or raised, `TYPE` of the answer, the number itself when it is one,
  and otherwise `STRING` of the answer written out as character codes. A
  matrix of reals is what the emulator already brings back as a file.
- **Which firmware answered.** The first row holds what `VERSION` answers on
  that calculator, so every result carries the firmware it came from, stated
  by the calculator itself rather than by the installer.
- **Where results live.** In the repository, beside the list of names:
  `docs/commands/results.tsv`, one row per example run, with the entry, the
  call, the answer as the calculator displays it, its type, the firmware and
  the date. An example labelled `emulator` must have a matching row, and
  `hpprime docs` checks it.
- **The command.** `hpprime examples`, to build a batch from the entries,
  install it on `DOCS`, print the keys and wait; and `--collect` for a run that
  was not waited for.
- **The Connectivity Kit's folder** is found by what it holds rather than by
  its name: the folder inside `HP Connectivity Kit` whose own folders are
  calculators.
- **The reader's wrong pick** is reproduced first with a container built for
  it, then fixed, then kept as a test.

## Specific Ideas

- The first batch: the 23 examples of `LEFT`, `RIGHT`, `MID`, `SIZE` and
  `FOR`, plus two questions the entries leave open: what `RIGHT` answers with
  a negative count, and whether `SIZE` of a matrix gives a list or a vector,
  which `TYPE` settles.
- The same pass can record what `IFERR` leaves in `Ans` when a call raises,
  and what `TYPE` answers for each kind of value, both of which the current
  reference marks as coming from HP's help only.

## Existing Code Insights

- `hpkit/compare.py` already has the pattern: one wrapper, `IFERR` per call,
  `MAKEMAT` into `M9`, install with `--restart`, wait for the emulator to
  close, `--collect`, and the wrapper taken off afterwards.
- `hpkit/emulator.py`: `install` refuses a running emulator; `close` asks the
  window to close, so the calculator saves; `launch`; `create` and `reset` for
  throwaway calculators; `which_opens` for the calculator an emulator comes up
  on.
- `hpkit/numbers.py` reads and writes real `.hpmat` files; complex ones raise.
- `docs/reference/deploy.md` §1: the folder is read at start, a copied program
  needs the editor's Check once, and `M9.hpmat` is written when the emulator
  exits.

## Deferred Ideas

- Automating the keypresses on the emulator.
- Running the examples on the physical G2.

---
*Phase: 03-evidence-on-the-emulator*
*Context gathered: 2026-09-11*
