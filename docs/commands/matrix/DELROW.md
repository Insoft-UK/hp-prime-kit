# DELROW

The matrix without one of its rows.

| | |
|---|---|
| Syntax | `DELROW(matrix, row)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DELROW([[1,2],[3,4]],1)` | `[[3,4]]` | [emulator](../results.tsv) |

## Behaviour

The row goes and the ones below move up, so a 2×2 matrix becomes 1×2
(emulator). Rows are counted from 1 (G2),
[ppl.one-based](../../topics/ppl.md#ppl.one-based).

A matrix of one row is still a matrix, written `[[3,4]]` with both pairs of
brackets, not a vector (emulator). That distinction matters when the result
is stored in `M1` and read back as a file:
[formats.hpmat-vector](../../topics/formats.md#formats.hpmat-vector).

What deleting the only row does has not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DELCOL](DELCOL.md) · [SUB](SUB.md) · [REDIM](REDIM.md)
