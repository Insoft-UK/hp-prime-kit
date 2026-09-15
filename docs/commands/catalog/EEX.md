# EEX

On HP's list of names, and refused as a call.

| | |
|---|---|
| Syntax | not published |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("EEX")` | *error* | [emulator](../results.tsv) |

## Behaviour

**Evaluating the bare name is an error** (emulator), the same answer
[ALPHA](ALPHA.md) and [ICON](ICON.md) give, and unlike
[COLOR](COLOR.md), which hands its own name back.

HP's list carries the name with no syntax string (HP help).

What the name is for is not measured here (unverified). On the keyboard EEX
is how an exponent is entered, so the likeliest reading is that this is the
key rather than a function, and that the exponent it produces is the glyph
recorded in
[ppl.exponent-glyph](../../topics/ppl.md#ppl.exponent-glyph) -- a character
the calculator writes and nobody can type. Nothing run here shows that.

This entry records a refusal, not a working form (unverified).

The interpreter does not know the name at all (unverified), so `hpprime run`
cannot check a program that uses it.

## Related

[ALPHA](ALPHA.md) · [ICON](ICON.md) ·
[ppl.exponent-glyph](../../topics/ppl.md#ppl.exponent-glyph)
