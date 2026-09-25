# Signed

Whether Home's integers are signed, 0 on a reset calculator.

| | |
|---|---|
| Syntax | `Signed` → real |
| Syntax | `Signed:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Signed")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Signed"); EXPR("Signed:=1"); r := EXPR("Signed"); EXPR("Signed:=" + STRING(o)); RETURN r;` | `1` | [emulator](../results.tsv) |

## Behaviour

**What it does is read from its name** (unverified): HP's list gives the name
and nothing more, and no row measured its effect.

**It reads 0 on a reset calculator, and a program can set it** (emulator):
set to 1, it read back 1. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Base](Base.md) · [Bits](Bits.md)
