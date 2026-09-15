# PercentTotal

The new value as a percentage of the old one.

| | |
|---|---|
| Syntax | `PercentTotal(old,new)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("PercentTotal(100,110)")` | `110` | [emulator](../results.tsv) |

## Behaviour

`PercentTotal(100,110)` answers 110 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): 110 is a hundred and
ten per cent of 100.

**This is where the value landed, not how far it moved** (emulator).
[PercentChange](PercentChange.md) answers 10 for the same two arguments. The
two differ by exactly one hundred whenever the old value is positive, which
is what makes them easy to mix up and hard to notice.

The arguments go old first, new second (HP help).

What it answers when the old value is zero was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PercentChange](PercentChange.md) · [PercentMargin](PercentMargin.md) ·
[PercentMarkup](PercentMarkup.md)
