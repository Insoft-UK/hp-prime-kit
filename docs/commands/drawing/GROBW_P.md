# GROBW_P

How wide a grob is, in pixels.

| | |
|---|---|
| Syntax | `GROBW_P(grob)` → number |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,100,50,0); RETURN GROBW_P(G1);` | `100` | [emulator](../results.tsv) |

## Behaviour

A grob created 100 pixels wide measures 100 (emulator), so the `_P` form
answers in the same units [DIMGROB_P](DIMGROB_P.md) was given.

**The form without `_P` does not**: the same grob measures 10 through
[GROBW](GROBW.md), because one drawing unit is ten pixels (emulator). That
factor is measured rather than guessed, and [C→PX](C→PX.md) holds the rows it
comes from.

It is also how a grob made in drawing units gets a size in pixels: a grob
made `DIMGROB(G4,10,5,0)` measures 100 through this command (emulator),
[DIMGROB](DIMGROB.md).

This is how a program finds out the size of a grob it did not create, such as
one loaded from a file (unverified), and it is half of the measured way to
measure text,
[interface.text-measure](../../topics/interface.md#interface.text-measure).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GROBW](GROBW.md) · [GROBH](GROBH.md) · [DIMGROB](DIMGROB.md)
