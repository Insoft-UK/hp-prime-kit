# Mean₂

The second sample mean, 0.522851 before anything was asked.

| | |
|---|---|
| Syntax | `Mean₂` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Mean₂")` | `0.522851` | [emulator](../results.tsv) |

## Behaviour

**It arrived holding 0.522851, with nothing assigned** (emulator). This was the
first read on a calculator the harness had just reset. The Inference app
ships with a worked example loaded, so a program reading before writing gets
somebody else's data rather than a blank, and nothing in the value says it is
a default. [Alpha](Alpha.md) carries the account.

**This app differs from the two measured before it in exactly that**
(emulator). The Triangle Solver marks an unknown side −1,
[SideA](../triangle-solver/SideA.md), and the Function app leaves its
variables at 0, [Root](../function/Root-var.md). Both make the absence
visible; this one does not.

**It is the larger of the pair** (emulator), against
[Mean₁](Mean₁.md)'s 0.461368. [TestScore](TestScore.md) came out
negative, which is the sign of that difference taken the other way round: the
first mean less the second.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Mean₁](Mean₁.md) · [s₂](s₂.md) · [TestScore](TestScore.md)
