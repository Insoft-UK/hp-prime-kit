# SAS

Two sides and the angle between them.

| | |
|---|---|
| Syntax | `SAS(side,angle,side)` |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SAS(3,50,4)")` | `{3.09404223751,82.0328713989,47.9671286011}` | [emulator](../results.tsv) |
| `EXPR("SAS(3,60,4)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It answers the missing side and the two missing angles** (emulator), type
6, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The first number is the third side and the cosine rule gives it**
(emulator): nine plus sixteen less twice three times four times the cosine of
50 degrees is 9.57, whose square root is 3.094. That is what came back, so
the command computes and the angle does sit between the two sides as its name
says.

**The two angles complete the triangle** (emulator): 82.03 and 47.97 with the
50 that was given sum to 180 exactly.

**Writing 50 as degrees was correct** (G2). This entry once warned that the
rest of the calculator works in radians, so 50 would be nearly eight full
turns. The app has its own mode,
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees),
and the warning was wrong.

**The two rows differ only in whether the Triangle Solver was active**
(emulator); [SSS](SSS.md) carries that account.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SSS](SSS.md) · [SSA](SSA.md) · [ASA](ASA.md)
