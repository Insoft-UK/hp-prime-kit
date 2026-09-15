# ContribMat

A one-by-one zero matrix, and holds each cell’s contribution in a two-way table.

| | |
|---|---|
| Syntax | `ContribMat` → matrix |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ContribMat")` | `[[0]]` | [emulator](../results.tsv) |

## Behaviour

**It read `[[0]]`, not an empty matrix** (emulator), type 4. The lists of
this app come back as `{}` when they hold nothing; a matrix comes back as a
single zero cell instead. So a program cannot test the two the same way, and
a matrix of one zero is indistinguishable from a real one-by-one table
holding zero.

**It holds each cell’s contribution in a two-way table** (unverified). The app's loaded example is a two-sample
test on summary statistics, not a table, so nothing here was ever filled.

**Whether [DoInference](DoInference.md) writes it is untested** (unverified).
The one run measured watched four variables across it, and this was not one
of them.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ObsMat](ObsMat.md) · [ExpMat](ExpMat.md) · [ContribList](ContribList.md)
