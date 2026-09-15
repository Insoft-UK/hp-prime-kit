# ISCHECK

Says whether one of the statistics app's analyses is on.

| | |
|---|---|
| Syntax | `ISCHECK(n)` |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("ISCHECK(1)")` | `0` | [emulator](../results.tsv) |

## Behaviour

`ISCHECK(1)` answers 0 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): the first analysis is
off on a calculator reset before the run.

**This was the row that showed the group reachable** (emulator). It was sent
in the probe that surveyed seven small groups at once, and it answered where
most of that probe refused, which is why this group was planned as ordinary
work rather than as a mystery.

**It asks rather than changes, which is why it was chosen** (emulator).
[CHECK](CHECK.md) and [UNCHECK](UNCHECK.md) alter the calculator; a survey
probe should not, so the read-only one went first.

**0 is off and the true answer was not measured** (unverified). Running this
after [CHECK](CHECK.md) is the one row that would settle both this scale and
what those two commands' own 1 means.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CHECK](CHECK.md) · [UNCHECK](UNCHECK.md) · [Do1VStats](Do1VStats.md)
