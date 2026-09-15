# CHISQUARE_ICDF

The point a chi-squared distribution reaches a probability at.

| | |
|---|---|
| Syntax | `CHISQUARE_ICDF(d, p)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CHISQUARE_ICDF(3,0.5)` | `2.36597388438` | [emulator](../results.tsv) |

## Behaviour

`CHISQUARE_ICDF(3,0.5)` answers 2.36597388438 (emulator): the median of the
distribution with three degrees of freedom.

**The median is not the degrees of freedom**, though the two are close here
and a reader glancing at 3 and 2.37 might think one determines the other in
some simple way. It does not; the mean is 3 and the median is this number
(unverified: the mean was not measured, only stated by what the distribution
is).

It agrees with its own cumulative, measured in the same batch:
[CHISQUARE_CDF](CHISQUARE_CDF.md) of 2 is 0.4276, below a half, and this
answers a point above 2 (emulator).

Unlike the counted distributions, a continuous one should invert exactly with
its cumulative, as [NORMALD_ICDF](NORMALD_ICDF.md) was measured doing
(unverified: the round trip was not run for this distribution).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CHISQUARE](CHISQUARE.md) · [CHISQUARE_CDF](CHISQUARE_CDF.md) ·
[NORMALD_ICDF](NORMALD_ICDF.md)
