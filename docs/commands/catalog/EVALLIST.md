# EVALLIST

Evaluates every element of a list.

| | |
|---|---|
| Syntax | `EVALLIST({list})` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("EVALLIST({1+1,2+2})")` | `{2,4}` | [emulator](../results.tsv) |

## Behaviour

`EVALLIST({1+1,2+2})` answers `{2,4}` (emulator): each element is evaluated
and the answers come back in a list of the same length, type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The elements have to survive being written before they are evaluated**
(emulator). Here they are arithmetic that any parser reads, so this row shows
the evaluation happening and says nothing about an element that only the CAS
would resolve.

What it does with an element that is a name rather than an expression was not
run (unverified). That is the case worth knowing, since it is the difference
between this and a list that was already evaluated when it was built.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SUPPRESS](SUPPRESS.md) · [QUOTE](QUOTE.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
