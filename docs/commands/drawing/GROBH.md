# GROBH

How tall a grob is, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `GROBH(grob)` → number |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,100,50,0); RETURN GROBH(G1);` | `5` | [emulator](../results.tsv) |

## Behaviour

A grob created 50 pixels tall answers 5 (emulator): the same factor of ten
[GROBW](GROBW.md) shows on the other axis, which is what makes the unit a
property of these forms rather than an oddity of one of them.

**That factor is measured.** One drawing unit is ten pixels on both axes, from
the point `(0,0)` being pixel `{160,109}` and `(1,1)` being `{170,99}`
(emulator), [C→PX](C→PX.md). Fifty pixels is five units, which is what this
answers.

For pixels, [GROBH_P](GROBH_P.md) answers 50 for that same grob (emulator),
so the pair is measured on both sides and neither number is expected rather
than seen.

Whether the factor follows a view the program sets itself has not been
measured (unverified), and [GROBW](GROBW.md) carries the probe.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GROBW](GROBW.md) · [GROBH_P](GROBH_P.md) · [C→PX](C→PX.md)
