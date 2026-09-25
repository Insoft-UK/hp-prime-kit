# Theme

The display theme, as a list of two integers.

| | |
|---|---|
| Syntax | `Theme` → list |
| Syntax | `Theme:=value` |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Theme")` | `{#1:64h,#5:64h}` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("Theme"); EXPR("Theme:=" + STRING(o)); RETURN EXPR("Theme");` | `{#1:64h,#5:64h}` | [emulator](../results.tsv) |

## Behaviour

**It is a list of two based integers** (emulator): `{#1:64h,#5:64h}` on a
reset calculator. What each one selects was not measured (unverified).

**A program can assign it** (emulator): given its own value back, it was
accepted and read back the same.

**The theme decides whether black text on white is readable** (unverified),
which is
[interface.two-themes](../../topics/interface.md#interface.two-themes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[interface.two-themes](../../topics/interface.md#interface.two-themes) · [Language](Language.md)
