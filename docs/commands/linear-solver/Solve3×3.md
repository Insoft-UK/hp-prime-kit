# Solve3×3

A syntax error like its pair, in a group whose other name answers.

| | |
|---|---|
| Syntax | not published |
| Group | linear-solver |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Solve3×3")` | *error* | [emulator](../results.tsv) |
| `EXPR("Solve3×3( )")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The second row was taken with the Linear Solver active** (emulator), in
the same batch where [LinSolve](LinSolve.md) answered `{2,1}`.
The app was working; this name was refused anyway. The first row is older and
was measured with the Function app active -- what a reset calculator has,
[apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active)
-- so only the second is evidence about the rule.

**Its pair was also retried by hand and gave a syntax error** (G2), which
[Solve2×2](Solve2×2.md) records. This one was not retried by hand,
and its entry does not assume the same screen message -- though the two
differ only in the size of the system and have refused identically at every
call tried.

**That makes these two the exception among app functions, and no longer the group**
(emulator). Selecting the app made [SSS](../triangle-solver/SSS.md),
[SUM](../spreadsheet/SUM.md), [ROOT](../function/ROOT.md) and
[LinSolve](LinSolve.md) answer, and it did not help here:
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
names the exception explicitly rather than pretending the rule is universal.

**Empty brackets were tried and refused** (emulator), which rules out this
being an app-state command in the manner of
[DoSolve](../triangle-solver/DoSolve.md).
[Solve2×2](Solve2×2.md) carries the reasoning.

**The middle character is U+00D7** (HP help), as in its pair.

The one probe left is the hand one: type it on Home with the Linear Solver
active, as its pair was, and read whether the screen suggests anything
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Solve2×2](Solve2×2.md) · [LinSolve](LinSolve.md) ·
[Solve](../solve/Solve.md) ·
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
