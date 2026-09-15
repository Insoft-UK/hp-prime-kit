# EIGENVAL

The eigenvalues of a square matrix.

| | |
|---|---|
| Syntax | `EIGENVAL(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EIGENVAL([[1,2],[3,4]])` | `[5.37228132327,-0.372281323269]` | [emulator](../results.tsv) |

## Behaviour

**The answer is a vector, not a list.** Its `TYPE` is 4, a matrix, and it is
written with single brackets (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). A program indexing it
should expect the matrix shape rather than the list one.

The two values add to 5, which is what [TRACE](TRACE.md) answers for the same
matrix (emulator). That is a cheap check a program can make on its own
arithmetic without trusting either command.

The larger of the two in size, 5.37228132327, is exactly what
[SPECRAD](SPECRAD.md) answers (emulator): the spectral radius is the largest
eigenvalue by magnitude, and here the two commands agree to every digit
brought back.

They are decimals rather than exact values, as [RREF](RREF.md) also answers
(emulator), so a program comparing an eigenvalue against zero needs a
tolerance.

What it does with a matrix whose eigenvalues are complex was not run
(unverified), and that is the interesting case, because the answer would then
carry the imaginary unit's own glyph,
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EIGENVV](EIGENVV.md) · [SPECRAD](SPECRAD.md) · [TRACE](TRACE.md)
