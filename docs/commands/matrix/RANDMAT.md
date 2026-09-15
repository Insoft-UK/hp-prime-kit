# RANDMAT

A matrix of random numbers.

| | |
|---|---|
| Syntax | `RANDMAT([MatrixName,] rows, columns)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SIZE(RANDMAT(2,3))` | `{2,3}` | [emulator](../results.tsv) |

## Behaviour

**The example asks for the shape, not the contents, and that is deliberate.**
This command answers something different every time it runs, so a stored
answer would be a number no later run reproduces, and the checker would
report a disagreement whenever the batch was repeated. What can be measured
and repeated is the size: `SIZE(RANDMAT(2,3))` answers `{2,3}` (emulator).

So the shape is rows first, then columns (emulator), which is the same order
[MAKEMAT](MAKEMAT.md) takes.

What range the numbers fall in, and whether they are whole or real, was not
measured (unverified). HP's syntax shows further arguments that choose
between them, and a name to store the result into.

`RANDSEED` is the command that would make a run repeatable, and the pair has
not been measured together (unverified); it belongs to the probability group
and comes later in this phase.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MAKEMAT](MAKEMAT.md) · [SIZE](../list/SIZE.md) · [IDENMAT](IDENMAT.md)
