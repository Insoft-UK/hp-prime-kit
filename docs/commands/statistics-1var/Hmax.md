# Hmax

A setting of the Statistics 1Var app, 24 on a reset calculator, which a program can set.

| | |
|---|---|
| Syntax | `Statistics_1Var.Hmax` → real |
| Syntax | `Statistics_1Var.Hmax:=value` |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Statistics_1Var.Hmax")` | `24` | [emulator](../results.tsv) |
| `EXPR("Hmax")` | *error* | [emulator](../results.tsv) |
| `EXPR("Statistics_1Var.D1:={1,2,2,3,7}"); EXPR("Statistics_1Var.Do1VStats(Statistics_1Var.H1)"); RETURN EXPR("Statistics_1Var.Hmax");` | `24` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Statistics_1Var.Hmax"); IFERR EXPR("Statistics_1Var.Hmax:=20"); r := EXPR("Statistics_1Var.Hmax"); THEN r := "refused"; END; IFERR EXPR("Statistics_1Var.Hmax:=" + STRING(o)); THEN r := r; END; RETURN r;` | `20` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name
and its app, and nothing more.

**A program reaches it with its app's name in front** (emulator):
`Statistics_1Var.Hmax` answered `24` with the Function app active, where
`Hmax` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**[Do1VStats](Do1VStats.md) does not change it** (emulator): it read 24 before
the command ran on `{1,2,2,3,7}` and 24 after.

**A program can set it** (emulator): set to 20 through `Statistics_1Var.Hmax`,
it read back 20. The row reads the first value, sets another, reads again and
puts the first one back.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Hmin](Hmin.md) · [Hwidth](Hwidth.md) · [Do1VStats](Do1VStats.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
