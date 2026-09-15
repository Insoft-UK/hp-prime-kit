# Prob

The p-value, 0 until DoInference put 0.172021922639 in it.

| | |
|---|---|
| Syntax | `Prob` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Prob")` | `0` | [emulator](../results.tsv) |
| `EXPR(" Prob")` | `0.172021922639` | [emulator](../results.tsv) |

## Behaviour

**The pair brackets one call to [DoInference](DoInference.md)** (emulator):
0 before, 0.172021922639 after. [TestScore](TestScore.md) carries the account
of what that shows about this app.

**0.172 does not reject at either level the app was holding** (emulator).
[Alpha](Alpha.md) arrived at 0.05 and [Conf](Conf.md) at 0.99, and 0.172 is
above both thresholds, which is consistent with [Result](Result.md) answering
1 rather than something else -- though what `Result`'s codes mean is not
measured (unverified).

**A p-value of 0 before the run is not a p-value** (emulator). It is the
variable's unwritten state, and 0 is a value a real p-value can approach, so
a program cannot tell one from the other. The Triangle Solver marks an
unwritten field −1 and this app does not,
[SideA](../triangle-solver/SideA.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TestScore](TestScore.md) · [Result](Result.md) · [Alpha](Alpha.md)
