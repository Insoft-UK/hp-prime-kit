# FISHER

The F density at a point.

| | |
|---|---|
| Syntax | `FISHER(n, d, x)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `FISHER(2,3,1)` | `0.278854800927` | [emulator](../results.tsv) |

## Behaviour

`FISHER(2,3,1)` answers 0.278854800927 (emulator): the density at 1 with two
and three degrees of freedom.

**It takes three arguments where the rest of this group takes two**, because
an F distribution has two degrees of freedom rather than one: a numerator and
a denominator, in that order, before the point (HP help). Passing them the
wrong way round gives a different distribution and a plausible number, not an
error.

That is the thing to check first when an F test disagrees with another tool:
which of the two counts each library puts first (unverified).

It follows the three-form pattern set out in [NORMALD](NORMALD.md):
[FISHER_CDF](FISHER_CDF.md) accumulates and
[FISHER_ICDF](FISHER_ICDF.md) goes back the other way (emulator).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[FISHER_CDF](FISHER_CDF.md) · [FISHER_ICDF](FISHER_ICDF.md) ·
[CHISQUARE](CHISQUARE.md)
