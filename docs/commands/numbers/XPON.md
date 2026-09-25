# XPON

The power of ten a value carries.

| | |
|---|---|
| Syntax | `XPON(value)` |
| Group | numbers |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `XPON(123.45)` | `2` | [emulator](../results.tsv) |
| `EXPR("xpon(1000)")` | `3` | [emulator](../results.tsv) |

## Behaviour

`XPON(123.45)` answers 2 (emulator): the exponent that goes with the mantissa
[MANT](MANT.md) gives, so that 1.2345 times ten squared is the value again.

**It is not the number of digits.** 123.45 has three digits before the point
and the answer is 2, one less, because the mantissa keeps one of them
(emulator). A program counting columns for a display has to add one.

**Written in lower case it still answers** (emulator): `xpon(1000)` gave 3
through `EXPR`,
[ppl.names-ignore-case](../../topics/ppl.md#ppl.names-ignore-case).

What it answers for a value below 1, where the exponent is negative, was not
run (unverified), and neither was zero.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MANT](MANT.md) · [TRUNCATE](TRUNCATE.md)
