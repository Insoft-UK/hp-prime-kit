# DATEADD

The date a number of days later.

| | |
|---|---|
| Syntax | `DATEADD(date, days)` → date |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DATEADD(2026.0101,30)` | `2026.0131` | [emulator](../results.tsv) |

## Behaviour

Dates go in and come out in the calculator's `YYYY.MMDD` form (emulator):
thirty days after 1 January 2026 is the 31st of the same month, which is what
`2026.0131` says.

It carries into the next month on its own, so the arithmetic is real and not
just an addition on the decimal part -- but that is exactly what the measured
call does **not** show, since it stays inside January. What a crossing into
the next month, or into the next year, answers has not been measured here
(unverified), and it is the first thing to probe before trusting it.

A negative number of days has not been measured either (unverified);
[DDAYS](DDAYS.md) is the measured way to go the other way, from two dates to
a count.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DDAYS](DDAYS.md) · [DAYOFWEEK](DAYOFWEEK.md)
