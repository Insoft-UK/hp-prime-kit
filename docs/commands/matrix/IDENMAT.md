# IDENMAT

An identity matrix of the size given.

| | |
|---|---|
| Syntax | `IDENMAT(n)` |
| Group | matrix |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `IDENMAT(2)` | `[[1,0],[0,1]]` | [emulator](../results.tsv) |
| `IDENMAT({2,3})` | `{[[1,0],[0,1]],[[1,0,0],[0,1,0],[0,0,1]]}` | [emulator](../results.tsv) |

## Behaviour

`IDENMAT(2)` is the two by two identity (HP help), and the interpreter
answers the same.

**Given a list of sizes it answers a list of matrices**, one per size:
`IDENMAT({2,3})` gives the two by two and the three by three together
(HP help). That is the same list form [DET](DET.md), [RREF](RREF.md) and [TRN](TRN.md)
carry, all four measured together (emulator): these commands map over a list
rather than refusing it.

The interpreter does not cover the list form and stops on it (unverified:
the interpreter on the PC, not a calculator), so that row is the
calculator's word alone.

It takes a size and not a matrix, which makes it the odd one of the group:
everything else here is given a matrix to work on (HP help).

## Related

[DET](DET.md) · [RREF](RREF.md) · [TRN](TRN.md)
