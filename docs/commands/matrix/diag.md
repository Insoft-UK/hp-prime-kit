# diag

Takes the diagonal out of a matrix, or builds a matrix from a diagonal.

| | |
|---|---|
| Syntax | `diag(list) or diag(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `diag([[1,2],[3,4]])` | `[1,4]` | [emulator](../results.tsv) |
| `diag({1,2})` | `[[1,0],[0,2]]` | [emulator](../results.tsv) |

## Behaviour

**One name does both directions**, and which one it does depends on what it is
given (emulator). A matrix answers its diagonal as a vector; a list answers a
matrix with that list down the diagonal and zeros elsewhere.

The two are inverses of each other where the sizes line up (emulator),
and a program can use the pair to store a diagonal matrix compactly and
rebuild it.

**The two forms take different brackets.** `[[1,2],[3,4]]` is a matrix and
`{1,2}` is a list (emulator); passing `[1,2]`, a vector, was not run
(unverified), and it is the shape most likely to do something surprising
because it is neither of the two measured.

`diag({1,2})` and [IDENMAT](IDENMAT.md) build the same kind of object, and
`diag` of a list of ones would be the identity (unverified: not run).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IDENMAT](IDENMAT.md) · [TRACE](TRACE.md) · [MAKEMAT](MAKEMAT.md)
