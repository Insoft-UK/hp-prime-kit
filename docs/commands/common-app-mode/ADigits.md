# ADigits

The active app's number of digits, 4 on a reset calculator, which STRING follows once the app's format is fixed.

| | |
|---|---|
| Syntax | `ADigits` → real |
| Syntax | `ADigits:=value` |
| Group | common-app-mode |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ADigits")` | `4` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("ADigits"); EXPR("ADigits:=3"); r := EXPR("ADigits"); EXPR("ADigits:=" + STRING(o)); RETURN r;` | `3` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("ADigits"); EXPR("ADigits:=2"); IFERR r := {EXPR("ADigits"), STRING(1/3)}; THEN r := "refused"; END; EXPR("ADigits:=" + STRING(o)); RETURN r;` | `{2,"0.333333333333"}` | [emulator](../results.tsv) |
| `LOCAL f, d, r; f := EXPR("AFormat"); d := EXPR("ADigits"); EXPR("AFormat:=2"); EXPR("ADigits:=2"); IFERR r := STRING(1/3); THEN r := "refused"; END; EXPR("ADigits:=" + STRING(d)); EXPR("AFormat:=" + STRING(f)); RETURN r;` | `"0.33"` | [emulator](../results.tsv) |

## Behaviour

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can set it** (emulator): set to 3, it read back 3. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

**`STRING` follows it once [AFormat](AFormat.md) is 2** (emulator): with
both at 2, `STRING(1/3)` answered `"0.33"`, and with the format at 2 and
this at its default of 4, `"0.3333"`. With the format left at 0, set to 2 it
changed nothing, as Home's own [HDigits](../home-settings/HDigits.md)
changes nothing in the standard format.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AFormat](AFormat.md) · [HDigits](../home-settings/HDigits.md) · [apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home)
