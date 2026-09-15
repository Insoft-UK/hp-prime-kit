---
phase: 04-facts-carried-over
plan: 01
status: complete
completed: 2026-09-12
key_files:
  - docs/topics/ppl.md
  - docs/topics/formats.md
  - .planning/phases/04-facts-carried-over/MIGRATION.md
commits: ["The language page becomes a topic page: 19 more facts, each with its label", "The formats page becomes a topic page"]
---

# Plan 01 summary: the language and the formats

The two pages the rest of the documentation leans on are topic pages now.
`docs/reference/` holds five, not seven.

| Page | Was | Is |
|---|---|---|
| `ppl` | 253 lines of prose, 6 sections | 22 facts, and an introduction |
| `formats` | 370 lines of prose, 7 sections | 19 facts, and an introduction |

41 facts in total, each with an identifier, one label, a statement and a
paragraph of evidence. `hpprime docs --check` holds every one of them to that.

## What the labels changed

Prose hid how sure each claim was; the format does not let it.

- Two items that read like rules are now `unverified`, and say what would
  settle them: locals initialised on one line, which rests on a published
  tutorial and not on a compile here, and whether `i` and `e` work as local
  names.
- `formats.header-words` is `unverified`: the words at offsets 20 and 44 were
  read from files, never measured on a calculator, and the same word at 44
  turns up again in the symbol table, so both records became one fact.
- Four more facts about the formats say plainly that they are not decoded:
  the value types other than a matrix, the flag before a matrix's type, where
  an entry would be spliced in, and how long a large block takes to compile.
- `ppl.type-codes` carries the emulator's label for the four numbers measured
  in Phase 3, and says the rest come from HP's help.
- The `G2` labels of `LEFT`, `RIGHT` and `MID` pointed at the old page's traps
  section. They are plain `G2` now, and each entry's evidence paragraph says
  what was run, which is what the format asks for when a label has no link.

## Deviations

- **A trap with no home yet.** `INSTRING` answers 0 when it finds nothing and
  1 when the second argument is empty. It belongs in `INSTRING`'s entry
  (FACT-04), and that entry is Phase 6. Rather than leave it in a page about
  to be deleted, the migration list carries the statement in full.
- **Links, not only pages.** Removing the two pages broke links in `AGENTS.md`,
  `README.md`, `SKILL.md`, `docs/tools.md`, `docs/ai/prompts.md`, two pages of
  the guided path, the keymap example, `deploy.md`, `interface.md`, `apps.md`,
  two suites and four docstrings in `hpkit/`. `tests/test_docs.py` found the
  ones a grep missed, including its own list of entry points.

## Results

```
python tests/run_all.py     705 passed, 0 failed, across 13 suites
hpprime docs --check        5 entries, 41 facts, 25 examples run: 0 problems
```

## Next

Plan 04-02: `interface` (12 sections, the largest page), `apps` and
`micropython`.
