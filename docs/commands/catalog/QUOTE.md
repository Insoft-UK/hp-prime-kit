# QUOTE

Hands back an expression without evaluating it.

| | |
|---|---|
| Syntax | `QUOTE(expression)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("QUOTE(1+2)")` | `1+2` | [emulator](../results.tsv) |

## Behaviour

`QUOTE(1+2)` answers `1+2` and not 3 (emulator): the expression comes back
unevaluated, as a symbolic object of type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**That is the whole point of it, and it is the opposite of
[EXPR](../strings/EXPR.md)** (emulator). One turns text into a value, this
one keeps a value from becoming one. A program that builds an expression to
hand somewhere else needs it; a program that wants the number does not.

**Nothing here shows how long the delay lasts** (unverified). What was
measured is that the answer is still `1+2` when it arrives; whether it
evaluates when stored, passed on, or used in arithmetic was not run, and
those are the cases a program actually meets.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[EXPR](../strings/EXPR.md) · [EVALLIST](EVALLIST.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
