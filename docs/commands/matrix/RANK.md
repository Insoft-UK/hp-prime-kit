# RANK

How many independent rows a matrix has.

| | |
|---|---|
| Syntax | `RANK(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `RANK([[1,2],[3,4]])` | `2` | [emulator](../results.tsv) |

## Behaviour

`RANK([[1,2],[3,4]])` answers 2 (emulator): both rows are independent, so the
rank is the full size of the matrix.

A rank below the number of rows is what says a system of equations
has no single solution, and it is the same thing a determinant of zero
says for a square matrix (unverified): this pairing was not measured
here, and [DET](DET.md) records that the zero case is unrun.

It answers a plain number (emulator). What it answers for a matrix of all
zeros, where the rank is 0, was not run (unverified).

For the reduced form that shows the independence directly, see
[RREF](RREF.md), which was measured on the same matrix shape (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DET](DET.md) · [RREF](RREF.md) · [TRACE](TRACE.md)
