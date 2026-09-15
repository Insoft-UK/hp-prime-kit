# PIECEWISE

Answers the case whose test is true.

| | |
|---|---|
| Syntax | `PIECEWISE(test1, case1, ...[, test8], case8)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("PIECEWISE(1<2,10,1>2,20)")` | `10` | [emulator](../results.tsv) |

## Behaviour

`PIECEWISE(1<2,10,1>2,20)` answers 10 (emulator): the arguments are read in
pairs, a test and the value that goes with it, and the first test that holds
decides the answer. Here `1<2` is true, so the second argument is the result
and the pair after it is never reached.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

HP's list allows up to eight pairs (HP help). What it answers when no test is
true was not run (unverified), and that is the case a program has to handle,
since a function here always produces something:
[ppl.function-always-answers](../../topics/ppl.md#ppl.function-always-answers).

**It is an expression, where `IF` is a statement** (emulator). This can sit
inside a larger formula and give it a value, which a branch cannot do, and
that is the reason to reach for it rather than for
[IF](../branch/IF.md).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[IF](../branch/IF.md) · [Heaviside](Heaviside.md) ·
[ppl.function-always-answers](../../topics/ppl.md#ppl.function-always-answers)
