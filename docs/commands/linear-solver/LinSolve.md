# LinSolve

Solves a linear system given as an augmented matrix.

| | |
|---|---|
| Syntax | `LinSolve(matrix)` |
| Group | linear-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LinSolve([[2,1,5],[1,-1,1]])")` | `{2,1}` | [emulator](../results.tsv) |
| `EXPR("LinSolve([[1,0,1],[0,1,2]],[x,y])")` | *error* | [emulator](../results.tsv) |
| `EXPR("LinSolve([[1,2],[3,4]])")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It answers the values of the unknowns, and they are right** (emulator). The
matrix stands for 2x plus y equals 5 and x less y equals 1; the answer `{2,1}`
satisfies both, a list of type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The last column is the right-hand side** (emulator). Two rows of three
numbers are read as two equations in two unknowns, which the plain square
matrix in the third row is not -- and that row is refused.

**It takes one argument and not two** (emulator). Adding a list of unknowns,
which several computer algebra systems want, is refused. The matrix alone
carries everything.

**The working row was measured with the Linear Solver app selected**
(emulator), and the refusals were not,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).
Two things differ between the first and third rows, the matrix and the app,
so this entry does not claim the third would work with the app active --
untested (unverified).

**It is the only name in its group that answers anything** (emulator).
[Solve2×2](Solve2×2.md) and [Solve3×3](Solve3×3.md) are refused in every form
tried, with and without the app.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Solve2×2](Solve2×2.md) · [Solve3×3](Solve3×3.md) ·
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
