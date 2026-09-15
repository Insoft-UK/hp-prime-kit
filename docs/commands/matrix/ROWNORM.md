# ROWNORM

The largest row sum of a matrix, taking absolute values.

| | |
|---|---|
| Syntax | `ROWNORM(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ROWNORM([[1,2],[3,4]])` | `7` | [emulator](../results.tsv) |

## Behaviour

`ROWNORM([[1,2],[3,4]])` answers 7 (emulator): the rows sum to 3 and to 7,
and the larger is the answer.

**The same matrix answers 6 through [COLNORM](COLNORM.md)** (emulator), which
is the whole reason to measure both on one shape rather than on a symmetric
one. A program that reaches for "the norm" without saying which gets a
different number depending on the name.

It answers a plain number (emulator). Whether absolute values are taken before
summing was not measured, since every element here is positive (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[COLNORM](COLNORM.md) · [SPECNORM](SPECNORM.md) · [ABS](ABS.md)
