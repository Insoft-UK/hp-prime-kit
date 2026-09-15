# UPART

The unit out of a value that carries one.

| | |
|---|---|
| Syntax | `UPART(Value_Unit)` |
| Group | units |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `UPART(2_m)` | `1_m` | [emulator](../results.tsv) |

## Behaviour

**It answers `1_m`, not `m`.** The unit comes back with a coefficient of one
rather than as a bare symbol (emulator), so what you get is still a value
carrying a unit, of type 9,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

That matters to a program expecting text (emulator): there is nothing
here to print as a label without taking it apart further, and
comparing it against the string `"m"` will not match.

**With [UVAL](UVAL.md) it takes a unit value apart**, that one answering 2 for
the same argument (emulator). Two times one metre is the value that went in,
which is the pair's whole purpose.

HP's list gives this name no syntax string (HP help), so the shape above is
what the measured call shows.

What it answers for a compound unit, where the coefficient may not be one, was
not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[UVAL](UVAL.md) · [MKSA](MKSA.md) · [XPON](../numbers/XPON.md)
