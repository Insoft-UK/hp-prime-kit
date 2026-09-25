# SOLVE

The Solve app's solver, which HP's list files as a variable: with the app's name in front it solves.

| | |
|---|---|
| Syntax | `Solve.SOLVE(equation,variable,guess)` → real |
| Group | solve |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SOLVE")` | *error* | [emulator](../results.tsv) |
| `EXPR("SOLVE( )")` | *error* | [emulator](../results.tsv) |
| `EXPR("SOLVE(E1,X)")` | *error* | [emulator](../results.tsv) |
| `EXPR("SOLVE(X^2-4=0,X)")` | *error* | [emulator](../results.tsv) |
| `EXPR("SOLVE(X^2-4=0,X,1)")` | *error* | [emulator](../results.tsv) |
| `EXPR("Solve.SOLVE")` | *error* | [emulator](../results.tsv) |
| `EXPR("Solve.SOLVE(X^2-4=0,X,1)")` | `2` | [emulator](../results.tsv) |
| `LOCAL r; IFERR EXPR("Solve.SOLVE:=2"); r := EXPR("Solve.SOLVE"); THEN r := "refused"; END; RETURN r;` | `"refused"` | [emulator](../results.tsv) |

## Behaviour

**Called with its app's name in front, it solves** (emulator): with the
Function app active, `Solve.SOLVE(X^2-4=0,X,1)` answered 2, a root of X²−4.
Bare, the same call and four other forms were refused under the same
condition, [apps.qualified-names](../../topics/apps.md#apps.qualified-names).

**HP's list files it as an app variable and gives it a function's syntax**
(HP help), `SOLVE(En,Var[,Guess])`. The measurement sides with the syntax.

**Which root a guess picks was not tried** (unverified): X²−4 has two, 2 and
−2, and only the guess 1 was used. A form without the guess was tried only
bare.

**Read as a variable it is refused** (emulator): `Solve.SOLVE` alone was
refused. Assigning 2 to it and reading it back was refused as a whole, and
since the read is refused anyway, that row does not say whether the assignment
was.

**[Solve](Solve.md), which differs from it only in case, was refused with the
app's name in front too** (emulator), so this is the one of the two a program
can call.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Solve](Solve.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
