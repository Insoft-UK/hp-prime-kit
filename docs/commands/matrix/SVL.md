# SVL

The singular values of a matrix.

| | |
|---|---|
| Syntax | `SVL(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SVL([[1,2],[3,4]])` | `[0.365966190626,5.46498570422]` | [emulator](../results.tsv) |

## Behaviour

`SVL([[1,2],[3,4]])` answers the two singular values as a vector, `TYPE` 4
(emulator), [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**They come back smallest first.** 0.365966190626 before 5.46498570422
(emulator), which is the opposite order from the one most libraries use and
the opposite of what a program reaching for "the largest" by taking the first
element would get.

The larger of the two is exactly what [SPECNORM](SPECNORM.md) answers for
this matrix (emulator): the spectral norm is the largest singular value, and
the two commands agree to every digit.

`SVD` answers the vectors as well as these values, and its answer
came back longer than the 160 characters the harness carries, so it
has no entry yet and no faithful result to show (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SPECNORM](SPECNORM.md) · [EIGENVAL](EIGENVAL.md)
