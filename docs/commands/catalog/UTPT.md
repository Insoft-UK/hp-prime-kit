# UTPT

The upper tail of a Student distribution, refused as written here.

| | |
|---|---|
| Syntax | `UTPT(Degrees, Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("UTPT(5,2)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused, and it follows HP's own syntax** (emulator): five
degrees of freedom and the value 2, in the published order.

**It is one of four refused together** (emulator). [UTPC](UTPC.md),
[UTPF](UTPF.md), [UTPN](UTPN.md) and this one were sent in the same batch,
each with its own published shape, and every one came back an error. The
shared explanation is set out in [UTPN](UTPN.md), which also names the probe.

A program that needs this today has [STUDENT_CDF](../probability/STUDENT_CDF.md),
which is measured: the upper tail is one minus what it answers (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STUDENT](../probability/STUDENT.md) ·
[STUDENT_CDF](../probability/STUDENT_CDF.md) · [UTPN](UTPN.md)
