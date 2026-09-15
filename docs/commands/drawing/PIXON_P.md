# PIXON_P

Paints one pixel.

| | |
|---|---|
| Syntax | `PIXON_P([grob,] x, y [, colour])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,10,10,0); PIXON_P(G1,1,1,RGB(255,0,0)); RETURN GETPIX_P(G1,1,1);` | `#FF0000h` | [emulator](../results.tsv) |

## Behaviour

**What is painted reads back.** The pixel written with `RGB(255,0,0)` answers
`#FF0000h` through [GETPIX_P](GETPIX_P.md) (emulator), which is the same
number [RGB](RGB.md) gave. That is the loop a program needs to measure
anything about what it has drawn, and it is measured end to end here.

Coordinates count from 0, as they do for
[GETPIX_P](GETPIX_P.md) (emulator): the pixel at `(1,1)` is the second of the
second row.

What it does without the colour argument, and whether it then uses a current
colour, has not been measured (unverified).
[PIXOFF_P](PIXOFF_P.md) is the other half of the pair, and it does not do
what its name suggests.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PIXOFF_P](PIXOFF_P.md) · [GETPIX_P](GETPIX_P.md) · [RGB](RGB.md)
