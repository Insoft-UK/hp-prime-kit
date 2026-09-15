# LINE_P

Draws a line, in pixels.

| | |
|---|---|
| Syntax | `LINE_P([grob,] x1, y1, x2, y2 [, colour])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,10,10,0); RETURN LINE_P(G1,0,0,9,9,RGB(0,0,255));` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, which is an acknowledgement and not a measurement: eleven of
the drawing commands run in the same batch answer the same 1, whatever they
drew (emulator). What a program learns from a drawing command is therefore
nothing -- to find out what landed on the screen it has to read pixels back
with [GETPIX_P](GETPIX_P.md).

The two ends are pixel coordinates counting from 0
([DIMGROB_P](DIMGROB_P.md)), and the colour is the kind [RGB](RGB.md)
answers (emulator).

Whether the line includes its last pixel, and what a line partly outside the
grob does, has not been measured (unverified): reading back the pixel at
`(9,9)` after this very call is the probe.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RECT_P](RECT_P.md) · [TRIANGLE_P](TRIANGLE_P.md) · [PIXON_P](PIXON_P.md)
