# DET

The determinant of a square matrix.

| | |
|---|---|
| Syntax | `DET(matrix)` |
| Group | matrix |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DET([[1,2],[3,4]])` | `-2` | [emulator](../results.tsv) |

## Behaviour

`DET([[1,2],[3,4]])` is -2 (HP help), and the interpreter answers the same,
so this row is checked on the PC as well as stated.

**A list of matrices answers a list of determinants.**
`DET({[[1,2],[5,6]],[[3,4],[-6,-2]]})` answers `{-4,18}` (emulator), one per
matrix. The interpreter refuses that form cleanly, saying it needs a matrix
(unverified: the interpreter on the PC, not a calculator), so the
example is not in the table above: a clean refusal against a stated value is
a problem for the checker rather than a note.

That list form is shared by [RREF](RREF.md), [TRN](TRN.md) and
[IDENMAT](IDENMAT.md), all four measured together, so it is a property of
these commands rather than of this one (emulator).

A determinant of zero is what says a matrix cannot be inverted, and whether
this answers exactly zero for a singular matrix, or something very small, was
not run (unverified).

## Related

[RREF](RREF.md) · [TRN](TRN.md) · [ABS](ABS.md)
