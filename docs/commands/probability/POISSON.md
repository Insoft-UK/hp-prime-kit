# POISSON

The probability of exactly k events when μ are expected.

| | |
|---|---|
| Syntax | `POISSON(μ, k)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `POISSON(2,3)` | `0.180447044315` | [emulator](../results.tsv) |

## Behaviour

`POISSON(2,3)` answers 0.180447044315 (emulator): the chance of exactly three
events when two are expected on average.

**The expected count comes first and the actual count second** (HP help).
Swapping them gives a number rather than an error -- `POISSON(3,2)` is a
perfectly good question with a different answer -- so this is a pair worth
reading twice.

Unlike [BINOMIAL](BINOMIAL.md) there is no number of tries: a Poisson
distribution counts events with no ceiling, where a binomial one cannot
exceed n (HP help).

It follows the three-form pattern [NORMALD](NORMALD.md) sets out: this is the
density, [POISSON_CDF](POISSON_CDF.md) accumulates, and
[POISSON_ICDF](POISSON_ICDF.md) goes back the other way (emulator).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[POISSON_CDF](POISSON_CDF.md) · [POISSON_ICDF](POISSON_ICDF.md) ·
[BINOMIAL](BINOMIAL.md)
