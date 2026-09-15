# MEMORY

Answers two figures about the calculator's memory.

| | |
|---|---|
| Syntax | `MEMORY` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("MEMORY")` | `{#356B000:64h,#86B6D58000:64h}` | [emulator](../results.tsv) |

## Behaviour

`MEMORY` answers a list of two based integers (emulator), type 6,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). Each is written with
the `:64h` suffix, which is how the Prime writes a 64-bit based integer.

**Which figure is which is not established** (unverified). The two are far
apart in size, and free-against-total is the obvious reading, but one row on
one calculator does not separate that from any other pair. The probe is the
same call after loading something large.

**It takes no parentheses** (HP help), which is the shape a name with no
arguments has, the same as [SERIAL](SERIAL.md) and `VERSION`.

The figures belong to the machine that answered and are not a property of the
Prime as a model (emulator). A different calculator, or the same one with
different content, gives different numbers, so nothing here is a constant to
compare against.

Unlike [SERIAL](SERIAL.md), nothing in this answer identifies the calculator,
which is why the row is stored where that one's is not (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SERIAL](SERIAL.md) · [GETBASE](GETBASE.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
