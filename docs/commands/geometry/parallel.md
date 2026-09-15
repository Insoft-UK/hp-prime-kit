# parallel

The parallel to a line through a point.

| | |
|---|---|
| Syntax | `parallel(Point, Line)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("parallel(point(0,1),segment(point(0,0),point(4,0)))")` | `line(y=1)` | [emulator](../results.tsv) |
| `EXPR("parallel(point(0,1),line(point(0,0),point(1,0)))")` | `line(y="Error: entrada no válida")` | [emulator](../results.tsv) |

## Behaviour

**Given a segment along the x axis and the point 0,1 it answers `line(y=1)`**
(emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): the horizontal through
that point, which is the answer arithmetic gives.

**The second row is the same call with the line built by [line](line.md)**
(emulator), and it comes back as a line object with the error message built
into it where the equation belongs. Both rows are kept: the command works,
and the argument was what broke it.

**That second row is still the sharpest warning in this group** (emulator). A
program checking that it received a line receives one, with the right type; a
program checking for an error finds none. Only reading inside the object
shows the difference between the two rows above.

**The second argument does not have to be a `line` object** (emulator), which
is what the first row shows: a segment was accepted where HP's syntax says
Line. That matters here because `line` itself is refused, so segments are the
only lines a program can readily build.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[perpendicular](perpendicular.md) · [line](line.md) · [segment](segment.md) ·
[inter](inter.md)
