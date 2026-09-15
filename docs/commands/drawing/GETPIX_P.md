# GETPIX_P

The colour of one pixel.

| | |
|---|---|
| Syntax | `GETPIX_P([grob,] x, y)` → integer |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,10,10,0); RETURN GETPIX_P(G1,0,0);` | `#0h` | [emulator](../results.tsv) |

## Behaviour

**The answer is a `#` integer**, of `TYPE` 1 rather than 0 (emulator), the
same kind [RGB](RGB.md) gives. So a pixel read back can be compared with what
`RGB` answered without converting anything.

A grob created with colour 0 reads back `#0h` at its first pixel (emulator),
which is the one thing this measures: that the colour given to
[DIMGROB_P](DIMGROB_P.md) is what lands in the pixels.

Coordinates count from 0 here, not from 1: the first pixel is `(0,0)`
(emulator). That is the exception to
[ppl.one-based](../../topics/ppl.md#ppl.one-based), which is about lists and
matrices, and it is worth knowing precisely because the rest of the language
goes the other way.

What it answers outside the grob has not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RGB](RGB.md) ·
[interface.geometry](../../topics/interface.md#interface.geometry)
