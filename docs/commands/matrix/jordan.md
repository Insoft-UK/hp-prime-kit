# jordan

The Jordan form of a matrix, with its change of basis.

| | |
|---|---|
| Syntax | `jordan(Matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `jordan([[1,2],[3,4]])` | `{[[2.74456264654,−8.74456264654],[6,6]],[[5.37228132327,0],[0,−0.372281323269]]}` | [emulator](../results.tsv) |

## Behaviour

**Two matrices in a list**: the change of basis and the Jordan form
itself (emulator).

The second is diagonal here, holding 5.37228132327 and -0.372281323269
(emulator) -- exactly the pair [EIGENVAL](EIGENVAL.md) answers for this
matrix. A Jordan form is diagonal when the eigenvalues are distinct, which
they are, so this example shows the easy case rather than the interesting one.

The interesting case is a repeated eigenvalue, where the form gains a 1 above
the diagonal the way [JordanBlock](JordanBlock.md) builds one, and it was not
run (unverified).

The values are decimals rather than exact (emulator), so nothing here is a
symbolic Jordan form.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[JordanBlock](JordanBlock.md) · [EIGENVAL](EIGENVAL.md) · [SCHUR](SCHUR.md)
