---
phase: 01-entry-format-and-checks
status: passed
verified: 2026-09-11
human_verification: approved by the user on 2026-09-11
---

# Phase 1 verification: Entry format and checks

**Goal:** a fixed, documented format for a command entry, a fact and an
example, and tests that reject anything that does not follow it.

## Success criteria

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | One page explains the format of an entry, a fact and an example, and the four ways each can state how it is known | VERIFIED | `docs/format.md` |
| 2 | A handful of real entries and facts exist in the final format and pass the tests | VERIFIED | `LEFT`, `RIGHT`, `MID`, `SIZE`, `FOR`; `ppl.local-limit`, `ppl.index-call`, `ppl.return-in-loop`. `hpprime docs --check`: 0 problems |
| 3 | The tests fail on a duplicate identifier, a reference that does not resolve, a documentation page that mentions the kit, and a broken link | VERIFIED | `tests/test_reference.py`: "catches a fact identifier used twice", "catches a link to a fact that does not exist", "catches a page that points at the layer built on it", "catches a link to a file that does not exist" |
| 4 | For a command the interpreter implements, its entry's examples also run through `hpprime run` in the tests | VERIFIED | `tests/test_reference.py`: "23 example(s) ran through the interpreter and agree" |

## Requirements

| Requirement | Status | How it is checked |
|---|---|---|
| CMD-03 | VERIFIED | the entry format in `docs/format.md`, enforced by `hpkit.docs.read_entry` |
| CMD-04 | VERIFIED | one label per example and a label in every Behaviour paragraph, enforced; two break cases |
| CMD-07 | VERIFIED | the `Runs on the PC` field; examples run through the interpreter; two break cases |
| READ-02 | VERIFIED by reading | no entry refers to text outside itself except through links. There is no automated check for this |
| CHECK-01 | VERIFIED | unique names and fact identifiers; links to facts must name one; break cases |
| CHECK-03 | VERIFIED | the pattern for the layer above in `hpkit.docs`; break case |
| CHECK-05 | VERIFIED | `tests/test_docs.py`, 188 links, none broken |

## Commands run

```
python tests/run_all.py          584 passed, 0 failed, across 12 suites
python hpprime.py docs --check   0 problem(s)
```

## Human verification

The user reviewed `docs/commands/strings.md`, `docs/commands/lists/SIZE.md`,
`docs/commands/index.md` and `docs/format.md`, and approved the phase.

## What this does not verify

- That each label is true. The check enforces that every claim carries one;
  its truth is the evidence behind it. The labels of the samples were checked
  by reading the probe commits (bbdbce8, 633aff9) and `tests/hp_examples.txt`.
