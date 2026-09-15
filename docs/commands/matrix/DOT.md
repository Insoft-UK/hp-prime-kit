# DOT

The dot product of two vectors.

| | |
|---|---|
| Syntax | `DOT(Vector1, Vector2)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `DOT([1,2,3],[4,5,6])` | `32` | [emulator](../results.tsv) |

## Behaviour

`DOT([1,2,3],[4,5,6])` answers 32 (emulator): four plus ten plus eighteen,
the products taken by position and added.

**A vector is written with single brackets**, `[1,2,3]`, where a matrix takes
double ones (emulator). That is the difference to watch: `[[1,2,3]]` is a
matrix of one row and is not the same argument.

It answers one number, `TYPE` 0 (emulator), while its companion
[CROSS](CROSS.md) answers a vector.

What it does with two vectors of different lengths was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CROSS](CROSS.md) · [TRACE](TRACE.md)
