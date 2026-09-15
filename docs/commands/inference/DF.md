# DF

The degrees of freedom.

| | |
|---|---|
| Syntax | `DF` → real |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DF")` | `0` | [emulator](../results.tsv) |

## Behaviour

**It read 0 with the Inference app active and nothing assigned**
(emulator), on a calculator the harness had just reset. Two samples of 50 -- [n₁](n₁.md) and [n₂](n₂.md) -- give 98 for the usual two-sample test, and this held 0 before the run, so the app computes it rather than keeping it.

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

[DFerr](DFerr.md) · [n₁](n₁.md) · [Method](Method.md)
