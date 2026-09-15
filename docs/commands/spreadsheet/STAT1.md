# STAT1

One-variable statistics over a range, refused from Home.

| | |
|---|---|
| Syntax | `STAT1(Input_Range, [Mode], ["Configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("STAT1(A1:A5)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`STAT1(A1:A5)` is refused** (emulator), given a spreadsheet range written
the way the app writes one.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator),
including two that take plain lists and need no range at all, so the range is
not what this row establishes. [SUM](SUM.md) carries the account.

**This is one of the four names that would have answered something long**
(emulator), with [STAT2](STAT2.md), [REGRS](REGRS.md) and [AMORT](AMORT.md).
A one-variable summary is several numbers, so it was the best chance in this
batch of finding out whether a long answer survives the harness's
160-character width. It refused, so that question is still open after two
batches.

What it answers from inside the Spreadsheet app with a sheet holding data is
untested (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STAT2](STAT2.md) · [REGRS](REGRS.md) · [SUM](SUM.md)
