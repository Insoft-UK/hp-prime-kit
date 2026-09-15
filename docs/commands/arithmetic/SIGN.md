# SIGN

Whether a value is positive, negative or zero.

| | |
|---|---|
| Syntax | `SIGN(value)` |
| Group | arithmetic |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SIGN(2)` | `1` | [emulator](../results.tsv) |

## Behaviour

A positive value answers 1 (HP help). What it answers for a negative value
and for zero is the obvious pair, -1 and 0, and HP's help documents no example
for either, so neither is stated here as though it were known (unverified).

What it does with a list, the way [MAX](MAX.md) and [MIN](MIN.md) take one,
has not been established (unverified).

One example is thin, and that is the honest state: HP's help gives exactly
one for this name, and it was run and agreed (emulator). The negative, the
zero and the list form are still unmeasured (unverified).

## Related

[MAX](MAX.md) · [MIN](MIN.md) · [IP](../numbers/IP.md)
