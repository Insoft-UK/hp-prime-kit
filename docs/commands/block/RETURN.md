# RETURN

Leaves the function, with a value.

| | |
|---|---|
| Syntax | `RETURN expression;` |
| Syntax | `RETURN;` |
| Group | block |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL z; z := 2; RETURN z;` | `2` | unverified |
| `LOCAL zi, zs; zs := 0; FOR zi FROM 1 TO 10 DO IF zi == 3 THEN RETURN zi; END; END; RETURN zs;` | `3` | [G2](../../topics/ppl.md#ppl.return-in-loop) |

## Behaviour

`RETURN` inside a `FOR` or a `REPEAT` is allowed, and leaves the function from
there (G2): [ppl.return-in-loop](../../topics/ppl.md#ppl.return-in-loop). That
was a hypothesis this kit held as a rule until a program that runs contradicted
it, which is why the fact is kept as a refuted hypothesis rather than deleted.

A bare `RETURN;` compiles, and the function answers 0 (G2). There is no way to
write a function that answers nothing at all: without a `RETURN` it answers the
value of the last statement that produced one
([ppl.function-always-answers](../../topics/ppl.md#ppl.function-always-answers)).
That matters because Home prints what a program answers, and people go looking
for a way to stop it.

## Related

[ppl.return-in-loop](../../topics/ppl.md#ppl.return-in-loop) ·
[ppl.function-always-answers](../../topics/ppl.md#ppl.function-always-answers)
