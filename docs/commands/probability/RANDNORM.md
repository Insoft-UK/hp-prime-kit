# RANDNORM

A random number from a normal distribution.

| | |
|---|---|
| Syntax | `RANDNORM([μ], [σ])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TYPE(RANDNORM(0,1))` | `0` | [emulator](../results.tsv) |

## Behaviour

It answers a real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), and the example asks
for the type because the value differs every run, as it does for
[RANDOM](RANDOM.md).

The two arguments are the mean and the standard deviation, written μ and σ in
HP's own syntax (HP help). They are the same pair [NORMALD](NORMALD.md) takes
before its x, so the family is consistent about their order.

**Whether they are optional here was not measured** (unverified). HP's syntax
puts both in brackets, and the measured call gave both. `NORMALD` was probed
in each of its forms and takes them either way (emulator), which is a reason
to expect the same rather than a reading of it.

Seeding with [RANDSEED](RANDSEED.md) makes a run repeat, measured for
[RANDOM](RANDOM.md) and expected here (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RANDOM](RANDOM.md) · [NORMALD](NORMALD.md) · [RANDSEED](RANDSEED.md)
