# ALOG

Ten raised to the value: the antilogarithm.

| | |
|---|---|
| Syntax | `ALOG(value)` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ALOG(3)` | `1000` | [emulator](../results.tsv) |
| `EXPR("ALOG(2)")` | `100` | [emulator](../results.tsv) |
| `EXPR("alog(2)")` | `100` | [emulator](../results.tsv) |
| `EXPR("Alog(2)")` | `100` | [emulator](../results.tsv) |

## Behaviour

`ALOG(3)` is 1000 (emulator), so this is base ten and not base e. It undoes
what `LOG` does, in the same way `EXP` undoes `LN`.

The answer came back as a plain number, `TYPE` 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), so it is not held as an
exact power of ten that a later calculation could keep whole.

**The calculator read its name in any case** (emulator): `alog(2)` and
`Alog(2)` answered 100, as `ALOG(2)` did, through `EXPR`. That is
[ppl.names-ignore-case](../../topics/ppl.md#ppl.names-ignore-case).

What it does with a negative or a fractional argument was not run
(unverified), though a fraction is the ordinary use: `ALOG(0.5)` is the square
root of ten.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EXPM1](EXPM1.md) · [LNP1](LNP1.md) · [XPON](../numbers/XPON.md)
