# AVERAGE

The mean of a list, once the Spreadsheet app is active.

| | |
|---|---|
| Syntax | `AVERAGE([Input])` |
| Group | spreadsheet |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("AVERAGE({2,4,6})")` | `4` | [emulator](../results.tsv) |
| `EXPR("AVERAGE({1,2,3})")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The two rows differ in one thing: whether the Spreadsheet was the active
app when the program ran** (emulator). With it active the mean of 2, 4 and 6
comes back as 4, a plain real of type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes). Without it, the same
kind of call is refused.

**The arguments differ only so that both rows could be kept** (emulator).
`results.tsv` keys a row by the entry and the exact text of the call, so
re-running the first call would have replaced its answer and lost the
contrast. Nothing about the values 1, 2, 3 against 2, 4, 6 matters here.

**This is the row that carried the rule from a keypress into a program**
(emulator). The rule itself was found by hand -- see
[SUM](SUM.md) -- and this one shows it holds for a batch as well, so the
harness can measure these names once somebody selects the app first.

**Only four of the group's twenty-two names answer even then** (emulator):
this one, [SUM](SUM.md), [CellHasData](CellHasData.md) and
[ClearCell](ClearCell.md). The rest want something the app does not have on
a calculator reset before the run -- data in its cells -- or may belong to
another app entirely; [SUM](SUM.md) carries that account.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SUM](SUM.md) · [CellHasData](CellHasData.md) · [STAT1](STAT1.md) ·
[apps.function-needs-active-app](../../topics/apps.md#apps.function-needs-active-app)
