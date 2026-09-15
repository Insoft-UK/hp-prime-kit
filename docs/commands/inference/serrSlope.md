# serrSlope

The standard error of the slope.

| | |
|---|---|
| Syntax | `serrSlope` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("serrSlope")` | `0` | [emulator](../results.tsv) |

## Behaviour

**It read 0 with the Inference app active and nothing assigned**
(emulator), on a calculator the harness had just reset. It is the error attached to the slope, and the slope itself has no variable of its own in this group -- only [Inter](Inter.md) does.

**Whether [DoInference](DoInference.md) writes it is untested** (unverified).
One run was measured, and the four variables watched across it were
[TestScore](TestScore.md), [Prob](Prob.md), [CritVal1](CritVal1.md) and
[Result](Result.md) -- all four moved off 0. This one was read before that run
and not after, so its 0 is a starting value and nothing more.

**0 is not a marker for "not set" in this app** (emulator). The Triangle
Solver uses −1, which a program can test for,
[SideA](../triangle-solver/SideA.md); here a stored 0 and an untouched 0 are
the same thing.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[serrInter](serrInter.md) · [serrLine](serrLine.md) · [corr](corr.md)
