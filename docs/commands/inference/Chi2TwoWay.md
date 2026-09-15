# Chi2TwoWay

The chi-square test on a table of counts.

| | |
|---|---|
| Syntax | `Chi2TwoWay(Matrix)` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Chi2TwoWay([[10,20],[30,40]])")` | `{0.793650793651,0.372998483613,1}` | [emulator](../results.tsv) |

## Behaviour

**It answers three numbers: the statistic, its p value, and the degrees of
freedom** (emulator), a list of type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The third number is right and checks the reading** (emulator). A two-by-two
table has one degree of freedom, which is what came back, so the answer is
being computed from the shape of the matrix rather than echoed.

**A p value of 0.37 means the table shows no association** (emulator), which
is the correct conclusion for counts as evenly spread as these. That is a
second check on the answer, from the arithmetic rather than from the shape.

**It takes a matrix where the rest of this group takes lists** (HP help),
which is what a two-way table needs.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Chi2GOF](Chi2GOF.md) · [AnovaOneWay](AnovaOneWay.md)
