# COS

The cosine.

| | |
|---|---|
| Syntax | `COS(Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `COS(1)` | `0.540302305868` | [emulator](../results.tsv) |

## Behaviour

`COS(1)` answers 0.540302305868 (emulator): the cosine of one radian. The
mode is recorded once, in [ACOT](../trigonometry/ACOT.md).

**That same number appeared elsewhere in this phase.**
[mkisom](../matrix/mkisom.md) answers a rotation matrix whose entries are the
cosine and sine of 1, and its first element is this value to every digit
(emulator). A command in another group built from these, which is what says
both readings are of the same function in the same mode.

Squaring this and [SIN](SIN.md)'s answer and adding gives 1 (emulator, and
the arithmetic between the two rows).

Its reciprocal is [SEC](../trigonometry/SEC.md) and its inverse is
[ACOS](ACOS.md) (HP help).

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SIN](SIN.md) · [TAN](TAN.md) · [ACOS](ACOS.md)
