# ARC_P

Draws a circle or an arc, in pixels.

| | |
|---|---|
| Syntax | `ARC_P([grob,] x, y, r [, a1, a2 [, colour]])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,20,20,0); RETURN ARC_P(G1,10,10,5);` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1 (emulator), which is what the drawing commands answer whatever
they draw.

The call that was run gives a centre and a radius and no angles, and it was
accepted, so the angles are optional in practice as well as in HP's syntax
(emulator). What a full circle looks like at radius 5 in a 20-pixel grob --
whether it is clipped, and where -- has not been measured (unverified).

The angles are the interesting unmeasured part: which unit they are in
depends on the calculator's angle setting, and a program that draws an arc
without setting that is at the mercy of whatever the user left it in
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TRIANGLE_P](TRIANGLE_P.md) · [LINE_P](LINE_P.md) · [RECT_P](RECT_P.md)
