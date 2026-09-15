# EXPORT

Makes a function or a variable visible from Home and from other programs.

| | |
|---|---|
| Syntax | `EXPORT FunctionName(Parameters)` |
| Syntax | `EXPORT Var1[:=Val1, Var2:=Val2, ...];` |
| Group | variable |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPORT AREA(zr);` | *no value* | HP help |

## Behaviour

A declaration rather than a call, which is why there is nothing to record
(HP help). Without it, a function is private to its own file.

Exported names share one namespace with Home, so two programs exporting
`AREA` collide, and so does a program exporting a name an app already uses
(G2): [ppl.global-namespace](../../topics/ppl.md#ppl.global-namespace).
Prefixing them is the habit that avoids it, and `hpprime lint --set` flags
names that would clash between files installed together.

Several exported variables with initial values on one line failed with seven
of them (G2):
[ppl.export-initialised](../../topics/ppl.md#ppl.export-initialised). One
declaration per line compiles. Locals are the opposite case, where HP's own
syntax puts several initial values on one line
([LOCAL](LOCAL.md)).

A program only sees another's functions if it was compiled afterwards (G2):
[ppl.compilation-order](../../topics/ppl.md#ppl.compilation-order). Install
the data first, then the engine, then the app.

On Home an exported function with no arguments is called without parentheses
(G2):
[ppl.home-no-parentheses](../../topics/ppl.md#ppl.home-no-parentheses).

`hpprime run` reads `EXPORT` at the top of a program -- that is how every
example in this documentation is run -- but not as a statement inside a body,
which is what the field above is saying no to (unverified).

## Related

[LOCAL](LOCAL.md) · [BEGIN](../block/BEGIN.md) ·
[ppl.global-namespace](../../topics/ppl.md#ppl.global-namespace)
