# hyperbola

A hyperbola, answered as two parametric plots in a list.

| | |
|---|---|
| Syntax | `hyperbola(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("hyperbola(point(-1,0),point(1,0),point(0,1))")` | `{plotparam(*SINH(t),t,−3,3),plotparam(-(*SINH(t)),t,−3,3)}` | [emulator](../results.tsv) |

## Behaviour

**The answer is a list of two plots, one per branch** (emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). A hyperbola has two
separate branches and each arrives as its own `plotparam`, the second the
negative of the first.

**That makes it the only curve here whose answer is a list** (emulator).
[ellipse](ellipse.md) and [parabola](parabola.md) answer a single plot, so a
program handling all three has to expect either shape.

**The branches are drawn with the hyperbolic sine** (emulator), over t from
minus three to three, which is a range rather than a full turn: unlike an
ellipse, neither branch closes.

**The Result cell carries the imaginary unit U+E003 and the real minus
U+2212** (emulator), both characters nobody can type, so it was built from
the stored row rather than typed,
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign).

The first two points are the foci and the third is on the curve (HP help),
unconfirmed here (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ellipse](ellipse.md) · [parabola](parabola.md) · [conic](conic.md)
