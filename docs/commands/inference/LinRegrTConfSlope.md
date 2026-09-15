# LinRegrTConfSlope

A confidence interval for the slope of a linear regression.

| | |
|---|---|
| Syntax | `LinRegrTConfSlope(List1, List2, C-value)` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LinRegrTConfSlope({1,2,3},{2,4,6},0.95)")` | `{0.95,12.7062047361,1,2,0,2,2}` | [emulator](../results.tsv) |

## Behaviour

**The answer is seven numbers and the first three match its sibling's**
(emulator): the confidence level, the t value for one degree of freedom, and
that 1 itself. [LinRegrTConfInt](LinRegrTConfInt.md) carries the account of
those three.

**From the fourth onwards it differs, and the difference is the slope**
(emulator). The data lie on y equals 2x, and 2 appears where its sibling had
0, with the interval's two ends also 2 because a perfect fit leaves no
uncertainty.

**So the two commands answer the same shape about different quantities**
(emulator), which one example is enough to show here, unlike the pair
[LinRegrTMeanResp](LinRegrTMeanResp.md) and
[LinRegrTPredInt](LinRegrTPredInt.md), which this documentation could not
tell apart.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LinRegrTConfInt](LinRegrTConfInt.md) ·
[LinRegrTMeanResp](LinRegrTMeanResp.md)
