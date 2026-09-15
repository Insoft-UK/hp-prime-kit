---
phase: 05-statements-and-program-commands
plan: 02
status: complete
completed: 2026-09-12
key_files:
  - docs/commands/strings/*.md
  - docs/commands/integer/*.md
  - docs/commands/results.tsv
  - hpkit/lint.py
  - docs/tools.md
  - README.md
commits: ["Four string entries, and the divergence the documentation caught", "Seventeen entries from the batch, and one claim withdrawn", "Phase 5's remaining entries are blocked on the emulator, written down", "Twenty-one entries from the second batch, and a withdrawal reversed", "Three compile questions, asked by hand because the kit refused to ask them", "The equality rule is gone: it flagged legal, correct code"]
---

# Plan 02 summary: the commands that take a value and give one back

## What was built

- 13 string entries and 11 integer entries. `LEFT`, `MID` and `RIGHT` already
  existed and gained links.
- The two integer names that carry an arrow, `B→R` and `R→B`, which needed
  their probes sent through a file: the Windows console mangles the arrow,
  though the bytes were correct UTF-8 all along.

## What this turned up

**A lint rule was wrong, and measuring it is what showed.** `equality`
called a bare `=` in a condition an error. A hand-written program settled it:
`IF a = 2 THEN` compiles and compares, `ZQ4` answering 6 and `ZQ5` answering
1. The rule flagged legal, correct code, so the user chose to remove it
rather than soften it. `docs/tools.md` and `README.md` claimed thirteen rules
and now say twelve.

**The harness refused to ask its own questions.** It lints what it sends, and
the two probes for `ppl.equality-operators` and `ppl.end-semicolon` were
exactly what the linter called errors. The guard was kept -- it is the right
behaviour -- and the user chose hand-written programs as the way round it.

**A claim was written, withdrawn, and then restored.** `STRING("abc")` was
first read as adding quotes, then withdrawn when it became clear the harness
brings every answer back through `STRING`, so the first reading had measured
two of them. `DIM(STRING("abc"))` answering 5 settled it cleanly, and the
claim went back in with the evidence that belongs to it.

## Deviations

- The plan assumed most of these entries could be drafted from HP's help and
  confirmed later. Six string commands and all eleven integer ones could not:
  the interpreter implements none of them and HP's help dump holds no example
  with a result. They were written after the batch answered, which is the
  order every later plan starts in. It is written down in
  `1d320e3`.

## Results

```
hpprime docs --check      43 entries: 0 problems
python tests/run_all.py    passed, 0 failed, across 13 suites
twelve lint rules, each citing its fact
```
