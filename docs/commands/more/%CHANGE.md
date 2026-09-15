# %CHANGE

The percentage change from one number to another.

| | |
|---|---|
| Syntax | `%CHANGE(value1, value2)` → number |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `%CHANGE(20,25)` | `25` | [emulator](../results.tsv) |

## Behaviour

From 20 to 25 is a rise of 5, which is 25% of the first number, and 25 is the
answer (emulator). So the first argument is the base and the answer is a
percentage, not a fraction: 25 rather than 0.25.

A fall has not been measured, so whether it answers a negative is not known
here (unverified), and neither is what a first argument of zero does, where
the percentage has no meaning.

The name begins with `%`, which is a character a program can use in a name on
this calculator and not in most languages (HP help). `hpprime lint` knows it,
because it is on the list of names built from HP's own sources (HP help).

The interpreter does not implement it -- it cannot even read the name -- so
`hpprime run` cannot check a program that uses it (unverified).

## Related

[%TOTAL](%TOTAL.md)
