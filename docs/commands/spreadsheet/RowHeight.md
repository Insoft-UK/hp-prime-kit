# RowHeight

A Spreadsheet setting, −1 on a reset calculator, which a program can set.

| | |
|---|---|
| Syntax | `Spreadsheet.RowHeight` → real |
| Syntax | `Spreadsheet.RowHeight:=value` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("RowHeight")` | *error* | [emulator](../results.tsv) |
| `EXPR("Spreadsheet.RowHeight")` | `−1` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Spreadsheet.RowHeight"); IFERR EXPR("Spreadsheet.RowHeight:=30"); r := EXPR("Spreadsheet.RowHeight"); THEN r := "refused"; END; IFERR EXPR("Spreadsheet.RowHeight:=" + STRING(o)); THEN r := r; END; RETURN r;` | `30` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name
and its app, and nothing more.

**A program reaches it with its app's name in front** (emulator):
`Spreadsheet.RowHeight` answered `−1` with the Function app active, where
`RowHeight` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**A program can set it** (emulator): set to 30 through
`Spreadsheet.RowHeight`, it read back 30. The row reads the first value, sets
another, reads again and puts the first one back.

**HP's list gives `ColWidth RowHeight Row Col Cell` where a syntax would go**
(HP help), which reads as a menu line rather than a syntax.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ColWidth](ColWidth.md) · [Col](Col.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
