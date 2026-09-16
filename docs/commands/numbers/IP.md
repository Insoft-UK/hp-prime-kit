# IP

The whole part of a value, with the fraction dropped.

| | |
|---|---|
| Syntax | `IP(value)` |
| Group | numbers |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `IP(23.2)` | `23` | [emulator](../results.tsv) |
| `IP(-23.2)` | `-23` | [emulator](../results.tsv) |
| `IP({23.2,15+1/4,51/2,10-4/5})` | `{23,15,25,9}` | [emulator](../results.tsv) |

## Behaviour

**It cuts towards zero rather than downwards.** `IP(-23.2)` is -23, while
[FLOOR](FLOOR.md) of the same number is -24 (HP help). For positive values
the two agree, so a program that only ever saw positives will not notice the
difference until it does.

The arguments may be arithmetic: `15+1/4` gives 15 and `10-4/5` gives 9
(HP help), so the expression is worked out before the cut.

A list is taken element by element (HP help), and the interpreter covers the
plain form but not the list one (unverified: the interpreter on the PC,
not a calculator).

With [FP](FP.md) it makes a pair: the whole part and the fraction, which
added back together give the value (HP help).

## Related

[FP](FP.md) · [FLOOR](FLOOR.md) · [CEILING](CEILING.md)
