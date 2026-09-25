# Bits

The size in bits of Home's integers, 32 on a reset calculator.

| | |
|---|---|
| Syntax | `Bits` → real |
| Syntax | `Bits:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Bits")` | `32` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Bits"); EXPR("Bits:=16"); r := EXPR("Bits"); EXPR("Bits:=" + STRING(o)); RETURN r;` | `16` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Bits"); EXPR("Bits:=8"); r := {EXPR("Bits"), STRING(R→B(300))}; EXPR("Bits:=" + STRING(o)); RETURN r;` | `{8,"#FFh"}` | [emulator](../results.tsv) |

## Behaviour

**It reads 32 on a reset calculator, and a program can set it** (emulator):
set to 16, it read back 16. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

**A number too large for the size is clipped, not wrapped** (emulator). With
it at 8, `STRING(R→B(300))` answered `"#FFh"`: 255, the largest 8-bit value,
where wrapping would give `#2Ch`, 44. A program counting on the wrap gets the
ceiling instead, with no error.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Base](Base.md) · [Signed](Signed.md) · [R→B](../integer/R→B.md)
