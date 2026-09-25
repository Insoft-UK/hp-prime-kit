---
phase: 10-what-a-pc-can-catch
status: approved
verified: 2026-09-25
requirements: [CHECK-04]
---

# Phase 10 verification: What a PC can catch

Counted on 2026-09-25 after plan 10-03, from `docs.load()`, `CAUGHT` in
`hpkit/lint.py`, `results.tsv` and the tests, not asserted.

## Criterion 1: a list covers every fact

| | |
|---|---|
| facts in `docs/topics/` | 122: 76 G2, 26 emulator, 20 unverified |
| with a line in `CAUGHT` | **122** |
| caught by a lint rule or another command, with its test | 59 |
| nothing to catch, `lint` held quiet on it | 9, two of them also held by `run` |
| only "not from a PC", each with its reason | 56 |
| the table in `docs/tools.md` | written by `hpprime docs`, and `--check` fails when it is stale |

## Criterion 2: every fact a PC can catch has a rule, with a case it catches and one it stays quiet on

| | |
|---|---|
| lint rules | 20: 18 tied to a fact, 2 saying what they come from |
| rules tied to a fact with a case each way | **18 of 18**, held by `rules_have_both_cases` |
| checks decided on and not written | **0**, and `caught_list` fails on one |
| quiet facts on which no rule says anything | 9 of 9, held by `QUIET` |
| the kit's own PPL -- `examples/`, `templates/`, the guided path -- with a finding | **0** |
| the user's 29 installed programs, with a finding from the new rules | 1, the probe written to be caught |

## Criterion 3: Phase 9's counts, taken again on the finished reference

| | Phase 9, 2026-09-24 | Now |
|---|---|---|
| guided path: steps | 6 | 6 |
| links to facts | 73, to 51 facts | **79, to 54 facts** |
| problems `hpprime docs --check` finds in `docs/start/` | 0 | **0** |
| the path's programs linting with an error or a warning | 0 | **0**, after 10-02 fixed `TDRAW` |
| the path's commands, run in a clean folder | all | `doctor`, `new`, `lint`, `run` twice, `write`, `verify`, `read`, `build --ppl`, `verify` of the app, `new --python`, `build` twice: all as the pages say. `install` and `pull` were not run, since they open the user's emulator |
| `docs/llms.txt` | 74,929 bytes | **91,335 bytes** of 100,000 |
| entries with their line in the index | 598 of 598 | **706 of 706** |
| facts with their line | 117 of 117 | **122 of 122** |
| README numbers held by their test | 10 | **9**, all current: "the other 42 app variables" went when there were none |
| `AGENTS.md`, `SKILL.md`, the paste block sending a model to `docs/llms.txt` first | 3 of 3 | **3 of 3** |
| rules in the paste block citing a fact or entry | 21 of 21 | **23 of 23** |
| examples | 800 | **1,149** |
| with the Virtual Calculator's answer | 779 | **1,128** |
| measured by hand on a G2 | 4 | **4** |
| *no value*, with the reason | 17 | **17** |
| run nowhere | 0 | **0** |

## Requirements

| | |
|---|---|
| CHECK-04 | complete: criteria 1 and 2 |
| Milestone 1 | **38 of 38 requirements complete** |

## What only a person can confirm

The 20 facts labelled `unverified` are waiting for a calculator, each saying
what would settle it. That the guided path gets somebody's program onto a
calculator, the drag in the Connectivity Kit and the keys on Home, was not
run here.

## Suite

`python tests/run_all.py`: **14,879 passed, 0 failed**, across 13 suites.
`hpprime docs --check`: 0 problems.
