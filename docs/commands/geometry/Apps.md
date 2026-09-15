# Apps

Answers the calculator's list of apps, by name.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Apps")` | `{"Función","Solucionador","Var 1 estadística","Var 2 estadística","Inferencia","Paramétrica","Polar","Secuencia","Finanzas","Solucionador lineal","Solucionador  (cut at 160 characters)` | [emulator](../results.tsv) |

## Behaviour

**It answers a list of strings, one per app** (emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). That makes it the only
name in this group that reports on the calculator itself rather than on
geometry.

**The answer was cut at 160 characters** (emulator), the harness's width, so
what the Result cell holds is the first eleven or so names and the marker
that says it was truncated. The full list is longer than the row can carry.

**The names are in the calculator's language** (emulator). They arrive as
`Función`, `Solucionador`, `Var 1 estadística` and so on, because this
machine is Spanish, so a program matching them against English names will
match nothing. That is a stronger warning than it looks: the app names are
data a program might reasonably compare against.

**A program wanting one app should not search this list by name**
(emulator). What it should use instead is not established here (unverified),
and no other name in this documentation answers the same question.

HP's list files it under the Geometry commands with no syntax string
(HP help), which is at odds with what it answers.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Instruction](Instruction.md) · [DelInstruction](DelInstruction.md) ·
[zoomin](zoomin.md)
