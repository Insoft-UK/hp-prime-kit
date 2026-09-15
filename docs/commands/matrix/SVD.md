# SVD

The singular value decomposition of a matrix.

| | |
|---|---|
| Syntax | `SVD(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SIZE(SVD([[1,2],[3,4]]))` | `3` | [emulator](../results.tsv) |

## Behaviour

**It answers three objects**: two matrices with a vector of singular values
between them (emulator). The example asks how many rather than showing them,
and that is not squeamishness -- the full answer came back longer than the
160 characters this kit's harness carries, so the stored row for the direct
call is cut and could not be quoted faithfully (emulator).

The middle object is what [SVL](SVL.md) answers on its own:
`[0.365966190626,5.46498570422]` for this matrix, smallest first (emulator).
A program that wants only the singular values should ask `SVL` and avoid the
size problem altogether.

The larger of those values is what [SPECNORM](SPECNORM.md) answers
(emulator), so three commands agree about this matrix from three different
directions.

Answering a list is the shape [LU](LU.md), [LQ](LQ.md) and [SCHUR](SCHUR.md)
share (emulator), and this one has the same count as the first two.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SVL](SVL.md) · [SPECNORM](SPECNORM.md) · [LU](LU.md)
