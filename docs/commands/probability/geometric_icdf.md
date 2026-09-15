# geometric_icdf

The try a geometric distribution reaches a probability at.

| | |
|---|---|
| Syntax | `geometric_icdf(p, q)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `geometric_icdf(0.5,0.5)` | `1` | [emulator](../results.tsv) |

## Behaviour

`geometric_icdf(0.5,0.5)` answers 1 (emulator): with a fair coin, one try
already carries an even chance of having succeeded.

**HP's list gives this name no syntax string** (HP help), so the shape above
is what the measured call shows. It was held back into a small batch of its
own for that reason, along with [!](!.md), and both compiled.

The answer is a whole number, because the distribution counts tries
(emulator), the same as [BINOMIAL_ICDF](BINOMIAL_ICDF.md) and
[POISSON_ICDF](POISSON_ICDF.md). Its type is still 0, an ordinary real,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

Like the other counted inverses it does not round-trip exactly with its
cumulative: [geometric_cdf](geometric_cdf.md) of 1 is 0.5 here, which happens
to match, but that is p being a half rather than a property of the pair
(unverified).

It is written in lower case as its cumulative is, while
[GEOMETRIC](GEOMETRIC.md) is upper case (HP help).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GEOMETRIC](GEOMETRIC.md) · [geometric_cdf](geometric_cdf.md) ·
[POISSON_ICDF](POISSON_ICDF.md)
