# FLOOR

The largest whole number that is not above the value.

| | |
|---|---|
| Syntax | `FLOOR(value)` |
| Group | numbers |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `FLOOR(3.2)` | `3` | [emulator](../results.tsv) |
| `FLOOR(-3.2)` | `-4` | [emulator](../results.tsv) |
| `FLOOR({3.2,-3.2})` | `{3,-4}` | [emulator](../results.tsv) |

## Behaviour

It rounds towards negative, always: 3.2 becomes 3 and -3.2 becomes **-4**
(HP help), which is smaller than the value rather than nearer to zero. That
is the difference from [IP](IP.md), which simply drops the fractional part
and answers -3 for the same number.

A list is taken element by element (HP help). The interpreter covers the plain
form and not the list one (unverified: the interpreter on the PC, not a
calculator), so that row rests on HP's help alone.

Choosing between this, [CEILING](CEILING.md) and [IP](IP.md) only matters for
negative values; for positives all three agree, which is exactly why the
mistake survives testing (HP help).

## Related

[CEILING](CEILING.md) · [IP](IP.md) · [FP](FP.md)
