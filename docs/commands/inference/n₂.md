# n₂

The second sample size, also 50.

| | |
|---|---|
| Syntax | `n₂` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("n₂")` | `50` | [emulator](../results.tsv) |

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

**It matches [n₁](n₁.md) exactly** (emulator). Two equal samples of
50 give 98 degrees of freedom for the usual two-sample test, and
[DF](DF.md) read 0 before [DoInference](DoInference.md) ran -- so the app
computes that rather than keeping it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[n₁](n₁.md) · [DF](DF.md) · [Method](Method.md)
