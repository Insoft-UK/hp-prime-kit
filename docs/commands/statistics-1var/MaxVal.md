# MaxVal

The largest data value of the Statistics 1Var data, which Do1VStats writes: 7 for {1,2,2,3,7}.

| | |
|---|---|
| Syntax | `Statistics_1Var.MaxVal` → real |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Statistics_1Var.MaxVal")` | `0` | [emulator](../results.tsv) |
| `EXPR("MaxVal")` | *error* | [emulator](../results.tsv) |
| `EXPR("Statistics_1Var.D1:={1,2,2,3,7}"); EXPR("Statistics_1Var.Do1VStats(Statistics_1Var.H1)"); RETURN EXPR("Statistics_1Var.MaxVal");` | `7` | [emulator](../results.tsv) |
| `LOCAL o, r; EXPR("Statistics_1Var.D1:={1,2,2,3,7}"); EXPR("Statistics_1Var.Do1VStats(Statistics_1Var.H1)"); o := EXPR("Statistics_1Var.MaxVal"); IFERR EXPR("Statistics_1Var.MaxVal:=99"); r := EXPR("Statistics_1Var.MaxVal"); THEN r := "refused"; END; IFERR EXPR("Statistics_1Var.MaxVal:=" + STRING(o)); THEN r := r; END; RETURN r;` | `"refused"` | [emulator](../results.tsv) |

## Behaviour

**A program reaches it with its app's name in front** (emulator):
`Statistics_1Var.MaxVal` answered `0` with the Function app active, where
`MaxVal` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**It reads 0 before there is data** (emulator), on a reset calculator, so a
program cannot tell a real 0 from no data by reading it. The Statistics 2Var
results refuse instead, as [MeanY](../statistics-2var/MeanY.md) does.

**It holds the largest value** (emulator): with the data `{1,2,2,3,7}` put in
`D1` and [Do1VStats](Do1VStats.md) run on `H1`, it answered 7.

**A program cannot set it** (emulator): assigning 99 was refused, in a call
whose read of it had answered just before. [Do1VStats](Do1VStats.md) writes
it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Do1VStats](Do1VStats.md) · [NbItem](NbItem.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
