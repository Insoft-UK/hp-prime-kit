# REDIM

The matrix resized to the dimensions you give.

| | |
|---|---|
| Syntax | `REDIM(matrix, {rows, columns})` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `REDIM([[1,2],[3,4]],{1,2})` | `[[1,2]]` | [emulator](../results.tsv) |

## Behaviour

The new size is a list, rows first (emulator). Making a matrix smaller keeps
the elements that still fit, counting from the top left: a 2×2 cut to 1×2
keeps the first row and drops the second, rather than keeping the last
(emulator).

What growing a matrix puts in the new places has not been measured
(unverified); zeros are the obvious guess and a guess is not a measurement.
Neither has what a size of `{0,0}` or a negative one does.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DELROW](DELROW.md) · [DELCOL](DELCOL.md) · [SUB](SUB.md) ·
[DIM](../strings/DIM.md)
