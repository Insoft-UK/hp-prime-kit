# perpen_bisector

The perpendicular through the middle of a segment.

| | |
|---|---|
| Syntax | `perpen_bisector(Segment)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("perpen_bisector(segment(point(0,0),point(4,0)))")` | `line(x=2)` | [emulator](../results.tsv) |

## Behaviour

`perpen_bisector` of a segment from the origin to 4,0 answers `line(x=2)`
(emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer was known before asking** (emulator): the middle of that segment
is at 2 and the perpendicular there is the vertical line, which is what came
back written as an equation in x rather than in y.

**It takes one segment, where [perpendicular](perpendicular.md) refused a
point and a line** (emulator). The two names sound alike and take different
things, and only this one worked in this batch.

It is the way to get a vertical line out of this group so far (emulator),
since the other line-building names answered equations in y.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[perpendicular](perpendicular.md) · [segment](segment.md) ·
[midpoint](midpoint.md)
