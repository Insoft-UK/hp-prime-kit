# B→R

A `#` integer as an ordinary number.

| | |
|---|---|
| Syntax | `B→R(#integer[m])` → number |
| Group | integer |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `B→R(SETBITS(12))` | `12` | [emulator](../results.tsv) |

## Behaviour

It undoes what [R→B](R→B.md) does: the `#` integer that
[SETBITS](SETBITS.md) answers for 12 comes back as plain 12, of `TYPE` 0
rather than 1 (emulator). The two are inverses on that value, measured in the
same batch.

The name carries an arrow, `→`, which is a character the calculator's own
names use and most keyboards do not (HP help). It is on the list of names, so
`hpprime lint` knows it; writing it from a PC means pasting it or using the
calculator's character menu (unverified).

What it does with a `#` integer of a stated width, and whether the width is
lost, has not been measured (unverified) --
[GETBITS](GETBITS.md) is the command that would say, and it needs a `#`
argument nobody has passed it yet.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[R→B](R→B.md) · [SETBITS](SETBITS.md) · [GETBITS](GETBITS.md)
