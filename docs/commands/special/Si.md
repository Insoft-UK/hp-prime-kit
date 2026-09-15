# Si

The sine integral.

| | |
|---|---|
| Syntax | `Si(Expr)` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `Si(1)` | `Si(1)` | [emulator](../results.tsv) |

## Behaviour

**The answer is the call itself**, of type 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers), the same as
[Ci](Ci.md) beside it.

The pair is the sine and cosine integral, and both were measured together
answering the same way, so this is a property of the family rather than of one
name (emulator).

Unlike its cosine twin, this one is defined at zero and has no singularity
there, which is the kind of difference a program handling both has to know
(unverified: only the point 1 was run).

What turns it into a number was not measured (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Ci](Ci.md) · [Ei](Ei.md) · [erf](erf.md)
