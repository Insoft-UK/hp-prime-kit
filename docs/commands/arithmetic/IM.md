# IM

The imaginary part of a complex number.

| | |
|---|---|
| Syntax | `IM(x+yi)` |
| Group | arithmetic |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `IM(3+4*i)` | `4` | [emulator](../results.tsv) |

## Behaviour

`IM(3+4*i)` answers 4 (emulator): the coefficient, as a plain number, without
the imaginary unit attached.

It is `TYPE` 0 (emulator),
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes), the same as
[RE](RE.md), so the pair takes a complex number apart into two ordinary
numbers a program can compare and print.

The pair form `(3,4)` was measured for [RE](RE.md) and not for this one
(unverified), though there is no reason to expect it to differ.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[RE](RE.md) · [ARG](ARG.md) · [CONJ](CONJ.md)
