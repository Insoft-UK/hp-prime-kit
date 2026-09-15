# UVAL

The number out of a value that carries a unit.

| | |
|---|---|
| Syntax | `UVAL(Value_Unit)` |
| Group | units |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `UVAL(2_m)` | `2` | [emulator](../results.tsv) |

## Behaviour

`UVAL(2_m)` answers 2 (emulator): the number, with the unit gone.

**The answer is type 0 where its argument was type 9** (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). That is the whole point
of the command: it hands back something ordinary arithmetic can use, and
something that no longer knows what it measures.

**With [UPART](UPART.md) it takes a unit value apart.** That answers `1_m` for
the same argument, so the two together give 2 and one metre, which multiply
back to what went in (emulator). It is the same division of labour
[MANT](../numbers/MANT.md) and [XPON](../numbers/XPON.md) make for a plain
number.

HP's list gives this name no syntax string (HP help), so the shape above is
what the measured call shows.

What it answers for a value with no unit at all was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[UPART](UPART.md) · [CONVERT](CONVERT.md) · [MANT](../numbers/MANT.md)
