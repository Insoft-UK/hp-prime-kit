# EXPM1

e raised to the value, minus one.

| | |
|---|---|
| Syntax | `EXPM1(value)` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPM1(0.5)` | `0.6487212707` | [emulator](../results.tsv) |

## Behaviour

`EXPM1(0.5)` is 0.6487212707 (emulator), which is e to the half less one.

**The point of having it is precision near zero.** For a small value, `EXP(x)`
is close to 1 and subtracting 1 from it throws away most of the digits that
mattered; this computes the difference directly and keeps them (unverified:
that is the reason the name exists in other languages, and nothing here has
measured the difference on a Prime). The probe that would show it is
`EXPM1(1e-12)` against `EXP(1e-12)-1`, and it has not been run.

[LNP1](LNP1.md) is the matching function on the other side, and the two are
used together for the same reason (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[LNP1](LNP1.md) · [ALOG](ALOG.md)
