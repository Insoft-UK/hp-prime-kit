# inter

The intersections of two curves, as a list.

| | |
|---|---|
| Syntax | `inter(Curve1, Curve2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("inter(segment(point(0,0),point(4,0)),segment(point(2,-1),point(2,1)))")` | `{point(2,0)}` | [emulator](../results.tsv) |
| `EXPR("inter(line(point(0,0),point(4,0)),line(point(2,-1),point(2,1)))")` | `{"Error: entrada no válida"}` | [emulator](../results.tsv) |

## Behaviour

**Given two segments it answers a list holding the crossing point**
(emulator): the x axis and the vertical at 2 meet at `point(2,0)`, which is
what came back, in a list of type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). A list is the right
shape, since two curves can meet more than once.

**The second row is the same call with its arguments built by
[line](line.md), and it fails** (emulator). The list comes back holding an
error message instead of a point. Both rows are kept because together they
say something neither says alone: the command works, and what broke it was
the argument.

**That settles a question this documentation had left open** (emulator). The
first geometry batch saw six commands fail on arguments built by `line`, and
each entry named the same probe -- rebuild with [segment](segment.md). The
probe ran. [parallel](parallel.md) and [equation](equation.md) recovered the
same way.

**A failure carried inside a list is still the pattern to guard against**
(emulator). The type is 6 either way, so a program checking that it received
a list receives one; only looking at what the list holds tells the two rows
apart.

The text is Spanish because this machine is (emulator), so it is evidence of
rejection rather than a property of the command.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[single_inter](single_inter.md) · [line](line.md) · [segment](segment.md) ·
[parallel](parallel.md)
