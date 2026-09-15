# rectangle

A rectangle on a side, with the second side given as a ratio.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("rectangle(point(0,0),point(2,0),1)")` | `polygon(point(0,0),point(2,0),point(2,2),point(0,2),point(0,0))` | [emulator](../results.tsv) |

## Behaviour

**Two points give a side and the third argument scales the other**
(emulator). With a ratio of 1 the two sides are equal, so the answer is a
square of side 2, closed the way [polygon](polygon.md) describes.

**[square](square.md) answered exactly the same polygon for the same two
points** (emulator), character for character. That agreement is what says the
third argument is a ratio rather than a length: a length of 1 would have
given a 2 by 1 rectangle instead.

**The reading is strong but not proven** (unverified). One row with a ratio
of 1 cannot separate a ratio from any other rule that happens to give a
square there. The probe is the same call with 2, which should give sides of 2
and 4 if the reading holds.

HP's list gives this name no syntax string (HP help), so even the argument
order comes from the answer rather than from the documentation.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[square](square.md) · [rhombus](rhombus.md) · [polygon](polygon.md)
