# NumYStep

A setting of the Advanced Graphing app's numeric view, 0.1 on a reset calculator, which a program can set.

| | |
|---|---|
| Syntax | `Advanced_Graphing.NumYStep` → real |
| Syntax | `Advanced_Graphing.NumYStep:=value` |
| Group | advanced-graphing |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("NumYStep")` | *error* | [emulator](../results.tsv) |
| `EXPR("Advanced_Graphing.NumYStep")` | `0.1` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Advanced_Graphing.NumYStep"); IFERR EXPR("Advanced_Graphing.NumYStep:=0.5"); r := EXPR("Advanced_Graphing.NumYStep"); THEN r := "refused"; END; IFERR EXPR("Advanced_Graphing.NumYStep:=" + STRING(o)); THEN r := r; END; RETURN r;` | `0.5` | [emulator](../results.tsv) |

## Behaviour

**What it holds is read from its name** (unverified): HP's list gives the name
and its app, and nothing more. It reads as the y counterpart of
[NumStep](../common-numeric-view/NumStep.md), which the other apps' numeric
views use.

**A program reaches it with its app's name in front** (emulator):
`Advanced_Graphing.NumYStep` answered `0.1` with the Function app active,
where `NumYStep` alone was refused,
[apps.qualified-names](../../topics/apps.md#apps.qualified-names). The bare
name was not tried with its own app active (unverified).

**A program can set it** (emulator): set to 0.5 through
`Advanced_Graphing.NumYStep`, it read back 0.5. The row reads the first value,
sets another, reads again and puts the first one back.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NumXStart](NumXStart.md) · [NumStep](../common-numeric-view/NumStep.md) · [apps.qualified-names](../../topics/apps.md#apps.qualified-names)
