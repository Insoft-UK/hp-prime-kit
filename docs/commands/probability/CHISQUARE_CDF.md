# CHISQUARE_CDF

The probability that a chi-squared value is at or below a point.

| | |
|---|---|
| Syntax | `CHISQUARE_CDF(d, x, [x2])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CHISQUARE_CDF(3,2)` | `0.427593295529` | [emulator](../results.tsv) |

## Behaviour

`CHISQUARE_CDF(3,2)` answers 0.427593295529 (emulator): a little under half
the distribution lies at or below 2 with three degrees of freedom.

**That is consistent with its own inverse**, and the pair was measured in one
batch: [CHISQUARE_ICDF](CHISQUARE_ICDF.md) of 0.5 is 2.36597388438, which is
above 2, exactly as it must be if 2 has not yet reached half the distribution
(emulator). Two rows checking each other is worth more than either alone.

This is the cumulative a program uses for a goodness-of-fit test: the answer
is how much of the distribution falls below the statistic, and one minus it is
the p-value (unverified: that is what the quantity is for, not something these
rows measure).

HP's syntax allows a second point (HP help), which was not run (unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CHISQUARE](CHISQUARE.md) · [CHISQUARE_ICDF](CHISQUARE_ICDF.md) ·
[NORMALD_CDF](NORMALD_CDF.md)
