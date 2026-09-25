# DelAVars

On HP's list of names, and refused when called with nothing.

| | |
|---|---|
| Syntax | `DelAVars` |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DelAVars")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Called bare it was refused** (emulator). What it takes -- a name, a list
of names -- and what it deletes are read from its name (unverified); the
active app, the Function app, held no variables of its own to delete, as
[AVars](AVars.md) shows.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AVars](AVars.md) · [DelHVars](../system/DelHVars.md)
