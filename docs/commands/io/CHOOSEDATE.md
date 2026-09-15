# CHOOSEDATE

Offers a calendar and puts the chosen date in a variable.

| | |
|---|---|
| Syntax | `CHOOSEDATE(var, ["title"], [min_date], [max_date])` |
| Group | io |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CHOOSEDATE(D)` | *no value* | HP help |

## Behaviour

There is nothing to record: it waits for a person to pick a day (HP help).

The dates it deals in are the calculator's own `YYYY.MMDD` numbers, the same
shape [DDAYS](../more/DDAYS.md) and [DATEADD](../more/DATEADD.md) take
(emulator): 1 January 2026 is `2026.0101`. That is measured for those two
commands rather than for this one, and the bounds here are described by HP
as dates (HP help).

What it answers when cancelled, and whether the variable is left alone, has
not been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DDAYS](../more/DDAYS.md) · [DATEADD](../more/DATEADD.md) ·
[CHOOSE](CHOOSE.md)
