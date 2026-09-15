# POS

Where an element sits in a list.

| | |
|---|---|
| Syntax | `POS(list, element)` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `POS({3,5,7},5)` | `2` | [emulator](../results.tsv) |

## Behaviour

`POS({3,5,7},5)` answers 2 (emulator): the position, counting from 1, and not
the element itself.

**What it answers when the element is not there is the thing to measure
next**, and it has not been run (unverified). If it is 0, then a `POS` result
can be tested directly; if it is an error, the call needs an `IFERR` around
it. The two lead to completely different code, and this entry does not guess
between them. The probe is `POS({3,5,7},4)`.

Positions count from 1 (emulator),
[ppl.one-based](../../topics/ppl.md#ppl.one-based), which is the opposite of
the 0 a screen coordinate uses.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[INSERT](INSERT.md) · [INTERSECT](INTERSECT.md) · [SIZE](SIZE.md)
