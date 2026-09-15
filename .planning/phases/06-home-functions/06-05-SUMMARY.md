---
phase: 06-home-functions
plan: 05
status: complete
completed: 2026-09-13
key_files:
  - docs/commands/catalog/*.md
  - docs/commands/strings/EXPR.md
  - docs/topics/ppl.md
  - docs/commands/results.tsv
commits: ["The last seven of catalog's mathematics, and why three rounds accused the wrong line"]
---

# Plan 05 summary: the mathematics of catalog

## What was built

- All 25 names: the trigonometric six, the logarithmic three, the polynomial
  three, the constants and edges, and the seven that held out --
  `Dirac`, `Heaviside`, `INVERSE`, `NEG`, `NTHROOT`, `PIECEWISE` and `Σ`.
- `ppl.check-last-error`, a new fact.
- `EXPR` gained what this plan measured about it, and lost two stale labels.

## What this turned up

**`NTHROOT` is an operator written between its arguments**, the second name
after `MOD` to turn out that way. `3 NTHROOT 8` answers 2, the cube root of
8, which also settles which operand is the degree; `NTHROOT(3,8)`, the same
two numbers in the same order, is refused. HP's list gives neither name a
syntax string, and that absence is now a signal worth reading rather than a
gap.

**The interpreter answers 3 where the calculator answers 2.** It does not
know `NTHROOT` as an operator, so it evaluates the left operand and drops the
rest without raising -- the defect `MOD` already records, but this is the
first time the calculator's true answer sits beside it. A program checked on
the PC gets a plausible number that is simply not what the calculator will
compute.

**A missing syntax string does not mean the name is not a function.**
`Heaviside(1)` answers 1 despite having none, while `NEG(5)` and
`INVERSE(4)` are refused. The four names share HP's silence and do not share
a shape, so each has to be measured.

**Infinity is an ordinary real.** `Dirac(0)` is `+Inf` read as text, and
`TYPE` answers 0 for it -- nothing in the type marks it, so a program
branching on `TYPE` carries the infinity forward like any other number. Asking
for the text and the type, rather than the value, is what let this be measured
at all: the kit's decoder still raises on that sign nibble.

**The compiler names the last bad line, not the first.** This is the finding
that explains the whole plan. Three batches were refused at lines 35, 33 and
31, and each accused a call that the round before had appeared to clear. They
had not been cleared: everything *below* a named line is clean and everything
above it is still unknown, which is the opposite of what was assumed.

**A doubtful call belongs inside `EXPR`.** A string compiles whatever it
holds and fails, if it fails, at run time, where the harness's `IFERR` marks
that row alone. The batch that finished this plan wrapped every call and came
back with nine answers including three refusals -- where the three before it,
carrying the same calls directly, had come back with nothing at all.

## Deviations

- **Four rounds of the user's keypresses, and three produced no data.** Two
  were refused at compile time, one was launched and never run before the
  harness gave up waiting. The wrapped batch was the first to return anything.
- **A false claim reached the repository.** Before the pause, `STATE.md` said
  `NTHROOT` was refused in both its forms. It rested on a line-map formula of
  `2N+21` that had never been checked; the true map is `2N+23`. The claim was
  withdrawn in its own commit, and the check that settled it was decoding the
  `.hpprgm` actually sent to the calculator and diffing it against a rebuild --
  43 lines, nothing differing but the container's binary header and trailer.
  Reconstructing what was sent is not the same as reading it.
- **The user's three line numbers were all correct.** The contradiction was
  built here, by assuming a compiler reports its first error. Every reading
  they reported survived; every inference drawn from them did not.
- **The wrong checker was being used.** `docs.load` with `cross_check` reports
  0 while `docs.check` reports the produced pages as stale, which is what the
  suite runs. Two rounds of green were declared on the narrower one.
- **`EXPR`'s own entry understated what was known**: an example labelled
  `unverified` that had a stored emulator row, and a paragraph saying the
  trappability of its failure had not been measured when `EXPR("")` had
  measured it. Found while leaning on the command, not by a check.

## Results

```
catalog, the mathematics   25 of 25
phase 6                   154 of 177
still to write             23, all of them catalog machine names
```
