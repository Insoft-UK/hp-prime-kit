# circle

The circle whose diameter joins two points.

| | |
|---|---|
| Syntax | `circle(Point1, Point2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("circle(point(0,0),point(2,0))")` | `circle(point(1,0),1)` | [emulator](../results.tsv) |

## Behaviour

**It takes a diameter and answers a centre and a radius** (emulator). Given
the origin and 2,0 it comes back as `circle(point(1,0),1)`, type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): the centre halfway
between the two points, the radius half their separation.

**So the call and the answer are written in different terms**, and that is
the trap worth knowing (emulator). A program that reads its own call as
centre-and-rim gets a circle twice the size it meant, and nothing raises.

**Three other commands confirmed the reading before this row existed**
(emulator): [center](center.md) answers `point(1,0)`,
[radius](radius.md) answers a half for the circle through the origin and 1,0,
and [area](area.md) answers a quarter of pi for the same. This entry is the
fourth witness and the only direct one.

Every circle-building command in this group answers in the same
centre-and-radius form (emulator), as
[circumcircle](circumcircle.md), [incircle](incircle.md) and
[excircle](excircle.md) show.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Models get wrong

| They write | What happens | Seen in |
|---|---|---|
| `circle(centre, pointOnRim)` | Builds a circle of twice the intended radius, silently: the two points are read as the ends of a diameter | [emulator](../results.tsv) |

## Related

[center](center.md) · [radius](radius.md) · [area](area.md) ·
[circumcircle](circumcircle.md)
