# TEXTOUT

Draws text in the coordinates of the current view.

| | |
|---|---|
| Syntax | `TEXTOUT(text, x, y, font, colour [, width])` |
| Syntax | `TEXTOUT(text, grob, x, y, font, colour [, width])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G9,512,22,0); RETURN TEXTOUT("abc",G9,0,0,2);` | `182` | [emulator](../results.tsv) |

## Behaviour

**It answers 182 where [TEXTOUT_P](TEXTOUT_P.md) answers 19** for the same
string, the same font and the same grob (emulator). Both are the x where the
drawing finished, so the two are counting in different units -- and the
factor here is not the ten that [GROBW](GROBW.md) shows against
[GROBW_P](GROBW_P.md). Neither number is explained yet, and this entry will
not invent a reason for either (unverified).

What that means in practice is simple enough: use the `_P` form when you are
placing text by pixel, which is what an interface does, and treat this one's
answer as belonging to whatever the view is (unverified: advice from the two
readings, not a rule anybody has tested).

Pass the width, in either form: without it a long string is painted over its
neighbour and off the screen, with no error (G2),
[interface.textout-width](../../topics/interface.md#interface.textout-width).

The interpreter records the call rather than drawing it, so `hpprime run`
cannot check what it painted (unverified).

## Related

[TEXTOUT_P](TEXTOUT_P.md) · [GROBW](GROBW.md) ·
[interface.textout-width](../../topics/interface.md#interface.textout-width)
