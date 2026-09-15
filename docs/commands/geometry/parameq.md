# parameq

The parametric equation of an object, refused for the line tried here.

| | |
|---|---|
| Syntax | `parameq(Obj)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("parameq(line(point(0,0),point(1,1)))")` | `"Error: entrada no válida"` | [emulator](../results.tsv) |

## Behaviour

**The answer is a string carrying an error message** (emulator), type 2,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). It failed the same way
[equation](equation.md) did, in the same batch, on an argument built the same
way.

**Both were given a line from [line](line.md), which was refused on its own**
(emulator), so neither row says much about its own command. The probe for
both is a line that did come back, such as
[bisector](bisector.md)'s `line(y=x)`.

**The calculator does produce parametric forms** (emulator): in the probe,
`plotfunc` rewrote a function as `plotparam` of a complex expression. So the
machinery exists and this name did not reach it here.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[equation](equation.md) · [line](line.md) · [affix](affix.md)
