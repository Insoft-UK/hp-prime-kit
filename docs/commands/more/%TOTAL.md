# %TOTAL

What percentage one number is of another.

| | |
|---|---|
| Syntax | `%TOTAL(value1, value2)` → number |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `%TOTAL(20,5)` | `25` | [emulator](../results.tsv) |

## Behaviour

5 is 25% of 20, and the answer is 25 (emulator). So the **first** argument is
the total and the second is the part, which is the order the name does not
tell you: `%TOTAL(part, total)` would answer something else and would not
complain.

It answers a percentage rather than a fraction, as [%CHANGE](%CHANGE.md)
does (emulator). The two measured calls both answer 25 for different reasons,
which is a coincidence of the numbers chosen and not a relation between the
commands (emulator).

A total of zero has not been measured (unverified).

The interpreter does not implement it -- it cannot even read the name -- so
`hpprime run` cannot check a program that uses it (unverified).

## Related

[%CHANGE](%CHANGE.md)
