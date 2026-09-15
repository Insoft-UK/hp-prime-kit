# RECT

Draws a filled rectangle in drawing units, and clears the screen when called bare.

| | |
|---|---|
| Syntax | `RECT()` |
| Syntax | `RECT([grob,] x1, y1, x2, y2 [, edge [, fill]])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,10,5,0); RETURN RECT(G1,0,0,4,4,RGB(0,255,0));` | `1` | [emulator](../results.tsv) |
| `RECT()` | `1` | [emulator](../results.tsv) |

## Behaviour

Both forms answer 1, the acknowledgement eleven drawing commands share
(emulator).

**The bare form runs and answers 1** (emulator). That is how most programs
start a redraw, and it is measured here rather than assumed:
[RECT_P](RECT_P.md) left the same form unrun, because a batch cannot tell a
cleared screen from an uncleared one by the answer alone. What it clears is
still not measured (unverified) -- only that the call is accepted with no
arguments at all.

The corners are drawing units, and one unit is ten pixels in the default view
(emulator), so `(0,0)` to `(4,4)` covers forty pixels by forty rather than
four by four, [C→PX](C→PX.md).

HP's syntax has both an edge colour and a fill colour; one colour argument
was measured and which of the two it sets has not been separated here
(unverified), exactly as in [RECT_P](RECT_P.md).

The interpreter records the call rather than drawing it
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)),
so `hpprime run` cannot check what it painted (unverified).

## Related

[RECT_P](RECT_P.md) · [LINE](LINE.md) · [INVERT](INVERT.md) ·
[C→PX](C→PX.md)
