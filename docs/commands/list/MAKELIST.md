# MAKELIST

Builds a list by working an expression out over a range.

| | |
|---|---|
| Syntax | `MAKELIST(expression, variable, begin, end, [increment])` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MAKELIST(X^2,X,1,5)` | `{1,4,9,16,25}` | [emulator](../results.tsv) |

## Behaviour

**The expression is live PPL and the variable is named rather than passed.**
`MAKELIST(X^2,X,1,5)` answers `{1,4,9,16,25}` (emulator): `X` takes each value
from 1 to 5 and the expression is worked out for each one.

**Both ends are included.** From 1 to 5 gives five elements, not four
(emulator), which is the opposite of how a range behaves in most languages.

This is the way to build a list without a loop (unverified), and it is the
natural partner of [SORT](SORT.md) and [CONCAT](CONCAT.md) for putting data
together before drawing or storing it.

The fifth argument steps by something other than 1 (HP help) and has not been
run here (unverified). Nor has a decreasing range, where `begin` is above
`end`.

It shares its shape with [FNROOT](../arithmetic/FNROOT.md) (HP help), which
also takes an expression and the name of its variable.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CONCAT](CONCAT.md) · [SORT](SORT.md) · [FNROOT](../arithmetic/FNROOT.md)
