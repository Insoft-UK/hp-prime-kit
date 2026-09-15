# ASEC

The inverse secant.

| | |
|---|---|
| Syntax | `ASEC(value)` |
| Group | trigonometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ASEC(2)` | `1.0471975512` | [emulator](../results.tsv) |

## Behaviour

`ASEC(2)` answers 1.0471975512 (emulator), which is a third of pi: the angle
whose secant is 2, in radians.

The mode those radians come from was read in the same batch and is recorded
once, in [ACOT](ACOT.md) (emulator).

**The argument is 2 and not 1, because a secant is never between -1 and 1.**
[SEC](SEC.md) answers 1.85 at one radian and never anything smaller than 1 in
size, so its inverse has nothing to answer for a fraction, and a probe at 0.5
would have measured an error rather than a value (unverified: the refusal was
avoided rather than measured).

What it does inside that gap is therefore still open (unverified), and it is
the case a program feeding it computed data has to guard. The probe is
`ASEC(0.5)`.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SEC](SEC.md) · [ACSC](ACSC.md) · [ACOT](ACOT.md)
