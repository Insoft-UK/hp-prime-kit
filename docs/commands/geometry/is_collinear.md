# is_collinear

Whether points lie on one line.

| | |
|---|---|
| Syntax | `is_collinear(Point1, Point2, ..., Pointn)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_collinear(point(0,0),point(1,1),point(2,2))")` | `1` | [emulator](../results.tsv) |

## Behaviour

`is_collinear` of three points along the diagonal answers 1 (emulator), a
plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). They do lie on one
line, so the answer was known before asking.

**It takes any number of points** (HP help), unlike most of this family,
which take a fixed three or four. Only the three-point form was run
(unverified).

**It answers 1 rather than a code** (emulator), which puts it with the seven
plain tests of this family rather than with
[is_isosceles](is_isosceles.md) and
[is_parallelogram](is_parallelogram.md).

What it answers for points that are not collinear was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[is_concyclic](is_concyclic.md) · [is_element](is_element.md) ·
[slope](slope.md)
