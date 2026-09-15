# geometric_cdf

The probability that the first success comes on try k or earlier.

| | |
|---|---|
| Syntax | `geometric_cdf(p, x, [x2])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `geometric_cdf(0.5,3)` | `0.875` | [emulator](../results.tsv) |

## Behaviour

`geometric_cdf(0.5,3)` answers 0.875 (emulator): seven chances in eight that
a fair coin has come up heads at least once in three tries.

**It includes the third try**, as the cumulative forms in this group do
(emulator). One minus 0.875 is 0.125, the chance of still failing after
three, which is the tail rather than the density at three -- those two happen
to be equal at p a half and are not in general,
[GEOMETRIC](GEOMETRIC.md).

**HP writes this name in lower case** and the inventory keeps it that way
(HP help), unlike the upper-case `GEOMETRIC` beside it. One distribution,
two spellings, and the linter cannot tell case apart -- a limitation it
already documents.

HP's syntax allows a second count (HP help), which was not run (unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GEOMETRIC](GEOMETRIC.md) · [geometric_icdf](geometric_icdf.md) ·
[BINOMIAL_CDF](BINOMIAL_CDF.md)
