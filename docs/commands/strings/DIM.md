# DIM

How long a string is, or the dimensions of a matrix.

| | |
|---|---|
| Syntax | `DIM(String)` → number |
| Syntax | `DIM(matrix)` → the dimensions, rows then columns |
| Group | strings |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIM("12345")` | `5` | [emulator](../results.tsv) |
| `DIM([[1,2],[4,5],[7,8]])` | `{3,2}` | [emulator](../results.tsv) |
| `DIM("abcdef")` | `6` | unverified |
| `DIM([[1,2,3],[4,5,6]])` | `{2,3}` | unverified |

## Behaviour

HP's help files it under strings, with the syntax `DIM(String)` (HP help). It
also answers the dimensions of a matrix, and that is the form worth reaching
for, because the result of a call cannot be indexed where it is produced:
`DIM(M)(1)` does not compile, so you assign it first (G2),
[ppl.index-call](../../topics/ppl.md#ppl.index-call).

[SIZE](../list/SIZE.md) answers the same pair for a matrix, `{2,3}`, measured
on the emulator. Which of the two to use is a matter of habit, not of
behaviour (emulator).

## Related

[SIZE](../list/SIZE.md) · [LEFT](LEFT.md) ·
[ppl.index-call](../../topics/ppl.md#ppl.index-call)
