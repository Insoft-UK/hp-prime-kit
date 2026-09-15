# CHISQUARE

The chi-squared density at a point.

| | |
|---|---|
| Syntax | `CHISQUARE(d, x)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CHISQUARE(3,2)` | `0.20755374871` | [emulator](../results.tsv) |

## Behaviour

`CHISQUARE(3,2)` answers 0.20755374871 (emulator): the density at 2 with
three degrees of freedom.

The degrees of freedom come first and the point second (HP help), the same
order [STUDENT](STUDENT.md) takes.

**Unlike Student's t it is not symmetric**, and lives only on the positive
side: there is no negative chi-squared value for the density to be measured
at (HP help). A program passing a negative point is asking something the
distribution has no answer for, and what the calculator does about that was
not run (unverified).

It follows the three-form pattern set out in [NORMALD](NORMALD.md):
[CHISQUARE_CDF](CHISQUARE_CDF.md) accumulates and
[CHISQUARE_ICDF](CHISQUARE_ICDF.md) goes back the other way (emulator).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CHISQUARE_CDF](CHISQUARE_CDF.md) · [CHISQUARE_ICDF](CHISQUARE_ICDF.md) ·
[STUDENT](STUDENT.md)
