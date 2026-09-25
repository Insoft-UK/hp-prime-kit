# AFormat

The active app's number format: 0 leaves it to Home, and at 2 STRING writes a fixed number of decimals.

| | |
|---|---|
| Syntax | `AFormat` → real |
| Syntax | `AFormat:=value` |
| Group | common-app-mode |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AFormat")` | `0` | [emulator](../results.tsv) |
| `LOCAL o; o := EXPR("AFormat"); EXPR("AFormat:=" + STRING(o)); RETURN EXPR("AFormat");` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AFormat"); EXPR("AFormat:=1"); IFERR r := {EXPR("AFormat"), STRING(1/3)}; THEN r := "refused"; END; EXPR("AFormat:=" + STRING(o)); RETURN r;` | `{1,"0.333333333333"}` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AFormat"); EXPR("AFormat:=2"); IFERR r := {EXPR("AFormat"), STRING(1/3)}; THEN r := "refused"; END; EXPR("AFormat:=" + STRING(o)); RETURN r;` | `{2,"0.3333"}` | [emulator](../results.tsv) |

## Behaviour

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can assign it** (emulator): given its own value back, it was
accepted.

**At 2, `STRING` writes a fixed number of decimals** (emulator):
`STRING(1/3)` answered `"0.3333"`, four places, the number
[ADigits](ADigits.md) held, while Home's [HFormat](../home-settings/HFormat.md)
stayed at 0. At 1 it answered `"0.333333333333"`, the standard format. So
the text a program makes from a number depends on the active app as well as
on Home, [apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home); it is likely what makes the Finance app write two decimals,
[apps.finance-shows-two-decimals](../../topics/apps.md#apps.finance-shows-two-decimals),
though Finance's own format was not read (unverified).

**Its values are shifted by one against Home's** (emulator): 0 leaves the
choice to Home, and the app's own choices start at 1, where Home's start at
0. [AAngle](AAngle.md) 1 is radians and 2 degrees, where
[HAngle](../home-settings/HAngle.md) 0 is radians and 1 degrees; the same
shift holds for the complex setting and the number format.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ADigits](ADigits.md) · [HFormat](../home-settings/HFormat.md) · [apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home)
