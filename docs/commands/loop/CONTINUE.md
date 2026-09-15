# CONTINUE

Skips the rest of the body and goes on to the next turn of the loop.

| | |
|---|---|
| Syntax | `CONTINUE [n];` |
| Group | loop |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL zi, zs; zs := 0; FOR zi FROM 1 TO 5 DO IF zi == 3 THEN CONTINUE; END; zs := zs + zi; END; RETURN zs;` | `12` | unverified |

## Behaviour

The loop carries on: the example adds 1, 2, 4 and 5 and leaves out 3, which is
12 (unverified). The counter still advances, so `CONTINUE` inside a `FOR` never
loops forever on its own; inside a `WHILE` or a `REPEAT` it can, if the
statement that moves the test is the one being skipped (unverified).

HP's syntax allows `CONTINUE n`, to carry on with an outer loop rather than
this one (HP help). Nothing here has measured what a number does, and the same
question is open for [BREAK](BREAK.md).

## Related

[BREAK](BREAK.md) · [FOR](FOR.md) · [WHILE](WHILE.md) · [REPEAT](REPEAT.md)
