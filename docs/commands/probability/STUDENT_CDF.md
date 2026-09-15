# STUDENT_CDF

The probability that a Student's t value is at or below a point.

| | |
|---|---|
| Syntax | `STUDENT_CDF(d, x, [x2])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `STUDENT_CDF(3,1)` | `0.804498890522` | [emulator](../results.tsv) |

## Behaviour

`STUDENT_CDF(3,1)` answers 0.804498890522 (emulator): about four fifths of
the distribution lies at or below t equal to one, with three degrees of
freedom.

That is less than the normal would give at the same point, which is the
heavier tail showing up in the cumulative rather than the density
(unverified: the normal was measured only at 0, so this comparison is
arithmetic on one side and reasoning on the other).

**It is the continuous kind of cumulative**, so it should invert exactly with
[STUDENT_ICDF](STUDENT_ICDF.md), the way [NORMALD_CDF](NORMALD_CDF.md) and
[NORMALD_ICDF](NORMALD_ICDF.md) were measured doing (unverified: the round
trip was measured for the normal and not for this one). The counted
distributions do not invert exactly, [BINOMIAL_ICDF](BINOMIAL_ICDF.md).

HP's syntax allows a second point for the probability between two values
(HP help), and that form was not run (unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STUDENT](STUDENT.md) · [STUDENT_ICDF](STUDENT_ICDF.md) ·
[NORMALD_CDF](NORMALD_CDF.md)
