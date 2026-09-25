# AComplex

The active app's setting for complex numbers: 0 leaves it to Home, and at 2 a program on Home gets complex answers.

| | |
|---|---|
| Syntax | `AComplex` → real |
| Syntax | `AComplex:=value` |
| Group | common-app-mode |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AComplex")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AComplex"); EXPR("AComplex:=1"); r := EXPR("AComplex"); EXPR("AComplex:=" + STRING(o)); RETURN r;` | `1` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AComplex"); EXPR("AComplex:=1"); IFERR r := {EXPR("AComplex"), EXPR("(-4)^0.5")}; THEN r := "refused"; END; EXPR("AComplex:=" + STRING(o)); RETURN r;` | `"refused"` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("AComplex"); EXPR("AComplex:=2"); IFERR r := {EXPR("AComplex"), EXPR("(-4)^0.5")}; THEN r := "refused"; END; EXPR("AComplex:=" + STRING(o)); RETURN r;` | `{2,2*}` | [emulator](../results.tsv) |

## Behaviour

**Measured with the Function app active** (emulator), the state every batch starts
in, [apps.reset-leaves-function-active](../../topics/apps.md#apps.reset-leaves-function-active). Whether another
app holds a different value was not tried (unverified).

**A program can set it** (emulator): set to 1, it read back 1. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

**At 2, a program on Home gets complex answers** (emulator): `(-4)^0.5`
answered `2*i`, while Home's own [HComplex](../home-settings/HComplex.md)
stayed at 0, under which the same power is refused. At 1 it was still
refused. This is [apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home).

**Its values are shifted by one against Home's** (emulator): 0 leaves the
choice to Home, and the app's own choices start at 1, where Home's start at
0. [AAngle](AAngle.md) 1 is radians and 2 degrees, where
[HAngle](../home-settings/HAngle.md) 0 is radians and 1 degrees; the same
shift holds for the complex setting and the number format.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HComplex](../home-settings/HComplex.md) · [apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home)
