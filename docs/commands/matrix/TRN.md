# TRN

The transpose of a matrix: rows become columns.

| | |
|---|---|
| Syntax | `TRN(matrix)` |
| Group | matrix |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TRN([[1,2],[3,4]])` | `[[1,3],[2,4]]` | [emulator](../results.tsv) |

## Behaviour

`TRN([[1,2],[3,4]])` answers `[[1,3],[2,4]]` (HP help), and the interpreter
answers the same: the element at row 1 column 2 moves to row 2 column 1.

**It is the plain transpose, not the conjugate transpose.** On several
calculators `TRN` negates the imaginary parts as well as moving them. This
one does not: `TRN([[1+2*i,3],[4,5]])` answers a matrix whose first element
is still `1+2*` and the imaginary unit, with the sign unchanged (emulator).
HP's documented example uses only whole numbers and could never have told
the two apart, which is why the probe was worth running.

A list of matrices answers one transpose per matrix (emulator):
`TRN({[[5,2],[1,3]],[[2,9],[7,8]]})` answers `{[[5,1],[2,3]],[[2,7],[9,8]]}`.
[DET](DET.md), [RREF](RREF.md) and [IDENMAT](IDENMAT.md) take the same form,
measured in the same batch (emulator).

A non-square matrix transposes to a different shape, which is the ordinary
use and was not run here (unverified).

## Related

[DET](DET.md) · [RREF](RREF.md) · [ABS](ABS.md) ·
[CONJ](../arithmetic/CONJ.md)
