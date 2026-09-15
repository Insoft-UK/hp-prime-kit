# hilbert

A Hilbert matrix of the size given.

| | |
|---|---|
| Syntax | `hilbert(n)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `hilbert(3)` | `[[1,0.5,0.333333333333],[0.5,0.333333333333,0.25],[0.333333333333,0.25,0.2]]` | [emulator](../results.tsv) |

## Behaviour

`hilbert(3)` answers the three by three Hilbert matrix (emulator), where each
element is one over the sum of its row and column numbers less one: 1, a half,
a third along the first row.

**HP writes this name in lower case and it compiles that way** (emulator).
That matters beyond this one command: a dozen names in this group are written
lower case on HP's list -- `cholesky`, `diag`, `jordan`, `valuation` and the
rest -- and this is the first of them measured, so they are callable from a
program rather than being CAS-only spellings.

**The elements are decimals, not fractions.** A third comes back as
0.333333333333 (emulator), so the matrix a program gets is already rounded
before anything is done with it.

That is the point of the thing: a Hilbert matrix is the standard example of a
system that is hard to solve accurately, because small rounding errors in
values like these grow. [COND](COND.md) is the command that puts a number on
how bad it is, and it was not run on this matrix (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[COND](COND.md) · [IDENMAT](IDENMAT.md) · [RREF](RREF.md)
