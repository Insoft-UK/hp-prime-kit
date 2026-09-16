# Solve

Refused in five forms, with and without its own app active.

| | |
|---|---|
| Syntax | not published |
| Group | solve |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Solve(2*X+1=7,X)")` | *error* | [emulator](../results.tsv) |
| `EXPR("Solve(X^2-4=0,X)")` | *error* | [emulator](../results.tsv) |
| `EXPR("Solve(X^2-4=0)")` | *error* | [emulator](../results.tsv) |
| `EXPR("Solve( )")` | *error* | [emulator](../results.tsv) |
| `EXPR("Solve")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Five forms have been tried and all five are refused** (emulator): the bare
name, two equations with their unknown, an equation alone, and empty
brackets. Three of the five -- `Solve(2*X+1=7,X)`, `Solve(X^2-4=0)` and
`Solve( )` -- were measured with the Solve app selected before the program
ran; the other two were measured earlier, with the Function
app active, which is what a reset calculator has,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active).
Five refusals across both conditions is a firm negative rather than an
untested name.

**That makes it the exception to the app rule** (emulator).
Selecting the app unblocked `SSS`, `SUM`, `ROOT` and `LinSolve`; here it
changed nothing,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).
Only [Solve2×2](../linear-solver/Solve2×2.md) and
[Solve3×3](../linear-solver/Solve3×3.md) behave the same way.

**The empty-brackets form was the most promising and it failed too**
(emulator). Three app commands read their app's own state rather
than arguments -- [DoSolve](../triangle-solver/DoSolve.md),
[DoInference](../inference/DoInference.md) and
[Do1VStats](../statistics-1var/Do1VStats.md) -- and all take no arguments. If
this name were one of those, empty brackets with the app open should have
reached it. They did not.

**HP's list gives it no syntax string** (HP help), which in this
documentation has meant an operator, a name typed from a menu rather than
written, or a command reading app state. The third is now unlikely, and the
first is odd for a word like this, so a menu name is what remains
(unverified).

**A name clash waits** (HP help): the app variable `SOLVE` differs from this
only in case, so its entry, when it is written, takes the file name
`SOLVE-var.md`, the way [Root](../function/Root-var.md) does.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DoSolve](../triangle-solver/DoSolve.md) ·
[LinSolve](../linear-solver/LinSolve.md) ·
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
