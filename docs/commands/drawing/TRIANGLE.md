# TRIANGLE

Draws a triangle, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `TRIANGLE([grob,] x1, y1, x2, y2, x3, y3 [, colour])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,20,20,0); RETURN TRIANGLE(G1,0,0,9,0,0,9,RGB(255,0,0));` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement eleven drawing commands share (emulator).

Three points and a colour are accepted in one call (emulator): six numbers
for the corners, then the colour, with no rectangle and no separate fill
argument.

A 0 is a legal coordinate (emulator): two of the three corners in the
measured call are on zero. That is the drawing exception to
[ppl.one-based](../../topics/ppl.md#ppl.one-based), which is about lists and
matrices.

The corners are drawing units, ten pixels each in the default view
(emulator), so the triangle measured here is ninety pixels on a side rather
than nine, [C→PX](C→PX.md).

Whether the shape is filled or outlined, and whether a second colour argument
separates the two as it seems to for [RECT](RECT.md), was not measured
(unverified).

The interpreter records the call rather than drawing it
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)),
so `hpprime run` cannot check what it painted (unverified).

## Related

[TRIANGLE_P](TRIANGLE_P.md) · [FILLPOLY](FILLPOLY.md) · [ARC](ARC.md)
