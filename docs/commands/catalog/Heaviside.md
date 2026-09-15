# Heaviside

The step that is 0 below zero and 1 above it.

| | |
|---|---|
| Syntax | `Heaviside(Real)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("Heaviside(1)")` | `1` | [emulator](../results.tsv) |

## Behaviour

`Heaviside(1)` answers 1 (emulator), a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**HP's list gives this name no syntax string, and it is a function anyway**
(emulator). That absence is worth reading carefully, because three names in
this group share it and refuse the same shape: `INVERSE`, `NEG` and
`NTHROOT` are all rejected when written with parentheses. This one is not.
So a missing syntax string does not by itself mean the name is not called
like a function; it means HP published nothing, and the shape has to be
measured.

The syntax above is written from the call that answered, not copied from HP
(emulator).

What it answers at zero, where the two halves of the step meet, was not run
(unverified). That is the one value a reader would want, since sources
disagree between 0, one half and 1.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[Dirac](Dirac.md) · [PIECEWISE](PIECEWISE.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
