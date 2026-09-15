# LU

The LU decomposition of a square matrix.

| | |
|---|---|
| Syntax | `LU(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LU([[1,2],[3,4]])` | `{[[1,0],[0.333333333333,1]],[[3,4],[0,0.666666666667]],[[0,1],[1,0]]}` | [emulator](../results.tsv) |

## Behaviour

**It answers three matrices, not two.** The lower triangular one, the upper
triangular one, and a permutation matrix that records which rows were swapped
on the way (emulator). A program written for the two-matrix form of LU that
other libraries give will index the wrong object.

That third matrix is `[[0,1],[1,0]]` here, which says the two rows were
exchanged before the factors were computed (emulator). Multiplying the
factors back together gives the permuted matrix rather than the original, and
a program that checks its own work has to account for it.

The list is `TYPE` 6 with `TYPE` 4 elements (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), the same shape
[EIGENVV](EIGENVV.md) and [SCHUR](SCHUR.md) answer with.

The values are decimals, a third and two thirds shown to twelve digits
(emulator), so nothing here is exact.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SCHUR](SCHUR.md) · [EIGENVV](EIGENVV.md) · [DET](DET.md)
