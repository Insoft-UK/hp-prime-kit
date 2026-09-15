# plotode

Refused, quoting the call back in its answer.

| | |
|---|---|
| Syntax | `plotode(Expr, [Var1, Var2, ...], [Val1, Val2. ...], [tstep=Value])` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("plotode(X,X,0)")` | `"plotode(X,X,0) \n Error: valor de argumento incorrecto"` | [emulator](../results.tsv) |

## Behaviour

**The answer is a string carrying the call and then an error message**
(emulator), type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), exactly as
[plotfield](plotfield.md) answered in the same batch.

**The arguments given were plain where HP wants lists** (HP help): a list of
variables and a list of their starting values, not one of each. So this row
most likely measures the shape of the call rather than the command
(unverified).

**The two commands that solve differential equations behaved identically**
(emulator), this one and [plotfield](plotfield.md), which carries the account
of the pattern and what it costs a program that tests only for errors.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[plotfield](plotfield.md) · [locus](locus.md) · [plotseq](plotseq.md)
