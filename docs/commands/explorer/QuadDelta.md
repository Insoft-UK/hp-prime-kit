# QuadDelta

The discriminant of a quadratic.

| | |
|---|---|
| Syntax | `QuadDelta(a, b, c)` |
| Group | explorer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("QuadDelta(1,-3,2)")` | `1` | [emulator](../results.tsv) |

## Behaviour

`QuadDelta(1,-3,2)` answers 1 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): nine less eight, which
is b squared less four a c.

**The two rows of this group check each other** (emulator). A positive
discriminant means two distinct real roots, and
[QuadSolve](QuadSolve.md) answers `{1,2}` for the same three coefficients.
Each row supports the other's reading of the argument order.

**The answer was known before the calculator was asked** (emulator).

**It answered from Home without its own app being selected** (emulator), like
the rest of this group. What was active was the Function app, which is what a
reset calculator has,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).

What it answers when the discriminant is negative was not run (unverified),
and that is the case worth knowing, since it decides whether
[QuadSolve](QuadSolve.md) has real roots to give.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[QuadSolve](QuadSolve.md) · [LinearSlope](LinearSlope.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
