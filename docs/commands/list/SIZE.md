# SIZE

How many elements a list has, or the dimensions of a matrix.

| | |
|---|---|
| Syntax | `SIZE(list)` → number |
| Syntax | `SIZE(matrix)` → the dimensions, rows then columns |
| Group | list |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SIZE({0,1,2,3})` | `4` | [emulator](../results.tsv) |
| `SIZE({1,2,3,4,5})` | `5` | [emulator](../results.tsv) |
| `SIZE([[1,2,3],[4,5,6]])` | `{2,3}` | [emulator](../results.tsv) |

## Behaviour

For a matrix it answers the dimensions, rows then columns, not the number of
elements (HP help). The pair is a list: the calculator shows `{2,3}`, and
`TYPE` of it is 6, which is what `TYPE` answers for a list (emulator). HP's
help calls it a list too and then prints it as a vector, `[2 3]`; what
disagrees is the printing, not the value.

The result cannot be indexed where it is produced: `SIZE(M)(1)` does not
compile. Assign it to a variable first, or use `DIM` (G2). The rule is
[ppl.index-call](../../topics/ppl.md#ppl.index-call).

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `SIZE(M)` for the number of elements of a matrix | it is the dimensions: `{2,3}` for a 2×3 matrix | the interpreter in this repository, written with an AI model, returned the element count until HP's examples caught it ([how](../../tools.md#run)) |

## Related

[ppl.index-call](../../topics/ppl.md#ppl.index-call)
