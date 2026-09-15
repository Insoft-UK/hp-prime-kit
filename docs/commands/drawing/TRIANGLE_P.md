# TRIANGLE_P

Draws a triangle, in pixels.

| | |
|---|---|
| Syntax | `TRIANGLE_P([grob,] x1, y1, x2, y2, x3, y3 [, colour])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,20,20,0); RETURN TRIANGLE_P(G1,0,0,9,0,0,9,RGB(255,0,0));` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1 (emulator). Three corners and a colour were accepted in that
order, which is the reading of HP's syntax this entry rests on.

Whether it fills the triangle or draws its outline has **not** been measured
(unverified), and the answer cannot show it: one
[GETPIX_P](GETPIX_P.md) inside the shape would. That is the first thing to
check before using it for anything but a marker.

[FILLPOLY_P](FILLPOLY_P.md) is the general form, and it takes its corners as
a list rather than as separate arguments (HP help).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[FILLPOLY_P](FILLPOLY_P.md) · [LINE_P](LINE_P.md) · [ARC_P](ARC_P.md)
