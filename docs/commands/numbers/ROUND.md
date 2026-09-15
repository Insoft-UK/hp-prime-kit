# ROUND

Rounds a value to a number of decimal places, or to significant figures.

| | |
|---|---|
| Syntax | `ROUND(value, [places])` |
| Group | numbers |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `ROUND(7.8676,2)` | `7.87` | [emulator](../results.tsv) |
| `ROUND(7.8676,-2)` | `7.9` | [emulator](../results.tsv) |
| `ROUND({22/6,7/6,13/6},{-3,3,4})` | `{3.67,1.167,2.1667}` | [emulator](../results.tsv) |

## Behaviour

**A negative number of places does not mean rounding to tens and hundreds.**
`ROUND(7.8676,-2)` answers 7.9, not 0 (HP help): a negative argument asks for
that many **significant figures**, so -2 gives two of them. Coming from
almost any other language, this is the one that surprises.

A positive argument is the ordinary meaning: 2 places gives 7.87 (HP help).

**The places may themselves be a list**, applied element by element alongside
the values: `{22/6,7/6,13/6}` with `{-3,3,4}` gives three significant figures,
then three decimal places, then four (HP help). The interpreter does not cover
that form and stops rather than answering (unverified: this kit's interpreter
on the PC, not a calculator), so it rests on HP's help alone.

Rounding for display is not the same as rounding a stored value, and this
changes the value (HP help). For a fraction that must survive comparison, see
the trap in [FP](FP.md).

## Related

[FP](FP.md) · [IP](IP.md) · [CEILING](CEILING.md)
