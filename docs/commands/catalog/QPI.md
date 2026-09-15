# QPI

Turns a decimal into an exact form, as a fraction or a multiple of pi.

| | |
|---|---|
| Syntax | `QPI(expr, [digits])` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `QPI(0.5)` | `1/2` | [emulator](../results.tsv) |

## Behaviour

`QPI(0.5)` answers the fraction `1/2` (emulator), of type 8 -- the exact kind,
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers).

**That row shows the fraction half of the job and not the pi half.** A half is
not a rational multiple of pi, so this call could only answer a fraction. What
it does with a value that *is* such a multiple was not run (unverified), and
that is the probe worth having: `QPI(1.5707963)` should come back as pi over
two if the name means what it says.

It is the opposite direction from [PI](PI.md), which answers a decimal of type
0 and loses the exact constant at once (emulator). Together they are the two
sides of the same choice: work in decimals, or keep a symbol.

The second argument sets how many digits are considered (HP help), and it was
not run (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PI](PI.md) · [POLYROOT](POLYROOT.md)
