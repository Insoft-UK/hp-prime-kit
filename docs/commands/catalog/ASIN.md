# ASIN

The inverse sine.

| | |
|---|---|
| Syntax | `ASIN(Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ASIN(0.5)` | `0.523598775598` | [emulator](../results.tsv) |

## Behaviour

`ASIN(0.5)` answers a sixth of pi (emulator): the angle whose sine is a half,
in radians. The mode is recorded once, in
[ACOT](../trigonometry/ACOT.md).

**It is exactly half of what [ACOS](ACOS.md) answers for the same argument**
(emulator), and the two add to a quarter turn -- the relation between an
inverse sine and an inverse cosine. Two rows checking each other is worth more
than either alone.

Like `ACOS` it takes only values between -1 and 1, and what it does outside
that range was not run (unverified).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ACOS](ACOS.md) · [ATAN](ATAN.md) · [SIN](SIN.md)
