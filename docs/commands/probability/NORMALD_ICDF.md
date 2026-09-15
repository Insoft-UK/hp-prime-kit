# NORMALD_ICDF

The point a normal distribution reaches a given probability at.

| | |
|---|---|
| Syntax | `NORMALD_ICDF([μ, σ,] p)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `NORMALD_ICDF(0.5)` | `0` | [emulator](../results.tsv) |

## Behaviour

`NORMALD_ICDF(0.5)` answers 0 (emulator): the point below which half the
standard normal lies is its mean.

**It goes the opposite way from [NORMALD_CDF](NORMALD_CDF.md)**, taking a
probability and answering a point where that one takes a point and answers a
probability (emulator). Reaching for the wrong one gives a plausible number
rather than an error, which is why the two entries state the direction
plainly.

The two were measured round-tripping on the same pair of values (emulator),
so the naming can be trusted in at least that one case.

It takes μ and σ before the probability, both optional (emulator), measured on
[NORMALD](NORMALD.md), whose syntax is the same.

What it answers for a probability of 0 or 1, where the point is infinite, was
not run (unverified) -- and the calculator does have a way to write infinity,
measured elsewhere in this phase.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NORMALD_CDF](NORMALD_CDF.md) · [NORMALD](NORMALD.md)
