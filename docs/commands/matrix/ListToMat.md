# ListToMat

Turns a list of lists into a matrix.

| | |
|---|---|
| Syntax | `ListToMat({{row}, {row}})` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ListToMat({{1,2},{3,4}})` | `[[1,2],[3,4]]` | [emulator](../results.tsv) |

## Behaviour

`ListToMat({{1,2},{3,4}})` answers the matrix with those rows (emulator): the
braces become brackets and each inner list becomes a row.

**HP's list gives this name no syntax string** (HP help), so the shape above
is what the measured call shows rather than something published. It was one
of the probes least likely to compile for that reason, and it compiled.

This is the bridge between the two kinds of container a program has
(emulator): lists, which [CONCAT](../list/CONCAT.md) and
[MAKELIST](../list/MAKELIST.md) build, and matrices, which the commands
in this group take. Data gathered as a list of rows becomes usable here
without a loop.

What it does with rows of different lengths was not run (unverified), and a
matrix cannot be ragged, so it must either refuse or pad.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MAKEMAT](MAKEMAT.md) · [MAKELIST](../list/MAKELIST.md) ·
[CONCAT](../list/CONCAT.md)
