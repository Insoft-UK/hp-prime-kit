# distance

The distance between two points.

| | |
|---|---|
| Syntax | `distance(Point1, Point2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("distance(point(0,0),point(3,4))")` | `5` | [emulator](../results.tsv) |

## Behaviour

`distance` of the origin and 3,4 answers 5 (emulator), a plain real of type
0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**This is the row that proved the whole group reachable** (emulator). Five is
the answer arithmetic gives for that triangle, known before the calculator
was asked, so the command computed rather than handing something back -- and
it did so from Home, with no Geometry app open, on a calculator reset before
the run. Every plan for this group rests on it.

**It answers a plain number where most of its neighbours answer objects**
(emulator), so its result can go straight into arithmetic.

Whether it accepts anything other than two points was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[point](point.md) · [radius](radius.md) · [slope](slope.md)
