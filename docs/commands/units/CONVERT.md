# CONVERT

Changes a value from one unit into another.

| | |
|---|---|
| Syntax | `CONVERT(Value_Unit1, 1_Unit2)` |
| Group | units |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CONVERT(2_m, 1_ft)` | `6.56167979003_ft` | [emulator](../results.tsv) |

## Behaviour

`CONVERT(2_m, 1_ft)` answers 6.56167979003 feet (emulator): two metres in the
unit asked for.

**The second argument is a unit written with a coefficient of 1**, not a bare
name (emulator). `1_ft` is how the target is spelled, which is the same shape
[UPART](UPART.md) answers with.

The answer carries its unit and is type 9 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). To get a plain number
out of it, [UVAL](UVAL.md) is the next call.

**[UFACTOR](UFACTOR.md) answered exactly the same thing for this pair**
(emulator), so one example cannot tell the two commands apart. What separates
them was not measured (unverified), and the probe is a compound unit, where a
conversion and a factoring should differ.

What it does when the two units do not measure the same kind of thing was not
run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[UFACTOR](UFACTOR.md) · [UVAL](UVAL.md) · [MKSA](MKSA.md)
