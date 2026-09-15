# ACSC

The inverse cosecant.

| | |
|---|---|
| Syntax | `ACSC(value)` |
| Group | trigonometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ACSC(2)` | `0.523598775598` | [emulator](../results.tsv) |

## Behaviour

`ACSC(2)` answers 0.523598775598 (emulator), which is a sixth of pi: the
angle whose cosecant is 2, in radians.

**It is exactly half of what [ASEC](ASEC.md) answers for the same argument**
(emulator), and the two add to a quarter turn, which is the relation between
a secant and a cosecant of complementary angles. Two rows checking each other
is worth more than either alone.

The mode those radians come from is recorded once, in [ACOT](ACOT.md)
(emulator).

Like `ASEC` it takes 2 rather than a fraction, because a cosecant never falls
between -1 and 1 (unverified): the refusal below 1 was avoided rather than
measured, and the probe is `ACSC(0.5)`.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CSC](CSC.md) · [ASEC](ASEC.md) · [ACOT](ACOT.md)
