# Row

A Spreadsheet variable, 0 on a reset calculator, which a program cannot set.

| | |
|---|---|
| Syntax | `Spreadsheet.Row` → real |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Row")` | *error* | [emulator](../results.tsv) |
| `EXPR("Spreadsheet.Row")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Spreadsheet.Row"); IFERR EXPR("Spreadsheet.Row:=3"); r := EXPR("Spreadsheet.Row"); THEN r := "refused"; END; IFERR EXPR("Spreadsheet.Row:=" + STRING(o)); THEN r := r; END; RETURN r;` | `"refused"` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name
and its app, and nothing more.

**A program reaches it with its app's name in front** (emulator):
`Spreadsheet.Row` answered `0` with the Function app active, where `Row` alone
was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**A program cannot set it** (emulator): assigning 3 was refused, in a call
whose read of it had answered just before.

**HP's list gives `ColWidth RowHeight Row Col Cell` where a syntax would go**
(HP help), which reads as a menu line rather than a syntax.

**Its name differs from the CAS command `row` only in case** (HP help).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Col](Col.md) · [ColWidth](ColWidth.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
