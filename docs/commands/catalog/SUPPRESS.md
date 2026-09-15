# SUPPRESS

Removes the element at a position.

| | |
|---|---|
| Syntax | `SUPPRESS(object, index)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("SUPPRESS({1,2,3},2)")` | `{1,3}` | [emulator](../results.tsv) |

## Behaviour

`SUPPRESS({1,2,3},2)` answers `{1,3}` (emulator): the second element is gone
and the rest close up, a list of type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The position is counted from 1** (emulator). Removing index 2 took the
value 2, which is the second element and not the third, so this follows
[ppl.one-based](../../topics/ppl.md#ppl.one-based) like everything else the
calculator indexes.

**It answers a new list rather than changing the one it was given**
(emulator). The call was made on a literal, so there was nothing to change,
and the answer carries the result -- which is what a program has to assign
somewhere.

HP's list calls the first argument an object rather than a list (HP help), so
a string or a matrix may work as well. Neither was run (unverified).

A name collision is worth knowing about: `suppress` in lower case is a
different command in the `list` group (HP help). The linter compares names
without regard to case and cannot tell the two apart, which it documents.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EVALLIST](EVALLIST.md) ·
[ppl.one-based](../../topics/ppl.md#ppl.one-based) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
