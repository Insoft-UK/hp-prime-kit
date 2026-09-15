# FISHER_CDF

The probability that an F value is at or below a point.

| | |
|---|---|
| Syntax | `FISHER_CDF(n, d, x, [x2])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `FISHER_CDF(2,3,1)` | `0.535241998455` | [emulator](../results.tsv) |

## Behaviour

`FISHER_CDF(2,3,1)` answers 0.535241998455 (emulator): a little over half the
distribution lies at or below 1 with two and three degrees of freedom.

**It agrees with its own inverse, measured in the same batch.**
[FISHER_ICDF](FISHER_ICDF.md) of 0.5 is 0.881101577954, which is below 1 --
as it must be if 1 has already passed half the distribution (emulator). The
two rows check each other.

Like [FISHER](FISHER.md) it takes both degrees of freedom, numerator first,
before the point (HP help). Three arguments before the optional one is what
sets this family apart from the rest of the group.

One minus this answer is the p-value of an F test (unverified: that is what
the quantity is for, not something this row measures).

HP's syntax allows a second point (HP help), which was not run (unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[FISHER](FISHER.md) · [FISHER_ICDF](FISHER_ICDF.md) ·
[CHISQUARE_CDF](CHISQUARE_CDF.md)
