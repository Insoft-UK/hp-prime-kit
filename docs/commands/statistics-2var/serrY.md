# serrY

The standard error of the mean of the second column of the Statistics 2Var data, which Do2VStats writes: refused until the app has data.

| | |
|---|---|
| Syntax | `Statistics_2Var.serrY` → real |
| Group | statistics-2var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("serrY")` | *error* | [emulator](../results.tsv) |
| `EXPR("Statistics_2Var.serrY")` | *error* | [emulator](../results.tsv) |
| `EXPR("Statistics_2Var.C1:={1,2,3,4}"); EXPR("Statistics_2Var.C2:={2,3,5,9}"); EXPR("Statistics_2Var.Do2VStats(Statistics_2Var.S1)"); RETURN EXPR("Statistics_2Var.serrY");` | `1.54784796842` | [emulator](../results.tsv) |
| `LOCAL o, r; EXPR("Statistics_2Var.C1:={1,2,3,4}"); EXPR("Statistics_2Var.C2:={2,3,5,9}"); EXPR("Statistics_2Var.Do2VStats(Statistics_2Var.S1)"); o := EXPR("Statistics_2Var.serrY"); IFERR EXPR("Statistics_2Var.serrY:=99"); r := EXPR("Statistics_2Var.serrY"); THEN r := "refused"; END; IFERR EXPR("Statistics_2Var.serrY:=" + STRING(o)); THEN r := r; END; RETURN r;` | `"refused"` | [emulator](../results.tsv) |

## Behaviour

**A program reaches it with its app's name in front, once there is data**
(emulator): with the Function app active, `Statistics_2Var.serrY` was refused
on a reset calculator and answered 1.54784796842 once `C1` and `C2` held data
and [Do2VStats](Do2VStats.md) had run on `S1`; `serrY` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**Before there is data it is refused, not 0** (emulator), unlike the
Statistics 1Var results, which read 0, as [MeanX](../statistics-1var/MeanX.md)
does. A program reading it should catch the error.

**It holds the standard error of the mean of the second column** (emulator):
with `{1,2,3,4}` in `C1` and `{2,3,5,9}` in `C2`, and
[Do2VStats](Do2VStats.md) run on `S1`, it answered 1.54784796842, the sample
deviation, 3.09569593683, over the square root of the count, 4.

**A program cannot set it** (emulator): assigning 99 was refused, in a call
whose read of it had answered just before. [Do2VStats](Do2VStats.md) writes
it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Do2VStats](Do2VStats.md) · [Corr](Corr.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
