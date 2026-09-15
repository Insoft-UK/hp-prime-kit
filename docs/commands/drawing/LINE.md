# LINE

Draws a straight line, in the drawing units of the current view.

| | |
|---|---|
| Syntax | `LINE([grob,] x1, y1, x2, y2 [, colour])` |
| Group | drawing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DIMGROB(G1,10,5,0); RETURN LINE(G1,0,0,9,4,RGB(0,0,255));` | `1` | [emulator](../results.tsv) |

## Behaviour

It answers 1, the acknowledgement eleven drawing commands share (emulator),
so the call says nothing about what was drawn.

**The corners are drawing units, not pixels**, and one unit is ten pixels in
the default view (emulator), [C→PX](C→PX.md). A line from `(0,0)` to `(9,4)`
therefore spans ninety pixels by forty, not nine by four, which is the
mistake worth avoiding when a program mixes the two forms.

A 0 is a legal coordinate here (emulator): the call ran with `(0,0)` as one
of its corners. That is the drawing exception to
[ppl.one-based](../../topics/ppl.md#ppl.one-based), which is about lists and
matrices.

[LINE_P](LINE_P.md) is the same command in pixels, and it is the one to
prefer when the sizes in your head are pixels (emulator: the `_P` forms give
back exactly the numbers they were given).

The interpreter records the call rather than drawing it
([interface.md](../../topics/interface.md#what-the-design-of-a-screen-comes-down-to)),
so `hpprime run` cannot check what it painted (unverified).

## Related

[LINE_P](LINE_P.md) · [RECT](RECT.md) · [C→PX](C→PX.md)
