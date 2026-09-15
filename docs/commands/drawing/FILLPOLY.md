# FILLPOLY

Fills a polygon given as a list of points, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `FILLPOLY([grob,] {points} [, colour] [, transparency])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,20,20,0); RETURN FILLPOLY(G1,{{0,0},{9,0},{0,9}},RGB(255,0,0));` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement eleven drawing commands share (emulator).

**The points go in as a list of lists**: `{{0,0},{9,0},{0,9}}` is accepted
(emulator), so each point is a two-element list and the polygon is one
argument rather than six loose numbers. That is the difference from
[TRIANGLE](TRIANGLE.md), which takes its corners spread out, and it is what
makes this the command for a shape whose corners a program computes.

The list is indexed from 1 like every other list
([ppl.one-based](../../topics/ppl.md#ppl.one-based)), while the coordinates
inside it start at 0 (emulator): both appear in the measured call, and mixing
them up is the easy mistake.

The points are drawing units, ten pixels each in the default view (emulator),
[C→PX](C→PX.md).

Whether the polygon is closed automatically, and what the transparency
argument does, were not measured (unverified).

The interpreter records the call rather than drawing it
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)),
so `hpprime run` cannot check what it painted (unverified).

## Related

[FILLPOLY_P](FILLPOLY_P.md) · [TRIANGLE](TRIANGLE.md) · [C→PX](C→PX.md)
