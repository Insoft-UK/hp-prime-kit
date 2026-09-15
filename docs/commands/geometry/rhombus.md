# rhombus

A rhombus on a side, with the angle given in radians.

| | |
|---|---|
| Syntax | `rhombus(Point1, Point2, Angle)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("rhombus(point(0,0),point(2,0),1)")` | `polygon(point(0,0),point(2,0),point(2*(COS(1)+*SIN(1))+2),point(2*(COS(1)+*SIN(1))),point(0,0))` | [emulator](../results.tsv) |

## Behaviour

**The answer names the angle explicitly, and that settles the units**
(emulator). It carries `COS(1)` and `SIN(1)` rather than a number, so the
third argument was taken as an angle of 1 radian and not as 1 degree or as a
ratio. The whole documentation's angle mode says the same:
[angle](angle.md) answers half of pi for a right angle.

**That separates it from its neighbours** (emulator).
[rectangle](rectangle.md) takes a ratio as its third argument and
[right_triangle](right_triangle.md) takes one too; this one takes an angle,
and all three look alike in a program.

**The answer is left unevaluated** (emulator). Where
[square](square.md) answers plain coordinates, this comes back with the
trigonometry still written out, so a program comparing coordinates has to
evaluate it first.

**The Result cell carries the imaginary unit U+E003** (emulator), which is
how these answers write a point, so it was built from the stored row rather
than typed, [ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit).

It answers in the closed `polygon(...)` form the family shares
(emulator), [polygon](polygon.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[square](square.md) · [rectangle](rectangle.md) · [angle](angle.md) ·
[polygon](polygon.md)
