# INSERT

Puts a value into a list at a given position.

| | |
|---|---|
| Syntax | `INSERT(object1, index, object2)` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `INSERT({1,2,3},2,9)` | `{1,9,2,3}` | [emulator](../results.tsv) |

## Behaviour

**The value lands before the element that was at that index, not after it.**
`INSERT({1,2,3},2,9)` answers `{1,9,2,3}` (emulator): the 9 takes position 2
and the 2 moves along. A program that means "after the second" has to say 3.

The index counts from 1 like every other list index (emulator),
[ppl.one-based](../../topics/ppl.md#ppl.one-based).

What it does with an index past the end of the list, and whether that appends
or is an error, has not been run (unverified).

The call answers the new list rather than changing the one given (emulator:
the literal `{1,2,3}` was not a variable that could be looked at afterwards,
so this reading is what the answer shows and not a test of the original).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[POS](POS.md) · [REVERSE](REVERSE.md) · [CONCAT](CONCAT.md)
