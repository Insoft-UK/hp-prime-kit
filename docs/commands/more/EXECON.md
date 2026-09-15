# EXECON

Applies one expression to the elements of one or more lists.

| | |
|---|---|
| Syntax | `EXECON("&Expr", List1, [List2,…])` → list |
| Group | more |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXECON("&1+1",{1,2,3})` | `{2,3,4}` | [emulator](../results.tsv) |
| `EXECON("&1+&2",{1,2,3},{10,20,30})` | `{11,22,33}` | [emulator](../results.tsv) |

## Behaviour

**`&1` stands for an element of the first list**, and the expression runs once
per element: `"&1+1"` over `{1,2,3}` answers `{2,3,4}` (emulator). The answer
is a list of the same length, so this is the command for doing arithmetic
across a whole list without writing a loop.

**`&2` is the element of the second list, paired by position.** `"&1+&2"` over
`{1,2,3}` and `{10,20,30}` answers `{11,22,33}` (emulator): 1 with 10, 2 with
20, 3 with 30. The lists are walked together, not crossed, which is the thing
worth knowing before reaching for it -- two lists of three give three answers,
not nine.

The expression goes in as a string, quoted, in both measured calls
(emulator). What the answer's `TYPE` is comes back as 6, a list,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

What it does with lists of different lengths has not been measured
(unverified), and neither has a third list.

It ran in the same small batch as [CAS](CAS.md) and deliberately before it,
so that a command which may change the evaluation mode had no row of this one
underneath it (emulator: the order was chosen, not incidental).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CAS](CAS.md) · [EVAL](EVAL.md) · [ITERATE](ITERATE.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
