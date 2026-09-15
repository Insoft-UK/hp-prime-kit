# UTPC

The upper tail of a chi-square distribution, refused as written here.

| | |
|---|---|
| Syntax | `UTPC(Degrees, Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("UTPC(3,2)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused, and it follows HP's own syntax** (emulator): three
degrees of freedom and the value 2, in the published order.

**It is one of four refused together** (emulator). This one, [UTPF](UTPF.md),
[UTPN](UTPN.md) and [UTPT](UTPT.md) were sent in the same batch, each with
its own published shape, and every one came back an error. The shared
explanation is set out in [UTPN](UTPN.md), which also names the probe.

A program that needs this today has
[CHISQUARE_CDF](../probability/CHISQUARE_CDF.md), which is measured: the
upper tail is one minus what it answers (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CHISQUARE](../probability/CHISQUARE.md) ·
[CHISQUARE_CDF](../probability/CHISQUARE_CDF.md) · [UTPN](UTPN.md)
