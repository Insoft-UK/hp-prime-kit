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
| `LOCAL za, zb; za := 2; zb := 3; RETURN za * zb;` | `6` | [emulator](../results.tsv) |
| `LOCAL z := 7; RETURN z;` | `7` | [emulator](../results.tsv) |
| `LOCAL za := 2, zb := 3; RETURN za + zb;` | `5` | [emulator](../results.tsv) |
| `LOCAL z; RETURN z;` | `0` | [emulator](../results.tsv) |

## Behaviour

Every local goes at the top of the `BEGIN`, before any other statement: a
`LOCAL` after code does not compile (G2), which is
[ppl.locals-at-top](../../topics/ppl.md#ppl.locals-at-top).

One `LOCAL` statement holds at most 7 or 8 variables, and past that the
compiler answers *syntax error* on that line without saying why (G2):
[ppl.local-limit](../../topics/ppl.md#ppl.local-limit). Several `LOCAL`
statements in a row do work, so the habit is groups of six.

A local declared and never assigned starts at 0, which is the fourth example
(emulator). A `LOCAL` can also give initial values: one on its own and two on
one line both compile and keep their values, the second and third examples
(emulator), which is
[ppl.locals-initialised-one-line](../../topics/ppl.md#ppl.locals-initialised-one-line).
HP's syntax allows up to eight (HP help), and more than two on one line has
not been run (unverified). Exported globals are the opposite case: several
initialised on one line failed (G2),
[ppl.export-initialised](../../topics/ppl.md#ppl.export-initialised).

Prefixed names (`zi`, `zs`, `za`) cost nothing and keep a local away from the
calculator's own variables. Whether `i` and `e` work as local names is not
known (unverified):
[ppl.i-e-as-locals](../../topics/ppl.md#ppl.i-e-as-locals).

## Related

[EXPORT](EXPORT.md) · [BEGIN](../block/BEGIN.md) ·
[ppl.local-limit](../../topics/ppl.md#ppl.local-limit)
