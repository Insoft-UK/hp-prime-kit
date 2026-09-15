# BLIT

Copies one grob into another, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `BLIT([target,] [x1, y1, x2, y2,] source [, sx1, sy1, sx2, sy2] [, transparent])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,10,5,0); DIMGROB(G2,10,5,0); RETURN BLIT(G2,G1);` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement eleven drawing commands share (emulator).
The two-argument form -- a target and a source, with no rectangles -- is
accepted (emulator), which is the shortest form and the one a redraw uses.

**Both grobs have to exist first.** `G1` and `G2` were created with
[DIMGROB](DIMGROB.md) before the call (emulator). That is the difference from
[SUBGROB_P](SUBGROB_P.md), which creates its target for you, and the reason a
`BLIT` into an unmade grob is worth checking before blaming the copy
(unverified: the unmade case was not run).

Whether the copy landed, and what it did with two pictures of the same size,
was not read back: the commands that read a point of a grob in these units
answer the same value whatever the picture holds (unverified),
[GETPIX](GETPIX.md).

For pixels, [BLIT_P](BLIT_P.md) is the measured form, and mixing the two in
one redraw is how a program ends up with a picture ten times the size it
meant, because a drawing unit is ten pixels (emulator), [C→PX](C→PX.md).

The interpreter records the call rather than drawing it
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)),
so `hpprime run` cannot check what it painted (unverified).

## Related

[BLIT_P](BLIT_P.md) · [SUBGROB](SUBGROB.md) · [DIMGROB](DIMGROB.md)
