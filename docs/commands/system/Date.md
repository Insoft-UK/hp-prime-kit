# Date

Today's date as a real, the year before the point and the month and day after it.

| | |
|---|---|
| Syntax | `Date` → real |
| Syntax | `Date:=value` |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TYPE(Date)")` | `0` | [emulator](../results.tsv) |

## Behaviour

**It is a real, of type 0, written year.monthday** (emulator): read on
2026-09-24 it answered 2026.0924, a row in
[results.tsv](../results.tsv). The example states its type, not its value,
because the value is different every day.

**A program can assign it** (emulator): given its own value back, it was
accepted and read back the same. Whether it accepts a different date, and
whether that changes the calculator's clock, was not tried (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Time](Time.md) · [TYPE](../more/TYPE.md)
