# coefDet

The coefficient of determination of a fitted line.

| | |
|---|---|
| Syntax | `coefDet` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("coefDet")` | `0` | [emulator](../results.tsv) |

## Behaviour

**It read 0 with the Inference app active and nothing assigned**
(emulator), on a calculator the harness had just reset. Its name differs by case alone from `CoefDet` in the statistics-2var group, and the two live in different folders, so neither needs a suffix.

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

[corr](corr.md) · [Inter](Inter.md) · [serrLine](serrLine.md)
