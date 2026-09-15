# is_perpendicular

Whether two lines are perpendicular, which this example cannot tell from is_orthogonal.

| | |
|---|---|
| Syntax | `is_perpendicular(Line1, Line2)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("is_perpendicular(segment(point(0,0),point(4,0)),segment(point(0,0),point(0,4)))")` | `1` | [emulator](../results.tsv) |

## Behaviour

`is_perpendicular` of a segment along each axis answers 1 (emulator), type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), which is the answer
arithmetic gives.

**[is_orthogonal](is_orthogonal.md) answered the same 1 for the same two
arguments in the same batch** (emulator). Two names, one example, one answer:
nothing here separates them, and this entry says so rather than inventing a
distinction. The account and the probe are in
[is_orthogonal](is_orthogonal.md).

**The same situation has arisen twice before in this documentation**
(emulator): two unit commands in Phase 6 agreed on the pair they were given,
and so did `CashFlowMIRR` beside `CashFlowFMRR`. The answer each time was to
record the agreement, name the probe, and not guess the difference.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[is_orthogonal](is_orthogonal.md) · [perpendicular](perpendicular.md)
