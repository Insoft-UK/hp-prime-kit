# SWAPCOL

Exchanges two columns of a matrix.

| | |
|---|---|
| Syntax | `SWAPCOL(matrix, col1, col2)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SWAPCOL([[1,2],[3,4]],1,2)` | `[[2,1],[4,3]]` | [emulator](../results.tsv) |

## Behaviour

The columns are counted from 1, like every index in PPL (G2):
[ppl.one-based](../../topics/ppl.md#ppl.one-based). The answer is a new
matrix, of `TYPE` 4 (emulator).

What it does when a column number is out of range, and whether it changes the
matrix you pass or only answers with a changed copy, has not been measured
(unverified). Matrices are passed by value (G2),
[ppl.matrices-by-value](../../topics/ppl.md#ppl.matrices-by-value), which
suggests the second, and suggesting is not measuring.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SWAPROW](SWAPROW.md) · [DELCOL](DELCOL.md) · [SUB](SUB.md)
