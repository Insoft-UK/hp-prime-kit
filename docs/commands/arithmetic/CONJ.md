# CONJ

The complex conjugate: the same number with the imaginary part negated.

| | |
|---|---|
| Syntax | `CONJ(x+yi)` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `CONJ(3+4*i)` | `3-4*` | [emulator](../results.tsv) |

## Behaviour

**The answer is a complex number, and it does not come back the way it went
in.** `3+4*i` was typed with the ASCII letter `i`; what came back is
`3-4*` followed by U+E003, a character in Unicode's private use area
(emulator). That is the Prime's own glyph for the imaginary unit, and the
Result cell above holds it literally because that is what the calculator
answered. It is recorded as a rule in
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit).

**This is the first measurement of `TYPE` 3.** The answer's type came back as
3 (emulator), which HP's help calls complex and which nothing here had run
until now, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). The help's
warning about 3 and 4 being easy to swap is now measured on one side.

A program that compares this answer against text of its own will not match
(emulator), because the character it must contain is not on any keyboard the
program was written with.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RE](RE.md) · [IM](IM.md) · [ARG](ARG.md) ·
[ppl.imaginary-unit](../../topics/ppl.md#ppl.imaginary-unit)
