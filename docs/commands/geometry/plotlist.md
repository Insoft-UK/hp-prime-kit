# plotlist

Joins a matrix of points into a segment.

| | |
|---|---|
| Syntax | `plotlist(Matrix)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("plotlist([[1,2],[3,4]])")` | `segment(point(1,2),point(3,4))` | [emulator](../results.tsv) |

## Behaviour

**Each row of the matrix is read as a point** (emulator). Two rows gave two
points and the answer joins them, type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It answers a `segment`, which is an object the rest of this group
understands** (emulator), unlike its neighbours in the plot family: they
answer `plotparam` objects, empty lists or error messages. So this is the one
plot command whose result can be handed to
[midpoint](midpoint.md) or [inter](inter.md).

**What three or more rows give was not run** (unverified). Two points can
only be a segment; more would show whether it joins them into a path or
answers a list of segments, and that is the row worth having.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[segment](segment.md) · [plotseq](plotseq.md) · [point](point.md)
