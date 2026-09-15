# homothety

Scales an object about a centre.

| | |
|---|---|
| Syntax | `homothety(Point, Realk, Object)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("homothety(point(0,0),2,point(1,1))")` | `point(2,2)` | [emulator](../results.tsv) |

## Behaviour

**The answer was known before asking** (emulator): doubling `point(1,1)` about
the origin gives `point(2,2)`, type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). This row shows the
command computing rather than echoing.

**The arguments go centre, factor, object** (emulator), which the answer
confirms: any other reading of those three would not have produced 2,2.

**[similarity](similarity.md) answered the same point for the same scaling**
(emulator), because it takes an angle as well and was given zero. One is the
other with a turn added, and with no turn they agree.

What it does to an object other than a point was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[similarity](similarity.md) · [inversion](inversion.md) ·
[projection](projection.md)
