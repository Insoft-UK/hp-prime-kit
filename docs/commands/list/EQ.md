# EQ

Whether two objects are equal.

| | |
|---|---|
| Syntax | `EQ(object_1, object2)` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EQ(1,1)` | `1` | [emulator](../results.tsv) |

## Behaviour

`EQ(1,1)` answers 1 (emulator), so equality is true as the number 1 rather
than as a separate kind of value.

**One example is thin, and this is the thin one.** What it answers for two
different values was not run, and 0 is the expectation rather than a
measurement (unverified). Nor is it known what it does with two lists, which
is the reason this name sits in the `list` group at all rather than beside the
comparison operators: the probe is `EQ({1,2},{1,2})`.

Whether it differs from `==` in any way a program would notice is the question
worth settling before reaching for it (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[POS](POS.md) · [DIFFERENCE](DIFFERENCE.md) ·
[ppl.equality-operators](../../topics/ppl.md#ppl.equality-operators)
