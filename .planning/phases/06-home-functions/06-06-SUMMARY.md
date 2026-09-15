---
phase: 06-home-functions
plan: 06
status: complete
completed: 2026-09-13
key_files:
  - docs/commands/catalog/*.md
  - hpkit/examples.py
  - tests/test_examples_run.py
  - docs/commands/results.tsv
commits: ["The machine half of catalog, and the guard that had to be widened first"]
---

# Plan 06 summary: the machine names of catalog

## What was built

- All 23 names: `ALPHA` `COLOR` `CopyVar` `DEBUG` `DrawSlp` `EEX` `EVALLIST`
  `GETBASE` `GF` `ICON` `IFTE` `LineHorz` `LineTan` `LineVert` `MEMORY`
  `QUOTE` `SERIAL` `SUPPRESS` `UTPC` `UTPF` `UTPN` `UTPT` `VERSION`.
- `NEVER_STORED` widened to hold `VERSION` as well as `SERIAL`, with the test
  that covers it.
- Phase 6 closes: 177 of 177, `catalog` 48 of 48.

## What this turned up

**`VERSION` would have leaked the serial number, and the batch had not run
yet.** The guard built in plan 01 covered `SERIAL`. `VERSION` answers the
serial too, and every row's firmware stamp already went through a function
that strips that line -- but a *case* whose entry is `VERSION` does not take
that path, it takes the ordinary one into `results.tsv`, which is committed
and published. Found while designing the batch rather than while reading the
file afterwards, which is the only reason nothing had to be scrubbed. The
answer was code, not care: the name went on the list before the batch was
launched, and both came back as `(not stored)`.

**The guard was lying in one small way.** It replaced the answer but left the
mark saying the answer had been cut at 160 characters, so the row read
`"(not stored)" (cut at 160 characters)` -- a placeholder claiming it was a
truncation of itself. Fixed in the guard, covered by a new assertion, and the
one row already written was repaired.

**All four upper-tail commands are refused**, each following HP's own
published syntax and argument count. Four refusals across three different
shapes is not four mistakes in writing calls; what they share is the way they
were reached, through `EXPR` on Home. The probe is one direct call in a
program, and it is named in `UTPN`, where the shared explanation lives.

**`LineTan` answered a collapsed expression**: `line(y=diff(0,0)*x-diff(0,0))`
rather than the tangent to x squared. The expression was evaluated before the
command saw it. It is the worst kind of wrong answer, because the call
succeeded and a line is exactly what the caller expected.

**Three of the four names HP publishes no syntax for are not callable at
all.** `ALPHA`, `EEX` and `ICON` are errors; `COLOR` hands its own name back
as a symbolic object, which is what an unknown symbol does as much as what a
constant would do, so that row does not settle what it is either.

**The drawing helpers do not draw.** `DrawSlp`, `LineHorz` and `LineVert`
answer line equations as symbolic objects. A program expecting pixels gets a
value.

Smaller ones: `GETBASE` answers a code rather than the base -- hexadecimal in
gave `#4h` back; `GF` answers a *string* describing the field it built,
polynomial included, where every other constructor here answers an object;
`MEMORY` answers two 64-bit based integers whose order is not established;
`QUOTE` returns `1+2` unevaluated, the exact opposite of `EXPR`.

**Two probes plan 05 left open both failed**, which is worth as much as if
they had worked: `NEG 5` is refused, so both forms of `NEG` are now refused
and its working shape is still unknown; and `INVERSE([[1,2],[3,4]])` is
refused, which kills the interpreter's lead that the argument merely wanted
to be a matrix.

## Deviations

- **`DEBUG` was deliberately not run.** It stops a program and waits for a
  person, so in a batch it would hold the emulator window open and cost a
  round of keypresses for nothing. Its entry says that rather than reading as
  though nobody got to it.
- **Labels went missing again**, four of them, in `MEMORY` and three of the
  `UTP` entries. Caught by the checker, as every time.
- **`DEBUG`'s example cell was invalid**: the Call column must hold PPL in
  backticks and it held the word `none`. The convention for an entry with no
  runnable value was already settled elsewhere -- a real call with
  `*no value*` -- and was copied rather than invented.
- **The narrow checker was used again by habit.** `docs.load` with
  `cross_check` reports 0 while `docs.check` reports stale produced pages.
  The suite runs the second one.

## Results

```
catalog, the machine names   23 of 23
catalog                      48 of 48
phase 6                     177 of 177
```
