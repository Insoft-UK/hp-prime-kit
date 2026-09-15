# equation

The equation of an object.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("equation(segment(point(0,0),point(4,0)))")` | `y=0` | [emulator](../results.tsv) |
| `EXPR("equation(line(point(0,0),point(1,1)))")` | `"Error: entrada no válida"` | [emulator](../results.tsv) |

## Behaviour

**Given a segment along the x axis it answers `y=0`** (emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): the equation of the
line the segment lies on, not a description of the segment itself.

**The second row is the same command given an object built by
[line](line.md), and it fails** (emulator). Both rows are kept because the
pair is the evidence: the command works, and `line` is what broke it.

**It answers an equation rather than a string** (emulator). The working row
is type 8, a symbolic object a program can carry on using; the failing row is
type 2, a string. So the type alone distinguishes success from failure here,
which is not true of [inter](inter.md) or [parallel](parallel.md).

HP's list gives this name no syntax string (HP help), so what other objects it
accepts is not published and only the segment was run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[parameq](parameq.md) · [segment](segment.md) · [line](line.md)
