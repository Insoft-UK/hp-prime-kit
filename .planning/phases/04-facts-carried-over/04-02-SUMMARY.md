---
phase: 04-facts-carried-over
plan: 02
status: complete
completed: 2026-09-12
key_files:
  - docs/topics/interface.md
  - docs/topics/apps.md
  - docs/topics/micropython.md
  - .planning/phases/04-facts-carried-over/MIGRATION.md
commits: ["Screen, apps and Python become topic pages: 45 more facts"]
---

# Plan 02 summary: the screen, the apps and Python

| Page | Was | Is |
|---|---|---|
| `interface` | 554 lines, 12 sections | 17 facts, and an introduction |
| `apps` | 309 lines, 9 sections | 14 facts, and an introduction |
| `micropython` | 269 lines, 7 sections | 14 facts, and an introduction |

86 facts in the documentation now. `docs/reference/` holds one page,
`libraries`, which plan 03 takes.

**A correction.** The commit message says "apps is 16". It is 14; the subject
line's 45 and the total of 86 are right.

## What moved, and what stayed prose

- A paragraph changed pages: the view keys that still arrive as keys in a
  blank app were in `interface`, and the evidence for them is an app built by
  this kit, so they are `apps.blank-app-keys` now, with `interface`'s key
  codes linked from it.
- `interface` keeps its judgement as prose, because it is judgement: the
  windowed list, the table against the form, units stated rather than asked
  for, and what can be tested on a PC. The facts are what carries a label.
- Half of `micropython`'s facts are `unverified` on purpose -- the modules the
  community documents and nobody here has run, whether the parentheses matter
  across the bridge, the number notation the community reports, PPL calling
  Python, and the speed and memory nobody has measured. Prose let those sit
  beside measurements; the format does not.

## Deviation

Four links in the new pages pointed outside `docs/`, at `templates/` and
`examples/`. They resolve in the repository, so `hpprime docs --check` passed,
and they do not resolve in the copy of `docs/` the tests check, so
`test_reference` and `test_examples_run` failed. The old reference pages were
never link-checked; a topic page is. They are paths in code style now, which
is the honest form for something outside the checked tree.

## Results

```
python tests/run_all.py     710 passed, 0 failed, across 13 suites
hpprime docs --check        5 entries, 86 facts, 25 examples run: 0 problems
```

## Next

Plan 04-03: `deploy` and `libraries`, then every lint rule naming the fact it
comes from, and the mistakes models make in the entries they concern.
