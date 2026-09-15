# area

The area of a circle.

| | |
|---|---|
| Syntax | `area(Circle)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("area(circle(point(0,0),point(1,0)))")` | `1/4*π` | [emulator](../results.tsv) |

## Behaviour

`area` of the circle through the origin and 1,0 answers a quarter of pi
(emulator), a symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer is what told this documentation that `circle` takes a
diameter** (emulator). A quarter of pi is the area of a circle of radius a
half; a radius of 1 would have given pi. [radius](radius.md) confirmed it
directly afterwards.

**It is exact rather than decimal** (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers), and the pi is
U+03C0, a character the calculator writes and nobody can type, so the Result
cell was built from the stored row rather than typed.

HP's syntax names a circle (HP help). What it does with a polygon, which
[perimeter](perimeter.md) is said to take, was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[radius](radius.md) · [perimeter](perimeter.md) · [center](center.md)
