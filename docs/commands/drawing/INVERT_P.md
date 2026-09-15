# INVERT_P

Inverts the colours of a grob, or part of one.

| | |
|---|---|
| Syntax | `INVERT_P([grob [, x1, y1, x2, y2]])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB_P(G1,10,10,0); RETURN INVERT_P(G1);` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement the drawing commands share (emulator), so
the call says nothing about what it did.

What "invert" means here has not been measured: whether a pixel of `#0h`
becomes `#FFFFFFh`, and what happens to a colour in between, would take one
[GETPIX_P](GETPIX_P.md) before and after (unverified). It is a one-line probe
and worth running before using this to highlight a selected row, which is
what it is usually for.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PIXON_P](PIXON_P.md) · [GETPIX_P](GETPIX_P.md) · [RECT_P](RECT_P.md)
