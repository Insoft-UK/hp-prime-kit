# cholesky

The Cholesky factor of a symmetric positive-definite matrix.

| | |
|---|---|
| Syntax | `cholesky(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `cholesky([[4,2],[2,3]])` | `[[2,0],[1,1.41421356237]]` | [emulator](../results.tsv) |

## Behaviour

**It answers one matrix, not a list**, which makes it the exception among the
decompositions: [LU](LU.md) and [LQ](LQ.md) answer three objects and
[SCHUR](SCHUR.md) two (emulator).

The answer is lower triangular (emulator), and multiplying it by its own
transpose gives back the matrix it was given -- which is what the
factorisation is for, and what a program can check for itself with
[TRN](TRN.md).

**The matrix given here is not the one used everywhere else in this group.**
`[[1,2],[3,4]]` is neither symmetric nor positive definite, so it has no
Cholesky factor; `[[4,2],[2,3]]` was used instead (emulator). What this
command does when given a matrix that does not qualify was not run
(unverified), and that is the case worth knowing, because a program feeding
it data cannot always promise the matrix is well behaved.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LU](LU.md) · [LQ](LQ.md) · [TRN](TRN.md)
