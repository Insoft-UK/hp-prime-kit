---
phase: 10-what-a-pc-can-catch
plan: 02
status: complete
completed: 2026-09-25
key_files:
  - hpkit/lint.py
  - hpkit/appdir.py
  - tests/test_lint.py
  - tests/test_appdir.py
  - docs/tools.md
  - docs/start/03-input-screen.md
  - examples/conformance/BISROOT.txt
---

# Plan 02 summary: the checks the list decided on

## What was built

- **Seven lint rules**, and one grown:

  | Rule | Fact | Level |
  |---|---|---|
  | `mu-zero` | `ppl.mu-zero-spelling` | error, emulator |
  | `getkey-code` | `interface.getkey-position`, `interface.key-codes` | warning, G2 |
  | `string-index` | `ppl.string-index-code` | warning, emulator |
  | `draw-units` | `interface.draw-units` | warning, emulator |
  | `draw-then-return` | `interface.draw-then-return` | warning, G2 |
  | `wait-undrained` | `interface.drain-then-wait` | warning, G2 |
  | `expr-in-loop` | `ppl.expr-dynamic-access` | warning, G2 |
  | `export-clash`, grown | `ppl.global-namespace` | warning, emulator, on an export named like one of HP's |

  Twenty rules now, eighteen tied to a fact. Three of the new ones read a
  whole function, and follow the file's own calls: `_functions`,
  `_key_loops` and `_function_findings` in `hpkit/lint.py`.
- **`build` warns on `MOUSE` handed to Python raw**, `appdir.check_mouse`,
  beside the import check.
- **Every line of `CAUGHT` names what catches its fact**, and
  `caught_list` now fails on a check decided and not written.
- **16 lint cases** in `EVIDENCE`, one each way for every new rule, and two
  in `tests/test_appdir.py` for `MOUSE`.

## What the rules found in the kit

- **The guided path taught a drawing that vanishes.** Step 3's `TDRAW`
  drew and returned; run from Home, it shows Home. The step warned about the
  trap further down and its own example fell into it. It now drains and
  waits, and step 2's table says `lint` warns on it, where it said `lint`
  could not see it.
- **The conformance example exported `ROOT`**, the Function app's. It is
  `BISROOT` now, file and function, with its script and its test.

Read against the 29 distinct programs in the user's Connectivity Kit mirror
and the emulator, locally and without changing them, the new rules said one
thing: `ZQMU1`, the probe of 10-01 written with the Greek mu. No false alarm.

## Deviations

- **A regular expression of mine backtracked.** `getkey-code` skipped every
  variable, because `\s*` gave back a space and let "assigned something
  other than `GETKEY`" match `zk := GETKEY`. The case it catches failed, as
  it should, and the rule now reads each value assigned.
- **A one-line function's calls were not counted**, an off-by-one in which
  lines belong to a function; found reading the code, before a test showed
  it.
- **`ppl.mu-zero-spelling` came out with a sentence twice** after its
  correction; fixed on reading it back.

## Results

```
lint rules                     13 -> 20 (18 tied to a fact)
checks left to write            0
lint tests                     84 -> 100
appdir tests                   38 -> 40
suite                          14,879 passed, 0 failed
docs/llms.txt                  91,335 bytes of 100,000
```
