# Conf

The confidence level, which arrived at 0.99.

| | |
|---|---|
| Syntax | `Conf` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Conf")` | `0.99` | [emulator](../results.tsv) |

## Behaviour

**It came with a value already in it** (emulator). This was the first read of
the variable on a calculator the harness had just reset, and nothing had
been assigned. The Inference app ships with a worked example loaded, which
is why this read 0.99 rather than 0 or a refusal.

**That makes this app unlike the two measured before it** (emulator). The
Triangle Solver marks an unknown side with −1,
[SideA](../triangle-solver/SideA.md), and the Function app leaves its
variables at 0, [Root](../function/Root-var.md). Here a program reading
before writing gets somebody else's data rather than a blank, and nothing
in the value says it is a default.

**0.99 is a confidence level, not a probability of anything measured**
(emulator). It is the setting a confidence interval is computed at, and
[CritVal1](CritVal1.md) and [CritVal2](CritVal2.md) are what get computed
from it. [Alpha](Alpha.md) records why the two settings do not agree with
each other.

**Whether a program can set it is untested** (unverified). [Alpha](Alpha.md)
took an assignment and this was not tried, so the reasonable expectation is
that it does, and the reasonable expectation is not a row.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Alpha](Alpha.md) · [CritVal1](CritVal1.md) · [Prob](Prob.md)
