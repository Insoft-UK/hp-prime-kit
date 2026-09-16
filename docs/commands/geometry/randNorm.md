# randNorm

A random point, which cannot have an example.

| | |
|---|---|
| Syntax | not published |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `randNorm(0,1)` | *no value* | unverified |

## Behaviour

**This name was deliberately left out of the batch** (unverified), and saying
so is more honest than an entry that reads as though nobody reached it.

**A random answer is not an example** (emulator). Whatever it returns changes
between runs, so a stored row would record one draw and the checker would
hold every later run to it. `RANDOM`, `RANDINT`, `RANDNORM`, `RANDMAT` and
`RANDSEED` met this first and settled it the same way: the entry
says what the command is for and stores nothing.

HP's list gives the name no syntax string (HP help), so even the call above is
a guess at its shape, written to show what a caller would type rather than
what was run.

**Its name does not match its family** (HP help). It sits in the `Point` menu
of the Geometry app while the Prime's other `rand` names are Home functions,
so a random *point* is the likeliest reading and nothing here confirms it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[point](point.md) · [element](element.md)
