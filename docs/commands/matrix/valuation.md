# valuation

The order of the lowest-degree term of a polynomial.

| | |
|---|---|
| Syntax | `valuation(Poly, [Var])` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `STRING(valuation(X^2+X))` | `"-Inf"` | [emulator](../results.tsv) |
| `TYPE(valuation(X^2+X))` | `0` | [emulator](../results.tsv) |

## Behaviour

**The call answered negative infinity, as an ordinary real.** Asked for as
text it reads `"-Inf"`, and its `TYPE` is 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes) -- not a CAS object and
not an error, just a real the calculator holds as infinite.

**That is almost certainly not the valuation of `X^2+X`.** The lowest-degree
term of that polynomial is `X`, so 1 is the answer to expect; minus infinity
is the conventional valuation of zero (unverified). The likely explanation is
that `X` held nothing, so the argument was worked out as a number rather than
kept as a polynomial, and the call did not ask what it looks like it asks.
The probe that would settle it gives `X` a value or quotes the expression, and
it has not been run.

That makes this entry a record of one measured answer rather than a
description of what the command does, in the same way `C→PX` once recorded a
call made with the wrong shape of argument (unverified).

**This is the value that broke the harness.** Its bytes are
`F3 91 99 99 99 99 99 29`: exponent 499, a mantissa of nines, and a sign
nibble of 2 where an ordinary negative uses 9 (emulator). `hpprime examples`
could not decode it, and because a batch is collected all at once, seventeen
calls were lost with it. The two examples above avoid the number field
entirely -- one asks for text, the other for a type code -- which is why they
came home. What the kit does about the format is written down in the project's
own notes rather than here.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[ihermite](ihermite.md) · [ismith](ismith.md) · [jordan](jordan.md)
