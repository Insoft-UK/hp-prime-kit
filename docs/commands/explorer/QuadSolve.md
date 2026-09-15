# QuadSolve

The roots of a quadratic, as a list.

| | |
|---|---|
| Syntax | `QuadSolve(a, b, c)` |
| Group | explorer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("QuadSolve(1,-3,2)")` | `{1,2}` | [emulator](../results.tsv) |

## Behaviour

`QuadSolve(1,-3,2)` answers `{1,2}` (emulator), a list of type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): the roots of x squared
less three x plus two.

**It answers a list where its three siblings answer numbers** (emulator), so
a program has to index into it rather than use it directly in arithmetic.

**The smaller root comes first here** (emulator). One row cannot say whether
that is the rule or an accident of these coefficients, and this entry does
not claim it is a rule.

**[QuadDelta](QuadDelta.md) agrees with it** (emulator): it answers 1 for the
same coefficients, a positive discriminant, which is exactly the condition
for the two distinct real roots that came back.

**The answer was known before the calculator was asked** (emulator).

What it answers when the discriminant is negative, and whether the list then
holds complex roots or nothing at all, was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[QuadDelta](QuadDelta.md) · [LinearYIntercept](LinearYIntercept.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
