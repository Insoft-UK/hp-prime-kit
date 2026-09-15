# EIGENVV

The eigenvectors and eigenvalues of a square matrix, together.

| | |
|---|---|
| Syntax | `EIGENVV(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EIGENVV([[1,2],[3,4]])` | `{[[0.415973557919,-0.83696500723],[0.909376709132,0.574275723826]],[[5.37228132327,0],[0,-0.372281323269]]}` | [emulator](../results.tsv) |

## Behaviour

**It answers two matrices in a list, not one object.** The first holds the
eigenvectors as its columns; the second is diagonal, with the eigenvalues on
the diagonal and zeros elsewhere (emulator). A program has to take the list
apart before it can use either.

The diagonal holds 5.37228132327 and -0.372281323269, which is exactly what
[EIGENVAL](EIGENVAL.md) answers for the same matrix (emulator). So this
command is the larger one: it gives what `EIGENVAL` gives, and the vectors as
well.

The list is `TYPE` 6 and each element inside it is `TYPE` 4 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

Answering several objects at once is the shape the decompositions share:
[LU](LU.md) and [SCHUR](SCHUR.md) both come back as a list
(emulator), and a program that expects a single matrix from any of them is
wrong about all of them.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EIGENVAL](EIGENVAL.md) · [SCHUR](SCHUR.md) · [SPECRAD](SPECRAD.md)
