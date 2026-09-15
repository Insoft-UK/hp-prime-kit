# KILL

Stops the program that is running.

| | |
|---|---|
| Syntax | `KILL;` |
| Group | block |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `KILL;` | *no value* | HP help |

## Behaviour

It ends the program there and then (HP help). There is nothing to record: a
program that stops answers nothing, and a batch cannot run it either, because
it would stop the batch's own program along with it (unverified).

[RETURN](RETURN.md) is the ordinary way out of a function, and it answers a
value; every function answers one whether you choose it or not (G2),
[ppl.function-always-answers](../../topics/ppl.md#ppl.function-always-answers).
`KILL` is the other thing: stopping everything. What it leaves on the screen,
and whether Home shows anything afterwards, has not been measured here
(unverified).

The interpreter does not know the name at all, so `hpprime run` cannot check
any of this for you (unverified).

## Related

[RETURN](RETURN.md) · [BEGIN](BEGIN.md)
