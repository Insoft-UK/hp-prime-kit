# DelAFiles

On HP's list of names, and refused when called with nothing.

| | |
|---|---|
| Syntax | `DelAFiles` |
| Group | common-numeric-view |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("DelAFiles")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Called bare it was refused** (emulator). What it takes and what it deletes
are read from its name (unverified); the active app held no files, as
[AFiles](AFiles.md) shows.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[AFiles](AFiles.md) · [DelAVars](DelAVars.md)
