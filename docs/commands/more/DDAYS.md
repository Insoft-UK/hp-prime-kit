# DDAYS

How many days between two dates.

| | |
|---|---|
| Syntax | `DDAYS(date1, date2)` → number |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DDAYS(2026.0101,2026.0201)` | `31` | [emulator](../results.tsv) |

## Behaviour

**A date is a number**, written `YYYY.MMDD`: 1 January 2026 is `2026.0101`
(emulator). That is the calculator's own date format, and it is why a date in
a program looks like a decimal number with a suspicious number of digits.

From the first to the first of the next month is 31 days here, so it counts
the days between rather than the days including both ends (emulator). What a
second date earlier than the first gives -- a negative, or an error -- has not
been measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DATEADD](DATEADD.md) · [DAYOFWEEK](DAYOFWEEK.md)
