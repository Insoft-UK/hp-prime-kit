# SCALEADD

Multiplies one row by a number and adds it to another row.

| | |
|---|---|
| Syntax | `SCALEADD(matrix, value, row1, row2)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SCALEADD([[1,2],[3,4]],2,1,2)` | `[[1,2],[5,8]]` | [emulator](../results.tsv) |

## Behaviour

The measured call doubles row 1 and adds it to row 2: `{3,4}` plus twice
`{1,2}` is `{5,8}`, and row 1 is left as it was (emulator). So the row that
changes is the **second** one named, and the value comes first, as it does in
[SCALE](SCALE.md).

This is the row operation of Gaussian elimination, which is why it exists
with that argument order (unverified: the reading is mine, and HP's help does
not say what it is for).

What an out-of-range row does has not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SCALE](SCALE.md) · [SWAPROW](SWAPROW.md)
