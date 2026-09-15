# pivot

One step of Gaussian elimination.

| | |
|---|---|
| Syntax | `pivot(matrix, n, m)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `pivot([[1,2],[3,4]],1,1)` | `[[1,2],[0,−2]]` | [emulator](../results.tsv) |

## Behaviour

`pivot([[1,2],[3,4]],1,1)` answers `[[1,2],[0,-2]]` (emulator): the
element below the chosen pivot has been cleared, and the rest of that row
changed with it.

**It does one step, where [RREF](RREF.md) does all of them.** That is the
reason to have both: this one lets a program watch the elimination happen, or
stop it part way (emulator).

The two indices choose the pivot's row and column, counting from 1 (emulator),
[ppl.one-based](../../topics/ppl.md#ppl.one-based).

What it does when the chosen pivot is zero, which is where elimination needs a
row swap, was not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RREF](RREF.md) · [LU](LU.md) · [RANK](RANK.md)
