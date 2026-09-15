---
phase: 02-command-inventory
status: passed
verified: 2026-09-11
human_verification: approved by the user on 2026-09-11
---

# Phase 2 verification: Command inventory

**Goal:** the complete list of PPL names lives in the repository as data, and
the linter uses it.

## Success criteria

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | The list holds every statement, command, Home function, app function and app variable in HP's help, with its category and syntax | VERIFIED | `docs/commands/names.tsv`: 1,173 names with kind and group; 831 with a syntax line. The names without one are mostly variables, for which HP's help gives none |
| 2 | Names added or removed after 13217 are identified from a second source, and every name says where it came from | VERIFIED | 50 names only in the 2.1.14181 export and 7 only in the release notes, each with its source. The notes from 13333 to 2.4 name one removal, `DoFinance`, which the 13217 help does not have either, so nothing on the list is gone |
| 3 | An index by name and one by HP's grouping are generated from the list | VERIFIED | `docs/commands/index.md` and `docs/commands/groups.md`, both checked for staleness by the tests. The second was added at close |
| 4 | `hpprime lint` flags `STRLEN(s)` as a name that does not exist, and stays quiet on the program's own functions, locals and globals | VERIFIED | `tests/test_lint.py`: "catches unknown-name", eleven "no unknown-name on ..." cases, four `--set` cases; the command run by hand on a file calling `STRLEN` |

## Requirements

| Requirement | Status | How it is checked |
|---|---|---|
| CMD-01 | VERIFIED | the list, rebuilt by `tests/names_extract.py`; `tests/test_reference.py` breaks a row of it |
| CMD-02 | VERIFIED | the source column; the removals checked against the notes |
| CMD-05 | VERIFIED | entries in the folder of their group, enforced; the index by name and the page by group, generated |
| TOOL-01 | VERIFIED | the rule, reading `docs/commands/names.tsv`; its cases in both directions |

## Commands run

```
python tests/run_all.py          612 passed, 0 failed, across 12 suites
python hpprime.py docs --check   0 problem(s); 5 of the 706 names have an entry
hpprime lint LEN.txt [--set]     a warning alone, an error with --set
```

## Human verification

The user reviewed the generated index and approved the phase.

## What this does not verify

- That every name on the list exists on 2.4.15515. The list says where each
  one came from; running the examples on the Virtual Calculator, from Phase 3
  on, is what confirms them one by one.
- What `GET` is.
