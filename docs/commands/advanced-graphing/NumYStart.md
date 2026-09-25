# NumYStart

A setting of the Advanced Graphing app's numeric view, 0 on a reset calculator, which a program can set.

| | |
|---|---|
| Syntax | `Advanced_Graphing.NumYStart` → real |
| Syntax | `Advanced_Graphing.NumYStart:=value` |
| Group | advanced-graphing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("NumYStart")` | *error* | [emulator](../results.tsv) |
| `EXPR("Advanced_Graphing.NumYStart")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Advanced_Graphing.NumYStart"); IFERR EXPR("Advanced_Graphing.NumYStart:=1"); r := EXPR("Advanced_Graphing.NumYStart"); THEN r := "refused"; END; IFERR EXPR("Advanced_Graphing.NumYStart:=" + STRING(o)); THEN r := r; END; RETURN r;` | `1` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name
and its app, and nothing more. It reads as the y counterpart of
[NumStart](../common-numeric-view/NumStart.md), which the other apps' numeric
views use.

**A program reaches it with its app's name in front** (emulator):
`Advanced_Graphing.NumYStart` answered `0` with the Function app active, where
`NumYStart` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**A program can set it** (emulator): set to 1 through
`Advanced_Graphing.NumYStart`, it read back 1. The row reads the first value,
sets another, reads again and puts the first one back.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NumXStart](NumXStart.md) · [NumStart](../common-numeric-view/NumStart.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
