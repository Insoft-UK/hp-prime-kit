# DAYOFWEEK

Which day of the week a date falls on.

| | |
|---|---|
| Syntax | `DAYOFWEEK(date)` → number |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DAYOFWEEK(2026.0912)` | `6` | [emulator](../results.tsv) |

## Behaviour

The date goes in as `YYYY.MMDD` (emulator). 12 September 2026 is a Saturday,
and the answer is 6, so the week is numbered with **Monday as 1** rather than
Sunday (emulator). That is worth knowing before indexing a list of day names
with it, and it is the opposite convention from several languages.

Only one date has been measured, so the numbering rests on that single
reading (emulator): a Sunday would confirm whether it answers 7 or 0, and
nobody has run one.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DDAYS](DDAYS.md) · [DATEADD](DATEADD.md)
