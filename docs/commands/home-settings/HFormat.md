# HFormat

How Home writes numbers: 0, the standard format, on a reset calculator, and 1 for a fixed number of decimals.

| | |
|---|---|
| Syntax | `HFormat` → real |
| Syntax | `HFormat:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HFormat")` | `0` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("HFormat"); EXPR("HFormat:=" + STRING(o)); RETURN EXPR("HFormat");` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("HFormat"); EXPR("HFormat:=1"); r := {EXPR("HFormat"), STRING(1/3)}; EXPR("HFormat:=" + STRING(o)); RETURN r;` | `{1,"0.33333333"}` | [emulator](../results.tsv) |

## Behaviour

**It reads 0 on a reset calculator, and a program can set it** (emulator):
assigned its own value, it read back the same.

**Set to 1, `STRING` writes a fixed number of decimals** (emulator):
`STRING(1/3)` answered `"0.33333333"`, eight places, the number
[HDigits](HDigits.md) held. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

**`STRING` follows it, so the text a program makes from a number depends on
it** (emulator). It is the same trap as the Finance app writing every number
with two decimals,
[apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals):
a string compared against `"0.333333333333"` fails on a calculator set to
the fixed format, and nothing in the program changed.

**The active app's format overrides it** (emulator): with the Function
app's [AFormat](../common-app-mode/AFormat.md) at 2 and this at 0,
`STRING(1/3)` answered `"0.3333"`, [apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home). So Home's setting alone does not say
what `STRING` writes.

**What 2, 3 and higher do was not tried** (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HDigits](HDigits.md) · [STRING](../strings/STRING.md) · [apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals)
