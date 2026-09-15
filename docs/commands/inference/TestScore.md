# TestScore

The test statistic, 0 until DoInference put −0.946205374811 in it.

| | |
|---|---|
| Syntax | `TestScore` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TestScore")` | `0` | [emulator](../results.tsv) |
| `EXPR(" TestScore")` | `−0.946205374811`  | [emulator](../results.tsv) |

## Behaviour

**The pair brackets one call to [DoInference](DoInference.md)** (emulator).
It read 0 before, −0.946205374811 after, and nothing else ran between
them. So this app's `Do` command writes its results into the app's variables,
exactly as [DoSolve](../triangle-solver/DoSolve.md) does and exactly as the
Function app's commands do not, [Root](../function/Root-var.md).

**The sign is the calculator's own U+2212** (emulator),
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign), and it is negative
because [Mean₁](Mean₁.md) is smaller than
[Mean₂](Mean₂.md): the difference is taken first minus second.

**A statistic of about one in magnitude is not a significant one** (emulator),
and [Prob](Prob.md) agrees at 0.172. Both were computed from the example the
app arrived with, so neither is a fact about anything but that example.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Prob](Prob.md) · [CritVal1](CritVal1.md) · [DoInference](DoInference.md)
