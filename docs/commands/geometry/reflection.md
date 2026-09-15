# reflection

Reflects an object in a line.

| | |
|---|---|
| Syntax | `reflection(Line, Object)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("reflection(segment(point(0,0),point(4,0)),point(1,2))")` | `point(1,−2)` | [emulator](../results.tsv) |

## Behaviour

**The answer was known before asking** (emulator): reflecting `point(1,2)` in
the x axis gives the point 1 across and 2 below, type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The minus is the calculator's own, U+2212** (emulator), not the hyphen a
keyboard types,
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign). The Result cell above
was built from the stored row rather than typed, because that character
cannot be typed into these files at all.

**The line comes first and the object second** (emulator), the same order
[projection](projection.md) takes and the opposite of
[is_element](is_element.md).

**A segment was accepted where the syntax says Line** (emulator), as
throughout this group.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[projection](projection.md) · [similarity](similarity.md) ·
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign)
