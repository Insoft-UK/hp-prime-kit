---
phase: 09-guided-path-index-and-readme
plan: 04
status: complete
completed: 2026-09-24
key_files:
  - README.md
  - AGENTS.md
  - SKILL.md
  - docs/ai/prompts.md
  - examples/apptest/README.md
  - tests/test_reference.py
---

# Plan 04 summary: the pages above the documentation lead to it

## What was built

- **The README leads with the documentation**, in the order of decision 7:
  what it is and the four labels; where it stands; where a person starts, the
  guided path; where a model starts, `docs/llms.txt`; the reference; then the
  tools; then working with an AI; then what it does not do, and the status.
  The user read the draft and approved it on 2026-09-24.
- **A test holds the README's numbers to the documentation.**
  `readme_numbers()` in `test_reference.py` computes ten of them from the
  entries, the facts, the list of names and `results.tsv` -- entries of names
  that get one, app functions, app variables, the variables of Home and the
  system, examples stored, measured by hand and *no value*, and facts by
  label -- and fails on any the README states otherwise. A stale copy, 129
  app variables and 741 stored examples, failed with both named.
- **`AGENTS.md` and `SKILL.md` send a model to `docs/llms.txt` first**, and
  to `names.tsv` for whether a name exists. The checklist of non-negotiables
  names a fact per line. `AGENTS.md` §3 asks for a command to be cited by its
  entry, and for a fact's label with its identifier.
- **Every rule of the paste block cites its source**, `[identifier, label]`,
  the shape `hpprime lint` uses: 21 rules, 17 in the PPL block and 4 in the
  MicroPython one. It still restates on purpose, and now says the
  documentation wins where they differ. `paste_block()` in
  `test_reference.py` fails on a rule with no citation, an identifier that is
  neither a fact nor an entry, and a label the fact does not carry; a broken
  copy with one of each failed with all three named.
- **The apptest README's open question is closed**: what published apps call
  soft key 6 is the physical `[Num]`, which is why both are 11, and the labels
  along the bottom report nothing.

## What the pages said that the reference contradicts, corrected

- `README.md`: 741 of 800 examples run on the emulator; it is 779.
- `AGENTS.md`, and the paste block: `L(0)` is a run-time error. Measured is
  `MID` with a 0; a list with a 0 is not.
- `AGENTS.md` and `SKILL.md`: four refuted hypotheses; there are five.
  `SKILL.md` also sent the reader to a "§2" of `ppl.md`, which has no
  numbered sections.
- The paste block: lists passed by value, where the fact is about matrices;
  `TEXTOUT_P`'s width as a seventh argument, true only with a grob; "there is
  no debugger", where `DEBUG` has an entry; `main.py` as required, where
  `apps.main-py` is `unverified`.
- The task prompts: the seventh argument again, and advice not to rely on
  `[Num]` and `[View]`, which arrive through `GETKEY` as 11 and 9.

## Deviations

- **The apptest README was not in decision 8.** 09-03 found it repeating the
  error the guided path had about the labels along the bottom, so it went
  here with the other pages above the documentation.
- **The README's claim about the facts went from "measured on a calculator"
  to the three counts.** A test can hold a count; it cannot hold an
  adjective.

## Results

```
README numbers held by a test         10
paste block rules, each citing        21: 17 PPL, 4 MicroPython
contradictions corrected              13, in 5 pages
test_reference.py                     35 -> 37
suite                                 12,308 passed, 0 failed
```
