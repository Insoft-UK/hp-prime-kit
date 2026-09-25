# Time

The time of day, a real that STRING writes in hours, minutes and seconds.

| | |
|---|---|
| Syntax | `Time` → real |
| Syntax | `Time:=value` |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("TYPE(Time)")` | `0` | [emulator](../results.tsv) |

## Behaviour

**It is a real, of type 0, and its text is in hours, minutes and seconds**
(emulator): read at 14:35 it answered `14°35′00″`, with the degree, minute and
second marks, a row in [results.tsv](../results.tsv). The example states its
type, because the value changes every second.

**A program can assign it** (emulator): given its own value back, it was
accepted. Whether a different time is accepted, and moves the clock, was not
tried (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Date](Date.md) · [TYPE](../more/TYPE.md)
