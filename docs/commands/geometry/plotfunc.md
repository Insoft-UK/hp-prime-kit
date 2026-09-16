# plotfunc

Rewrites a function as a parametric plot.

| | |
|---|---|
| Syntax | `plotfunc(Expr)` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("plotfunc(X^2)")` | `plotparam(X+*X^2,X,−15.9,15.9)` | [emulator](../results.tsv) |

## Behaviour

**It answers an object, not a picture** (emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). The function comes back
rewritten as a `plotparam` whose real part is the variable and whose
imaginary part is the expression.

**The range is the screen's, not the caller's** (emulator): from about minus
sixteen to sixteen, which the call never asked for. So the answer carries a
default a program should know about before comparing two plots.

**A point is written as a complex number here** (emulator), the same way
[affix](affix.md) writes one and [rotation](rotation.md) answers a turn: real
part across, imaginary part up.

**The Result cell carries two characters nobody can type** (emulator), the
imaginary unit U+E003 and the real minus U+2212, so it was built from the
stored row rather than typed,
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit).

**The form it answers in is itself refused** (emulator):
[plotparam](plotparam.md) called directly gives an error, though this command
produces one on demand.

This row was measured in the first probe of the geometry family, which is why
it predates the rest of the family (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[plotparam](plotparam.md) · [plotpolar](plotpolar.md) · [affix](affix.md) ·
[ppl.minus-sign](../../topics/ppl.md#ppl.minus-sign)
