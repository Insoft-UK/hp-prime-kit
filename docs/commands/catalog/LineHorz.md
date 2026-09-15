# LineHorz

Answers a horizontal line, as an equation.

| | |
|---|---|
| Syntax | `LineHorz(Exp)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LineHorz(2)")` | `line(y=2)` | [emulator](../results.tsv) |

## Behaviour

`LineHorz(2)` answers `line(y=2)` (emulator), a symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It answers a line rather than drawing one** (emulator). The name reads like
a drawing command and the answer is an equation, so a program that expects
pixels to change gets a value instead. What the calculator does with that
value when it reaches a plot was not measured (unverified).

[LineVert](LineVert.md) is its pair and answers `line(x=2)` for the same
argument (emulator), which is what says the two differ in the axis and not in
anything else.

The argument is called an expression by HP (HP help), so a name or a formula
may work where this row used a number. Neither was run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LineVert](LineVert.md) · [DrawSlp](DrawSlp.md) · [LineTan](LineTan.md)
