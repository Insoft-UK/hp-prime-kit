---
phase: 04-facts-carried-over
plan: 03
status: complete
completed: 2026-09-12
key_files:
  - docs/topics/deploy.md
  - docs/topics/libraries.md
  - docs/topics/ppl.md
  - hpkit/lint.py
  - tests/test_lint.py
  - docs/tools.md
  - docs/commands/strings/LEFT.md
commits: ["docs/reference/ is empty: deploy and libraries are topic pages", "Every lint rule says where it comes from"]
---

# Plan 03 summary: the last two pages, and the linter's sources

## What was built

- `docs/topics/deploy.md`, 13 facts, and `docs/topics/libraries.md`, 3 facts
  and the judgement kept as prose. `docs/reference/` is empty.
- Three facts that only existed as prose, because three rules had to cite
  them: `ppl.one-based`, `ppl.equality-operators`, `ppl.end-semicolon`.
- `hpkit/lint.py`: `FACTS` maps eleven rules to the fact each comes from,
  `NO_FACT` says what the other two come from, and every message carries the
  identifier in brackets: `file:line: level: rule: message [fact]`.
- `tests/test_lint.py` reads the rules out of the linter's own source and
  fails if one names a fact no topic page defines, names none and gives no
  reason, or is mapped and never emitted.
- `LEFT`'s entry has its first **Models get wrong** row, dated and sourced.

105 facts in the documentation.

## What this turned up

Writing the facts the rules cite showed that two rules were stricter than
their evidence:

| Rule | What it does | What is actually known |
|---|---|---|
| `equality` | **error** on a bare `=` in a condition | HP's help documents `==`, `:=` and `<>`, and every program here that compiles uses `==`. Nobody has watched the compiler refuse `IF a = 1 THEN` |
| `end-semicolon` | **error** on a line that is exactly `END` | every program here that compiles writes `END;`, and HP's examples do. Nobody has watched a bare `END` fail |

Both facts are labelled `unverified` and say what would settle them: two small
programs, one probe. The rules keep their level -- changing what the linter
calls an error is the user's decision, not a side effect of writing a page --
and `docs/tools.md` now names those two instead of claiming, as it did, that
twelve of the thirteen rules come from errors measured on a G2. `README.md`
repeated that claim and no longer does.

`unbalanced` and `unknown-name` name no fact on purpose: an unclosed block is
something the compiler reports itself, and `unknown-name` comes from the list
of names, which is an inventory rather than something measured.

## Deviations

- The plan said "thirteen rules, thirteen identifiers". It is eleven
  identifiers and two written reasons, which is what CHECK-04 allows and what
  the evidence supports.
- CHECK-04's other half -- every fact that can be caught from a PC has a rule
  or says why not -- is not done here: 105 facts against 13 rules, and no
  audit of which of the remaining ones a linter could catch. The verification
  says so rather than claiming it.

## Results

```
python tests/run_all.py     720 passed, 0 failed, across 13 suites
hpprime docs --check        5 entries, 105 facts, 25 examples run: 0 problems
docs/reference/             empty
```
