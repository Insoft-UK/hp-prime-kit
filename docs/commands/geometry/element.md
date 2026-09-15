# element

A point part of the way along an object.

| | |
|---|---|
| Syntax | `element(Object, Real)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("element(segment(point(0,0),point(4,0)),0.5)")` | `point(2,0)` | [emulator](../results.tsv) |

## Behaviour

`element` of a segment from the origin to 4,0 at 0.5 answers `point(2,0)`
(emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The second argument is a fraction of the way along, not a distance**
(emulator). The answer was known in advance: 0.5 of a segment four long ends
at 2, and a distance of 0.5 would have ended at 0.5. That is what the row
settles.

**It agrees with [midpoint](midpoint.md)** (emulator), which answered
`point(1,1)` for a segment from the origin to 2,2. Half of a segment is the
same point whichever of the two names asks for it.

What it does with a fraction above 1 or below 0 was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[midpoint](midpoint.md) · [segment](segment.md) · [point](point.md)
