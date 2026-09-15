# QR

The QR decomposition of a matrix.

| | |
|---|---|
| Syntax | `QR(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `QR([[1,2],[3,4]])` | `{[[−0.316227766017,0.948683298051],[−0.948683298051,−0.316227766017]],[[−3.16227766017,−4.42718872424],[−8.881784197ᴇ−16,0.632455532034]],[[1,0],[0,1]]}` | [emulator](../results.tsv) |

## Behaviour

**Three matrices in a list**: an orthogonal one, an upper triangular one,
and a permutation (emulator). That is the same count [LU](LU.md) and
[LQ](LQ.md) answer with, and the permutation here is the identity, as it is
for `LQ` and unlike `LU` on the same input (emulator).

The element below the diagonal of the triangular factor is not zero but very
small, carrying the calculator's exponent glyph (emulator),
[ppl.exponent-glyph](../../topics/ppl.md#ppl.exponent-glyph). Testing a QR
factor for triangularity with `== 0` will fail, the same trap
[SCHUR](SCHUR.md) and [LQ](LQ.md) carry.

The Result cell was built from the stored row rather than typed, because that
glyph is not on any keyboard (emulator).

This entry exists late: `QR` was named when the plan was written and left out
of the probe list by mistake, so it was measured a batch after the rest
(emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LQ](LQ.md) · [LU](LU.md) · [SCHUR](SCHUR.md)
