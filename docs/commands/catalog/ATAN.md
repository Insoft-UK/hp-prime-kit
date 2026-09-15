# ATAN

The inverse tangent.

| | |
|---|---|
| Syntax | `ATAN(Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ATAN(1)` | `0.785398163397` | [emulator](../results.tsv) |

## Behaviour

`ATAN(1)` answers a quarter of pi (emulator): the angle whose tangent is one,
in radians.

**Three inverse functions measured in one batch all answer in radians**, and
they agree with the home setting read beside them: this is a quarter of pi,
[ASIN](ASIN.md) a sixth and [ACOS](ACOS.md) a third (emulator). The mode
itself is recorded once, in
[ACOT](../trigonometry/ACOT.md), where `HAngle` answered 0.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). That is worth setting
beside [PI](PI.md), which answers a decimal too rather than an exact symbol,
while [QPI](QPI.md) is the one that gives back an exact form.

HP's list files this under `catalog` rather than with the six reciprocal
functions in `trigonometry` (HP help), so a program looking for the ordinary
trigonometry finds it here and the secant family there.

What it answers in a different angle mode was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ACOS](ACOS.md) · [ASIN](ASIN.md) · [TAN](TAN.md)
