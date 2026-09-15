# GROBW

How wide a grob is, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `GROBW(grob)` → number |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,100,50,0); RETURN GROBW(G1);` | `10` | [emulator](../results.tsv) |

## Behaviour

**A grob created 100 pixels wide measures 10 here**, while
[GROBW_P](GROBW_P.md) measures the same grob as 100 (emulator). So this form
is not in pixels, and the two are not interchangeable.

**The unit is settled: one drawing unit is ten pixels.** The point `(0,0)` of
the default view is pixel `{160,109}` and `(1,1)` is `{170,99}` (emulator),
ten pixels per unit on both axes, [C→PX](C→PX.md). A hundred pixels is ten
units, which is exactly what this answers, and [GROBH](GROBH.md) shows the
same ten on the other axis.

The factor was measured in the view a program gets before it changes
anything. Whether it follows a view the program sets itself is still open
(unverified), and the probe is the one this entry has carried from the start:
the same grob measured after the view has been set explicitly.

Use the `_P` forms when you mean pixels, which is what a program drawing an
interface almost always means (emulator: the `_P` forms give back exactly the
numbers they were given, and these do not).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GROBW_P](GROBW_P.md) · [GROBH](GROBH.md) · [C→PX](C→PX.md) ·
[interface.geometry](../../topics/interface.md#interface.geometry)
