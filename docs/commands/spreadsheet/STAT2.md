# STAT2

Two-variable statistics over a range, refused from Home.

| | |
|---|---|
| Syntax | `STAT2(Input_Range, [Mode], ["Configuration"])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("STAT2(A1:A5)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**`STAT2(A1:A5)` is refused** (emulator), given a range in the app's own
notation.

**Eighteen of the group's twenty-two names are refused even with the Spreadsheet app active** (emulator),
and [SUM](SUM.md) carries the account and the probes.

**It is the two-variable counterpart of [STAT1](STAT1.md)** (HP help), and
both take the same three arguments, so nothing here separates them: they were
refused identically and this entry does not describe a difference it has not
seen.

What it answers from inside the Spreadsheet app is untested (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STAT1](STAT1.md) · [REGRS](REGRS.md) · [SUM](SUM.md)
