# CEILING

The smallest whole number that is not below the value.

| | |
|---|---|
| Syntax | `CEILING(value)` |
| Group | numbers |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CEILING(3.2)` | `4` | [emulator](../results.tsv) |
| `CEILING(-3.2)` | `-3` | [emulator](../results.tsv) |
| `CEILING({3.2,-3.2})` | `{4,-3}` | [emulator](../results.tsv) |

## Behaviour

It rounds towards positive, always: 3.2 becomes 4 and -3.2 becomes -3
(HP help). **The negative case is the one to hold on to** -- rounding "up" a
negative number makes it smaller in size, not larger, which is the opposite of
what [FLOOR](FLOOR.md) does.

A list is taken element by element and answers a list (HP help). The
interpreter covers the plain form but not the list one, where it stops rather
than answering (unverified: that is the interpreter on the PC, not a
calculator), so that row is HP's statement and not something run here.

Together with [FLOOR](FLOOR.md), [IP](IP.md) and [FP](FP.md) this is the set
a program picks from when it needs a whole number, and they disagree on
negatives, which is where the choice matters (HP help).

## Related

[FLOOR](FLOOR.md) · [IP](IP.md) · [ROUND](ROUND.md)
