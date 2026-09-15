# BINOMIAL_CDF

The probability of k successes or fewer in n tries.

| | |
|---|---|
| Syntax | `BINOMIAL_CDF(n, p, k, [k2])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `BINOMIAL_CDF(10,0.5,5)` | `0.623046875` | [emulator](../results.tsv) |

## Behaviour

`BINOMIAL_CDF(10,0.5,5)` answers 0.623046875 (emulator): the chance of five
heads or fewer in ten fair tosses.

**It includes k rather than stopping below it.** The bare
[BINOMIAL](BINOMIAL.md) answers 0.24609375 for exactly five, and adding that
to the chance of four or fewer is what gives this number (emulator, and the
arithmetic between the two rows). A program that wanted "fewer than five" has
to subtract the exact term itself.

More than half the distribution lies at or below five, which is what says the
count is inclusive: without the exact term the total would fall under 0.5
(emulator).

HP's syntax allows a second count (HP help), which would give the probability
of landing between two values. That form was not run (unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BINOMIAL](BINOMIAL.md) · [BINOMIAL_ICDF](BINOMIAL_ICDF.md)
