# LSystem

The Linear Solver's system, one row per equation with its constant last; setting it solves it.

| | |
|---|---|
| Syntax | `Linear_Solver.LSystem` → matrix |
| Syntax | `Linear_Solver.LSystem:=matrix` |
| Group | linear-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LSystem")` | *error* | [emulator](../results.tsv) |
| `EXPR("Linear_Solver.LSystem")` | `[[0,0,0,0],[0,0,0,0],[0,0,0,0]]` | [emulator](../results.tsv) |
| `EXPR("Linear_Solver.LSystem:=[[2,1,5],[1,-1,1]]")` | `[[2,1,5],[1,−1,1]]` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Linear_Solver.LSystem"); IFERR EXPR("Linear_Solver.LSystem:=[[1,1,3],[1,-1,1]]"); r := EXPR("Linear_Solver.LSystem"); THEN r := "refused"; END; IFERR EXPR("Linear_Solver.LSystem:=" + STRING(o)); THEN r := r; END; RETURN r;` | `[[1,1,3],[1,−1,1]]` | [emulator](../results.tsv) |

## Behaviour

**A program reaches it with its app's name in front** (emulator):
`Linear_Solver.LSystem` answered `[[0,0,0,0],[0,0,0,0],[0,0,0,0]]`, three
equations in three unknowns, all 0, with the Function app active, where
`LSystem` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**Setting it solves it** (emulator): set to `[[2,1,5],[1,-1,1]]`, the system
2x+y=5 and x−y=1, it answered the matrix, and a read of
[LSolution](LSolution.md) straight after answered `{2,1}` with no command run
in between. That is the answer [LinSolve](LinSolve.md) gives for the same
matrix, which shows each row ending with its equation's constant.

**A program can set it** (emulator): set to `[[1,1,3],[1,−1,1]]` through
`Linear_Solver.LSystem`, it read back `[[1,1,3],[1,−1,1]]`. The row reads the
first value, sets another, reads again and puts the first one back. A system
of two equations replaced one of three.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LSolution](LSolution.md) · [LinSolve](LinSolve.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
