# PIXON

Paints one point, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `PIXON([grob,] x, y [, colour])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,10,5,0); PIXON(G1,1,1,RGB(255,0,0)); RETURN GETPIX(G1,1,1);` | `#FF000000h` | [emulator](../results.tsv) |

## Behaviour

**What was painted did not read back.** The point was written with
`RGB(255,0,0)` and [GETPIX](GETPIX.md) answered `#FF000000h` rather than a
red (emulator). The same loop in pixels does work: [PIXON_P](PIXON_P.md)
paints and [GETPIX_P](GETPIX_P.md) reads `#FF0000h` back (emulator).

So this row measures a write and a read that disagree, and it does not show
that the command fails: either the paint or the read landed somewhere other
than where the call looks like it points, and nothing here separates the two
(unverified).

The reason to suspect the coordinates is that a drawing unit is ten pixels
([C→PX](C→PX.md)), which puts the point `(1,1)` well outside a grob of 10 by
5 units if a grob is measured in pixels of its own (unverified). Painting
with this form and reading with [GETPIX_P](GETPIX_P.md) is the probe that
would tell them apart, and it has not been run (unverified).

Use the `_P` form when you mean a pixel, which is what a program drawing an
interface means (emulator: the `_P` pair is the one measured end to end).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PIXON_P](PIXON_P.md) · [PIXOFF](PIXOFF.md) · [GETPIX](GETPIX.md) ·
[C→PX](C→PX.md)
