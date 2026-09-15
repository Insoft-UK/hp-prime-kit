# ismith

The Smith normal form of an integer matrix.

| | |
|---|---|
| Syntax | `ismith(Matrix_A)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ismith([[1,2],[3,4]])` | `{[[1,0],[3,−1]],[[1,0],[0,2]],[[1,−2],[0,1]]}` | [emulator](../results.tsv) |

## Behaviour

**Three matrices in a list**, where [ihermite](ihermite.md) answers two
(emulator): a transformation on each side and the form between them.

Like `ihermite`, everything is whole numbers (emulator), so this is an exact
factorisation rather than a numerical one.

The middle matrix is diagonal here (emulator), which is what the Smith form
is: the two outer matrices absorb everything else.

What it does with a matrix holding decimals was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ihermite](ihermite.md) · [RREF](RREF.md) · [DET](DET.md)
