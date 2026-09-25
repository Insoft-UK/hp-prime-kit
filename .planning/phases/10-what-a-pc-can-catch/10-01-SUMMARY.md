---
phase: 10-what-a-pc-can-catch
plan: 01
status: complete
completed: 2026-09-25
key_files:
  - hpkit/lint.py
  - hpkit/docs.py
  - docs/tools.md
  - docs/topics/ppl.md
  - tests/test_lint.py
  - tests/test_appdir.py
---

# Plan 01 summary: the compile session, and the list of every fact

## What was run

7 programs and 7 calls on the Virtual Calculator 2.4, build 2025-09-15, on
2026-09-25, with `hpprime examples --compile`. **Both controls came out
right**, so all 14 answers are stored.

| Program | Compiled | Answered |
|---|---|---|
| `GETKEY()`, with parentheses | yes | −1 |
| `GETKEY`, without | yes | −1 |
| `Inference.μ₀`, Greek mu | **no** | refused |
| `Inference.µ₀`, micro sign | yes | 0.5 |
| `ENDPROC` closing a function | **no** | refused |
| `EXPORT` with 3 initialised | yes | 4 |
| `EXPORT` with 5 initialised | yes | 6 |

## What followed from it

- **`getkey-parentheses` is dropped from the candidates**: `GETKEY()`
  compiles and answers as `GETKEY` does. `ppl.getkey-no-parentheses` said
  it "takes no parentheses"; it is retitled and says both work, and
  `GETKEY`'s entry, step 3 of the guided path and
  `micropython.eval-parentheses` follow.
- **`ENDPROC` is an error**, labelled `emulator`, beside `ENDCASE` and
  `ENDFUNC`; `single-end` no longer warns `unverified` on anything.
- **`EXPORT` from 2 to 6 initialised variables compiles**, all five counts
  measured now. The two open questions of Phase 8.1 are closed.
- **`ppl.mu-zero-spelling` gains the source measurement, and loses a false
  claim.** It said the linter accepts the refused spelling and flags the one
  that works; the linter checks the names a program calls and not the ones
  it reads, so it flags neither. The `mu-zero` check stays a candidate, now
  an error on a measured refusal.

## The list

`CAUGHT` in `hpkit/lint.py`: one line for each of the 122 facts. `hpprime
docs` writes it as a table into `docs/tools.md`, between two marked lines,
and `--check` fails when the table is out of date or the lines are gone.

| Answer | Facts |
|---|---|
| a lint rule | 11 |
| another command, with its test | 43 answers: `build`, `verify`, `write`, `read`, `run`, `install`, `pull`, `emu`, `examples`, `compare`, `matrix` |
| nothing to catch, `lint` quiet | 9 |
| not from a PC, with the reason | 59 answers |
| a check decided on, to write | 9 checks over 11 facts |

Some facts have two answers: `apps.install` is `hpprime install` on the
emulator and a person's drag on hardware.

**Nine checks to write**, eight of the context's and one found by writing
the list: `ppl.global-namespace` has been measured to hide an app's name
when a program exports it (08.1-04), and no rule looks for an export that is
a name on HP's list.

## Tests that hold it

- `caught_list` in `tests/test_lint.py`: every fact has a line and every
  line names a fact; a rule named is a rule tied to that fact, and every
  such rule appears on its fact's line; a command's test is in its file, by
  its words; a quiet fact has its `QUIET` case.
- `QUIET`: one program for each of the nine, on which no rule may say
  anything, not even a warning; the global indexed from another program is
  linted as a set of two files.
- `rules_have_both_cases`: every rule tied to a fact has a case it catches
  and one it stays quiet on. Six had no quiet case and `export-clash` had no
  test at all; they have them now, the last as `MULTI`, two files at a time.
- `tests/test_appdir.py` gains the warning `build` gives a Python app with
  no `main.py`, which it gave and nothing tested.

## Deviations

- **A sentence of `ppl.mu-zero-spelling` was wrong** about what the linter
  does, as above.
- **`export-clash` had shipped with no test.** Found because the list asks
  each rule for two.

## Results

```
programs in the session       7, and 2 controls, both right
facts with a line             122 of 122
checks to write               9
lint tests                    66 -> 84
suite                         14,860 passed, 0 failed
```
