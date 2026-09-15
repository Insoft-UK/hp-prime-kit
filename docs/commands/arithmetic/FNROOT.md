# FNROOT

Finds a value of the variable that makes the expression zero.

| | |
|---|---|
| Syntax | `FNROOT(Expr, Var, [guess], [guess2])` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `FNROOT(X^2-4,X,1)` | `2` | [emulator](../results.tsv) |

## Behaviour

**The expression goes in unquoted, and the variable is named, not passed.**
`FNROOT(X^2-4,X,1)` answers 2 (emulator): the first argument is live PPL, the
second is the name to solve for, and the third is where the search starts.

`X^2-4` has two roots, -2 and 2, and starting from 1 found the positive one
(emulator). **So the guess chooses which root you get**, and a program that
needs a particular one has to start near it rather than trust the command.

A fourth argument gives a second guess (HP help), which is how a search is
bracketed rather than started from a point, and it has not been run here
(unverified). What it answers when there is no root, and whether that is an
error or a value, is also unmeasured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MAKELIST](../list/MAKELIST.md) · [EQ](../list/EQ.md)
