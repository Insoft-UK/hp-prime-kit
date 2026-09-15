# ADDROW

Inserts a row into a matrix.

| | |
|---|---|
| Syntax | `ADDROW(matrix, list, row)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ADDROW([[1,2],[3,4]],{5,6},3)` | *error* | [emulator](../results.tsv) |
| `ADDROW([[1,2],[3,4]],{5,6},2)` | *error* | [emulator](../results.tsv) |
| `ADDROW([[1,2],[3,4]],[[5,6]],3)` | *error* | [emulator](../results.tsv) |
| `M1 := [[1,2],[3,4]]; ADDROW(M1,{5,6},3); RETURN M1;` | *error* | [emulator](../results.tsv) |

## Behaviour

**Four forms were tried and all four are refused** (emulator): the row as a
list at position 3, the same at position 2, the row as a one-row matrix
`[[5,6]]`, and the command applied to a matrix held in the variable `M1`.
[ADDCOL](ADDCOL.md) refuses the matching shapes, so the reading of HP's syntax
behind them is wrong at the root rather than in the position argument.

**The variable was the candidate that looked most likely, and it failed**
(emulator). Several matrix commands on this calculator change a variable
rather than answering a copy, which would have explained a refusal on a
literal; it does not, because `M1` is refused as well.

What form does work is not established (unverified). What is still untried is
the same short list as for columns: a vector rather than a list or a matrix,
and a position inside the matrix rather than one past the end.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ADDCOL](ADDCOL.md) · [DELROW](DELROW.md) · [REPLACE](REPLACE.md)
