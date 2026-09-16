# EXP

e raised to the value.

| | |
|---|---|
| Syntax | `EXP(value)` |
| Group | catalog |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXP(5)` | `148.413159103` | [emulator](../results.tsv) |
| `EXP({-2.3,0})` | `{0.100258843723,1}` | [emulator](../results.tsv) |

## Behaviour

`EXP(5)` is 148.413159103 (HP help).

**HP prints that rounded.** The interpreter answers 148.41315910258, and the
checker treats the two as the same number because it compares within a small
tolerance (unverified: the interpreter on the PC, not a calculator). A
test expecting HP's printed digits will not match.

A list is taken element by element, and the zero in it answers 1 (emulator),
which is the value worth recognising: anything raised to nothing is one. The
interpreter does not cover the list form and stops on it (unverified), so
that row is the calculator's word alone.

[LN](LN.md) undoes it (HP help). [EXPM1](../arithmetic/EXPM1.md) is the
variant that keeps precision for a small argument, where subtracting one
afterwards would throw the digits away, and [ALOG](../arithmetic/ALOG.md)
is the base-ten counterpart.

## Related

[LN](LN.md) · [EXPM1](../arithmetic/EXPM1.md) · [ALOG](../arithmetic/ALOG.md)
