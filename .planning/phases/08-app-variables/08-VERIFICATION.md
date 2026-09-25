---
phase: 08-app-variables
status: approved
verified: 2026-09-25
requirements: [CMD-11]
---

# Phase 8 verification: App variables

Counted on 2026-09-25 after plan 08-05, from `docs.load()`, the list of
names and `results.tsv`.

## Criterion 1: every app variable on the list has an entry

| | |
|---|---|
| names of kind `app variable` | 172 |
| with an entry | **172** |
| groups | finance 68, inference 50, statistics-1var 16, statistics-2var 12, triangle-solver 7, advanced-graphing 6, function 5, spreadsheet 4, linear-solver 2, sequence 1, solve 1 |
| problems `hpprime docs --check` reports | **0** |

Each names its app in its group, says what it holds -- labelled
`unverified` where HP's list gives only the name and no row pins it down --
and whether a program can set it, from a row that tried.

## Criterion 2: every example has a result on file, or says why not

| | |
|---|---|
| examples in the app-variable entries | 355 |
| with the Virtual Calculator's answer | **355** |
| measured by hand on a G2 | 0 |
| *no value* | 0 |
| run nowhere | **0** |

## Requirements

| | |
|---|---|
| CMD-11 | complete |

## Suite

`python tests/run_all.py`: **14,713 passed, 0 failed**, across 13 suites.
