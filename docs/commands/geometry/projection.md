# projection

The foot of the perpendicular from a point to a curve.

| | |
|---|---|
| Syntax | `projection(Curve, Point)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("projection(segment(point(0,0),point(4,0)),point(2,3))")` | `point(2,0)` | [emulator](../results.tsv) |

## Behaviour

**The answer was known before asking** (emulator): dropping `point(2,3)` onto
the x axis gives `point(2,0)`, type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The curve comes first and the point second** (emulator), which is the
opposite order to [is_element](is_element.md), where the point leads. Two
commands in this group take the same two things in opposite orders, and
nothing in either answer warns of it.

**A segment was accepted where the syntax says Curve** (emulator), as
throughout this group, which matters because [line](line.md) is refused.

What it does when the foot falls outside the segment was not run
(unverified), and that is the case where a segment and an infinite line would
differ.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[is_element](is_element.md) · [perpendicular](perpendicular.md) ·
[reflection](reflection.md)
