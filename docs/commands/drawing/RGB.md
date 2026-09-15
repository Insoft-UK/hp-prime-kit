# RGB

A colour, from its red, green and blue parts.

| | |
|---|---|
| Syntax | `RGB(r, g, b)` → integer |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `RGB(255,0,0)` | `#FF0000h` | [emulator](../results.tsv) |
| `RGB(0,0,255)` | `#FFh` | [emulator](../results.tsv) |

## Behaviour

**The answer is a `#` integer, not an ordinary number**: its `TYPE` is 1
rather than 0 (emulator), which is the same kind
[SETBITS](../integer/SETBITS.md) answers with.

The three parts pack into one number as `0xRRGGBB`: red 255 is `#FF0000h`
and blue 255 is `#FFh`, which is `0x0000FF` with the leading zeros not shown
(emulator). So from Python, where colours are written as plain `0xRRGGBB`
integers, the two agree
([micropython.hpprime-module](../../topics/micropython.md#micropython.hpprime-module)).

Each part is measured only at 0 and 255. What a value above 255 does, and
whether there is a fourth argument for transparency, has not been measured
(unverified).

## Related

[TEXTOUT_P](TEXTOUT_P.md) · [GETPIX_P](GETPIX_P.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
