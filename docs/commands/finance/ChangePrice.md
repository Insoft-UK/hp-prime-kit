# ChangePrice

The price that a cost and a percentage give.

| | |
|---|---|
| Syntax | `ChangePrice(cost,percentage,option)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ChangePrice(60,10,0)")` | `66` | [emulator](../results.tsv) |

## Behaviour

`ChangePrice(60,10,0)` answers 66 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): sixty raised by ten per
cent.

**[ChangeCost](ChangeCost.md) undoes it** (emulator). Given a hundred and the
same ten per cent it answers 90.9090909091, which is a hundred divided by
1.1, so the pair go up and down the same step.

**The third argument is called an option and nothing here says what it
selects** (emulator). It was 0 in this row, and 0 gives the plain reading
above. What any other value does was not run (unverified), and it matters,
because two of the four names in this family answer something the same
reading does not explain -- see [ChangeNew](ChangeNew.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ChangeCost](ChangeCost.md) · [ChangeNew](ChangeNew.md) ·
[ChangeOld](ChangeOld.md)
