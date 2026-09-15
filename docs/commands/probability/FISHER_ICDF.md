# FISHER_ICDF

The point an F distribution reaches a probability at.

| | |
|---|---|
| Syntax | `FISHER_ICDF(n, d, p)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `FISHER_ICDF(2,3,0.5)` | `0.881101577954` | [emulator](../results.tsv) |

## Behaviour

`FISHER_ICDF(2,3,0.5)` answers 0.881101577954 (emulator): the median of the
F distribution with two and three degrees of freedom.

**The median is below 1**, which is worth noticing because an F statistic is
a ratio of variances and 1 is the value that means "no difference". So more
than half of this distribution sits below the point a test is asking about
(emulator).

It agrees with [FISHER_CDF](FISHER_CDF.md), measured in the same batch: that
answers 0.535 at the point 1, just over a half, and this answers a point just
under 1 for exactly a half (emulator).

The two degrees of freedom come first, numerator before denominator, then the
probability (HP help) -- the same order [FISHER](FISHER.md) takes, with a
probability where that one takes a point.

This is the command a program uses to find a critical value for an F test
(unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[FISHER](FISHER.md) · [FISHER_CDF](FISHER_CDF.md) ·
[CHISQUARE_ICDF](CHISQUARE_ICDF.md)
