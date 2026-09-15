# TEVAL

How long an expression takes to evaluate.

| | |
|---|---|
| Syntax | `TEVAL(expression)` → duration |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TEVAL(1+1)` | `0_s` | [emulator](../results.tsv) |

## Behaviour

**The answer is a unit, not a number**: `0_s` is zero seconds, and its `TYPE`
is 9, which is what HP's help calls a unit (emulator). So a program that
compares it with a number, or prints it expecting digits, is in for a
surprise: it is the same kind of value as `2_m` or `3_kg`.

`1+1` was too fast to register and came back as zero (emulator). What the
resolution is -- whether anything under a millisecond reads as zero -- has
not been measured (unverified), and neither has how to get a plain number out
of the unit.

For timing something real, [TICKS](TICKS.md) read before and after is the
measured way, and it is what the one speed figure in this documentation rests
on (G2), [ppl.speed-anchor](../../topics/ppl.md#ppl.speed-anchor).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[TICKS](TICKS.md) · [EVAL](EVAL.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
