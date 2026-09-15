# TRACE

The sum of the diagonal of a square matrix.

| | |
|---|---|
| Syntax | `TRACE(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TRACE([[1,2],[3,4]])` | `5` | [emulator](../results.tsv) |

## Behaviour

`TRACE([[1,2],[3,4]])` answers 5 (emulator): one plus four, the two elements
on the diagonal, and nothing else.

It answers a plain number, `TYPE` 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The trace is also the sum of the eigenvalues, and the two measured here agree:
[EIGENVAL](EIGENVAL.md) answers 5.37228132327 and -0.372281323269, which add
to 5 (emulator). That is a cheap check on a decomposition that a program can
make without trusting either command.

What it does with a matrix that is not square was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DET](DET.md) · [EIGENVAL](EIGENVAL.md) · [RANK](RANK.md)
