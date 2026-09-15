---
phase: 01-entry-format-and-checks
plan: 02
status: complete
completed: 2026-09-11
key_files:
  - hpkit/docs.py
  - hpkit/cli.py
  - hpkit/interp.py
  - tests/test_reference.py
  - tests/test_hpdocs.py
  - tests/run_all.py
  - tests/test_docs.py
  - docs/commands/index.md
  - docs/commands/strings.md
  - docs/commands/lists.md
  - docs/commands/loops.md
  - docs/tools.md
  - README.md
commits: [6148c50, 0a121d9, 28b2f44, d022ace]
---

# Plan 02 summary: the checks and the generator

## What was built

- `hpkit/docs.py` reads the command entries and the facts, and reports what
  breaks `docs/format.md` as `file:line: message`. It checks the fields and
  their order, the sections, one label per example, a label in every
  Behaviour paragraph, unique names and fact identifiers, links that resolve
  (including links to a fact), and that nothing points at the layer built on
  the documentation.
- It runs the examples of every entry that says `Runs on the PC: yes` through
  the interpreter. A different answer, or an error where the entry gives a
  value, is a problem; an example the interpreter does not cover is a note.
- It generates the group pages (entries in full, headings shifted one level,
  links rebased, an explicit anchor per entry) and the index (name, group,
  summary, weakest label). A page that is missing, out of date, or no longer
  produced by any folder is a problem.
- `hpprime docs` checks, then regenerates; `hpprime docs --check` changes
  nothing and exits 1 on any problem. Documented in `docs/tools.md` and in
  `hpprime --help`.
- `tests/test_reference.py`: the real documentation passes; 23 examples run
  through the interpreter and agree; an uncovered example stays a note; and
  17 deliberate breaks of a copy are each caught. Registered in
  `tests/run_all.py`. `tests/test_docs.py` now requires `docs/format.md` and
  `docs/commands/index.md`.
- `tests/test_hpdocs.py` imports the reading of a printed result from
  `hpkit.docs` instead of keeping its own copy.

## Results

```
python tests/run_all.py        584 passed, 0 failed, across 12 suites
python hpprime.py docs --check 5 entries, 3 facts, 23 example(s) run
                               through the interpreter: 0 problem(s)
```

## Deviations

- The check found a fault in the interpreter. It raised `PPLError`, which
  means an error of the kind the calculator gives, for `RIGHT` with a negative
  count, an edge nobody has measured. It raises `Unsupported` now (6148c50).
  The other `PPLError` raises in the string functions and `SORT` are errors
  measured on a G2.

## For later phases

- Telling an error from an uncovered example relies on the interpreter
  raising `PPLError` only for refusals seen on a calculator. `_as_string`
  (for example `LEFT(42, 2)`) raises `PPLError` with no recorded measurement;
  check it before an entry relies on that case.
