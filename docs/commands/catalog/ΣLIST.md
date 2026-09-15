# ΣLIST

The sum of every element of a list.

| | |
|---|---|
| Syntax | `ΣLIST(list)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ΣLIST({1,2,3,4})` | `10` | [emulator](../results.tsv) |

## Behaviour

`ΣLIST({1,2,3,4})` answers 10 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It pairs with `ΠLIST`, which multiplies the same list to 24** (emulator).
The Greek capital sigma is the mathematician's sum sign and the pi is the
product sign, which is where both names come from.

The first character is U+03A3 and it is part of the name. HP files this one
and [ΔLIST](ΔLIST.md) under `catalog` while putting `ΠLIST` under `list`
(HP help) -- one family in two groups, which is the inventory's arrangement
and not a difference in what they do.

There is also a bare `Σ` on HP's list, U+03A3 on its own, and it is a
different command with its own entry, [Σ](Σ.md): it sums an expression over a
range rather than the elements of a list, and `Σ(X,X,1,4)` answers 10
(emulator).

What it answers for an empty list was not run (unverified); zero is the
mathematical answer.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ΔLIST](ΔLIST.md) · [ΠLIST](../list/ΠLIST.md) · [Σ](Σ.md)
