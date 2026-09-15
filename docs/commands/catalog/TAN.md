# TAN

The tangent.

| | |
|---|---|
| Syntax | `TAN(Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TAN(1)` | `1.55740772465` | [emulator](../results.tsv) |

## Behaviour

`TAN(1)` answers 1.55740772465 (emulator): the tangent of one radian. The
mode is recorded once, in [ACOT](../trigonometry/ACOT.md).

**It is [SIN](SIN.md) over [COS](COS.md), and the three rows agree**:
0.841470984808 divided by 0.540302305868 gives this number to every digit
brought back (emulator, and the arithmetic between them).

Its reciprocal [COT](../trigonometry/COT.md) answers 0.642092615934 for the
same argument, which is one over this (emulator). Four commands across two
groups, all consistent on a single angle.

Unlike a sine or a cosine it has no bound, and near a quarter turn it grows
without limit. What it answers exactly there was not run (unverified), and the
calculator does have a way to write infinity, measured elsewhere in this
phase.

It answers a plain real, type 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SIN](SIN.md) · [COS](COS.md) · [ATAN](ATAN.md)
