---
phase: 10-what-a-pc-can-catch
created: 2026-09-25
requirements: [CHECK-04]
---

# Phase 10 context: What a PC can catch

## What this phase is

CHECK-04's open half: every fact a PC could catch is caught, or says why not.
Phase 4 tied every lint rule to a fact; nobody has gone the other way, from
the facts to the rules. And Phase 9's counts, taken again on the finished
reference, close milestone 1.

Measured before planning, on 2026-09-25:

| | |
|---|---|
| facts in `docs/topics/` | 122: 76 G2, 26 emulator, 20 unverified |
| lint rules | 13: 11 tied to a fact, 2 to no fact (`unbalanced`, `unknown-name`) |
| facts a lint rule cites | 11 |
| facts cited by any test or tool, by identifier | 13 |
| `docs/llms.txt` | 91,328 bytes of 100,000 |

So 111 facts have no rule, and most of them never can: a person dragging a
file, a touch that arrives twice, the time a bridge crossing takes. The work
is to say which is which, one fact at a time, and to write the rules the list
says are missing.

## Decisions, from the user on 2026-09-25

1. **Any `hpprime` command counts as catching a fact**, not only `lint`.
   `run` follows `ppl.matrices-by-value`, `build` catches
   `micropython.imports`, `write` holds the `formats` facts. The list names
   the command and the test that holds it. New lint rules are written only
   where no command covers a fact and a source file is enough to see it.
2. **The list lives with the linter.** The data goes in `hpkit/lint.py`,
   next to `FACTS`; `hpprime docs` writes it as a table in `docs/tools.md`;
   a test fails if a fact has no line or a line names no fact. The fact
   format does not change, and `docs/llms.txt` does not grow with it.
3. **One compile session on the emulator**, like 08.1-04's, for what the
   new rules need measured, so that a rule is an error only where the
   calculator refused.

## The list: four answers a fact can have

| Answer | Means | Held by |
|---|---|---|
| a lint rule | `hpprime lint` finds it in a source file | a test it catches and one it must stay quiet on |
| a command | `run`, `build`, `verify`, `write`, `read`, `install`, `pull`, `examples` or `matrix` implements or checks it | the test that fails if the command stops |
| nothing to catch | a permission or a refuted hypothesis: the mistake would be flagging it | a test that `lint` stays quiet, and `run` does not call it an error |
| not from a PC | it depends on something no file holds: which app is active, the screen, a person's hands, timing, the hardware, or somebody else's code | the reason, in one line |

A fact can have more than one; the table gives each.

## What a first reading found

**Nine checks look missing**, each backed by a fact whose failure is
silent or confusing on the calculator:

| Check | Fact | What it would flag | Level |
|---|---|---|---|
| `mu-zero` | `ppl.mu-zero-spelling` (emulator) | `μ₀` spelled with the Greek mu, which the calculator refuses; and stop flagging the micro-sign spelling that works | error, if the session sees it refused in source |
| `getkey-parentheses` | `ppl.getkey-no-parentheses` (G2) | `GETKEY()` in PPL source | error if it does not compile; if it does, no rule and the fact is corrected |
| `getkey-code` | `interface.getkey-position`, `interface.key-codes` (G2) | a variable read from `GETKEY` compared with a string, or with a number outside 0 to 50 | warning |
| `string-index` | `ppl.string-index-code` (emulator) | a variable holding a string, indexed and compared with a string: always false | warning |
| `draw-units` | `interface.draw-units` (emulator) | a drawing command without `_P` given coordinates far outside the window a reset calculator has, which reads as pixels | warning |
| `draw-then-return` | `interface.draw-then-return` (G2) | an exported function that draws and returns without waiting | warning |
| `wait-undrained` | `interface.drain-then-wait` (G2) | a loop waiting for `GETKEY` with no draining loop before it | warning |
| `expr-in-loop` | `ppl.expr-dynamic-access` (G2) | `EXPR` inside a loop | warning |
| `build`: raw `MOUSE` | `interface.mouse-lists`, `micropython.list-with-string-closes-the-app` (G2) | `eval('MOUSE')` passed straight to Python, which closes the app without a word | warning, in `build` and `verify`, beside the import check |

The final set is the list's to decide, and each check has to pay for
itself: a test it catches, a test it stays quiet on, and the kit's own
examples and templates still clean.

**The compile session** asks: `GETKEY()` with parentheses; `μ₀` with the
Greek mu and with the micro sign, in source; `ENDPROC`, which 08.1-04 left
out; and `EXPORT` with 3 and with 5 initialised variables, the two counts
08.1-04 did not try. The last two close the open questions of Phase 8.1.

**Eight facts are "nothing to catch"** and want a quiet test each:
`ppl.global-index-other-program`, `ppl.return-in-loop`,
`ppl.letter-digit-names`, `ppl.local-m-matrices`,
`ppl.locals-initialised-one-line`, `ppl.i-e-as-locals`,
`ppl.names-ignore-case`, and `apps.qualified-names` for `lint`.

## Risks, each with what would settle it

**False alarms.** Issue #1 was two of them, and a warning that fires on
correct code teaches people to ignore the linter. Every new rule gets a
quiet test built from the fact's own correct form, and the whole kit --
`examples/`, `templates/`, the guided path -- is linted before a rule is
kept. A rule that fires there is either right, and the example is fixed, or
wrong, and the rule is narrowed.

**Heuristics across functions.** `draw-then-return` and `wait-undrained`
have to follow calls within the file to be right, and cannot see into other
files. What they cannot see they leave alone rather than guess.

**The index budget.** `docs/llms.txt` is at 91% of its budget before the
recount. The list goes in `tools.md`, which the index does not copy, so it
should not move; if the recount finds it over, trimming comes before
raising the budget, and the user decides.

## Constraints that do not change

An error only where a calculator refused; a warning carries its fact's
label. No dependencies. Batches run on `Prime_1`. `results.tsv` is written by
`hpprime examples` only. Nothing is pushed without asking.
