# ADDCOL

Inserts a column into a matrix.

| | |
|---|---|
| Syntax | `ADDCOL(matrix, list, col)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ADDCOL([[1,2],[3,4]],{5,6},3)` | *error* | [emulator](../results.tsv) |
| `ADDCOL([[1,2],[3,4]],{5,6},2)` | *error* | [emulator](../results.tsv) |
| `ADDCOL([[1,2],[3,4]],[[5],[6]],3)` | *error* | [emulator](../results.tsv) |
| `M1 := [[1,2],[3,4]]; ADDCOL(M1,{5,6},3); RETURN M1;` | *error* | [emulator](../results.tsv) |
| `ADDCOL({5,6},[[1,2],[3,4]],3)` | *error* | [emulator](../results.tsv) |

## Behaviour

**Five forms were tried and all five are refused** (emulator): the column as a
list at position 3, the same list at position 2, the column as a one-column
matrix `[[5],[6]]`, the command applied to a matrix held in the variable `M1`,
and the arguments in the other order with the list first.

**The most likely explanation was tested and is wrong.** This entry used to
say that a refusal on a literal would be explained if the command changed a
variable instead of answering a copy, the way several matrix commands here do.
Run on `M1`, it is refused too (emulator), so that is not it.

This entry is the record of those refusals, not a guide to the working form,
which nobody here knows (unverified). What is still untried: a vector `[5,6]`
rather than a list or a matrix, and a position of 1 rather than one past the
end.

[ADDROW](ADDROW.md) refuses the matching shapes, which is what says the
mistake is shared rather than specific to columns (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ADDROW](ADDROW.md) · [DELCOL](DELCOL.md) · [REPLACE](REPLACE.md)
