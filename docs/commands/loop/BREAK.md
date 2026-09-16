# BREAK

Leaves a loop before its test says to.

| | |
|---|---|
| Syntax | `BREAK [n];` |
| Group | loop |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL z; z := 0; FOR z FROM 1 TO 5 DO IF z == 3 THEN BREAK; END; END; RETURN z;` | `3` | [emulator](../results.tsv) |
| `LOCAL zi, zj, z; z := 0; FOR zi FROM 1 TO 3 DO FOR zj FROM 1 TO 3 DO BREAK 2; END; z := 9; END; RETURN z;` | `0` | [emulator](../results.tsv) |

## Behaviour

Without a number it leaves the loop it is in, and the counter keeps the value
it had when the loop was left (emulator).

`BREAK n` leaves n levels of loop at once, and it really does leave them: in
the second example the statement after the inner loop never runs, so the
answer is 0 and not 9 (emulator). The interpreter on the PC dropped the number
and left one loop until that measurement, which is the third divergence the
documentation caught in one batch.

What the calculator does with a number larger than the levels that are open
has not been measured (unverified).

`RETURN` inside a loop leaves the whole function rather than the loop, and it
is allowed (G2):
[ppl.return-in-loop](../../topics/ppl.md#ppl.return-in-loop). Where `BREAK`
carries on after the loop, `RETURN` does not carry on at all.

## Related

[CONTINUE](CONTINUE.md) · [FOR](FOR.md) · [WHILE](WHILE.md) ·
[REPEAT](REPEAT.md)
