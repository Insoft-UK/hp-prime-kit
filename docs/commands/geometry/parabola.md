# parabola

A parabola, answered as a parametric plot.

| | |
|---|---|
| Syntax | `parabola(Point, Line)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("parabola(point(0,1),segment(point(0,0),point(4,0)))")` | `plotparam(t+*(1/2+t*2*t/4),t,−12,12)` | [emulator](../results.tsv) |

## Behaviour

**It answers a parametric plot** (emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), over t from minus
twelve to twelve, in the same shape [ellipse](ellipse.md) uses.

**The focus and the directrix are what it takes** (HP help): the point given
is the focus and the line is the directrix. The answer is consistent with
that reading, since the curve it describes rises away from the x axis with
the point 0,1 above it, but one row cannot prove the assignment
(unverified).

**A segment was accepted where the syntax says Line** (emulator), as
everywhere else in this group, which matters because [line](line.md) is
refused.

**The Result cell carries the imaginary unit U+E003 and the real minus
U+2212** (emulator), so it was built from the stored row rather than typed.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ellipse](ellipse.md) · [hyperbola](hyperbola.md) · [segment](segment.md)
