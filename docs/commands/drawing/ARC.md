# ARC

Draws a circle or an arc, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `ARC([grob,] x, y, r [, a1, a2] [, colour])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,20,20,0); RETURN ARC(G1,10,10,5);` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement eleven drawing commands share (emulator).

**Centre, radius and nothing else is enough**: with no angles and no colour
the call is accepted (emulator), so the short form draws a whole circle
rather than needing a sweep spelled out.

The radius is in drawing units, and one unit is ten pixels in the default
view (emulator), so a radius of 5 here is fifty pixels across the screen --
the kind of difference that makes a circle vanish off the edge when the two
forms are mixed, [C→PX](C→PX.md).

With two more arguments it takes the angles the arc sweeps (HP help), and
whether they are read in degrees or radians follows the calculator's angle
mode, which was not measured here (unverified).

The interpreter records the call rather than drawing it
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)),
so `hpprime run` cannot check what it painted (unverified).

## Related

[ARC_P](ARC_P.md) · [TRIANGLE](TRIANGLE.md) · [C→PX](C→PX.md)
