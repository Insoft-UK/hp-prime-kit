# Entry

Home's entry mode, 0 on a reset calculator.

| | |
|---|---|
| Syntax | `Entry` → real |
| Syntax | `Entry:=value` |
| Group | home-settings |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Entry")` | `0` | [emulator](../results.tsv) |
| `LOCAL o, r; o := EXPR("Entry"); EXPR("Entry:=2"); r := EXPR("Entry"); EXPR("Entry:=" + STRING(o)); RETURN r;` | `2` | [emulator](../results.tsv) |

## Behaviour

**What the values mean is not measured** (unverified): HP's list gives the
name and nothing more. It is how Home takes what is typed, so it is not
expected to change what a program computes, and no row looked for that.

**It reads 0 on a reset calculator, and a program can set it** (emulator):
set to 2, it read back 2. Each row that sets it reads the first value, sets another, reads again and
puts the first one back, so no later row of the batch saw the change.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HAngle](HAngle.md)
