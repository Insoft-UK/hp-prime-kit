# erfc

The complementary error function.

| | |
|---|---|
| Syntax | `erfc(x)` |
| Group | special |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `erfc(1)` | `1-erf(1)` | [emulator](../results.tsv) |

## Behaviour

**It was rewritten, not evaluated.** `erfc(1)` comes back as `1-erf(1)`, of
type 8 (emulator),
[ppl.exact-answers](../../topics/ppl.md#ppl.exact-answers). The calculator
turned one function into an expression in another and stopped there.

That makes it the most revealing row of the group. [erf](erf.md) and three
others echo the call back unchanged; this one shows the algebra happening,
which is what says these are symbolic objects being manipulated rather than
names the calculator failed to recognise (emulator).

A program wanting a number from either has to convert it, and nothing here
measures what does that (unverified).

The identity it used -- that the complement is one minus the function -- is
the definition, so the rewrite loses nothing (unverified).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[erf](erf.md) · [Ci](Ci.md) · [Ei](Ei.md)
