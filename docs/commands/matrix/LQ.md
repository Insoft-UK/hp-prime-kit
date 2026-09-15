# LQ

The LQ decomposition of a matrix.

| | |
|---|---|
| Syntax | `LQ(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LQ([[1,2],[3,4]])` | `{[[−2.2360679775,−2.22044604925ᴇ−16],[−4.9193495505,0.894427191]],[[−0.4472135955,−0.894427191],[0.894427191,−0.4472135955]],[[1,0],[0,1]]}` | [emulator](../results.tsv) |

## Behaviour

**It answers three matrices in a list**, like [LU](LU.md): a lower triangular
one, an orthogonal one, and a permutation (emulator).

**The permutation is the identity here, where [LU](LU.md) needed a swap.** On
the very same matrix, `LU` returns `[[0,1],[1,0]]` as its third factor and
this returns `[[1,0],[0,1]]` (emulator). So whether rows are exchanged is a
property of the decomposition rather than of the matrix, and a program cannot
assume from one that it knows the other.

The element above the diagonal of the first factor is not zero but very
small, written with the calculator's exponent glyph (emulator),
[ppl.exponent-glyph](../../topics/ppl.md#ppl.exponent-glyph). A program
testing this factor for triangularity with `== 0` will find it is not, the
same trap [SCHUR](SCHUR.md) carries.

The Result cell was built from the stored row rather than typed, because that
glyph is not a character anybody has on a keyboard (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LU](LU.md) · [SCHUR](SCHUR.md) · [RREF](RREF.md)
