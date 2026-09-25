# HComplex

Whether Home answers with complex numbers: at 0 the square root of a negative is refused, at 1 it is imaginary.

| | |
|---|---|
| Syntax | `HComplex` → real |
| Syntax | `HComplex:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HComplex")` | `0` | [emulator](../results.tsv) |
| `EXPR("(-4)^0.5")` | *error* | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("HComplex"); EXPR("HComplex:=1"); r := EXPR("HComplex"); EXPR("HComplex:=" + STRING(o)); RETURN r;` | `1` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("HComplex"); EXPR("HComplex:=1"); r := {EXPR("HComplex"), EXPR("(-4)^0.5")}; EXPR("HComplex:=" + STRING(o)); RETURN r;` | `{1,2*}` | [emulator](../results.tsv) |

| `LOCAL o, r; o := EXPR("HComplex"); EXPR("HComplex:=1"); IFERR r := {EXPR("HComplex"), EXPR("2 NTHROOT (-4)"), EXPR("3 NTHROOT (-8)")}; THEN r := "refused"; END; EXPR("HComplex:=" + STRING(o)); RETURN r;` | `{1,2*,−2}` | [emulator](../results.tsv) |

## Behaviour

**It reads 0 on a reset calculator, and then `(-4)^0.5` is refused**
(emulator): an error, not a value and not a string.

**Set to 1, the same power answers `2*i`** (emulator), with the imaginary
unit written as the calculator's own glyph,
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit). Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

**The active app's setting overrides it** (emulator): with the Function
app's [AComplex](../common-app-mode/AComplex.md) at 2 and this at 0,
`(-4)^0.5` answered `2*i`, [apps.app-mode-overrides-home](../../topics/apps.md#apps.app-mode-overrides-home).

**It decides `NTHROOT` too** (emulator): with it at 1, `2 NTHROOT (-4)`
answered `2*i`, where at 0 it is refused, and `3 NTHROOT (-8)` still
answered `−2`, the real root, not a complex one.

**A program that takes a square root of something that can be negative
depends on this setting** (emulator): the same line raises with it at 0 and
answers with it at 1.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HAngle](HAngle.md) · [ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit)
