# GEOMETRIC

The probability that the first success comes on try k.

| | |
|---|---|
| Syntax | `GEOMETRIC(p, x)` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `GEOMETRIC(0.5,3)` | `0.125` | [emulator](../results.tsv) |

## Behaviour

`GEOMETRIC(0.5,3)` answers 0.125 (emulator): a half for failing twice and
succeeding on the third try, which is one eighth.

**That says which of the two usual parameterisations this is.** Counting
tries until the first success gives an eighth here; counting failures before
it would give a quarter (emulator, and the arithmetic that separates them).
A program ported from a library using the other convention is off by one try.

**Two numbers coincide here and it is worth not reading a rule into it.** The
chance of exactly three is 0.125, and so is the chance of needing more than
three, which is why [geometric_cdf](geometric_cdf.md) answers 0.875. They
match only because p is a half (emulator, and arithmetic). With any other p
they differ.

The probability comes first and the count second (HP help), the opposite
order from [POISSON](POISSON.md), where the parameter is also first but reads
as a count. Two commands in one group ordering their arguments by different
logic is worth a second look before calling either.

This family has two forms rather than three: a density and a cumulative, with
the inverse written in lower case as
[geometric_icdf](geometric_icdf.md) (HP help).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[geometric_cdf](geometric_cdf.md) · [geometric_icdf](geometric_icdf.md) ·
[POISSON](POISSON.md)
