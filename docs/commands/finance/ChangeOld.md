# ChangeOld

Answers something an ordinary reading of its arguments does not explain.

| | |
|---|---|
| Syntax | `ChangeOld(new,percentage,option)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ChangeOld(110,10,0)")` | `1100` | [emulator](../results.tsv) |

## Behaviour

`ChangeOld(110,10,0)` answers 1100 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**That is not the value before a ten per cent rise, which would be 100**
(emulator). It is 110 times ten, so the percentage appears to have been used
as a plain multiplier rather than as a percentage at all.

**[ChangeNew](ChangeNew.md) behaves the same way** and carries the full
account of what is and is not known about this family (emulator), including
the probe that would settle it: the same call with other values of the third
argument, which HP calls an option and documents no values for.

A program that needs the value before a rise has
[ChangeCost](ChangeCost.md), which divides and is measured (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ChangeNew](ChangeNew.md) · [ChangeCost](ChangeCost.md) ·
[ChangePrice](ChangePrice.md)
