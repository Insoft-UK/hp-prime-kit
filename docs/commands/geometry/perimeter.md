# perimeter

The perimeter of a polygon, refused because its argument was.

| | |
|---|---|
| Syntax | `perimeter(Polygon)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("perimeter(triangle(point(0,0),point(3,0),point(0,4)))")` | `"Error: entrada no válida"` | [emulator](../results.tsv) |

## Behaviour

**The call is refused, and the reason is now known** (emulator):
[triangle](triangle.md) is itself refused, so nothing ever reached this
command. The perimeter of that triangle is 12 and was known before asking.

**This is the one debt of the first geometry batch still unpaid**
(emulator). Three others -- [inter](inter.md), [parallel](parallel.md) and
[equation](equation.md) -- were rebuilt with [segment](segment.md) and all
three recovered. This one could not be, because the polygon families have no
working triangle to hand it.

**The probe is now obvious and cheap** (unverified): the same call on a
polygon that did come back, such as the `polygon(...)` that
[square](square.md) or [polygon](polygon.md) answers. Either the command
works and this row was never about it, or it does not and the row finally
means something.

[area](area.md) answered for a circle in the same phase (emulator), so the
measuring family is not refused as a whole.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[triangle](triangle.md) · [area](area.md) · [polygon](polygon.md) ·
[inter](inter.md)
