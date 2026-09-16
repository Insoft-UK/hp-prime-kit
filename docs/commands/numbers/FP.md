# FP

The fractional part of a value, with the whole part dropped.

| | |
|---|---|
| Syntax | `FP(value)` |
| Group | numbers |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `FP(23.2)` | `0.2` | [emulator](../results.tsv) |
| `FP(-23.2)` | `-0.2` | [emulator](../results.tsv) |
| `FP({23.2,15+1/4,51/2,10-4/5})` | `{0.2,0.25,0.5,0.2}` | [emulator](../results.tsv) |

## Behaviour

**The fraction keeps the sign of the value**: `FP(-23.2)` is -0.2, not 0.2
(HP help). So `IP(v) + FP(v)` gives back `v` for a negative number as well as
a positive one, which would not hold if the sign were dropped.

**`0.2` is not exactly what a binary machine holds.** Running `FP(23.2)` on
the PC answers 0.1999999999999993, and the checker treats that and HP's `0.2`
as the same number because it compares within a small tolerance (unverified:
the interpreter on the PC, not a calculator). A program that compares
the result with `== 0.2` will find they differ, and that is a real trap rather
than a rounding curiosity.

A list is taken element by element (HP help), and the interpreter covers the
plain form but not the list one (unverified: the interpreter on the PC,
not a calculator).

## Related

[IP](IP.md) · [ROUND](ROUND.md) · [FLOOR](FLOOR.md)
