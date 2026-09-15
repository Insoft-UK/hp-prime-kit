# triangle

Refused, where every other polygon constructor answered.

| | |
|---|---|
| Syntax | `triangle(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("triangle(point(0,0),point(3,0),point(0,4))")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`triangle` is refused while the other eight polygon constructors answer**
(emulator). [square](square.md), [rectangle](rectangle.md),
[rhombus](rhombus.md), [parallelogram](parallelogram.md),
[quadrilateral](quadrilateral.md), [right_triangle](right_triangle.md),
[isopolygon](isopolygon.md) and [polygon](polygon.md) all came back in the
same batch; this one gave a plain error with no type at all.

**That is the second time the plainest name of a family is the broken one**
(emulator). [line](line.md) is refused while `segment` and `half_line`
answer, and now `triangle` is refused while every shape around it works. Two
families, two gaps, both at the most obvious name.

**It cost another entry its evidence** (emulator).
[perimeter](perimeter.md) was called on the triangle this command would have
built, so its refusal says nothing about perimeters: nothing ever reached it.

**A triangle is still reachable two ways** (emulator):
[right_triangle](right_triangle.md) builds one from two points and a ratio,
and [polygon](polygon.md) takes three points and answers a closed three-sided
figure. Either is what a program should use today.

What `triangle` needs instead is not established (unverified). The probes
worth one row each: the three points as a list, and the same call with
[QUOTE](../catalog/QUOTE.md) around its arguments.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[polygon](polygon.md) · [right_triangle](right_triangle.md) ·
[perimeter](perimeter.md) · [line](line.md)
