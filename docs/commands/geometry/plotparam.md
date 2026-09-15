# plotparam

Refused, though two other commands answer by building one.

| | |
|---|---|
| Syntax | `plotparam(f(Var)+i*g(Var), Var= Interval, [tstep=Value])` |
| Group | geometry |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("plotparam(t,t,0,1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It is refused, and it is the form its own neighbours answer in**
(emulator). [plotfunc](plotfunc.md) and [plotpolar](plotpolar.md) were both
given ordinary arguments and both came back written as `plotparam(...)`, so
the calculator builds these objects readily. Called directly it gives a plain
error with no type.

**That is the third family whose plainest name is the broken one**
(emulator), after [line](line.md) among the line builders and
[triangle](triangle.md) among the polygons. Three families, three gaps, each
at the name a reader would reach for first.

**The call above does not follow the published syntax** (HP help), and that
may be the whole of it: HP writes the interval as `Var=Interval` and the
expression as a complex sum, where this row passed four plain arguments. So
the refusal may be about the shape rather than the name (unverified).

**The probe is the shape the answers use** (unverified): copy what
[plotfunc](plotfunc.md) came back with, which is a working `plotparam`
expression by construction, and hand it straight back.

Until that runs, a program wanting a parametric plot should build one through
[plotfunc](plotfunc.md) or [plotpolar](plotpolar.md), which are measured
(emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[plotfunc](plotfunc.md) · [plotpolar](plotpolar.md) · [line](line.md) ·
[triangle](triangle.md)
