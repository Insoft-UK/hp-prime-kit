# LNP1

The natural logarithm of one plus the value.

| | |
|---|---|
| Syntax | `LNP1(value)` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LNP1(0.5)` | `0.405465108108` | [emulator](../results.tsv) |

## Behaviour

`LNP1(0.5)` is 0.405465108108 (emulator), the natural logarithm of 1.5 rather
than of 0.5.

**The one is added for you, and that is the whole trap in the name**
(emulator). A program that writes `LNP1(x)` meaning `LN(x)` gets a wrong
answer rather than an error, which is the kind of mistake that survives a
test suite.

Like [EXPM1](EXPM1.md), it exists to keep precision for a small value, where
`1 + x` rounds to 1 and the logarithm of that is zero (unverified: the reason
is the same one those functions carry in other languages, and no probe here
has measured it on a Prime).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EXPM1](EXPM1.md) · [ALOG](ALOG.md)
