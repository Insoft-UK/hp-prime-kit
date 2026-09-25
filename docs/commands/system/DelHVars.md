# DelHVars

On HP's list of names, and the one use of it tried was refused.

| | |
|---|---|
| Syntax | `DelHVars` |
| Group | system |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `LOCAL q, a, b; q := CHAR(34); EXPR("ZQ:=5"); a := SIZE(EXPR("HVars")); EXPR("DelHVars(" + q + "ZQ" + q + ")"); b := SIZE(EXPR("HVars")); RETURN {a, b};` | *error* | [emulator](../results.tsv) |

## Behaviour

**The row tried to create a Home variable, count, delete it and count
again, and was refused** (emulator). It made `ZQ` with `EXPR("ZQ:=5")`, took
`SIZE` of [HVars](HVars.md), called `DelHVars` with the name in quotes, and
took the size again. Any of those steps may be the one that failed: the row
says only that one did.

**What it takes and what it deletes are read from its name** (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[HVars](HVars.md)
