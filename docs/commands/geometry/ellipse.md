# ellipse

An ellipse, answered as a parametric plot.

| | |
|---|---|
| Syntax | `ellipse(Point1, Point2, Point3)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ellipse(point(-1,0),point(1,0),point(0,1))")` | `plotparam((√2+√2)/2*COS(t)+*SIN(t),t,0,6.28318530718)` | [emulator](../results.tsv) |

## Behaviour

**It answers a parametric plot rather than an ellipse object** (emulator),
type 8, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). Where
[circle](circle.md) comes back as `circle(centre,radius)`, this comes back as
a `plotparam` over t from 0 to a full turn, built out of cosine and sine.

**So the curve families do not answer alike** (emulator). The four circle
commands answer objects a program can take apart with
[center](center.md) and [radius](radius.md); this one, together with
[hyperbola](hyperbola.md) and [parabola](parabola.md), answers something
shaped for drawing.

**The Result cell carries two characters nobody can type** (emulator): the
radical U+221A and the imaginary unit U+E003. It was built from the stored
row rather than typed, as the format requires,
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit).

**The imaginary unit is how a point is written in these answers**
(emulator), the same form [affix](affix.md) gives for a point: a real part
and an imaginary one standing for x and y.

The first two points are the foci and the third is on the curve (HP help),
which the answer neither confirms nor contradicts (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[hyperbola](hyperbola.md) · [parabola](parabola.md) · [circle](circle.md) ·
[affix](affix.md)
