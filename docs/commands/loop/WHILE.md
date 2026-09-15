# WHILE

Repeats a block while a test is true, checking the test first.

| | |
|---|---|
| Syntax | `WHILE test DO commands END;` |
| Group | loop |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL z; z := 0; WHILE z < 4 DO z := z + 1; END; RETURN z;` | `4` | unverified |
| `LOCAL z; z := 9; WHILE z < 4 DO z := z + 1; END; RETURN z;` | `9` | unverified |

## Behaviour

The test is checked before the first pass, so a body whose test starts false
never runs at all, which is the second example (unverified).
[REPEAT](REPEAT.md) is the other way round: its body always runs once.

The test compares with `==`, `<`, `>`, `<=`, `>=` or `<>`, never with a single
`=` (unverified):
[ppl.equality-operators](../../topics/ppl.md#ppl.equality-operators). `END;`
closes the loop, because `ENDWHILE` does not exist (G2):
[ppl.no-end-keywords](../../topics/ppl.md#ppl.no-end-keywords).

Nothing advances the test for you. The statement that moves it has to be in
the body, and a [CONTINUE](CONTINUE.md) that skips that statement is how a
`WHILE` is made to loop forever (unverified).

## Related

[REPEAT](REPEAT.md) · [FOR](FOR.md) · [BREAK](BREAK.md) ·
[CONTINUE](CONTINUE.md)
