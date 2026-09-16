# REPEAT

Repeats a block until a test becomes true, checking the test last.

| | |
|---|---|
| Syntax | `REPEAT commands UNTIL test;` |
| Group | loop |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL z; z := 0; REPEAT z := z + 1; UNTIL z >= 4; RETURN z;` | `4` | [emulator](../results.tsv) |
| `LOCAL z; z := 0; REPEAT z := z + 1; UNTIL 1 == 1; RETURN z;` | `1` | [emulator](../results.tsv) |

## Behaviour

The body always runs at least once, because the test comes after it: the
second example runs the body once even though the test was true from the
start (emulator). [WHILE](WHILE.md) is the other way round.

`UNTIL` ends the statement with a semicolon rather than an `END;`, which is
the one loop that closes differently (HP help).

This is the shape the measured way of waiting for a key is written in, twice
over: drain what is pending, then wait
([interface.drain-then-wait](../../topics/interface.md#interface.drain-then-wait)).
`RETURN` inside it is allowed and leaves the function (G2):
[ppl.return-in-loop](../../topics/ppl.md#ppl.return-in-loop).

## Related

[WHILE](WHILE.md) · [FOR](FOR.md) · [BREAK](BREAK.md) ·
[interface.drain-then-wait](../../topics/interface.md#interface.drain-then-wait)
