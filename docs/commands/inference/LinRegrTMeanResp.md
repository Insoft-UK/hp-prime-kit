# LinRegrTMeanResp

An interval for the mean response at a value, indistinguishable here from LinRegrTPredInt.

| | |
|---|---|
| Syntax | `LinRegrTMeanResp(List1, List2, X_value, C-value)` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("LinRegrTMeanResp({1,2,3},{2,4,6},2,0.95)")` | `{2,0.95,12.7062047361,1,4,0,4,4}` | [emulator](../results.tsv) |

## Behaviour

**The answer is eight numbers, one more than its two siblings** (emulator),
type 6, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). The extra one
is at the front: the x value the question was asked at.

**The 4 is the prediction and it is right** (emulator). The data lie on y
equals 2x, so at x of 2 the response is 4, and it appears three times over
with a zero width between, because a perfect fit leaves no uncertainty.

**[LinRegrTPredInt](LinRegrTPredInt.md) answered exactly the same eight
numbers** (emulator), from the same call. One example cannot tell the two
commands apart, and this entry does not invent a difference it has not seen.

**The two should differ on real data** (HP help): a mean response is the
average at that x, a prediction interval is for a single new observation, and
the second is the wider of the two. With no spread in the data both collapse
to the same answer, which is why this example cannot separate them. The probe
is data that does not lie exactly on a line.

**This documentation has met that situation three times now** (emulator),
with two unit commands in Phase 6, with `CashFlowMIRR` beside
`CashFlowFMRR`, and with `is_orthogonal` beside `is_perpendicular`. The
answer each time is the same: record the agreement, name the probe, guess
nothing.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LinRegrTPredInt](LinRegrTPredInt.md) · [LinRegrTConfInt](LinRegrTConfInt.md)
