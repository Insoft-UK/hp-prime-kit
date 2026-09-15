# LinRegrTPredInt

A prediction interval at a value, indistinguishable here from LinRegrTMeanResp.

| | |
|---|---|
| Syntax | `LinRegrTPredInt(List1, List2, X-value, C-value)` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LinRegrTPredInt({1,2,3},{2,4,6},2,0.95)")` | `{2,0.95,12.7062047361,1,4,0,4,4}` | [emulator](../results.tsv) |

## Behaviour

**[LinRegrTMeanResp](LinRegrTMeanResp.md) answered the same eight numbers for
the same call** (emulator), so nothing here separates the two commands. That
entry carries the account, the reason the two collapse together on this data,
and the probe that would tell them apart.

**The answer is right as far as it goes** (emulator): the data lie on y
equals 2x, so 4 is the response at x of 2, and the interval has no width
because the fit is exact.

**A prediction interval should be wider than a mean response interval**
(HP help) on any data with spread, so the pair is worth distinguishing before
either is used in a program.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LinRegrTMeanResp](LinRegrTMeanResp.md) ·
[LinRegrTConfSlope](LinRegrTConfSlope.md)
