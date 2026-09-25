# Alpha

The significance level: refused bare with the wrong app, set and kept with its own.

| | |
|---|---|
| Syntax | `Alpha` → real |
| Syntax | `Alpha:=real` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Alpha")` | *error* | [emulator](../results.tsv) |
| `EXPR("Alpha:=0.05")` | *error* | [emulator](../results.tsv) |
| `EXPR(" Alpha")` | `0.05` | [emulator](../results.tsv) |
| `EXPR("Alpha:=0.01")` | `0.01` | [emulator](../results.tsv) |
| `EXPR("(Alpha)")` | `0.01` | [emulator](../results.tsv) |
| `EXPR("Inference.Alpha")` | `0.05` | [emulator](../results.tsv) |

## Behaviour

**The first five rows are one name under two conditions** (emulator). With the
Function app active, which is what a reset calculator has,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active),
both reading and assigning were refused. With the Inference app selected by
hand, the read answered 0.05, the assignment answered 0.01, and a later read
answered 0.01. Nothing about the name changed between the two batches.

**A program can set it and the value stays** (emulator). That is the second
app in which this has been measured, after
[SideA](../triangle-solver/SideA.md), and the first in which what is written
is a setting rather than a measurement.

**With its app's name in front it answers from another app** (emulator):
the last row, `Inference.Alpha`, read 0.05 with the Function app active,
where `Alpha` alone was refused, [apps.qualified-names](../../topics/apps.md#apps.qualified-names).

**It was 0.05 before anything touched it** (emulator). The Inference app
ships with a worked example loaded, so a program reading this before writing
it gets a default rather than a blank.

**It does not agree with [Conf](Conf.md), and that is not a mistake**
(emulator). This arrived at 0.05 and `Conf` at 0.99, where a significance
level of 0.05 pairs with a confidence of 0.95. The likely reading is that the
two belong to different kinds of inference, one to hypothesis tests and one
to confidence intervals, and the app keeps a setting for each. Likely is not
measured (unverified).

**Its name collides with `ALPHA` by case alone** (HP help), and the two live
in different folders, this one in `inference` and the command in `catalog`.
So neither file needs the `-var` suffix that
[Root](../function/Root-var.md) carries: the folder already separates them.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Conf](Conf.md) · [AltHyp](AltHyp.md) · [Prob](Prob.md)
