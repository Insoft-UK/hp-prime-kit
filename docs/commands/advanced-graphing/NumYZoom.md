# NumYZoom

A setting of the Advanced Graphing app's numeric view, 2 on a reset calculator, which a program can set.

| | |
|---|---|
| Syntax | `Advanced_Graphing.NumYZoom` → real |
| Syntax | `Advanced_Graphing.NumYZoom:=value` |
| Group | advanced-graphing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("NumYZoom")` | *error* | [emulator](../results.tsv) |
| `EXPR("Advanced_Graphing.NumYZoom")` | `2` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Advanced_Graphing.NumYZoom"); IFERR EXPR("Advanced_Graphing.NumYZoom:=4"); r := EXPR("Advanced_Graphing.NumYZoom"); THEN r := "refused"; END; IFERR EXPR("Advanced_Graphing.NumYZoom:=" + STRING(o)); THEN r := r; END; RETURN r;` | `4` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name
and its app, and nothing more. It reads as the y counterpart of
[NumZoom](../common-numeric-view/NumZoom.md), which the other apps' numeric
views use.

**A program reaches it with its app's name in front** (emulator):
`Advanced_Graphing.NumYZoom` answered `2` with the Function app active, where
`NumYZoom` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**A program can set it** (emulator): set to 4 through
`Advanced_Graphing.NumYZoom`, it read back 4. The row reads the first value,
sets another, reads again and puts the first one back.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NumXStart](NumXStart.md) · [NumZoom](../common-numeric-view/NumZoom.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
