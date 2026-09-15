# TRUNCATE

Cuts a value to a number of decimal places, without rounding.

| | |
|---|---|
| Syntax | `TRUNCATE(value, [places])` |
| Group | numbers |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TRUNCATE(7.8676,2)` | `7.86` | [emulator](../results.tsv) |

## Behaviour

**It cuts where [ROUND](ROUND.md) rounds.** The same number and the same two
places give 7.86 here and 7.87 there (emulator). That difference of one in
the last digit is the whole reason both commands exist, and it is the one to
check when a total does not match by a penny.

It is to [ROUND](ROUND.md) what [IP](IP.md) is to [FLOOR](FLOOR.md)
(emulator): the pair that discards rather than the pair that moves.

Whether a negative number of places means significant figures here, as it
does for [ROUND](ROUND.md), was not run (unverified). The probe is
`TRUNCATE(7.8676,-2)`, and the two commands are documented with the same
argument, so the expectation is that it matches -- which is a reason to
measure it rather than to assume it.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ROUND](ROUND.md) · [IP](IP.md) · [MANT](MANT.md)
