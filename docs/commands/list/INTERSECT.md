# INTERSECT

The elements that are in every list given.

| | |
|---|---|
| Syntax | `INTERSECT({list1}, ...{listN})` |
| Group | list |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `INTERSECT({1,2,3},{2,3,4})` | `{2,3}` | [emulator](../results.tsv) |

## Behaviour

`INTERSECT({1,2,3},{2,3,4})` answers `{2,3}` (emulator), which is what the
name promises and, unlike [DIFFERENCE](DIFFERENCE.md), what a reader coming
from another language would expect.

The order of the answer followed the order of the first list in this one run
(emulator). One example is not enough to call that a rule (unverified), and a
program that depends on the order should sort the answer rather than trust it.

HP's syntax shows more than two lists (HP help); three have not been run here
(unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[DIFFERENCE](DIFFERENCE.md) · [UNION](UNION.md) · [POS](POS.md)
