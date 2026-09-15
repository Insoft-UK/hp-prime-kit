# ihermite

The Hermite normal form of an integer matrix.

| | |
|---|---|
| Syntax | `ihermite(Matrix_A)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ihermite([[1,2],[3,4]])` | `{[[−2,1],[3,−1]],[[1,0],[0,2]]}` | [emulator](../results.tsv) |

## Behaviour

**Two matrices in a list**: the transformation and the form (emulator).

The answer holds whole numbers, not decimals (emulator), which is what
separates this from the decompositions in this group: it works over the
integers, so nothing is rounded and the factors multiply back exactly.

That makes it usable where [LU](LU.md) and [QR](QR.md) are not, for a program
that must not lose precision. Whether it refuses a matrix holding decimals was
not run (unverified).

[ismith](ismith.md) is the other integer form and answers three matrices
rather than two (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ismith](ismith.md) · [RREF](RREF.md) · [LU](LU.md)
