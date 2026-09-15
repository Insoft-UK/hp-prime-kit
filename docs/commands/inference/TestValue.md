# TestValue

The hypothesised value the test is measured against.

| | |
|---|---|
| Syntax | `TestValue` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TestValue")` | `0` | [emulator](../results.tsv) |

## Behaviour

**It read 0 with the Inference app active and nothing assigned**
(emulator), on a calculator the harness had just reset. It is the general form of what [μ₀](μ₀.md) and [π₀](π₀.md) hold for particular tests, and those two arrived at 0.5 while this stayed at 0.

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

[μ₀](μ₀.md) · [π₀](π₀.md) · [TestScore](TestScore.md)
