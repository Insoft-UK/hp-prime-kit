# LSolution

The Linear Solver's solution, computed as soon as LSystem is set; refused while LSystem is all zeros.

| | |
|---|---|
| Syntax | `Linear_Solver.LSolution` → list |
| Group | linear-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LSolution")` | *error* | [emulator](../results.tsv) |
| `EXPR("Linear_Solver.LSolution")` | *error* | [emulator](../results.tsv) |
| `EXPR("Linear_Solver.LSystem:=[[2,1,5],[1,-1,1]]"); RETURN EXPR("Linear_Solver.LSolution");` | `{2,1}` | [emulator](../results.tsv) |
| `LOCAL o, r; EXPR("Linear_Solver.LSystem:=[[2,1,5],[1,-1,1]]"); o := EXPR("Linear_Solver.LSolution"); IFERR EXPR("Linear_Solver.LSolution:={5,6}"); r := EXPR("Linear_Solver.LSolution"); THEN r := "refused"; END; IFERR EXPR("Linear_Solver.LSolution:=" + STRING(o)); THEN r := r; END; RETURN r;` | `"refused"` | [emulator](../results.tsv) |

## Behaviour

**A program reaches it with its app's name in front, once there is a system**
(emulator): with the Function app active, `Linear_Solver.LSolution` was
refused on a reset calculator and answered `{2,1}` once [LSystem](LSystem.md)
held `[[2,1,5],[1,-1,1]]`; `LSolution` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**Refused while the system is all zeros** (emulator), as a reset leaves it,
rather than answering an empty list. A program reading it should catch the
error. A system with no solution, or with many, was not tried (unverified).

**Nothing has to run for it to be computed** (emulator): the row that answered
set [LSystem](LSystem.md) and read this, with no command between. It agrees
with [LinSolve](LinSolve.md) on the same matrix.

**A program cannot set it** (emulator): assigning `{5,6}` was refused, in a
call whose read of it had answered just before.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LSystem](LSystem.md) · [LinSolve](LinSolve.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
