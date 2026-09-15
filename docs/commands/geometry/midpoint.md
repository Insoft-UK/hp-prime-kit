# midpoint

The middle of a segment.

| | |
|---|---|
| Syntax | `midpoint(Segment)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("midpoint(segment(point(0,0),point(2,2)))")` | `point(1,1)` | [emulator](../results.tsv) |

## Behaviour

`midpoint` of a segment from the origin to 2,2 answers `point(1,1)`
(emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It takes a segment, not two points** (HP help), which is why the call
builds one with [segment](segment.md) first. That nesting also showed the
group's objects can be passed straight from one command to another
(emulator).

[element](element.md) answers the same kind of point for a fraction of 0.5
(emulator), so the two agree where they overlap.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[element](element.md) · [segment](segment.md) ·
[perpen_bisector](perpen_bisector.md)
