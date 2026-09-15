# SUB

The rectangle of a matrix between two corners.

| | |
|---|---|
| Syntax | `SUB(matrix, {row1, col1}, {row2, col2})` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SUB([[1,2,3],[4,5,6]],{1,1},{2,2})` | `[[1,2],[4,5]]` | [emulator](../results.tsv) |

## Behaviour

Both corners are lists, row first, counted from 1, and **both are included**:
from `{1,1}` to `{2,2}` is a 2×2 block, not 1×1 (emulator).

What a second corner before the first does, and what happens when a corner is
outside the matrix, has not been measured (unverified).

HP files `SUB` under matrices (HP help); whether the same name takes a
sublist or a substring has not been measured here either (unverified), and
[MID](../strings/MID.md) is the measured way to cut a string (G2).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[REPLACE](REPLACE.md) · [REDIM](REDIM.md) · [DELCOL](DELCOL.md)
