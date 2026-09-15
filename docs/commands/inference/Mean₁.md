# Mean₁

The first sample mean, 0.461368 before anything was asked.

| | |
|---|---|
| Syntax | `Mean₁` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Mean₁")` | `0.461368` | [emulator](../results.tsv) |

## Behaviour

**It arrived holding 0.461368, with nothing assigned** (emulator). This was the
first read on a calculator the harness had just reset. The Inference app
ships with a worked example loaded, so a program reading before writing gets
somebody else's data rather than a blank, and nothing in the value says it is
a default. [Alpha](Alpha.md) carries the account.

**This app differs from the two measured before it in exactly that**
(emulator). The Triangle Solver marks an unknown side −1,
[SideA](../triangle-solver/SideA.md), and the Function app leaves its
variables at 0, [Root](../function/Root-var.md). Both make the absence
visible; this one does not.

**0.461368 and [Mean₂](Mean₂.md)'s 0.522851 are a pair** (emulator),
and their difference is what a two-sample test is about. With
[n₁](n₁.md) and [n₂](n₂.md) both 50 and
[s₁](s₁.md) and [s₂](s₂.md) near 0.28, that difference is
small against the spread, which is why [DoInference](DoInference.md) answered
a probability of 0.17 rather than a significant one.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Mean₂](Mean₂.md) · [s₁](s₁.md) · [n₁](n₁.md)
