# Ylist

The second data list, and the one that proved a list can be assigned.

| | |
|---|---|
| Syntax | `Ylist` → list |
| Syntax | `Ylist:=list` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Ylist")` | `{}` | [emulator](../results.tsv) |
| `EXPR(" Ylist")` | `{}` | [emulator](../results.tsv) |
| `EXPR("Ylist:={1,2,3}")` | `{1,2,3}` | [emulator](../results.tsv) |
| `EXPR("(Ylist)")` | `{1,2,3}` | [emulator](../results.tsv) |

## Behaviour

**A program can put a list in it and the list stays** (emulator): empty on
the first read, `{1,2,3}` after the assignment, `{1,2,3}` on a later read in
the same pass. Everything set from a program before this had been a single
number -- [SideA](../triangle-solver/SideA.md) and [Alpha](Alpha.md) -- so
this is the row that shows a whole data set can be handed to an app.

**That is the missing half of the app's working shape** (emulator). The
Triangle Solver took its inputs one number at a time and
[DoSolve](../triangle-solver/DoSolve.md) solved them; this app takes lists,
and [DoInference](DoInference.md) runs over what it holds.

**It also reads `{}` with the Function app active** (emulator), the second
row, like every list of this app, [Xlist](Xlist.md).

**It was empty before, while the app's summary statistics were not**
(emulator). The loaded example fills means and counts rather than lists, so a
program supplying its own data has to know which of the two the app is set to
use, and [InfType](InfType.md) is untested (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Xlist](Xlist.md) · [DoInference](DoInference.md) · [Yval](Yval.md)
