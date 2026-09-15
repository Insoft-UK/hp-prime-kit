---
phase: 02-command-inventory
plan: 01
status: complete
completed: 2026-09-11
key_files:
  - tests/names_extract.py
  - docs/commands/names.tsv
  - hpkit/names.py
  - hpkit/docs.py
  - docs/format.md
  - tests/test_reference.py
  - docs/commands/index.md
  - docs/commands/groups.md
commits: [17bf061, f5f9435, "the by-group index, after 26d1ec0"]
---

# Plan 01 summary: the list of names

## What was built

- `docs/commands/names.tsv`: 1,173 names, one per line, with kind, HP's
  group, menu, the first syntax line HP gives, and source.
  - By kind: 14 statements, 7 keywords, 24 operators, 98 commands, 177
    functions, 179 app functions, 172 app variables, 65 variables, 436 CAS
    names, and 1 of unknown kind (`GET`).
  - By source: 1,116 in the help of firmware 13217, 50 only in the 2.1.14181
    export, 7 only in the release notes up to 2.4.15515 (`UVAL`, `UPART`,
    `SeqPlot`, `ListToMat`, `GET`, `normald_cdf`, `normald_icdf`).
  - 831 names carry a syntax line.
- `tests/names_extract.py` rebuilds the list from the three sources, kept
  outside the repository, and says how to get them.
- `hpkit/names.py` reads it. `hpkit/docs.py` builds the index over the 706
  names that get an entry, and the page by group; an entry whose name is not
  on the list, or whose folder is not its group, is a problem.
- The sample entries moved to HP's group names, `list/` and `loop/`.

## Deviations

- The extraction needed four fixes after its first run: one-word menu titles
  taken for names, a topic taken for an app, camel-case CAS names taken for
  functions, and a typo inherited from the 2.1 export (`probabiity`).
- The folder renames were staged before the list's commit and went into it
  (17bf061) without their Group fields and links; f5f9435 completes them. One
  commit in the history is inconsistent on its own.
- At the phase's close, the index by HP's grouping (the third success
  criterion) had not been generated. `docs/commands/groups.md` was added.

## For later phases

- What `GET` is, is not known; the notes of 2.2 name it once.
- The keyboard's functions (`SIN`, `LN` and the like) sit in the group
  "catalog" until their entries are written.
- 84 Geometry app functions are lower-case; whether a program calls them as
  app functions is for Phase 7.
- The calculator's variables (`A` to `Z`, `L0` to `L9`...) are not names on
  the list; the linter knows them by pattern. Phase 8 decides whether they
  get entries.
- The syntax lines use HP's argument names; the entries write their own.
