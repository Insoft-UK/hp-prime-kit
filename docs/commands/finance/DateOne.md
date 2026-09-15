# DateOne

The first date of a date calculation, 2017.0101 as the app arrives.

| | |
|---|---|
| Syntax | `DateOne` → real |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DateOne")` | `2017.0101` | [emulator](../results.tsv) |

## Behaviour

**It answered `2017.0101` with the Function app active, not its own** (emulator),
on a calculator the harness had just reset. Finance is the app where this is
common: 50 of its 68 variables answered from outside it, which is not what the
Triangle Solver's or the Function app's did,
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app).

**It holds the first of two dates** (unverified): HP’s list gives this name and its app,
and nothing more.

**2017.0101 is a default, and all five date variables of this app arrived
holding it** (emulator). Read in the YYYY.MMDD form HP's date values take, it
is 1 January 2017, which is untested here (unverified). A program reading it
as a plain number gets 2017.0101.

**Whether a program can set it is untested** (unverified). [PV](PV.md) took
`PV:=1000` and kept it with the Finance app active, so a Finance variable can
be written; this one was not tried.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DateTwo](DateTwo.md) · [DateDiff](DateDiff.md) · [SetDate](SetDate.md)
