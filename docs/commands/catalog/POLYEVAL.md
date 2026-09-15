# POLYEVAL

Works a polynomial out at a value.

| | |
|---|---|
| Syntax | `POLYEVAL(Vector, Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `POLYEVAL([1,2,3],2)` | `11` | [emulator](../results.tsv) |

## Behaviour

`POLYEVAL([1,2,3],2)` answers 11 (emulator): four plus four plus three, so the
vector is read as x squared plus two x plus three, **highest power first**.

That ordering is the thing to get right. Read the other way round the same
vector would be three x squared plus two x plus one, which at 2 gives 17 --
a plausible number rather than an error (emulator, and the arithmetic that
separates the two readings).

It is the same ordering [POLYCOEF](POLYCOEF.md) answers with, so the two
commands agree about how a polynomial is written down (emulator).

The polynomial is a vector of type 4 and the answer a plain real of type 0
(emulator), [ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[POLYCOEF](POLYCOEF.md) · [POLYROOT](POLYROOT.md)
