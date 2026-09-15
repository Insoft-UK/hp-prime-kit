# GETPIX

The colour of one point, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `GETPIX([grob,] x, y)` → integer |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,10,5,0); RETURN GETPIX(G1,0,0);` | `#FF000000h` | [emulator](../results.tsv) |

## Behaviour

The answer is a `#` integer of `TYPE` 1, the same kind [RGB](RGB.md) gives
(emulator).

**It is not the same number the `_P` form gives for the same grob**:
[GETPIX_P](GETPIX_P.md) reads `#0h` at the first pixel of a grob created with
colour 0, and this reads `#FF000000h` (emulator). Two answers for what looks
like the same question, so one of the two readings of the syntax is wrong,
and this entry does not guess which.

**Three probes answered `#FF000000h` and one of them was a grob filled red**
(emulator): this call, [PIXON](PIXON.md) after painting a pixel red, and
[PIXOFF](PIXOFF.md) after clearing one on a red grob. An answer that does not
move when the picture underneath changes is not measuring the picture, which
is what these three rows record.

The hypothesis is that the point lands outside the grob, because a drawing
unit is ten pixels ([C→PX](C→PX.md)) and the coordinates of a grob may be the
view's rather than its own, putting `(0,0)` and `(1,1)` off a picture only 10
by 5 units wide (unverified). What would settle it is painting with this form
and reading back with [GETPIX_P](GETPIX_P.md), so that the write and the read
do not share the mistake (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GETPIX_P](GETPIX_P.md) · [PIXON](PIXON.md) · [RGB](RGB.md) ·
[C→PX](C→PX.md)
