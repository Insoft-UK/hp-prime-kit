---
phase: 06-home-functions
plan: 02
status: complete
completed: 2026-09-13
key_files:
  - docs/commands/matrix/*.md
  - docs/topics/ppl.md
  - docs/commands/results.tsv
commits: ["Five matrix functions, drafted from HP and checked on the PC first", "Fourteen matrix functions, and a third character only the calculator writes", "Five more matrix functions: the shape-builders, and LQ", "The matrix group closes but for valuation, and a fourth glyph", "valuation closes the matrix group, and explains the byte that broke it"]
---

# Plan 02 summary: the matrix functions

## What was built

- All 40 matrix functions. `valuation` came last, and the reason it came
  last is a measurement in itself.
- Two facts: `ppl.exponent-glyph` and `ppl.exact-answers`. `ppl.type-codes`
  gained a measured code 3 and a second, independent measurement of code 8.

## What this turned up

**Two questions the entries themselves had posed were answered.** `TRN` is the
plain transpose, not the conjugate one: `TRN([[1+2*i,3],[4,5]])` comes back
with the imaginary part's sign unchanged. And the list-of-matrices form is
real and shared -- `DET`, `RREF`, `TRN` and `IDENMAT` all map over a list,
measured in one batch, so what three entries called a suggestion became a
property of these commands.

**`l2norm` answers exactly and its siblings do not.** The square root of 14,
written with U+221A and held as `TYPE` 8, where `l1norm` answers 6 and
`maxnorm` answers 3 as plain numbers. A program cannot tell from the family
whether it will get a number back. `TYPE` 8 is what `CAS` answers with, and
this reached it with no `CAS` call around it.

**Four commands answer a "norm" for one 2x2 matrix and no two agree**: 6, 7,
5.46498570422 and 5.47722557505, with `SPECRAD` a fifth number again from the
eigenvalues rather than the singular values.

**The calculator writes four characters nobody can type.** The minus sign was
known; this plan added the exponent glyph U+1D07 and the radical U+221A, and
Phase 6's first plan added the imaginary unit. Only the minus sign is
normalised anywhere in this kit, so entries carrying the others were written
from the stored row rather than typed.

**One undecodable cell lost a whole batch.** `valuation(X^2+X)` answered
negative infinity -- exponent 499, a mantissa of nines, and a sign nibble
of 2 where an ordinary negative uses 9, measured afterwards by asking for
the value as text. `numbers.decode` accepts only
0 and 9, so it raised, and `collect()` raised with it before writing a single
row: seventeen calls and a round of the user's keypresses gone. The sixteen
good rows were recovered afterwards by reading `M9.hpmat` directly and writing
them through the kit's own `firmware` and `write_results`, which is what says
the data was there the whole time. Both halves are in `STATE.md`, and the
second -- that `collect()` is all-or-nothing where it could keep what it can
read -- matters more than the first.

## Deviations

- **`QR` was named in the plan and left out of the probe list.** A coverage
  count caught it, a batch later than the rest. `LQ` was measured on time and
  then missed when the entries were written; the same count caught that too.
  Counting what is on disk against the inventory is worth more than
  remembering what was done.
- **`SVD` and `RANDMAT` are documented by their shape, not their contents.**
  One answer is longer than the 160 characters the harness carries and comes
  back cut; the other differs every run, so a stored answer would be a number
  no later run reproduces. `SIZE(...)` of each is repeatable, and both entries
  say why the example asks what it asks.
- **`valuation` needed a probe shaped around the decoder.**
  `STRING(valuation(X^2+X))` answers `"-Inf"` and `TYPE(...)` answers 0:
  negative infinity, held as an ordinary real. So sign nibble 2 marks an
  infinity where 9 marks an ordinary negative, and the byte pattern that
  cost a whole batch is now explained rather than guessed at. The entry
  also says plainly that -Inf is almost certainly not the valuation of
  `X^2+X` -- the probe most likely did not ask what it appears to ask.
- **Three shell heredocs failed** -- one on `$TMPDIR`, one on backslashes, one
  on length -- and each cost a round. The work moved to a `.py` file run by
  path, which is what the session's own memory note already said to do.
- **`write_results` was called without knowing whether it merges or
  replaces.** It merges, and nothing was lost, but that was luck rather than
  care: it mutates a committed data file holding every measurement in the
  project.

## Results

```
python tests/run_all.py     0 failed, across 13 suites
hpprime docs --check        186 entries, 111 facts: 0 problems
matrix                      40 of 40
phase 6                     74 of 177
```
