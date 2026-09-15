# Depreciate

Depreciation over the life of an asset, refused in the form tried here.

| | |
|---|---|
| Syntax | `Depreciate(method, cost, salvage, life, [first], [factor])` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Depreciate(\"SL\",1000,100,5)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator). The method was sent as the string `"SL"`,
for straight line, with a cost of a thousand, a salvage of a hundred and a
life of five.

**The method is the argument nothing is known about** (emulator). HP's list
names it and gives no values for it (HP help), so a string was chosen because
a method has to be named somehow. The refusal says that choice was wrong, or
that something else in the call was, and it does not say which.

**It is the only finance command refused that takes no date** (emulator),
which separates it from [DateDays](DateDays.md),
[BondPrice](BondPrice.md) and [BondYield](BondYield.md), whose shared suspect
is the date shape. Whatever is wrong here is its own.

The probes worth one row each (unverified): the method as a bare name rather
than a string, and the method as a number, which is how several HP apps
select a mode.

The last two arguments are optional (HP help) and were not reached.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BondPrice](BondPrice.md) · [CashFlowTotal](CashFlowTotal.md)
