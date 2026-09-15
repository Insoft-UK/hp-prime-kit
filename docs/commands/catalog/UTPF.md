# UTPF

The upper tail of a Fisher distribution, refused as written here.

| | |
|---|---|
| Syntax | `UTPF(Numerator, Denominator, Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("UTPF(2,3,1)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused, and it follows HP's own syntax** (emulator): two
degrees of freedom for the numerator, three for the denominator and the value
1, in the published order.

**It is one of four refused together** (emulator). [UTPC](UTPC.md), this one,
[UTPN](UTPN.md) and [UTPT](UTPT.md) were sent in the same batch, each with
its own published shape, and every one came back an error. The shared
explanation is set out in [UTPN](UTPN.md), which also names the probe.

A program that needs this today has
[FISHER_CDF](../probability/FISHER_CDF.md), which is measured: the upper tail
is one minus what it answers (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[FISHER](../probability/FISHER.md) ·
[FISHER_CDF](../probability/FISHER_CDF.md) · [UTPN](UTPN.md)
