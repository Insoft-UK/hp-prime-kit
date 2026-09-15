# GROBH_P

How tall a grob is, in pixels.

| | |
|---|---|
| Syntax | `GROBH_P(grob)` → number |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,100,50,0); RETURN GROBH_P(G1);` | `50` | [emulator](../results.tsv) |

## Behaviour

A grob created 50 pixels tall measures 50 (emulator), so the `_P` form gives
back exactly what [DIMGROB_P](DIMGROB_P.md) was given.

[GROBH](GROBH.md) answers 5 for that same grob, and [GROBW](GROBW.md) answers
10 where [GROBW_P](GROBW_P.md) answers 100 (emulator). The pattern is
consistent, and its cause is now measured: one drawing unit is ten pixels,
[C→PX](C→PX.md).

What is left open is whether that factor follows a view the program sets
itself (unverified), which does not affect this command: the `_P` forms answer
pixels whatever the view is doing.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GROBW_P](GROBW_P.md) · [GROBH](GROBH.md) · [DIMGROB_P](DIMGROB_P.md)
