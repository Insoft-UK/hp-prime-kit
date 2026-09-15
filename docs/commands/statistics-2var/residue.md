# residue

The residue of a function, which reports its own failure as text.

| | |
|---|---|
| Syntax | `residue(Expr, Var, Value)` |
| Group | statistics-2var |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("residue(1/X,X,0)")` | `"residue(1/X,X,0) \n Error: valor de argumento incorrecto"` | [emulator](../results.tsv) |

## Behaviour

**The call was accepted and answered a string describing its own failure**
(emulator), type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). It quotes the call back
and then the message, so a caller can see which call went wrong.

**This row opened a question that took two more batches to settle**
(emulator). It looked at first as though reporting failure as text might be
this command's own habit; a later probe found `Chi2GOF` and `LinRegrTTest`
refusing outright, which seemed to confirm that; and then the geometry
batches found seven commands answering with their errors as data, in three
different types. So the behaviour is common, and a claim that it was not had
to be corrected in this repository.

**A program cannot assume a failure arrives as a refusal** (emulator). The
type here is a string, and a caller testing only for an error takes the
sentence as a value.

**It sits oddly in its group** (HP help). Everything else under
`statistics-2var` works on the app's data sets; this is a symbolic command
about a function, and it is the only name here that answered anything at all.

The message is in the calculator's language (emulator), so it is evidence of
rejection rather than a property of the command.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Do2VStats](Do2VStats.md) · [Resid](Resid.md)
