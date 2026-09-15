# plotpolar

Rewrites a polar expression as a parametric plot.

| | |
|---|---|
| Syntax | `plotpolar(Expr,Var=Interval, [Step])` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("plotpolar(X,X,0,1)")` | `plotparam(X*COS(X)+*X*SIN(X),X,0,1)` | [emulator](../results.tsv) |

## Behaviour

**It answers a `plotparam` with the polar-to-cartesian conversion written
out** (emulator), type 8,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes): the radius times cosine
for the real part and the radius times sine for the imaginary one. The
conversion is visible in the answer rather than done silently.

**The interval given was kept** (emulator), from 0 to 1, unlike
[plotfunc](plotfunc.md), which substituted the screen's own range because the
call supplied none.

**The call did not follow the published syntax and was accepted anyway**
(emulator). HP writes the second argument as `Var=Interval`; four plain
arguments were sent and the command took them. That is worth noting beside
[plotparam](plotparam.md), which was refused for what may be the same
liberty.

**The Result cell carries the imaginary unit U+E003** (emulator), so it was
built from the stored row rather than typed.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[plotfunc](plotfunc.md) · [plotparam](plotparam.md) · [affix](affix.md)
