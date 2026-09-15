# is_orthogonal

Whether two lines meet at a right angle.

| | |
|---|---|
| Syntax | `is_orthogonal(Line1, Line2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_orthogonal(segment(point(0,0),point(4,0)),segment(point(0,0),point(0,4)))")` | `1` | [emulator](../results.tsv) |

## Behaviour

`is_orthogonal` of a segment along each axis answers 1 (emulator), a plain
real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). The two axes do meet at
a right angle, so the answer was known before asking.

**[is_perpendicular](is_perpendicular.md) answered 1 for exactly the same two
arguments** (emulator). One example cannot tell the two commands apart, and
this entry does not describe a difference it has not seen. The probe is a
pair perpendicular in one sense and not the other, such as two lines that
would cross at a right angle if extended but never meet.

**Segments were accepted where HP's syntax says Line** (emulator), as
elsewhere in this group, which matters because [line](line.md) is refused and
segments are the only lines a program can readily build.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[is_perpendicular](is_perpendicular.md) · [perpendicular](perpendicular.md) ·
[angle](angle.md)
