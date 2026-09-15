# line

Refused, where the two commands beside it answered.

| | |
|---|---|
| Syntax | `line(Point1, Point2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("line(point(0,0),point(3,4))")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`line` is refused where [segment](segment.md) and
[half_line](half_line.md) are not** (emulator). All three were given the same
two points in the same batch. The other two answered with an object naming
themselves -- `segment(point(0,0),point(3,4))` and the matching `half_line`
-- and this one gave a plain error.

**That is a refusal, not a message** (emulator). It has no type at all, unlike
the seven answers in this batch that carried their failure as text; see
[inter](inter.md). So whatever went wrong here went wrong before an answer
could be built.

**Other commands do build lines** (emulator). [altitude](altitude.md),
[bisector](bisector.md), [median_line](median_line.md) and
[perpen_bisector](perpen_bisector.md) all answered with `line(...)` objects
in this batch, so the calculator makes lines readily. It is this name, given
two points, that would not.

What the name needs instead is not established (unverified). The probes worth
one row each: an equation rather than two points, since the answers of its
neighbours are written as equations, and two points given as a list.

Until that runs, a program needing a line through two points has
[segment](segment.md), which is measured (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[segment](segment.md) · [half_line](half_line.md) · [altitude](altitude.md) ·
[inter](inter.md)
