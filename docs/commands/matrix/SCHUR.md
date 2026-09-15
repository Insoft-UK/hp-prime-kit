# SCHUR

The Schur decomposition of a square matrix.

| | |
|---|---|
| Syntax | `SCHUR(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SCHUR([[1,2],[3,4]])` | `{[[0.415973557919,0.909376709132],[0.909376709132,−0.415973557919]],[[5.37228132327,1],[5.55111512313ᴇ−17,−0.372281323269]]}` | [emulator](../results.tsv) |

## Behaviour

**It answers two matrices in a list**: an orthogonal one and an upper
triangular one, whose diagonal holds the eigenvalues (emulator). Like
[EIGENVV](EIGENVV.md), a program has to take the list apart before it can use
either half.

Those diagonal values, 5.37228132327 and -0.372281323269, are the same two
[EIGENVAL](EIGENVAL.md) answers for this matrix (emulator), which is what
says the decomposition is of the matrix asked about rather than of something
else.

**The element below the diagonal is not zero, it is very small.** It reads as
5.55111512313 followed by the calculator's exponent glyph and -17 (emulator),
which is machine epsilon rather than an exact zero. A program testing a Schur
form for triangularity with `== 0` will find it is not, and the answer above
carries the calculator's own typography for that exponent,
[ppl.exponent-glyph](../../topics/ppl.md#ppl.exponent-glyph).

The Result cell was built from the stored row rather than typed, because the
exponent glyph is not a character anybody has on a keyboard (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EIGENVV](EIGENVV.md) · [LU](LU.md) · [EIGENVAL](EIGENVAL.md)
