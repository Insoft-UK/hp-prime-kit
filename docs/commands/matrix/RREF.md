# RREF

The reduced row echelon form of a matrix.

| | |
|---|---|
| Syntax | `RREF(matrix)` |
| Group | matrix |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `RREF([[1,-2,1],[3,4,-1]])` | `[[1,0,0.2],[0,1,-0.4]]` | [emulator](../results.tsv) |

## Behaviour

`RREF([[1,-2,1],[3,4,-1]])` answers `[[1,0,0.2],[0,1,-0.4]]` (HP help), and
the interpreter answers the same.

**The answer is decimal, not exact.** 0.2 and -0.4 are a fifth and two
fifths, and they come back as decimals rather than as fractions (HP help). A
program solving a system this way gets floating point, with everything that
implies for comparing the result against zero.

This is how a system of equations is solved without inverting anything: the
last column holds the solution once the rest is reduced to the identity
(unverified: that is what the form is for, and no probe here has solved a
system with it end to end).

A list of matrices answers one reduced matrix per input (emulator):
`RREF({[[-2,2,1],[1,4,0]],[[1,3,1],[3,6,9]]})` answers
`{[[1,0,-0.4],[0,1,0.1]],[[1,0,7],[0,1,-2]]}`. The interpreter refuses that
form cleanly (unverified: this kit's interpreter on the PC, not a
calculator), which is why it is not in the table above.

## Related

[DET](DET.md) · [IDENMAT](IDENMAT.md) · [TRN](TRN.md)
