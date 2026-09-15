# DIMGROB

Creates an off-screen picture, sized in the coordinates of the current view.

| | |
|---|---|
| Syntax | `DIMGROB(G, w, h, [color])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G2,10,5,0)` | `1` | [emulator](../results.tsv) |
| `DIMGROB(G4,10,5,0); RETURN GROBW_P(G4);` | `100` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement eleven drawing commands share (emulator),
so the call says nothing about the grob it made.

**The size is not in pixels here**, and that is the whole difference from
[DIMGROB_P](DIMGROB_P.md). A grob made `DIMGROB(G4,10,5,0)` measures 100
pixels wide through [GROBW_P](GROBW_P.md) (emulator): ten units, ten pixels
each.

**So `DIMGROB(G2,10,5,0)` and `DIMGROB_P(G1,100,50,0)` make the same picture**
(emulator). That was the entry's guess before this was run, and it is now
measured rather than probable.

The unit comes from the view, not from the grob: `(0,0)` is pixel `{160,109}`
and `(1,1)` is `{170,99}` in the view a program starts with (emulator),
[C→PX](C→PX.md). Whether the factor follows a view the program sets itself is
still open (unverified), and [GROBW](GROBW.md) carries the probe.

A grob of ten by five units is a hundred by fifty pixels, which is a sixth of
the screen and not the small stamp the numbers suggest (emulator). Sizing a
picture with the wrong form is how a redraw ends up ten times too big.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DIMGROB_P](DIMGROB_P.md) · [GROBW](GROBW.md) · [GROBW_P](GROBW_P.md) ·
[C→PX](C→PX.md)
