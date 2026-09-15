# LOCAL

Declares the variables that belong to one function.

| | |
|---|---|
| Syntax | `LOCAL Var1[:=Val1, Var2:=Val2, ... Var8:=Val8];` |
| Group | variable |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL za, zb; za := 2; zb := 3; RETURN za * zb;` | `6` | unverified |
| `LOCAL z := 7; RETURN z;` | `7` | unverified |
| `LOCAL za := 2, zb := 3; RETURN za + zb;` | `5` | unverified |
| `LOCAL z; RETURN z;` | `0` | unverified |

## Behaviour

Every local goes at the top of the `BEGIN`, before any other statement: a
`LOCAL` after code does not compile (G2), which is
[ppl.locals-at-top](../../topics/ppl.md#ppl.locals-at-top).

One `LOCAL` statement holds at most 7 or 8 variables, and past that the
compiler answers *syntax error* on that line without saying why (G2):
[ppl.local-limit](../../topics/ppl.md#ppl.local-limit). Several `LOCAL`
statements in a row do work, so the habit is groups of six.

A local declared and never assigned starts at 0 (unverified). HP's syntax
shows initial values on the declaration, up to eight variables, and a
published tutorial writes three of them on one line; nobody here has compiled
that on a calculator, which is why
[ppl.locals-initialised-one-line](../../topics/ppl.md#ppl.locals-initialised-one-line)
is a refuted hypothesis labelled `unverified` and why the second and third
examples above are waiting for a batch. Exported globals are the opposite
case: several initialised on one line failed (G2),
[ppl.export-initialised](../../topics/ppl.md#ppl.export-initialised).

Prefixed names (`zi`, `zs`, `za`) cost nothing and keep a local away from the
calculator's own variables. Whether `i` and `e` work as local names is not
known (unverified):
[ppl.i-e-as-locals](../../topics/ppl.md#ppl.i-e-as-locals).

## Related

[EXPORT](EXPORT.md) · [BEGIN](../block/BEGIN.md) ·
[ppl.local-limit](../../topics/ppl.md#ppl.local-limit)
