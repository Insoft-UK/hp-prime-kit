# MAKEMAT

Builds a matrix of a given shape from an expression.

| | |
|---|---|
| Syntax | `MAKEMAT(Expr, Rows, Columns)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MAKEMAT(1,2,3)` | `[[1,1,1],[1,1,1]]` | [emulator](../results.tsv) |

## Behaviour

`MAKEMAT(1,2,3)` answers two rows of three (emulator): **rows first, then
columns**, and the expression before both. Read carelessly, the call looks
like it might mean a matrix from 1 to 2 by 3.

Every element is the expression worked out, and with a constant that gives a
constant matrix (emulator). HP's syntax calls the first argument an
expression rather than a value, which suggests it may depend on the row and
column, the way [MAKELIST](../list/MAKELIST.md) depends on its variable
(HP help). What names those positions carry was not measured (unverified),
and that is the probe worth running next, because a matrix built from its own
indices is the useful case.

It answers `TYPE` 4 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

This is the matrix counterpart of [MAKELIST](../list/MAKELIST.md), which was
measured the same way and does take a named variable (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IDENMAT](IDENMAT.md) · [JordanBlock](JordanBlock.md) ·
[MAKELIST](../list/MAKELIST.md)
