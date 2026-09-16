# Solve2×2

A syntax error even with its own app active, unlike every other app function.

| | |
|---|---|
| Syntax | not published |
| Group | linear-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `Solve2×2` | *error* | G2 |
| `EXPR("Solve2×2")` | *error* | [emulator](../results.tsv) |
| `EXPR("Solve2×2( )")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It is the one name that does not follow the rule the other app functions
obey** (G2). Selecting the Linear Solver and typing the name on Home gives a
**syntax error**, where the same treatment made
[SSS](../triangle-solver/SSS.md), [SUM](../spreadsheet/SUM.md),
[ROOT](../function/ROOT.md) and [LinSolve](LinSolve.md) answer:
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**Its own group contains the counter-example** (emulator).
[LinSolve](LinSolve.md) sits in this group and now answers `{2,1}` with the
app active. The third row here was taken in that same round, with that same
app selected, and was refused; the second row predates it and was measured
with the Function app active, which is what a reset calculator has,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).
So the Linear Solver was demonstrably doing its work when this name was
refused, which is what makes the refusal belong to the name rather than to
the conditions.

**A syntax error is a different thing from a refusal** (G2). The other names
were rejected once the calculator had read them; this one is not read as a
name at all. So the likeliest reading is that it is not callable by this
spelling -- a menu item rather than a command a program can type, in the way
`NTHROOT` turned out to need an operator form and never a call.

**Empty brackets were tried because three other app commands take no
arguments** (emulator) -- [DoSolve](../triangle-solver/DoSolve.md),
[DoInference](../inference/DoInference.md) and
[Do1VStats](../statistics-1var/Do1VStats.md) all read their app's state
instead. If this name worked that way, `Solve2×2( )` with the Linear
Solver open should have reached it. It did not, which is the same negative
[Solve](../solve/Solve.md) returned.

**The screen offered no correction** (G2), unlike `translation` and
`perpendicular` in the geometry group, which replied in words saying what
they wanted. There is nothing here to follow.

**The middle character is U+00D7, the multiplication sign** (HP help), not
the letter x, and the name was typed from the calculator's own keyboard for
the first row. A file holding that character was created and read back
identical before anything was planned around it.

What form the Linear Solver accepts for a two-by-two system is still unknown
(unverified); what is known is that [LinSolve](LinSolve.md) solves one when
given the coefficients as a matrix, so the group is no longer without a
working call.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Solve3×3](Solve3×3.md) · [LinSolve](LinSolve.md) ·
[Solve](../solve/Solve.md) ·
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
