# COND

The condition number of a matrix.

| | |
|---|---|
| Syntax | `COND(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `COND([[1,2],[3,4]])` | `21` | [emulator](../results.tsv) |

## Behaviour

`COND([[1,2],[3,4]])` answers 21 (emulator), a whole number where most of the
matrix commands answer decimals.

**Which norm it uses is not settled by this row.** The condition number is a
ratio of norms, and this matrix has four different ones measured -- 6 from
[COLNORM](COLNORM.md), 7 from [ROWNORM](ROWNORM.md), 5.46498570422 from
[SPECNORM](SPECNORM.md) and 5.47722557505 from [ABS](ABS.md) (emulator). The
answer 21 is exactly 7 times 3, and the row norms of this matrix and of its
inverse are 7 and 3, which points at [ROWNORM](ROWNORM.md) (unverified: that
is arithmetic on one example, not a measurement of what the command does).

The probe that would settle it is `COND` of a matrix whose row and
column norms differ from each other in both the matrix and its
inverse (unverified).

A large condition number says a system is sensitive to small changes in its
input, which is the reason to ask for it at all (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SPECNORM](SPECNORM.md) · [ROWNORM](ROWNORM.md) · [RANK](RANK.md)
