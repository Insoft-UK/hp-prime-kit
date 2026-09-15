# DELCOL

The matrix without one of its columns.

| | |
|---|---|
| Syntax | `DELCOL(matrix, col)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DELCOL([[1,2,3],[4,5,6]],2)` | `[[1,3],[4,6]]` | [emulator](../results.tsv) |

## Behaviour

The column goes and the ones to its right move left, so a 2×3 matrix becomes
2×2 (emulator). Columns are counted from 1 (G2),
[ppl.one-based](../../topics/ppl.md#ppl.one-based).

What deleting the only column does, and what an out-of-range number does, has
not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DELROW](DELROW.md) · [SUB](SUB.md) · [REDIM](REDIM.md)
