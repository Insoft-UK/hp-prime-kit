# DoInference

Runs the Inference app's own test and writes the results into the app's variables.

| | |
|---|---|
| Syntax | `DoInference()` |
| Group | inference |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DoInference")` | `1` | [emulator](../results.tsv) |
| `EXPR(" DoInference( )")` | `1` | [emulator](../results.tsv) |
| `EXPR("DoInference()")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It answers with its own app active, and was refused with another**
(emulator). The first two rows were taken with the Inference app selected by
hand; the third, a batch earlier, with the Function app active, which is what
a reset calculator has,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).
The rule is
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**It writes its results into the app's variables** (emulator). Across the
first call, [TestScore](TestScore.md) went from 0 to −0.946205374811,
[Prob](Prob.md) from 0 to 0.172021922639, [CritVal1](CritVal1.md) from 0 to
0.432843347747 and [Result](Result.md) from 0 to 1, with nothing else run
between the reads. So a program collects this command's answers from those
variables; the return value is only 1.

**The same shape as [DoSolve](../triangle-solver/DoSolve.md), and the opposite
of the Function app's commands** (emulator). `DoSolve` wrote its angles into
the Triangle Solver's variables. `ROOT`, `SLOPE`, `ISECT` and `AREA` wrote
nothing into theirs, [Root](../function/Root-var.md). Two apps with a `Do`
command, both of which write, and one app whose commands take arguments and
do not: that is a pattern with a reason behind it, since a `Do` command runs
over state the app already holds and has nowhere to put its answer but back
into that state. Two apps are not every app (unverified).

**The app did not arrive empty** (emulator). It ships with a worked example --
[n₁](n₁.md) and [n₂](n₂.md) at 50, [Mean₁](Mean₁.md) at 0.461368,
[Alpha](Alpha.md) at 0.05 -- which is why this answered with no data supplied
by the program at all. What it tested was HP's example, and the numbers it
wrote are facts about that example only.

**The brackets made no difference here** (emulator). The bare name and the
bracketed form both returned 1, the second run after the first. That is the
question [DoSolve](../triangle-solver/DoSolve.md) could not settle, because
its bracketed form ran on an already-solved triangle and answered `{}`. This
entry settles it for this command and does not settle it for that one.

**This entry said the opposite until these rows existed** (emulator). It said
the command was refused from a batch, that a reset calculator left the app
holding nothing, and that measuring it would take pressing keys by hand. The refusal was
the wrong app, the app was not empty, and a batch measured it with one
selection made by hand beforehand.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TestScore](TestScore.md) · [Prob](Prob.md) · [Result](Result.md) ·
[DoSolve](../triangle-solver/DoSolve.md)
