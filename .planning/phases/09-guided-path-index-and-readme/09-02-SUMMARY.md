---
phase: 09-guided-path-index-and-readme
plan: 02
status: complete
completed: 2026-09-16
key_files:
  - hpkit/docs.py
  - tests/test_reference.py
  - docs/format.md
  - docs/tools.md
---

# Plan 02 summary: the documentation no longer speaks of how it was built

## What was built

- **A check**, `PLANNING` in `hpkit/docs.py`: "phase" in any form, and
  "this kit" or "the kit" at any case of the first letter, are refused on
  every page of the documentation and in `docs/llms.txt`. Two new breaks in
  `test_reference.py`, which goes from 30 to 32.
- **132 scripted rewrites in 100 pages** -- 93 entries and all 7 topic
  pages -- in two passes, each
  replacement required to match exactly. The generated group pages and the
  index followed from them.
- **A glossary in `format.md`**, "How the examples were run": a batch, the
  harness, a probe, and keys pressed by hand where a batch cannot reach.
  `tools.md` says what the check refuses.

## What the rewrite turned into

- **A phase became what the sentence meant.** "Measured elsewhere in this
  phase" about infinity now links to [Dirac](../../../docs/commands/catalog/Dirac.md)
  in five entries; "the mode Phase 6 measured" links to `ACOT`, where the
  mode is recorded; "the second answer in this phase to overflow" became "in
  this group"; and where the phase added nothing, it went.
- **"This kit" became the thing meant**: the interpreter on the PC in
  most of the entries that named it, the decoder that reads the results, `hpprime build`,
  `hpprime write`, the list of names, or "here".
- **`Solve`'s promise of a clash "recorded in the phase context"** now says
  what the rule is: the app variable's entry will take `SOLVE-var.md`, the
  way `Root` does.
- **`valuation` lost a sentence** that sent the reader to "the project's own
  notes", which is the layer above the documentation.
- **What stayed**: "round trip" and "one round per bad line", keys a program
  waits for, the user of a program, and `Prime_1` in `deploy.md`, where the
  emulator naming its second calculator is itself a measured fact.

## Deviations

- **The first scan missed two shapes**: "This kit" at the start of a sentence,
  and "this" and "kit" on two lines. The check caught the first, and a scan
  over whole paragraphs the second; 18 more rewrites followed.
- **Some pages are stored with CRLF on this checkout**, which made the first
  run of the script fail on a replacement that spans two lines. It now reads
  and writes each file with its own line endings.
- **"the kit" is refused too**, which the context did not state in so many
  words: every use was the repository, so a pattern can hold it.

## Results

```
rewrites                   132, in 93 entries and 7 topic pages
planning words left        0, across line breaks included
checker                    0 problems
suite                      12,161 passed, 0 failed
```
