# ChangeCost

The cost that a price and a percentage give.

| | |
|---|---|
| Syntax | `ChangeCost(price,percentage,option)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ChangeCost(100,10,0)")` | `90.9090909091` | [emulator](../results.tsv) |

## Behaviour

`ChangeCost(100,10,0)` answers 90.9090909091 (emulator), a plain real of type
0, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes): a hundred divided by
1.1.

**It divides where [ChangePrice](ChangePrice.md) multiplies** (emulator). The
two are inverses at the same percentage, so a cost sent through one and back
through the other returns where it started.

**It is not a hundred less ten per cent** (emulator). That would be ninety,
and a program that subtracts instead of dividing is out by about one per cent
here and by more as the percentage grows. The difference is small enough to
pass a glance and large enough to matter.

The third argument is called an option and was 0 here (emulator). What
another value does was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ChangePrice](ChangePrice.md) · [ChangeNew](ChangeNew.md) ·
[ChangeOld](ChangeOld.md)
