# ABS

The absolute value of a number, or the norm of a matrix.

| | |
|---|---|
| Syntax | `ABS(expr)` |
| Group | matrix |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ABS(-3.14)` | `3.14` | [emulator](../results.tsv) |
| `ABS([[1,2],[3,4]])` | `5.47722557505` | [emulator](../results.tsv) |

## Behaviour

Of a number it is the absolute value (HP help), which is what the name
suggests and what a program usually wants.

**Of a matrix it is one number, not a matrix.** `ABS([[1,2],[3,4]])` is
5.47722557505 (HP help), which is the square root of 1+4+9+16: the norm of
the whole matrix, taken element by element and gathered into a single figure.
It is **not** the absolute value of each element, which is what a program
written in the habits of another language will assume, and the shapes differ
so the mistake shows up later as a type error rather than a wrong number.

The interpreter covers the plain number and raises on the matrix form
(unverified: this kit's interpreter on the PC, not a calculator), so that row
rests on HP's help until the batch runs it.

For the size of a matrix rather than its norm, the command is
[SIZE](../list/SIZE.md), which answers a list of two rather than a
number (emulator).

## Related

[DET](DET.md) · [TRN](TRN.md) · [SIZE](../list/SIZE.md)
