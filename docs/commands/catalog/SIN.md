# SIN

The sine.

| | |
|---|---|
| Syntax | `SIN(Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SIN(1)` | `0.841470984808` | [emulator](../results.tsv) |

## Behaviour

`SIN(1)` answers 0.841470984808 (emulator): the sine of one **radian**, not
of one degree, which would be about 0.0175. The mode is recorded once, in
[ACOT](../trigonometry/ACOT.md).

**That difference is the trap** (emulator). A program written against a
library that takes degrees gets a number rather than an error, and the number
is wrong by a factor no test catches unless it knows the expected value.

Its reciprocal is [CSC](../trigonometry/CSC.md), which HP files in a different
group (HP help), and its inverse is [ASIN](ASIN.md).

Squaring this and [COS](COS.md)'s answer and adding gives 1 (emulator, and the
arithmetic between the two rows), which is the identity a program can use to
check its own handling.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[COS](COS.md) · [TAN](TAN.md) · [ASIN](ASIN.md)
