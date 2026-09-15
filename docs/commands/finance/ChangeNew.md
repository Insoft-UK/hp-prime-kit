# ChangeNew

Answers something an ordinary reading of its arguments does not explain.

| | |
|---|---|
| Syntax | `ChangeNew(old,percentage,option)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ChangeNew(100,10,0)")` | `10` | [emulator](../results.tsv) |

## Behaviour

`ChangeNew(100,10,0)` answers 10 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**That is not a hundred raised by ten per cent, which would be 110**
(emulator). Ten is a hundred *times* ten per cent, so what came back looks
like the size of the change rather than the value after it -- but this entry
does not state that as the rule, because one row cannot tell that reading
from several others.

**Its sibling behaves the same way** (emulator): [ChangeOld](ChangeOld.md)
answers 1100 for 110 and ten per cent, which is 110 times ten, not 110
reduced to its earlier value. Two of this family read as multiplications by
the percentage while the other two,
[ChangePrice](ChangePrice.md) and [ChangeCost](ChangeCost.md), read as a
proper rise and fall.

**The third argument is the likeliest explanation and it is untested**
(unverified). HP calls it an option and publishes no values for it; 0 was
used here because a probe has to pick something. The probe is the same call
with 1 and with 2, which is two rows and would either explain these answers
or rule the option out.

Until that runs, a program should not use this name expecting the value after
a change (unverified). [ChangePrice](ChangePrice.md) is measured and does
that.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ChangeOld](ChangeOld.md) · [ChangePrice](ChangePrice.md) ·
[ChangeCost](ChangeCost.md)
