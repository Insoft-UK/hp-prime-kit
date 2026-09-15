# GETBASE

Answers the base a based integer is written in.

| | |
|---|---|
| Syntax | `GETBASE(#integer[m])` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("GETBASE(#12h)")` | `#4h` | [emulator](../results.tsv) |

## Behaviour

`GETBASE(#12h)` answers `#4h` (emulator), itself a based integer of type 1,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**The answer is a code, not the number 16** (emulator). A hexadecimal
argument came back as 4, so what this gives is an identifier for the base
rather than the base itself, and `#4h` is written in hexadecimal too, which
makes the answer easy to misread as data about the value.

What the other codes are was not run (unverified). Four suggests a small
numbering over the bases the Prime writes -- binary, octal, decimal and
hexadecimal -- but which number means which is not established by one row,
and this entry does not guess it. The probe is the same call on `#12b`,
`#12o` and `#12d`.

That the argument is a based integer at all is part of the syntax (HP help):
the `#` and the trailing letter are how the Prime writes one, and a plain
number is a different type.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[MEMORY](MEMORY.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
