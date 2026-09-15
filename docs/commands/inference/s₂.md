# s₂

The second sample standard deviation, 0.2943.

| | |
|---|---|
| Syntax | `s₂` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("s₂")` | `0.2943` | [emulator](../results.tsv) |

## Behaviour

**It arrived holding 0.2943, with nothing assigned** (emulator). This was the
first read on a calculator the harness had just reset. The Inference app
ships with a worked example loaded, so a program reading before writing gets
somebody else's data rather than a blank, and nothing in the value says it is
a default. [Alpha](Alpha.md) carries the account.

**This app differs from the two measured before it in exactly that**
(emulator). The Triangle Solver marks an unknown side −1,
[SideA](../triangle-solver/SideA.md), and the Function app leaves its
variables at 0, [Root](../function/Root-var.md). Both make the absence
visible; this one does not.

**It differs from [s₁](s₁.md) while
[σ₁](σ₁.md) and [σ₂](σ₂.md) do not**
(emulator): 0.2776 against 0.2943 here, and 0.2887 twice there. So the two
pairs are not two spellings of one thing.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[s₁](s₁.md) · [σ₂](σ₂.md) · [Mean₂](Mean₂.md)
