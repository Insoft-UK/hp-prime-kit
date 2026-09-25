# Do1VStats

Computes the one-variable statistics of an analysis and writes them into the app's variables; answers 1.

| | |
|---|---|
| Syntax | `Do1VStats(Hn)` |
| Syntax | `Statistics_1Var.Do1VStats(Statistics_1Var.Hn)` |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Do1VStats(H1)")` | *error* | [emulator](../results.tsv) |
| `EXPR("Statistics_1Var.D1:={1,2,2,3,7}")` | `{1,2,2,3,7}` | [emulator](../results.tsv) |
| `EXPR("Statistics_1Var.Do1VStats(Statistics_1Var.H1)")` | `1` | [emulator](../results.tsv) |

## Behaviour

**Bare it was refused because another app was active, not for want of data**
(emulator). The first row was taken with the Function app active,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active),
and this entry used to blame the empty data set. With the app's name in front,
under the same condition, it answered 1 once `D1` held data,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names).

**A program puts the data in with an assignment** (emulator):
`Statistics_1Var.D1:={1,2,2,3,7}` answered the list. On a reset calculator
`H1` takes its data from `D1`: that is what made the results below come out.

**It writes its results into the app, and answers only 1** (emulator): after
it ran on `{1,2,2,3,7}`, [NbItem](NbItem.md) read 5, [MeanX](MeanX.md) 3,
[MedVal](MedVal.md) 2, [Q₁](Q₁.md) 1.5 and [sX](sX.md) 2.34520787991, all of
which read 0 before. So a program collects the statistics from those
variables, not from what this returns, as with
[DoInference](../inference/DoInference.md).

**Bare, three of this group's names answer from another app and three do not**
(emulator): [CHECK](CHECK.md), [UNCHECK](UNCHECK.md) and [ISCHECK](ISCHECK.md)
answered with the Function app active; this one, [SetFreq](SetFreq.md) and
[SetSample](SetSample.md) were refused. The other two were not tried with the
app's name in front (unverified).

**Whether it answers with no data was not tried** (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NbItem](NbItem.md) · [MeanX](MeanX.md) · [SetFreq](SetFreq.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
