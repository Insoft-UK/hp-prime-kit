# LinRegrTConfInt

A confidence interval for a linear regression.

| | |
|---|---|
| Syntax | `LinRegrTConfInt(List1, List2, C-value)` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LinRegrTConfInt({1,2,3},{2,4,6},0.95)")` | `{0.95,12.7062047361,1,0,0,0,0}` | [emulator](../results.tsv) |

## Behaviour

**The answer is a list of seven numbers** (emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), beginning with the
confidence level it was given and then a t value.

**The second number is the t for one degree of freedom** (emulator).
12.706 is the classical two-tailed t at 95 per cent with one degree of
freedom, and three points fitted by a line leave exactly one. That is what
says the command computed rather than echoed.

**The four zeros at the end are the fit being perfect** (emulator). The data
given lie exactly on the line y equals 2x, so there is no residual spread and
the interval has no width. A program reading a zero interval as a failure
would be wrong.

**Its three siblings answer the same shape with different numbers**
(emulator): [LinRegrTConfSlope](LinRegrTConfSlope.md) differs from the fourth
entry onwards, and the two response commands take an extra x value in front.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LinRegrTConfSlope](LinRegrTConfSlope.md) ·
[LinRegrTMeanResp](LinRegrTMeanResp.md) · [LinRegrTTest](LinRegrTTest.md)
