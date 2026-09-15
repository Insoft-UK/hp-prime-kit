# s₁

The first sample standard deviation, 0.2776.

| | |
|---|---|
| Syntax | `s₁` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("s₁")` | `0.2776` | [emulator](../results.tsv) |

## Behaviour

**It arrived holding 0.2776, with nothing assigned** (emulator). This was the
first read on a calculator the harness had just reset. The Inference app
ships with a worked example loaded, so a program reading before writing gets
somebody else's data rather than a blank, and nothing in the value says it is
a default. [Alpha](Alpha.md) carries the account.

**This app differs from the two measured before it in exactly that**
(emulator). The Triangle Solver marks an unknown side −1,
[SideA](../triangle-solver/SideA.md), and the Function app leaves its
variables at 0, [Root](../function/Root-var.md). Both make the absence
visible; this one does not.

**It is a sample deviation, where [σ₁](σ₁.md) is a
population one** (unverified), and the app carries both: 0.2776 here against
0.2887 there. A program picking the wrong one gets a plausible number.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[s₂](s₂.md) · [σ₁](σ₁.md) · [Mean₁](Mean₁.md)
