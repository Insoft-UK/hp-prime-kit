# COLNORM

The largest column sum of a matrix, taking absolute values.

| | |
|---|---|
| Syntax | `COLNORM(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `COLNORM([[1,2],[3,4]])` | `6` | [emulator](../results.tsv) |

## Behaviour

`COLNORM([[1,2],[3,4]])` answers 6 (emulator). The columns are 1 and 3,
summing to 4, and 2 and 4, summing to 6; the larger is the answer.

**It is a column sum, not a row sum**, and the matrix above is chosen so the
two differ: [ROWNORM](ROWNORM.md) answers 7 for the same matrix (emulator).
An example where they agreed would have documented nothing.

It answers a plain number (emulator), and it is one of several norms the
calculator offers: [SPECNORM](SPECNORM.md) answers 5.46498570422 for this
matrix and [ABS](ABS.md) answers 5.47722557505, so the word "norm" alone does
not say which number you get.

Whether the absolute value is taken before summing was not measured, because
every element here is positive (unverified). The probe is a matrix with a
negative element.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ROWNORM](ROWNORM.md) · [SPECNORM](SPECNORM.md) · [ABS](ABS.md)
