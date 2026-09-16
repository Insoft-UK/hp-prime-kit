# AngleA

The angle opposite side A, which DoSolve writes rather than reads.

| | |
|---|---|
| Syntax | `AngleA` → real |
| Group | triangle-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR(" AngleA")` | `−1` | [emulator](../results.tsv) |
| `EXPR("  AngleA")` | `36.8698976458` | [emulator](../results.tsv) |
| `EXPR("AngleA")` | *error* | [emulator](../results.tsv) |
| `EXPR("AngleA:=30")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The last two rows are the same calls with another app active** (emulator),
and they are the clearest evidence here that the app rule can reach
a variable, not only a function. It does not reach every one: most of the
Finance app's variables answer from any app,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app). In one batch, with nothing selected, both
reading and assigning were refused. In the next, with the Triangle Solver
selected and nothing else changed, both worked. Nothing about the name
changed between them.

**What was active in the refused batch was the Function app** (emulator), not
nothing: a reset calculator always has one,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).
The same batch read `Root`, `Slope` and `SignedArea` -- the Function app's own
variables -- and got 0 from all three.

**[DoSolve](DoSolve.md) wrote the second row** (emulator). Before it ran, this
read −1, the app's mark for "not given". After it ran on sides of 3, 4 and
5, it read 36.8698976458. So this variable is an output of the app, where
[SideA](SideA.md) is an input, and a program can collect its answer here
instead of from `DoSolve`'s return value.

**The number is in degrees**
(emulator), which is
[apps.triangle-solver-degrees](../../topics/apps.md#apps.triangle-solver-degrees):
36.8698976458 degrees is the smaller acute angle of a 3-4-5 triangle. In
radians it would be 0.6435. A program feeding this straight into `SIN` is
wrong and nothing raises.

**That it can be assigned is untested under the right conditions**
(unverified). The one assignment tried, `AngleA:=30`, was made with the wrong
app active and refused for that reason. Whether setting an angle and leaving
a side unknown makes `DoSolve` solve the other way round is the obvious next
row, and this documentation does not have it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AngleB](AngleB.md) · [AngleC](AngleC.md) · [SideA](SideA.md) ·
[DoSolve](DoSolve.md) ·
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active)
