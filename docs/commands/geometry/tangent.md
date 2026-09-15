# tangent

The tangent to a curve, which answered an empty list.

| | |
|---|---|
| Syntax | `tangent(Curve, Point)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("tangent(circle(point(0,0),point(2,0)),point(1,0))")` | `{}` | [emulator](../results.tsv) |

## Behaviour

**The answer is an empty list** (emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): not an error, not a
line, nothing at all.

**The point given is the centre of that circle, not a point on it**
(emulator). The circle through the origin and 2,0 has its centre at 1,0, as
[center](center.md) answered in the same batch, and no tangent passes through
the centre. So an empty list may be the honest answer to an impossible
question rather than a failure.

**That reading is untested and the probe is one row** (unverified): the same
call with a point on the circle, where a tangent exists. If a line comes back
then the empty list means "none", which is useful; if another empty list
comes back it means the command is not working.

**An empty answer is the third way this batch reported trouble** (emulator),
after a plain refusal and a message carried as data; see [inter](inter.md).
A program looping over the answer simply does nothing, silently.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[center](center.md) · [inter](inter.md) · [perpendicular](perpendicular.md)
