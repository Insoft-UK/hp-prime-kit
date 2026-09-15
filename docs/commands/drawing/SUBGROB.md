# SUBGROB

Copies part of a grob into another grob, in drawing units.

| | |
|---|---|
| Syntax | `SUBGROB(source [, x1, y1, x2, y2], target)` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,10,5,0); SUBGROB(G1,0,0,4,4,G3); RETURN GROBW_P(G3);` | *error* | [emulator](../results.tsv) |

## Behaviour

**The same shape that works in pixels is refused here** (emulator).
[SUBGROB_P](SUBGROB_P.md) run as `SUBGROB_P(G1,0,0,4,4,G3)` cuts the piece
and creates `G3`, which then measures 4 pixels wide; with the form without
`_P`, on a grob made by [DIMGROB](DIMGROB.md), the call is an error.

What the error is was not separated (unverified). Two candidates: the
rectangle `(0,0)` to `(4,4)` may fall outside a grob whose drawing units are
the view's rather than its own -- a unit is ten pixels (emulator),
[C→PX](C→PX.md) -- or this form may not create its target the way
the `_P` form does, in which case `G3` had to exist first. Creating `G3` with
[DIMGROB](DIMGROB.md) before the call is the probe that separates them, and
it has not been run (unverified).

Until that is settled, use [SUBGROB_P](SUBGROB_P.md): it is the measured form,
and it counts corners half-open, giving 4 rather than 5 from `(0,0)` to
`(4,4)` (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SUBGROB_P](SUBGROB_P.md) · [BLIT](BLIT.md) · [DIMGROB](DIMGROB.md) ·
[C→PX](C→PX.md)
