# UTPN

The upper tail of a normal distribution, refused as written here.

| | |
|---|---|
| Syntax | `UTPN(Mean, Variance, Value)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("UTPN(0,1,1.96)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused, and it follows HP's own syntax** (emulator). Mean 0,
variance 1 and the value 1.96 are three arguments in the published order, and
the answer is an error rather than a probability.

**All four of the upper-tail commands behave the same way** (emulator):
[UTPC](UTPC.md), [UTPF](UTPF.md), this one and [UTPT](UTPT.md) were sent in
one batch, each following its own published shape, and all four were refused.
Four refusals with four different argument counts is not four mistakes in
writing the calls; something they share is what the batch did not supply.

What they share is the way they were called (unverified). Each went through
[EXPR](../strings/EXPR.md), which evaluates a string as if it were typed on
Home. The probe is the same call written straight into a program instead,
which is a different context and the one HP's help describes.

Until that runs, this entry records a refusal and not a working form
(unverified). A program that needs the upper tail of a normal distribution
today has [NORMALD_CDF](../probability/NORMALD_CDF.md), which is measured:
the upper tail is one minus what it answers.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[NORMALD](../probability/NORMALD.md) ·
[NORMALD_CDF](../probability/NORMALD_CDF.md) · [UTPT](UTPT.md)
