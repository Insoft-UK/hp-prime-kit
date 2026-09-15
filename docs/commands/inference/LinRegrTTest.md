# LinRegrTTest

The t test on a linear regression, refused for the arguments given.

| | |
|---|---|
| Syntax | `LinRegrTTest(List1, List2, AltHyp)` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LinRegrTTest(1,2,3)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Three plain numbers were sent where two lists are wanted** (HP help), the
same wrong shape [Chi2GOF](Chi2GOF.md) was given and for the same reason: a
probe asking whether failure arrives as a refusal or as text. Both refuse
outright.

**Its four siblings answered when given real lists** (emulator):
[LinRegrTConfInt](LinRegrTConfInt.md),
[LinRegrTConfSlope](LinRegrTConfSlope.md),
[LinRegrTMeanResp](LinRegrTMeanResp.md) and
[LinRegrTPredInt](LinRegrTPredInt.md) all returned lists from the same two
lists of numbers. So this row is about the call.

**The third argument names the alternative hypothesis** (HP help), which is
the one argument the four siblings do not take, and nothing here shows what
values it accepts (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LinRegrTConfInt](LinRegrTConfInt.md) · [Chi2GOF](Chi2GOF.md)
