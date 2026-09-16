# plotfield

Refused, quoting the call back in its answer.

| | |
|---|---|
| Syntax | `plotfield(Expr, VectorVar, [xstep=Val, ystep=Val, Option])` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("plotfield(X,X)")` | `"plotfield(X,X) \n Error: valor de argumento incorrecto"` | [emulator](../results.tsv) |

## Behaviour

**The answer is a string carrying the call and then an error message**
(emulator), type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). Quoting the call back
makes it the most useful kind of failure in this group: a caller can see
which call went wrong without tracking it.

**The line break arrives as the two characters backslash and n** (emulator),
not as a break, the same thing [locus](locus.md) and
[plotode](plotode.md) do and the same thing `STRING` does elsewhere in this
documentation.

**The second argument is wrong and HP says what it should be** (HP help): a
VectorVar, meaning a pair of variables for a direction field, where a single
`X` was sent. So this row most likely measures a bad argument rather than a
broken command (unverified).

**Three commands in this family report failure as text** (emulator): this
one, [plotode](plotode.md) and [locus](locus.md) in the curve family. A
program testing for an error finds none and carries the sentence on as a
value.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[plotode](plotode.md) · [locus](locus.md) · [plotimplicit](plotimplicit.md)
