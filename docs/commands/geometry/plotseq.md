# plotseq

Answers the whole staircase of a sequence, and overflowed the row.

| | |
|---|---|
| Syntax | `plotseq(f(Var), Var={Start, Xmin, Xmax}, Integern)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("plotseq(X/2,X,3)")` | `{segment(point(−15.9,0),point(15.9,0)),line(y=x),polygon(point(0,−15.9),point(0,0),point(0,0),point(0,0),point(0,0),point(0,0),point(0,0)),polygon(point(0,0),po (cut at 160 characters)` | [emulator](../results.tsv) |

## Behaviour

**It answers a list of drawing objects, not a single plot** (emulator), type
6, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). What survived the
row holds an axis as a segment, the line y equals x, and polygons: the
cobweb construction a sequence plot is drawn from.

**The answer was cut at 160 characters** (emulator), the harness's width, so
the Result cell above holds a beginning and the marker that says so. It is
the second answer in this phase to overflow, after
[isopolygon](isopolygon.md), and both overflowed for the same reason: the
calculator answers with construction rather than with a picture.

**The polygons carry repeated identical points** (emulator), several
`point(0,0)` in a row, which is what a cobweb looks like before any steps
have been taken.

**The call did not follow the published syntax** (HP help), which wants the
second argument as a list of start and bounds; three plain arguments were
sent and accepted, as [plotpolar](plotpolar.md) also was.

**The Result cell carries the real minus U+2212** (emulator), so it was built
from the stored row rather than typed.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[plotlist](plotlist.md) · [isopolygon](isopolygon.md) ·
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign)
