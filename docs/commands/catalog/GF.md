# GF

Builds a Galois field and describes it back as text.

| | |
|---|---|
| Syntax | `GF(Integerp, Integern)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("GF(2,3)")` | `"GF(2,v^3+v+1,[v,k,g],undef)"` | [emulator](../results.tsv) |

## Behaviour

`GF(2,3)` answers the text `GF(2,v^3+v+1,[v,k,g],undef)` (emulator), a string
of type 2, [ppl.type-codes](../../topics/ppl.md#ppl.type-codes). The answer
is a description of the field rather than a number.

**The answer names more than the call did** (emulator). Two arguments went
in, the characteristic 2 and the degree 3, and what came back also carries a
polynomial `v^3+v+1`, whose degree is the 3 that was asked for, along with
three names and the word `undef`. So the calculator chose the polynomial; it
was not given one.

What the three names and the final `undef` stand for is not established here
(unverified). Reading them as a variable, a generator and a placeholder for
something not yet set is the obvious guess and no row measured it.

**A string is an odd thing for this to answer** (emulator). Every other
constructor measured in this group answers an object the calculator can
compute with; this one answers text describing an object. Whether the field
is usable afterwards, and under which of those names, was not run
(unverified).

It is a computer-algebra name that HP files with the machine commands rather
than with the mathematics (HP help), which is the inventory's arrangement and
not a statement about what it does.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[GETBASE](GETBASE.md) · [QUOTE](QUOTE.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
