# is_element

Whether a point lies on an object.

| | |
|---|---|
| Syntax | `is_element(Point, Object)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_element(point(2,0),segment(point(0,0),point(4,0)))")` | `1` | [emulator](../results.tsv) |

## Behaviour

`is_element` of the point 2,0 and a segment from the origin to 4,0 answers 1
(emulator), type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). The point is the middle
of that segment, so the answer was known before asking.

**The point comes first and the object second** (emulator), which is the
order the answer confirms; the other way round would have asked whether a
segment lies on a point.

**It pairs with [element](element.md)** (emulator), which goes the other way:
that one hands back a point part of the way along an object, this one asks
whether a point is already on one.

What it answers for a point off the object, and whether it takes a curve as
readily as a segment, were not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[element](element.md) · [is_collinear](is_collinear.md) ·
[segment](segment.md)
