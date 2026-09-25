# Do2VStats

Computes the two-variable statistics of an analysis and writes them into the app's variables; answers 1.

| | |
|---|---|
| Syntax | `Do2VStats(Sn)` |
| Syntax | `Statistics_2Var.Do2VStats(Statistics_2Var.Sn)` |
| Group | statistics-2var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("S1:=[[1,2],[2,4],[3,6]]")` | *error* | [emulator](../results.tsv) |
| `EXPR("Do2VStats(S1)")` | *error* | [emulator](../results.tsv) |
| `EXPR("Statistics_2Var.C1:={1,2,3,4}")` | `{1,2,3,4}` | [emulator](../results.tsv) |
| `EXPR("Statistics_2Var.C2:={2,3,5,9}")` | `{2,3,5,9}` | [emulator](../results.tsv) |
| `EXPR("Statistics_2Var.Do2VStats(Statistics_2Var.S1)")` | `1` | [emulator](../results.tsv) |

## Behaviour

**Bare it was refused because another app was active** (emulator): the first
two rows were taken with the Function app active,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).
With the app's name in front, under the same condition, it answered 1 once the
columns held data,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names).

**The data goes in the columns** (emulator): `Statistics_2Var.C1:={1,2,3,4}`
and `Statistics_2Var.C2:={2,3,5,9}` answered their lists. The first row, a
matrix assigned to `S1`, was refused with the Function app active, as every
bare name of this app is, and this entry took it to mean the data could not be
filled. `S1` is the analysis the command takes; whether it can be assigned at
all was not tried (unverified).

**It writes its results into the app, and answers only 1** (emulator): after
it ran, [MeanY](MeanY.md) read 4.75, [Corr](Corr.md) 0.959166304663 and
[CoefDet](CoefDet.md) 0.92, all three refused before, and
`Statistics_2Var.MeanX` read 2.5.

**On a reset calculator `S1` pairs `C1` as x with `C2` as y** (emulator): the
means came out 2.5 and 4.75, those of the two columns in that order.

[Resid](Resid.md), [SetIndep](SetIndep.md) and [SetDepend](SetDepend.md) were
not tried with the app's name in front (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MeanY](MeanY.md) · [Corr](Corr.md) · [residue](residue.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
