# ACOS

The inverse cosine.

| | |
|---|---|
| Syntax | `ACOS(Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ACOS(0.5)` | `1.0471975512` | [emulator](../results.tsv) |

## Behaviour

`ACOS(0.5)` answers a third of pi (emulator): the angle whose cosine is a
half, in radians. The mode is recorded once, in
[ACOT](../trigonometry/ACOT.md).

**It takes only values between -1 and 1**, because a cosine never leaves that
range. A probe outside it would have measured an error rather than a value,
and it was not run (unverified). That is the guard a program feeding it
computed data needs, and [ASIN](ASIN.md) needs the same one while
[ATAN](ATAN.md) needs none.

The answer and [ASIN](ASIN.md)'s add to half of pi for the same argument
(emulator, and the arithmetic between the two rows), which is the relation
between the two and a cheap check on both.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ASIN](ASIN.md) · [ATAN](ATAN.md) · [COS](COS.md)
