# Dirac

The Dirac delta, which is infinite at zero.

| | |
|---|---|
| Syntax | `Dirac(Real)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("STRING(Dirac(0))")` | `"+Inf"` | [emulator](../results.tsv) |
| `EXPR("TYPE(Dirac(0))")` | `0` | [emulator](../results.tsv) |

## Behaviour

`Dirac(0)` is positive infinity, and the calculator writes it `+Inf`
(emulator). The answer here is the text of it rather than the number,
because the number is what this kit cannot yet read back.

**Infinity is stored as an ordinary real** (emulator). `TYPE` answers 0, the
same code a plain number gets, so nothing in the type says the value is
special: [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). A program that
branches on `TYPE` will treat this like any other real and carry the infinity
forward.

The bytes are exponent 499 with a mantissa of nines and a sign nibble of 6,
where an ordinary negative uses 9 (emulator). `MAXREAL` has that same
exponent and mantissa with an ordinary nibble, which is what says the nibble
marks infinity itself rather than a magnitude.

**Both calls were sent inside `EXPR` on purpose** (emulator). A batch is
refused whole if any line will not compile, and a string cannot be refused at
compile time, so wrapping a doubtful call buys a per-row answer instead of a
lost batch. What the bare call does at the top level of a program is not
measured here (unverified).

Asking for the text and the type, rather than the value, is also deliberate
(emulator): this kit's decoder does not know that sign nibble and raises on
it, and one unreadable cell used to lose every row beside it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Heaviside](Heaviside.md) · [MAXREAL](MAXREAL.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
