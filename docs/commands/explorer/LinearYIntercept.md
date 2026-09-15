# LinearYIntercept

Where a line of a given slope through a point crosses the y axis.

| | |
|---|---|
| Syntax | `LinearYIntercept(x, y, m)` |
| Group | explorer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LinearYIntercept(2,3,1)")` | `1` | [emulator](../results.tsv) |

## Behaviour

`LinearYIntercept(2,3,1)` answers 1 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): three less one times
two, which is where the line of slope 1 through the point 2,3 meets the axis.

**The third argument is the slope, not a second point** (emulator). The
answer is what the arithmetic gives for that reading, and two points would
need four numbers, which is what [LinearSlope](LinearSlope.md) takes.

**The answer was known before the calculator was asked** (emulator), so this
row shows the command computing rather than echoing.

**It answered from Home without its own app being selected** (emulator), like
the rest of this group and unlike every name in `spreadsheet`. What was
active was the Function app, which is what a reset calculator has,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LinearSlope](LinearSlope.md) · [QuadDelta](QuadDelta.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
