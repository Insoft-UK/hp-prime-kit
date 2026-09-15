# PercentChange

How far the new value is from the old one, as a percentage of the old.

| | |
|---|---|
| Syntax | `PercentChange(old,new)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("PercentChange(100,110)")` | `10` | [emulator](../results.tsv) |

## Behaviour

`PercentChange(100,110)` answers 10 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): 110 is ten per cent
above 100.

**The answer is the change, not the total** (emulator).
[PercentTotal](PercentTotal.md) takes the same two arguments and answers 110,
which is the new value as a percentage of the old. One says how much it
moved, the other says where it landed, and confusing them is off by a
hundred.

The arguments go old first, new second (HP help), and the answer is
consistent with that order: the other way round would give a negative number
near nine.

What it answers when the old value is zero was not run (unverified), and that
is the case a program has to guard, since the division has nothing to divide
by.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PercentTotal](PercentTotal.md) · [PercentMargin](PercentMargin.md) ·
[PercentMarkup](PercentMarkup.md)
