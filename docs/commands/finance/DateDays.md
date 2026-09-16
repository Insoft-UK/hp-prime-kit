# DateDays

The days between two dates, refused in the form tried here.

| | |
|---|---|
| Syntax | `DateDays(first_date,second_date,[cal_360])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DateDays(1.012024,12.312024)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator). The two arguments were written in the
shape the Prime uses to show a date, a month before the point and a day and
year after it, and the answer was an error rather than a count of days.

**Two more commands that take dates were refused in the same batch**
(emulator): [BondPrice](BondPrice.md) and [BondYield](BondYield.md), each
with dates written the same way. Three refusals sharing one argument shape is
better evidence about the shape than about the three commands.

**So the likeliest cause is the date, not the command** (unverified). Nothing
here measures what the calculator will accept: a different number of digits
in the year, a date built by the calculator itself rather than typed, or a
date held in one of the app's own variables are all untried.

The probe is one call whose date comes from the machine rather than from these
pages (unverified), which separates a bad format from a command that needs
something else entirely.

The third argument chooses a 360-day calendar (HP help) and was not reached.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BondPrice](BondPrice.md) · [BondYield](BondYield.md)
