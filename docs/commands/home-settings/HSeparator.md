# HSeparator

A Home setting for how numbers are separated, 0 on a reset calculator.

| | |
|---|---|
| Syntax | `HSeparator` → real |
| Syntax | `HSeparator:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HSeparator")` | `0` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("HSeparator"); EXPR("HSeparator:=" + STRING(o)); RETURN EXPR("HSeparator");` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("HSeparator"); EXPR("HSeparator:=1"); r := {EXPR("HSeparator"), STRING(1234.5)}; EXPR("HSeparator:=" + STRING(o)); RETURN r;` | `{1,"1234.5"}` | [emulator](../results.tsv) |

## Behaviour

**What it separates is read from its name** (unverified): HP's list gives
the name and nothing more.

**It reads 0 on a reset calculator, and a program can set it** (emulator).
Set to 1 it read back 1, and `STRING(1234.5)` still answered `"1234.5"`: the
text a program makes did not follow it, where it follows
[HFormat](HFormat.md). Whether the screen does was not looked at. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HFormat](HFormat.md) · [STRING](../strings/STRING.md)
