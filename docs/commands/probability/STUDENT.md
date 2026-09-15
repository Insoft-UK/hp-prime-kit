# STUDENT

The Student's t density at a point.

| | |
|---|---|
| Syntax | `STUDENT(d, x)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `STUDENT(3,1)` | `0.206748335783` | [emulator](../results.tsv) |

## Behaviour

`STUDENT(3,1)` answers 0.206748335783 (emulator): the density at t equal to
one, with three degrees of freedom.

**The degrees of freedom come first and the point second** (HP help), the
same order [CHISQUARE](CHISQUARE.md) uses and one argument shorter than
[FISHER](FISHER.md), which needs two of them.

It is lower at 1 than the normal density is at the same distance from centre
-- [NORMALD](NORMALD.md) answers 0.398942280401 at its own peak -- which is
the heavier tail Student's t is chosen for (emulator, and the comparison
between those two rows).

It follows the three-form pattern set out in [NORMALD](NORMALD.md):
[STUDENT_CDF](STUDENT_CDF.md) accumulates and
[STUDENT_ICDF](STUDENT_ICDF.md) goes back the other way (emulator).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STUDENT_CDF](STUDENT_CDF.md) · [STUDENT_ICDF](STUDENT_ICDF.md) ·
[NORMALD](NORMALD.md)
