# n₁

The first sample size, 50 in the app’s loaded example.

| | |
|---|---|
| Syntax | `n₁` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("n₁")` | `50` | [emulator](../results.tsv) |

## Behaviour

**It arrived holding 50, with nothing assigned** (emulator). This was the
first read on a calculator the harness had just reset. The Inference app
ships with a worked example loaded, so a program reading before writing gets
somebody else's data rather than a blank, and nothing in the value says it is
a default. [Alpha](Alpha.md) carries the account.

**This app differs from the two measured before it in exactly that**
(emulator). The Triangle Solver marks an unknown side −1,
[SideA](../triangle-solver/SideA.md), and the Function app leaves its
variables at 0, [Root](../function/Root-var.md). Both make the absence
visible; this one does not.

**Both samples are 50** (emulator), which is what makes the loaded example a
balanced one. Equal sizes are also the condition under which
[Pooled](Pooled.md) makes least difference, and `Pooled` read 0.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[n₂](n₂.md) · [Pooled](Pooled.md) · [DF](DF.md)
