# REPLACE

Puts one matrix inside another, starting at a position you give.

| | |
|---|---|
| Syntax | `REPLACE(matrix, {row, column}, matrix2)` → matrix |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `REPLACE([[1,2],[3,4]],{1,1},[[9]])` | `[[9,2],[3,4]]` | [emulator](../results.tsv) |

## Behaviour

The position is a list, row first, counted from 1 (emulator):
[ppl.one-based](../../topics/ppl.md#ppl.one-based). What goes in is itself a
matrix, so replacing one element means writing `[[9]]` rather than `9`
(emulator).

What happens when the replacement runs past the edge -- refused, or clipped --
has not been measured (unverified), and it is the first thing to probe before
using this on data whose size varies.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SUB](SUB.md) · [REDIM](REDIM.md) · [SCALE](SCALE.md)
