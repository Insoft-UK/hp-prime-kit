# AAngle

The active app's angle mode: 0 leaves it to Home, 1 is radians and 2 degrees, and a program on Home follows it.

| | |
|---|---|
| Syntax | `AAngle` → real |
| Syntax | `AAngle:=value` |
| Group | common-app-mode |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AAngle")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AAngle"); EXPR("AAngle:=2"); r := EXPR("AAngle"); EXPR("AAngle:=" + STRING(o)); RETURN r;` | `2` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AAngle"); EXPR("AAngle:=0"); IFERR r := {EXPR("AAngle"), SIN(90)}; THEN r := "refused"; END; EXPR("AAngle:=" + STRING(o)); RETURN r;` | `{0,0.893996663601}` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AAngle"); EXPR("AAngle:=1"); IFERR r := {EXPR("AAngle"), SIN(90)}; THEN r := "refused"; END; EXPR("AAngle:=" + STRING(o)); RETURN r;` | `{1,0.893996663601}` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AAngle"); EXPR("AAngle:=2"); IFERR r := {EXPR("AAngle"), SIN(90)}; THEN r := "refused"; END; EXPR("AAngle:=" + STRING(o)); RETURN r;` | `{2,1}` | [emulator](../results.tsv) |

## Behaviour

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program on Home follows it** (emulator). Set to 2, `SIN(90)` answered 1,
in degrees, while [HAngle](../home-settings/HAngle.md) stayed at 0, radians.
Set to 1, it answered 0.893996663601, the sine of 90 radians. This is
[apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home).

**At 0, its reset value, Home's setting decides** (emulator): set to 0,
`SIN(90)` answered 0.893996663601 with `HAngle` at 0, radians, and in
another batch `HAngle` set to 1 made it answer 1.

**A program can set it** (emulator): set to 2, it read back 2. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HAngle](../home-settings/HAngle.md) · [apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home)
