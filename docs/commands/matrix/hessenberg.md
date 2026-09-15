# hessenberg

The Hessenberg reduction of a matrix.

| | |
|---|---|
| Syntax | `hessenberg(Matrix_A)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `hessenberg([[1,2],[3,4]])` | `{[[1,0],[0,1]],[[1,2],[3,4]]}` | [emulator](../results.tsv) |

## Behaviour

It answers two matrices in a list (emulator): the transformation and the
reduced form.

**Both halves came back unchanged here, and that is the example's weakness.**
The transformation is the identity and the reduced form is the matrix that
was given. A two by two matrix is already in Hessenberg form, so nothing had
to be done, and this row shows the shape of the answer rather than the work
(emulator). The probe that would show the work is a three by three matrix,
and it was not run (unverified).

Answering a list of matrices is the shape [LU](LU.md), [LQ](LQ.md) and
[SCHUR](SCHUR.md) share (emulator), and [cholesky](cholesky.md) is the one
that does not.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SCHUR](SCHUR.md) · [LU](LU.md) · [cholesky](cholesky.md)
