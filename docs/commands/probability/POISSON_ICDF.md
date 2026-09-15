# POISSON_ICDF

The count a Poisson distribution reaches a probability at.

| | |
|---|---|
| Syntax | `POISSON_ICDF(μ, p)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `POISSON_ICDF(2,0.5)` | `2` | [emulator](../results.tsv) |

## Behaviour

`POISSON_ICDF(2,0.5)` answers 2 (emulator): two events is where the
distribution reaches even odds when two are expected.

**It answers a whole number, because the distribution counts** (emulator),
the same as [BINOMIAL_ICDF](BINOMIAL_ICDF.md). Its type is still 0, an
ordinary real,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

It does not round-trip exactly with [POISSON_CDF](POISSON_CDF.md), and for the
same reason a counted distribution never does: the cumulative probability
steps, so the count this answers is the first whose total reaches the
probability asked for, not one whose total equals it (emulator), comparing
this row with `POISSON_CDF(2,3)`. The continuous family does round-trip
exactly, [NORMALD_ICDF](NORMALD_ICDF.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[POISSON](POISSON.md) · [POISSON_CDF](POISSON_CDF.md) ·
[BINOMIAL_ICDF](BINOMIAL_ICDF.md)
