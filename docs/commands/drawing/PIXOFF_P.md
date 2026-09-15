# PIXOFF_P

Sets one pixel to white.

| | |
|---|---|
| Syntax | `PIXOFF_P([grob,] x, y)` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,10,10,RGB(255,0,0)); PIXOFF_P(G1,1,1); RETURN GETPIX_P(G1,1,1);` | `#FFFFFFh` | [emulator](../results.tsv) |

## Behaviour

**"Off" means white, not black and not transparent.** On a grob filled red,
the pixel it touched reads back `#FFFFFFh` (emulator). A program that uses it
to clear part of a dark screen paints a white dot instead, which is the kind
of thing you see on the calculator and not in the code.

To put back a particular colour, [PIXON_P](PIXON_P.md) with that colour is
the measured way (emulator).

Coordinates count from 0 (emulator), as for the rest of the `_P` family.
Whether it means white or "the background colour" has not been separated
here: the grob was red, so a background-coloured answer would have been red
(unverified). A grob made with some third colour would say which.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PIXON_P](PIXON_P.md) · [GETPIX_P](GETPIX_P.md) · [RGB](RGB.md)
