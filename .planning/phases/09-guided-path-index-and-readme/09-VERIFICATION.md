---
phase: 09-guided-path-index-and-readme
status: approved
verified: 2026-09-24
requirements: [READ-01, READ-03, READ-04, READ-05, READ-06, CHECK-02]
recount: in Phase 10, on the finished reference
---

# Phase 9 verification: Guided path, index and README

The criteria are counted here, not asserted, on 2026-09-24 after plan 09-04.
The phase ran ahead of Phases 8 and 8.1, so the counts are of a reference
that still lacks 42 app variables, 65 variables and `GET`. Phase 10 takes
them again on the finished one.

## Criterion 1: the guided path, from an empty folder to a program on the calculator, linking rather than restating

| | |
|---|---|
| steps, in their original order | 6 |
| links to facts across them | **73**, to 51 facts |
| problems `hpprime docs --check` reports in `docs/start/` | **0**, of 13 before 09-03 |
| programs on the path that lint with an error or a warning | **0**, held by `test_examples.py` |
| commands the path gives, run in a clean folder | all, each doing what its page says |

What only a person can confirm: that somebody following the path gets the
program onto a calculator. The commands were run on the PC; the drag in the
Connectivity Kit and the keys on Home were not, in this phase.

## Criterion 2: one index, within its budget, with every entry and fact

| | |
|---|---|
| `docs/llms.txt` | **74,929 bytes** of a 100,000 budget |
| entries with their line | 598 of 598 |
| facts with their line | 117 of 117 |
| stale, or over budget | fails the check, held by three breaks in `test_reference.py` |

## Criterion 3: the README leads with the documentation, and the pages above it point at it

| | |
|---|---|
| README order | the documentation, where a person and a model start, the reference, then the tools, then AI |
| README numbers held to the documentation by a test | 10 |
| README approved by the user | 2026-09-24 |
| `AGENTS.md`, `SKILL.md`, the paste block sending a model to `docs/llms.txt` first | 3 of 3 |
| rules in the paste block citing a fact or entry with its label | 21 of 21, held by a test |

## Criterion 4: every example has been run, or says why not

| | |
|---|---|
| examples | 800 |
| with the Virtual Calculator's answer in `results.tsv` | **779** |
| measured by hand on a G2, with the evidence in the entry | **4** |
| *no value*, with the reason | **17** |
| run nowhere | **0**, and the check fails on one |

## Requirements

| | |
|---|---|
| READ-01 | complete: criterion 1 |
| READ-03 | complete: criterion 2 |
| READ-04 | complete as far as a check can hold it: one format, no planning words, the glossary in `format.md` (09-02). Whether the whole reads well is a reader's judgement, not measured here |
| READ-05 | complete: criterion 3 |
| READ-06 | complete: criterion 3 |
| CHECK-02 | complete: criterion 4 |

## Suite

`python tests/run_all.py`: **12,308 passed, 0 failed**, across 13 suites.
`hpprime docs --check`: 0 problems.
