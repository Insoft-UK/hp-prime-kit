---
phase: 09-guided-path-index-and-readme
plan: 03
status: complete
completed: 2026-09-23
key_files:
  - docs/start/01-setup.md to 06-working-with-ai.md
  - hpkit/docs.py
  - templates/starters/program.txt
  - docs/topics/ppl.md
  - tests/test_examples.py
  - tests/test_reference.py
---

# Plan 03 summary: the guided path links, and is checked like the rest

## What was built

- **`docs/start/` is checked documentation.** `_layer_files()` walks it, so
  its links, the facts it names, the layer above and the planning words are
  held to the same rules as the entries. On the pages as they were, that
  found 13 problems: nine "this kit" or "the kit", and four pointers at
  `AGENTS.md`, `SKILL.md` and `docs/ai/`. Three new breaks in
  `test_reference.py`, which goes from 32 to 35.
- **The six steps rewritten, in their order.** Where a step uses a fact it
  says what to do and links the fact: 73 links to 51 different facts across
  the six pages.
  Step 2's table of first-day failures has a column for the fact and one for
  what `hpprime lint` does about each row. Step 6 sends a model to
  `docs/llms.txt`, and teaches citing a fact by its identifier and reading its
  label. The path no longer links outside `docs/`: `CONTRIBUTING.md` became
  `format.md`, and `examples/apptest/` is named rather than linked, so the
  documentation can still be split out.
- **The starter exports `CIRCAREA`**, not `AREA`. `AREA` is the Function
  app's, a reset calculator has that app active, and what Home answers when a
  program exports the same name is not measured
  ([ppl.global-namespace](../../../docs/topics/ppl.md#ppl.global-namespace)).
  The user chose the rename over a measurement on 2026-09-23. The template,
  the `Next:` that `hpprime new` prints, its tests, `tools.md`, `compare.py`,
  `ppl.home-no-parentheses` and one line of the README follow.
- **`ppl.one-based` says what was measured.** An index of 0 is an error for
  `MID`; what it does to a list or a matrix has not been measured, which is
  what the linter has said since 9704074.
- **The path's programs are held clean.** `test_examples.py`, from 17 to 24:
  step 2 shows the program `hpprime new` writes; each step's programs,
  together with the starter, lint with no error and no warning and load in the
  interpreter. Breaking step 3 by hand, an `ENDIF` and a `TEXTOUT_P` without
  its width, fails it with both named.

## What the reading turned up

The context found three errors. Reading every step against the facts it
relies on found sixteen more, all corrected:

- The six labels along the bottom were called soft keys that `GETKEY` reports
  as 0, 5, 10, 1, 6 and 11; touching them reports nothing, and those are
  physical keys other apps picked
  ([interface.soft-labels-not-keys](../../../docs/topics/interface.md#interface.soft-labels-not-keys)).
  Step 4 said one of those codes was still ambiguous, which no fact says.
- Step 3 said `[Num]` and `[View]` never reach a blank app; they arrive as 11
  and 9 while the program polls `GETKEY`
  ([apps.blank-app-keys](../../../docs/topics/apps.md#apps.blank-app-keys)).
- A PC run was said to show what the calculator will do. It shows what the
  interpreter does; `hpprime compare` is what asks both.
- `main.py` was stated as required, where
  [apps.main-py](../../../docs/topics/apps.md#apps.main-py) is `unverified`.
- Step 1 said there is no debugger, where `DEBUG` has an entry; that
  everything was measured on a G2, where 19 facts are `emulator`; and that the
  Virtual Calculator comes with the Connectivity Kit, where this machine had
  the CK without it.
- The example of too many locals declared ten, inside the 9 to 12 nobody has
  run, and named `e` and `i` among them
  ([ppl.i-e-as-locals](../../../docs/topics/ppl.md#ppl.i-e-as-locals)). It is
  13 now, the smallest count measured to fail.
- `L(0)` was a run-time error and a big matrix made a function crawl; neither
  was measured. The rows now say what was: `MID` with a 0, and a copy.
- Thirty bridge crossings were 8 ms; the fact says 30 to 40.
- Step 2 said every lint rule comes from an error measured on a calculator.
  Since 9704074 a rule is an error only as far as its measurement reaches, and
  `unknown-name` comes from HP's list rather than from a measurement.
- `TEXTOUT_P` was drawn without its width two lines before the reader was
  told to pass it, and was said to take a seventh argument, which is only true
  with a grob.

Beside the errors, step 2 told the story of five rounds spent on the `LOCAL`
limit; it now links
[ppl.check-last-error](../../../docs/topics/ppl.md#ppl.check-last-error).

## Deviations

- **Tasks 2 and 3 were not in the context's decision 6.** Both came from
  reading: the collision from the starter itself, and the fact from the lint
  change in 9704074, which narrowed `one-based` to a warning and left the fact
  saying more.
- **`doctor`'s last line is paraphrased, not quoted**: it says "Everything
  the kit needs is in place", and the check refuses "the kit" on any page. The
  message is the tool's, and was left alone.

## Left for plan 09-04

- `AGENTS.md` and `docs/ai/prompts.md` §1 say `L(0)` is a run-time error.
- `examples/apptest/README.md` still asks for the six on-screen label
  positions to be pressed to settle an ambiguous code, against
  `interface.soft-labels-not-keys`.

## Results

```
docs/start/ problems found by the check   13, now 0
fact links on the path                    73, to 51 facts
errors corrected on the path              19: 3 from the context, 16 from reading
test_reference.py                         32 -> 35
test_examples.py                          17 -> 24
checker                                   0 problems
suite                                     12,287 passed, 0 failed
```
