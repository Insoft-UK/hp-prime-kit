# x₁

The first count, 21 of 50 in the loaded example.

| | |
|---|---|
| Syntax | `x₁` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("x₁")` | `21` | [emulator](../results.tsv) |

## Behaviour

**It arrived holding 21, with nothing assigned** (emulator). This was the
first read on a calculator the harness had just reset. The Inference app
ships with a worked example loaded, so a program reading before writing gets
somebody else's data rather than a blank, and nothing in the value says it is
a default. [Alpha](Alpha.md) carries the account.

**This app differs from the two measured before it in exactly that**
(emulator). The Triangle Solver marks an unknown side −1,
[SideA](../triangle-solver/SideA.md), and the Function app leaves its
variables at 0, [Root](../function/Root-var.md). Both make the absence
visible; this one does not.

**21 out of [n₁](n₁.md)'s 50 is 0.42, and
[Mean₁](Mean₁.md) holds 0.461368** (emulator), so these are not the
same example: the app keeps counts for a test on proportions and means for a
test on means, and the loaded values belong to different tests. Which pair
[InfType](InfType.md) selects is not measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[x₂](x₂.md) · [n₁](n₁.md) · [InfType](InfType.md)
