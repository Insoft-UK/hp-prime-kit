# SWAPROW

Exchanges two rows of a matrix.

| | |
|---|---|
| Syntax | `SWAPROW(matrix, row1, row2)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SWAPROW([[1,2],[3,4]],1,2)` | `[[3,4],[1,2]]` | [emulator](../results.tsv) |

## Behaviour

The rows are counted from 1 (G2):
[ppl.one-based](../../topics/ppl.md#ppl.one-based). The answer is a matrix,
`TYPE` 4 (emulator).

It is the row-wise twin of [SWAPCOL](SWAPCOL.md), and the same two questions
are open for it: what an out-of-range row does, and whether the matrix you
pass is left alone (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SWAPCOL](SWAPCOL.md) · [DELROW](DELROW.md) · [SUB](SUB.md)
