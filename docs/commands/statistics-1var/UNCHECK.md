# UNCHECK

Turns off one of the statistics app's analyses.

| | |
|---|---|
| Syntax | `UNCHECK(n)` |
| Group | statistics-1var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("UNCHECK(1)")` | `1` | [emulator](../results.tsv) |

## Behaviour

`UNCHECK(1)` answers 1 (emulator), type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It answers the same 1 as [CHECK](CHECK.md)** (emulator), its opposite,
which were run one after the other in the same batch. Two commands that do
contrary things and answer alike, so the answer cannot be the new state -- or
if it is, one of the two rows is reporting the state it just left.

**That makes 1 most likely a report of success** (unverified), not of the
setting. The probe is [ISCHECK](ISCHECK.md) run between the two, which would
separate them in one row.

**It changes the calculator** (HP help), so like `CHECK` it was sent only to
the throwaway calculator.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CHECK](CHECK.md) · [ISCHECK](ISCHECK.md)
