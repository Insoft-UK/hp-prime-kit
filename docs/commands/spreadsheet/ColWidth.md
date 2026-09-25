# ColWidth

A Spreadsheet setting, −1 on a reset calculator, which a program can set.

| | |
|---|---|
| Syntax | `Spreadsheet.ColWidth` → real |
| Syntax | `Spreadsheet.ColWidth:=value` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ColWidth")` | *error* | [emulator](../results.tsv) |
| `EXPR("Spreadsheet.ColWidth")` | `−1` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Spreadsheet.ColWidth"); IFERR EXPR("Spreadsheet.ColWidth:=40"); r := EXPR("Spreadsheet.ColWidth"); THEN r := "refused"; END; IFERR EXPR("Spreadsheet.ColWidth:=" + STRING(o)); THEN r := r; END; RETURN r;` | `40` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name
and its app, and nothing more.

**A program reaches it with its app's name in front** (emulator):
`Spreadsheet.ColWidth` answered `−1` with the Function app active, where
`ColWidth` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**A program can set it** (emulator): set to 40 through `Spreadsheet.ColWidth`,
it read back 40. The row reads the first value, sets another, reads again and
puts the first one back.

**HP's list gives `ColWidth RowHeight Row Col Cell` where a syntax would go**
(HP help), which reads as a menu line rather than a syntax.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RowHeight](RowHeight.md) · [Col](Col.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
