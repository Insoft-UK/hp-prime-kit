# RANDINT

A random whole number.

| | |
|---|---|
| Syntax | `RANDINT([a], [b], [c])` |
| Group | probability |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TYPE(RANDINT(1,6))` | `0` | [emulator](../results.tsv) |

## Behaviour

**It answers a real, not an integer.** The type is 0 and not 1 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), even though the value
is whole. A program branching on `TYPE` to tell a whole number from a
fractional one will not learn anything here.

The example asks for the type rather than the value, because a random number
cannot be an example: it differs every run, and the reasoning is the same one
[RANDOM](RANDOM.md) carries (emulator).

Two arguments read as bounds, and `RANDINT(1,6)` is the way to roll a die
(unverified: the call was made and its type read, but no row checked that the
answers fall between 1 and 6, nor whether both ends are included).

Seeding with [RANDSEED](RANDSEED.md) makes a run repeat, which is measured
for [RANDOM](RANDOM.md) and expected here (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RANDOM](RANDOM.md) · [RANDSEED](RANDSEED.md) · [RANDNORM](RANDNORM.md)
