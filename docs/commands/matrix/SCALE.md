# SCALE

Multiplies one row of a matrix by a number.

| | |
|---|---|
| Syntax | `SCALE(matrix, value, row)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SCALE([[1,2],[3,4]],2,1)` | `[[2,4],[3,4]]` | [emulator](../results.tsv) |

## Behaviour

**The number comes before the row**, which is the opposite of what the name
suggests to most readers: `SCALE(M, 2, 1)` doubles row 1, it does not scale
row 2 by 1 (emulator). Getting that pair the wrong way round answers a
matrix rather than an error, so nothing warns you.

Rows are counted from 1 (G2),
[ppl.one-based](../../topics/ppl.md#ppl.one-based). What an out-of-range row
does has not been measured (unverified).

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `SCALE(M, row, factor)`, reading the arguments as position then value | the other row is scaled, by the position; no error, just wrong numbers | measured on the Virtual Calculator 2.4, build 2025-09-15 while writing this entry: `SCALE([[1,2],[3,4]],2,1)` answers `[[2,4],[3,4]]` ([results.tsv](../results.tsv)) |

## Related

[SCALEADD](SCALEADD.md) · [SWAPROW](SWAPROW.md) · [REPLACE](REPLACE.md)
