# PI

The constant pi.

| | |
|---|---|
| Syntax | `PI` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `PI` | `3.14159265359` | [emulator](../results.tsv) |

## Behaviour

**It is a bare name, not a call.** `PI` on its own answers, with no
parentheses and no argument (emulator). HP's list gives it no syntax string
for that reason, the same as [MAXREAL](MAXREAL.md) and
[MINREAL](MINREAL.md).

**It answers a decimal, not a symbol.** The type is 0, an ordinary real
(emulator), [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). So a
calculation using `PI` is in floating point from that moment: nothing
downstream can recover the exact constant.

That is the difference from [QPI](QPI.md), which answers type 8 and keeps an
exact form (emulator). A program that wants pi to survive as a symbol has to
go through the exact side rather than through this name.

Twelve digits come back, which is what the calculator shows rather than what
it holds (unverified: nothing here measured its internal precision).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[QPI](QPI.md) · [MAXREAL](MAXREAL.md) · [ATAN](ATAN.md)
