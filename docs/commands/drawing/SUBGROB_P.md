# SUBGROB_P

Copies part of a grob into another grob, in pixels.

| | |
|---|---|
| Syntax | `SUBGROB_P(source [, x1, y1, x2, y2], target)` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,10,10,0); SUBGROB_P(G1,0,0,4,4,G3); RETURN GROBW_P(G3);` | `4` | [emulator](../results.tsv) |

## Behaviour

**The piece is the size you asked for, and the target grob is created for
you**: `G3` did not exist before the call and measures 4 pixels wide
afterwards (emulator). So this both cuts and allocates, which is why it needs
no [DIMGROB_P](DIMGROB_P.md) of its own.

From `(0,0)` to `(4,4)` gives 4 rather than 5, so the corners are not both
included -- the opposite of [SUB](../matrix/SUB.md), where a rectangle of a
matrix from `{1,1}` to `{2,2}` is 2×2 (emulator). Two commands that look
alike and count differently is exactly the kind of thing worth measuring
rather than assuming.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BLIT_P](BLIT_P.md) · [DIMGROB_P](DIMGROB_P.md) · [GROBW_P](GROBW_P.md)
