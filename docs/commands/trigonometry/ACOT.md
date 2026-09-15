# ACOT

The inverse cotangent.

| | |
|---|---|
| Syntax | `ACOT(value)` |
| Group | trigonometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ACOT(1)` | `0.785398163397` | [emulator](../results.tsv) |

## Behaviour

`ACOT(1)` answers 0.785398163397 (emulator), which is a quarter of pi: the
angle whose cotangent is 1, in radians.

**The angle mode was read back in the same batch, and it is 0** (emulator).
The home setting `HAngle` answered 0 while these calls answered radians, so 0
is the radian mode. Three rows say it together: this one is pi over four,
[ASEC](ASEC.md) is pi over three and [ACSC](ACSC.md) is pi over six.

That closes a question three entries had left open. [ARC](../drawing/ARC.md)
and [ARG](../arithmetic/ARG.md) both recorded an answer that looked like
radians while saying plainly that nobody had read the mode; now somebody has,
on this calculator, in this state (emulator). What a different `HAngle` does
to these answers is still unmeasured (unverified), and that is the remaining
half: the probe sets the mode and repeats one call.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[COT](COT.md) · [ASEC](ASEC.md) · [ACSC](ACSC.md)
