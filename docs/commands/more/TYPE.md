# TYPE

What kind of value something is, as a number.

| | |
|---|---|
| Syntax | `TYPE(value)` → number |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `TYPE(3)` | `0` | [emulator](../results.tsv) |
| `TYPE("a")` | `2` | [emulator](../results.tsv) |
| `TYPE([[1,2],[3,4]])` | `4` | [emulator](../results.tsv) |
| `TYPE({1,2})` | `6` | [emulator](../results.tsv) |

## Behaviour

Four of the codes are measured, each by a call of its own (emulator), and the
rest come from HP's help: 1 integer, 3 complex, 5 error, 8 function, 9 unit,
and 14.x for a CAS object. The whole table is
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**Watch 3 and 4.** This kit had them the other way round until HP's help was
read, so `IF TYPE(v) == 3` branched on complex numbers where it meant
matrices. The measurement above settles 4; 3 is still HP's word (HP help).

A number is 0 whether it is whole or not: `TYPE(3)` is 0, and nothing here
has produced a 1, which is what HP calls an integer (emulator). The `#`
integers that [SETBITS](../integer/SETBITS.md) answers do come back as 1, so
that is where the distinction lives.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified). That is why the four calls above are examples here
rather than in `SIZE`'s entry, where the question first came up.

## Related

[ppl.type-codes](../../topics/ppl.md#ppl.type-codes) ·
[SETBITS](../integer/SETBITS.md) · [SIZE](../list/SIZE.md)
