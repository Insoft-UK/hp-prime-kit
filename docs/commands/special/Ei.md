# Ei

The exponential integral.

| | |
|---|---|
| Syntax | `Ei(x)` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `Ei(1)` | `Ei(1)` | [emulator](../results.tsv) |

## Behaviour

**The answer is the call itself**, of type 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers), as for
[Ci](Ci.md) and [Si](Si.md).

Five of the nine names in this group answer that way, one rewrites itself and
one computes, which makes the group the clearest example in the phase of a
family whose members do not behave alike (emulator).

It has a singularity at zero and its value there is not a number, so what the
calculator does with `Ei(0)` is the probe worth having, especially now that
the calculator is known to have a way of writing infinity (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Ci](Ci.md) · [Si](Si.md) · [erf](erf.md)
