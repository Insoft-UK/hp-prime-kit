# INVERT

Inverts the colours of a grob or of a rectangle of it.

| | |
|---|---|
| Syntax | `INVERT([grob] [, x1, y1, x2, y2])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,10,5,0); RETURN INVERT(G1);` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement eleven drawing commands share (emulator),
so the answer does not say what the picture looks like afterwards.

Called with a grob and nothing else it inverts the whole of it (HP help), and
that is the form measured here (emulator). What the inverted colours are was
not read back, because the pair of commands that would read a point of this
grob answers the same value whatever it holds (unverified),
[GETPIX](GETPIX.md).

With four more arguments it takes a rectangle, in drawing units like the rest
of the forms without `_P` (HP help); that form has not been run here
(unverified).

This is the usual way to show a selected row without drawing it twice
(unverified: it is what the `_P` form is used for in the example programs here,
not something measured), [INVERT_P](INVERT_P.md).

The interpreter records the call rather than drawing it
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)),
so `hpprime run` cannot check what it painted (unverified).

## Related

[INVERT_P](INVERT_P.md) · [RECT](RECT.md) · [BLIT](BLIT.md)
