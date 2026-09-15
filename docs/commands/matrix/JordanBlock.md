# JordanBlock

A square matrix with one value on the diagonal and ones just above it.

| | |
|---|---|
| Syntax | `JordanBlock(Expr, n)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `JordanBlock(2,3)` | `[[2,1,0],[0,2,1],[0,0,2]]` | [emulator](../results.tsv) |

## Behaviour

`JordanBlock(2,3)` answers a three by three matrix with 2 down the diagonal
and 1 on the diagonal immediately above it (emulator). The value comes first
and the size second, which is the opposite order from the one the name
suggests to a reader expecting a size first.

**The ones are above the diagonal, not below.** That is what makes it an
upper Jordan block, and a program comparing against a lower one built by hand
will find every off-diagonal element in the wrong place (emulator).

It answers `TYPE` 4, a matrix (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

Unlike [IDENMAT](IDENMAT.md), which also builds a matrix from a size, this one
takes a value as well, so the two are not interchangeable even though
`JordanBlock(1,n)` and `IDENMAT(n)` differ only in the superdiagonal
(unverified: that comparison was not run).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IDENMAT](IDENMAT.md) · [MAKEMAT](MAKEMAT.md) · [SCHUR](SCHUR.md)
