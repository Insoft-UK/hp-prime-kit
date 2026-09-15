# RECT_P

Draws a filled rectangle, in pixels, and clears the screen when called bare.

| | |
|---|---|
| Syntax | `RECT_P()` |
| Syntax | `RECT_P([grob,] x1, y1, x2, y2 [, edge [, fill]])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,10,10,0); RETURN RECT_P(G1,0,0,4,4,RGB(0,255,0));` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement eleven drawing commands share (emulator).

Called with no arguments it clears the screen, which is how most programs
start a redraw (HP help). That form was not run here, because a batch's
answer would look the same either way (unverified).

The corners are pixel coordinates counting from 0
([DIMGROB_P](DIMGROB_P.md)). HP's syntax has both an edge colour and a fill
colour; only one colour argument was measured, and which of the two it sets
has not been separated (unverified).

The interpreter records the call rather than drawing it
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)),
so `hpprime run` cannot check what it painted (unverified).

## Related

[LINE_P](LINE_P.md) · [INVERT_P](INVERT_P.md) · [DIMGROB_P](DIMGROB_P.md)
