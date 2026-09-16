# locus

The path a point traces, refused for the two points given.

| | |
|---|---|
| Syntax | `locus(Point,Element, [tstep=Value]))` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("locus(point(0,0),point(1,1))")` | `"locus(point(0,0),point(1,1)) \n Error: valor de argumento incorrecto"` | [emulator](../results.tsv) |

## Behaviour

**The answer is a string carrying an error message** (emulator), type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), and it quotes the call
back before the message. That makes it the most informative of the failures
in this group: a caller can see which call went wrong without tracking it.

**The line break arrives as the two characters backslash and n** (emulator),
not as a break, which is the same thing `STRING` does to a multi-line answer
elsewhere in this documentation.

**The second argument is not a point** (HP help): HP calls it an Element,
meaning something the first point is constrained to move along. Two plain
points give it nothing to trace, so this row most likely measures a wrong
argument rather than a broken command (unverified).

The probe is a point and a curve it lies on (unverified), such as a point
built by [element](element.md) on a [segment](segment.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[element](element.md) · [conic](conic.md) · [inter](inter.md)
