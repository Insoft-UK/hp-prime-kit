# LinearSlope

The slope of the line through two points.

| | |
|---|---|
| Syntax | `LinearSlope(x1,y1,x2,y2)` |
| Group | explorer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LinearSlope(0,0,2,1)")` | `0.5` | [emulator](../results.tsv) |

## Behaviour

`LinearSlope(0,0,2,1)` answers 0.5 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): one over two, the rise
between the origin and the point 2,1 divided by the run.

**The four arguments are two points, not a point and a vector** (emulator).
The answer is the only one consistent with reading them as x1, y1, x2, y2 in
that order; reading the middle pair as a direction would give a different
number.

**The answer was known before the calculator was asked** (emulator), which is
what makes this row evidence that the command computes rather than hands
something back. The same is true of the three names beside it in this group.

**It answered from Home without its own app being selected** (emulator).
That separates this group sharply from `spreadsheet`, whose twenty-two names
were all refused in the same batch: see [SUM](../spreadsheet/SUM.md). The
condition is not "no app open", which cannot happen -- a reset calculator has
the Function app active,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active)
-- but "some app other than this one".

What it answers for two points with the same x, where the slope is infinite,
was not run (unverified). That is the case a program has to guard.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LinearYIntercept](LinearYIntercept.md) · [QuadSolve](QuadSolve.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
