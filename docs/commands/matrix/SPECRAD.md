# SPECRAD

The spectral radius: the largest eigenvalue by magnitude.

| | |
|---|---|
| Syntax | `SPECRAD(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SPECRAD([[1,2],[3,4]])` | `5.37228132327` | [emulator](../results.tsv) |

## Behaviour

`SPECRAD([[1,2],[3,4]])` answers 5.37228132327 (emulator), which is the
larger of the two eigenvalues [EIGENVAL](EIGENVAL.md) gives for the same
matrix, to every digit brought back.

**It is not the same as the spectral norm.** [SPECNORM](SPECNORM.md) answers
5.46498570422 for this matrix (emulator): close enough to be mistaken for a
rounding difference and far enough apart to be a different quantity
altogether. The radius comes from the eigenvalues, the norm from the singular
values.

It answers a plain number, `TYPE` 0 (emulator).

Whether it takes the magnitude of a negative eigenvalue before comparing was
not settled here, because the larger value is positive in this matrix
(unverified). The probe is a matrix whose most negative eigenvalue is the
largest in size.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SPECNORM](SPECNORM.md) · [EIGENVAL](EIGENVAL.md) · [COND](COND.md)
