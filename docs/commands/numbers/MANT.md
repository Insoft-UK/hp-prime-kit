# MANT

The digits of a value, with the decimal point moved to the front.

| | |
|---|---|
| Syntax | `MANT(Value)` |
| Group | numbers |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `MANT(123.45)` | `1.2345` | [emulator](../results.tsv) |

## Behaviour

`MANT(123.45)` answers 1.2345 (emulator): the mantissa, a number at least 1
and below 10.

**With [XPON](XPON.md) it takes a number apart and puts it back.** `XPON`
answers 2 for the same value (emulator), and 1.2345 times ten squared is
123.45. That pair is how a program formats a number itself, or decides how
many digits it can show.

What it answers for a negative value, and for zero, was not run (unverified).
Zero is the interesting one, because it has no mantissa in the usual sense.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[XPON](XPON.md) · [TRUNCATE](TRUNCATE.md) · [ROUND](ROUND.md)
