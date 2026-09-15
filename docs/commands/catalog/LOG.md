# LOG

The logarithm, base ten unless another base is given.

| | |
|---|---|
| Syntax | `LOG(value, [base])` |
| Group | catalog |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOG(8)` | `0.903089986992` | [emulator](../results.tsv) |
| `LOG(8,2)` | `3` | [emulator](../results.tsv) |
| `LOG({100,10})` | `{2,1}` | [emulator](../results.tsv) |
| `LOG({8,27,10000},{2,3,10})` | `{3,3,4}` | [emulator](../results.tsv) |

## Behaviour

**With one argument it is base ten.** `LOG(8)` is 0.903089986992, not the 2.08
a natural logarithm would give (HP help). A program porting code from a
language where `log` means the natural one gets a plausible wrong number
rather than an error.

**The second argument is the base**, so `LOG(8,2)` is 3 (HP help). For the
natural logarithm the command is [LN](LN.md), and [ALOG](../arithmetic/ALOG.md)
undoes this one.

Both the value and the base may be lists, taken element by element and paired
by position: `{8,27,10000}` with `{2,3,10}` gives `{3,3,4}` (HP help). The
interpreter covers neither list form and stops on them (unverified), so those
two rows are the calculator's word alone rather than anything the PC could
confirm.

All four rows have since been run on the calculator and agree with what HP's
help states (emulator).

## Related

[LN](LN.md) · [EXP](EXP.md) · [ALOG](../arithmetic/ALOG.md)
