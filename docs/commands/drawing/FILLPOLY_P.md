# FILLPOLY_P

Fills a polygon given as a list of points, in pixels.

| | |
|---|---|
| Syntax | `FILLPOLY_P([grob,] {points} [, colour])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,20,20,0); RETURN FILLPOLY_P(G1,{0,9,{9,9}},RGB(255,0,0));` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1 (emulator), and that is nearly all this measurement says.

The list that was passed, `{0,9,{9,9}}`, mixes two plain numbers and a pair,
which is not a shape anybody would write on purpose: it was accepted anyway
(emulator). So the command tolerates a list nobody here understands, and
what it drew from it is unknown. How the points are really written -- pairs,
or a flat list of alternating coordinates -- has not been measured
(unverified), and the call above should not be copied.

That it did not refuse a malformed list is itself worth knowing (emulator): a
program building points from data will not be told when the shape is wrong.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TRIANGLE_P](TRIANGLE_P.md) · [LINE_P](LINE_P.md)
