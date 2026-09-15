---
phase: 01-entry-format-and-checks
plan: 01
status: complete
completed: 2026-09-11
key_files:
  - docs/format.md
  - docs/commands/strings/LEFT.md
  - docs/commands/strings/RIGHT.md
  - docs/commands/strings/MID.md
  - docs/commands/lists/SIZE.md
  - docs/commands/loops/FOR.md
  - docs/topics/ppl.md
commits: [4846a1f, 87d8d82, 0c07996]
---

# Plan 01 summary: the format, and real content in it

## What was built

- `docs/format.md` states the format once: the four labels and what each
  needs as evidence, the seven parts of a command entry in order, what an
  example is (an expression, or a function body when it has a `;`; a result
  as the calculator displays it, or *error*), what a fact holds, how
  identifiers are formed, and which pages are generated.
- Five command entries: `LEFT`, `RIGHT` and `MID` (strings), `SIZE` (lists)
  and `FOR` (loops). 23 examples in all, every one labelled.
- `docs/topics/ppl.md` with three facts: `ppl.local-limit`,
  `ppl.index-call` and `ppl.return-in-loop` (a refuted hypothesis).

## How the labels were decided

- `G2` only for what the two probes on a G2 with 2.4.15515 recorded
  (commits bbdbce8 and 633aff9) and for what `docs/reference/ppl.md` states
  as measured.
- `HP help` only for what the Command Tree 13217 dump prints. The two `FOR`
  examples are HP's own loops, collecting the values in a list instead of
  printing them; the entry says so.
- What nobody has measured says so, labelled `unverified`: `RIGHT` with a
  negative count, and whether `SIZE` of a matrix gives back a list or a
  vector (HP's help says a list and prints a vector).
- "Models get wrong" appears only in `SIZE`, the one case with a record.

## Deviations

- The check written in plan 02 made one rule explicit that plan 01 had left
  implicit: a Behaviour paragraph that says where the measurements come from
  begins **Evidence.** and needs no label of its own, as in a fact. The three
  string entries and `docs/format.md` were changed to match before their
  commits.

## For later phases

- The `G2` labels link to `docs/reference/ppl.md`, where the measurements
  are recorded today. Phase 4 moves that page and must re-point them to the
  new evidence records.
- `SIZE` of a matrix, list or vector, is a first candidate for a run on the
  Virtual Calculator in Phase 3.
