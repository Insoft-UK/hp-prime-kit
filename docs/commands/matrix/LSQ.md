# LSQ

The least-squares solution of a system of equations.

| | |
|---|---|
| Syntax | `LSQ(matrix1, matrix2)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LSQ([[1,2],[3,4]],[[1],[2]])` | `[[0],[0.5]]` | [emulator](../results.tsv) |

## Behaviour

`LSQ([[1,2],[3,4]],[[1],[2]])` answers `[[0],[0.5]]` (emulator), and that is
the exact solution rather than an approximation to one: multiplying the first
matrix by it gives back `[[1],[2]]`.

**"Least squares" only means something when there is no exact answer.** This
matrix is square and invertible, so the system has one solution and this
command finds it; the name matters for a system with more equations than
unknowns, which was not run here (unverified). That is the probe worth
having, because it is the case the command exists for.

**The right-hand side is a column, not a vector.** It is written `[[1],[2]]`
with double brackets, where [DOT](DOT.md) and [CROSS](CROSS.md) take single
ones (emulator). Passing `[1,2]` here is the mistake to expect.

The answer is a column too, `TYPE` 4 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

For a square system, [RREF](RREF.md) reaches the same answer by a different
route and shows the working (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RREF](RREF.md) · [RANK](RANK.md) · [COND](COND.md)
