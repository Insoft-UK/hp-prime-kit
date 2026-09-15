# POISSON_CDF

The probability of k events or fewer when μ are expected.

| | |
|---|---|
| Syntax | `POISSON_CDF(μ, k, [k2])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `POISSON_CDF(2,3)` | `0.857123460499` | [emulator](../results.tsv) |

## Behaviour

`POISSON_CDF(2,3)` answers 0.857123460499 (emulator): the chance of three
events or fewer when two are expected.

**The count is included, as it is for [BINOMIAL_CDF](BINOMIAL_CDF.md)**
(emulator). The bare [POISSON](POISSON.md) answers 0.180447044315 for exactly
three, and this total is large enough that it can only be the sum through
three rather than through two.

A program wanting "more than three" subtracts this from 1; there is no
command for the upper tail in this family (HP help).

HP's syntax allows a second count for the probability between two values
(HP help), and that form was not run (unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[POISSON](POISSON.md) · [POISSON_ICDF](POISSON_ICDF.md) ·
[BINOMIAL_CDF](BINOMIAL_CDF.md)
