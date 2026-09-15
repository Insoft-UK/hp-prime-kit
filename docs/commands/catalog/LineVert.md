# LineVert

Answers a vertical line, as an equation.

| | |
|---|---|
| Syntax | `LineVert(Expr)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LineVert(2)")` | `line(x=2)` | [emulator](../results.tsv) |

## Behaviour

`LineVert(2)` answers `line(x=2)` (emulator), a symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It answers a line rather than drawing one** (emulator), the same as
[LineHorz](LineHorz.md), which answered `line(y=2)` for the same argument in
the same batch. The two differ in the axis and in nothing else that was
measured.

What the calculator does with that value when it reaches a plot was not
measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LineHorz](LineHorz.md) · [DrawSlp](DrawSlp.md) · [LineTan](LineTan.md)
