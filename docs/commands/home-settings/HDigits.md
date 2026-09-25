# HDigits

How many decimal places Home's fixed format shows, 8 on a reset calculator.

| | |
|---|---|
| Syntax | `HDigits` → real |
| Syntax | `HDigits:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("HDigits")` | `8` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("HDigits"); EXPR("HDigits:=5"); r := EXPR("HDigits"); EXPR("HDigits:=" + STRING(o)); RETURN r;` | `5` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("HDigits"); EXPR("HDigits:=2"); r := {EXPR("HDigits"), STRING(1/3)}; EXPR("HDigits:=" + STRING(o)); RETURN r;` | `{2,"0.333333333333"}` | [emulator](../results.tsv) |
| `LOCAL f, d, r; f := EXPR("HFormat"); d := EXPR("HDigits"); EXPR("HFormat:=1"); EXPR("HDigits:=2"); r := STRING(1/3); EXPR("HDigits:=" + STRING(d)); EXPR("HFormat:=" + STRING(f)); RETURN r;` | `"0.33"` | [emulator](../results.tsv) |

## Behaviour

**It reads 8 on a reset calculator, and a program can set it** (emulator):
set to 5, it read back 5. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

**With Home in its standard format it changes nothing** (emulator): set to 2,
`STRING(1/3)` still answered `"0.333333333333"`.

**With [HFormat](HFormat.md) at 1 it sets the decimals `STRING` writes**
(emulator): both set in one row, `STRING(1/3)` answered `"0.33"`, and with
this at its default of 8 the same call answered `"0.33333333"`. So a program
building text from a number gets a string that depends on two settings it
may never have touched.

**What it does in the scientific and engineering formats was not tried**
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HFormat](HFormat.md) · [STRING](../strings/STRING.md)
