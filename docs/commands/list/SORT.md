# SORT

Puts a list in order, optionally by a chosen element.

| | |
|---|---|
| Syntax | `SORT(list,[sort_by])` |
| Group | list |
| Runs on the PC | yes |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SORT({2,9,5,3})` | `{2,3,5,9}` | [emulator](../results.tsv) |
| `SORT({"foo","bar","bra"})` | `{"bar","bra","foo"}` | [emulator](../results.tsv) |
| `SORT({"foo","bar","bra"},2)` | `{"bar","foo","bra"}` | [emulator](../results.tsv) |

## Behaviour

Numbers sort smallest first and strings sort alphabetically (HP help). Both
of those run through the interpreter and agree with HP.

**The second argument sorts by one element rather than by the whole value.**
`SORT({"foo","bar","bra"},2)` answers `{"bar","foo","bra"}` (HP help): ordered
by each string's second character, a before o before r. Sorted whole, `"bra"`
would come second; it comes last. That is what the argument is for, and it is
easy to mistake for a direction flag.

**The interpreter refuses that form cleanly**, saying it does not cover `SORT`
with a second argument (unverified: that is this kit's interpreter on the PC,
not a calculator). That is a proper refusal rather than a crash, which is not
true of every uncovered name.

What it does with a list of lists, which HP's help also shows, is the same
idea applied to rows and has not been run here (unverified).

## Related

[CONCAT](CONCAT.md) · [SIZE](SIZE.md) ·
[ppl.one-based](../../topics/ppl.md#ppl.one-based)
