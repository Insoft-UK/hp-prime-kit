# MeanX

The mean of the Statistics 1Var data, which Do1VStats writes: 3 for {1,2,2,3,7}.

| | |
|---|---|
| Syntax | `Statistics_1Var.MeanX` → real |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Statistics_1Var.MeanX")` | `0` | [emulator](../results.tsv) |
| `EXPR("MeanX")` | *error* | [emulator](../results.tsv) |
| `EXPR("Statistics_1Var.D1:={1,2,2,3,7}"); EXPR("Statistics_1Var.Do1VStats(Statistics_1Var.H1)"); RETURN EXPR("Statistics_1Var.MeanX");` | `3` | [emulator](../results.tsv) |
| `EXPR("Statistics_2Var.C1:={1,2,3,4}"); EXPR("Statistics_2Var.C2:={2,3,5,9}"); EXPR("Statistics_2Var.Do2VStats(Statistics_2Var.S1)"); RETURN EXPR("Statistics_2Var.MeanX");` | `2.5` | [emulator](../results.tsv) |
| `LOCAL o, r; EXPR("Statistics_1Var.D1:={1,2,2,3,7}"); EXPR("Statistics_1Var.Do1VStats(Statistics_1Var.H1)"); o := EXPR("Statistics_1Var.MeanX"); IFERR EXPR("Statistics_1Var.MeanX:=99"); r := EXPR("Statistics_1Var.MeanX"); THEN r := "refused"; END; IFERR EXPR("Statistics_1Var.MeanX:=" + STRING(o)); THEN r := r; END; RETURN r;` | `"refused"` | [emulator](../results.tsv) |

## Behaviour

**A program reaches it with its app's name in front** (emulator):
`Statistics_1Var.MeanX` answered `0` with the Function app active, where
`MeanX` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**It reads 0 before there is data** (emulator), on a reset calculator, so a
program cannot tell a real 0 from no data by reading it. The Statistics 2Var
results refuse instead, as [MeanY](../statistics-2var/MeanY.md) does.

**It holds the mean** (emulator): with the data `{1,2,2,3,7}` put in `D1` and
[Do1VStats](Do1VStats.md) run on `H1`, it answered 3, which is not the median,
2.

**Read through Statistics 2Var it is that app's** (emulator): with `{1,2,3,4}`
and `{2,3,5,9}` in `C1` and `C2` and
[Do2VStats](../statistics-2var/Do2VStats.md) run on `S1`,
`Statistics_2Var.MeanX` answered 2.5, the mean of `C1`, in the batch where
`Statistics_1Var.MeanX` answered 3. So the app's name in front decides which
app's value is read. The other statistics of x were not read through
Statistics 2Var (unverified).

**A program cannot set it** (emulator): assigning 99 was refused, in a call
whose read of it had answered just before. [Do1VStats](Do1VStats.md) writes
it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Do1VStats](Do1VStats.md) · [NbItem](NbItem.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
