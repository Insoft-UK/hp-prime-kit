# BINOMIAL_ICDF

The number of successes a binomial distribution reaches a probability at.

| | |
|---|---|
| Syntax | `BINOMIAL_ICDF(n, p, q)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BINOMIAL_ICDF(10,0.5,0.5)` | `5` | [emulator](../results.tsv) |

## Behaviour

`BINOMIAL_ICDF(10,0.5,0.5)` answers 5 (emulator): five heads is where ten
fair tosses reach even odds.

**The answer is a whole number because the distribution is counted, not
measured**, which makes this the one of the three forms whose result a program
can use as a count directly (emulator). Its type is still 0, an ordinary real
rather than an integer,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

It answers the opposite question from [BINOMIAL_CDF](BINOMIAL_CDF.md), which
takes a count and answers a probability (emulator). The two are not exact
inverses here: `BINOMIAL_CDF(10,0.5,5)` is 0.623046875 rather than the 0.5
that went in, because a counted distribution steps rather than sliding, and 5
is the first count whose cumulative probability reaches a half.

That is worth knowing before treating this pair the way
[NORMALD_ICDF](NORMALD_ICDF.md) and [NORMALD_CDF](NORMALD_CDF.md) round-trip,
which they do exactly (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BINOMIAL](BINOMIAL.md) · [BINOMIAL_CDF](BINOMIAL_CDF.md)
