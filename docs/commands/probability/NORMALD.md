# NORMALD

The normal density at a point.

| | |
|---|---|
| Syntax | `NORMALD([μ, σ,] x)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `NORMALD(0)` | `0.398942280401` | [emulator](../results.tsv) |
| `NORMALD(1,2,3)` | `0.12098536226` | [emulator](../results.tsv) |

## Behaviour

**Both forms compile and both answer**, so the mean and the standard
deviation really are optional (emulator). With one argument the distribution
is the standard normal; with three, the first two are μ and σ and the last is
the point.

`NORMALD(0)` is 0.398942280401 (emulator), which is one over the square root
of two pi: the height of the standard normal at its peak. That is a value
worth recognising, because it is what says the call was read as the standard
form rather than as something else.

**Six distributions here share one naming pattern**, and this is the entry
that states it once (emulator): a bare name is the density, `_CDF` is the
probability of being at or below a point, and `_ICDF` goes back the other way
from a probability to a point. `NORMALD`, `POISSON`, `BINOMIAL`, `CHISQUARE`,
`FISHER` and `STUDENT` all come in those three, and `GEOMETRIC` in two.

The pair round-trips exactly: [NORMALD_CDF](NORMALD_CDF.md) of 0 is 0.5 and
[NORMALD_ICDF](NORMALD_ICDF.md) of 0.5 is 0 (emulator), which is the cheapest
check that a program has the right one of the three.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NORMALD_CDF](NORMALD_CDF.md) · [NORMALD_ICDF](NORMALD_ICDF.md) ·
[RANDNORM](RANDNORM.md)
