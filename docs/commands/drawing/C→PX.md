# C→PX

Turns a point of the current view into pixel coordinates.

| | |
|---|---|
| Syntax | `C→PX(x, y)` → list |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `C→PX(0,0)` | `{160,109}` | [emulator](../results.tsv) |
| `C→PX(1,1)` | `{170,99}` | [emulator](../results.tsv) |
| `C→PX(1)` | `{0,0}` | [emulator](../results.tsv) |
| `C→PX(10)` | `{0,0}` | [emulator](../results.tsv) |

## Behaviour

**The origin of the default view is the middle of the screen.** The point
`(0,0)` is pixel `{160,109}` (emulator), not the top-left corner, which is
where a program that assumes pixels puts it.

**One drawing unit is ten pixels.** Moving one unit along each axis moves the
answer from `{160,109}` to `{170,99}` (emulator): plus ten pixels across, and
minus ten down, because pixels count downwards while the view counts upwards.
The whole conversion in the default view is `px = 160 + 10x` and
`py = 109 - 10y`, which is the arithmetic that follows from those two rows.

That is what settles the disagreement these probes were run for:
[GROBW](GROBW.md) answers 10 where [GROBW_P](GROBW_P.md) answers 100 because
a unit is ten pixels (emulator), not because either is rounding.

What has not been measured is whether the factor follows the view when a
program sets one explicitly (unverified). Everything above is the view a
program gets before it changes anything, and that is the view most programs
draw in.

With a single argument it answers `{0,0}` (emulator), for one and for ten
alike. That is not the conversion: it takes a point, and one number is not a
point, so those two rows record a call that cannot be built on.

The answer is a list of two, which is what a pixel coordinate looks like
(emulator), and [PX→C](PX→C.md) converts the other way.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PX→C](PX→C.md) · [GROBW](GROBW.md) · [DIMGROB](DIMGROB.md) ·
[interface.geometry](../../topics/interface.md#interface.geometry)
