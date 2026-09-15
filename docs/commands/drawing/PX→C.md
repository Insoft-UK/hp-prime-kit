# PX→C

Turns a pixel position into the coordinates of the current view.

| | |
|---|---|
| Syntax | `PX→C(x, y)` → list |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `PX→C(0,0)` | `{-16,10.9}` | [emulator](../results.tsv) |
| `PX→C(100,50)` | `{-6,5.9}` | [emulator](../results.tsv) |
| `PX→C(10)` | `{-16,10.9}` | [emulator](../results.tsv) |
| `PX→C(100)` | `{-16,10.9}` | [emulator](../results.tsv) |

## Behaviour

**The top-left pixel is not the origin.** Pixel `(0,0)` is the point
`{-16,10.9}` of the default view (emulator): x starts negative because the
origin sits in the middle of the screen, and y starts positive because the
view counts upwards while pixels count down.

**A hundred pixels across is ten units, and fifty down is five.** From
`{-16,10.9}` to `{-6,5.9}` (emulator) is exactly that, so one unit is ten
pixels on both axes and the conversion is `x = (px - 160) / 10` and
`y = (109 - py) / 10` -- the inverse of what [C→PX](C→PX.md) measured, from
its own rows rather than from arithmetic on them.

It also puts a number on the screen in the view's units: 320 pixels across is
32 units, x running from -16 to 16 (emulator), which is where the -16 comes
from.

This is what explains the factor of ten between [GROBW](GROBW.md) and
[GROBW_P](GROBW_P.md) (emulator). Whether the factor follows a view the
program sets itself has not been measured (unverified).

With one argument it answers `{-16,10.9}` whatever the number is (emulator),
which is the answer for `(0,0)`: it takes a point, and the two single-argument
rows record a call that was asking the wrong question.

The negative comes back with the calculator's minus sign (emulator),
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[C→PX](C→PX.md) · [GROBW](GROBW.md) ·
[interface.geometry](../../topics/interface.md#interface.geometry)
