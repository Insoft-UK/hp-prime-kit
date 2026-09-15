# EDITMAT

Opens the matrix editor on a matrix variable.

| | |
|---|---|
| Syntax | `EDITMAT(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EDITMAT(M1)` | *no value* | HP help |

## Behaviour

It hands the screen to the calculator's own matrix editor and waits for the
person using it (HP help). There is nothing to record: a batch cannot run it,
because it would sit there until somebody pressed a key, and what it answers
when the editor closes has not been measured (unverified).

It is the one command of this group that is not a calculation (HP help). The
rest take a matrix and answer a matrix, and have been run:
[SUB](SUB.md), [REPLACE](REPLACE.md) and [REDIM](REDIM.md) are how a program
changes data without asking anybody (emulator).

The interpreter does not implement it, and could not: it draws no screen
(unverified).

## Related

[SUB](SUB.md) · [REPLACE](REPLACE.md) · [REDIM](REDIM.md)
