# x₂

The second count, 26 of 50.

| | |
|---|---|
| Syntax | `x₂` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("x₂")` | `26` | [emulator](../results.tsv) |

## Behaviour

**It arrived holding 26, with nothing assigned** (emulator). This was the
first read on a calculator the harness had just reset. The Inference app
ships with a worked example loaded, so a program reading before writing gets
somebody else's data rather than a blank, and nothing in the value says it is
a default. [Alpha](Alpha.md) carries the account.

**This app differs from the two measured before it in exactly that**
(emulator). The Triangle Solver marks an unknown side −1,
[SideA](../triangle-solver/SideA.md), and the Function app leaves its
variables at 0, [Root](../function/Root-var.md). Both make the absence
visible; this one does not.

**26 of 50 against [x₁](x₁.md)'s 21 of 50** (emulator) is the
comparison a two-proportion test makes, and
[π₀](π₀.md)'s 0.5 is the null value it would be measured
against.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[x₁](x₁.md) · [π₀](π₀.md) · [n₂](n₂.md)
