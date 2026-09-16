# NPV

The net present value, refused with or without the Finance app.

| | |
|---|---|
| Syntax | `NPV` → real |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("NPV")` | *error* | [emulator](../results.tsv) |
| `EXPR(" NPV")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It refused with the Function app active and again with Finance's**
(emulator). So this is not the app rule, which freed nine of its neighbours
the moment Finance was selected -- see [PV](PV.md). Something other than the
active app keeps it from answering.

**It holds the net present value of the cash flows** (unverified): HP's list gives this name and its app, and
nothing more.

**The likeliest reason is that there is nothing to compute from** (unverified).
[CFData](CFData.md), the list of cash flows, read `{}` in the same batches,
and eight results of those cash flows -- this one among them -- refused while
[TotalCF](TotalCF.md), their plain sum, answered 0. A sum of nothing is 0; a
present value, a rate or a payback period of nothing has none to give. Filling `CFData` and reading this
again would settle it.

**Its twin function answers, given the flows as arguments** (emulator):
[CashFlowNPV](CashFlowNPV.md) was measured and returned a value. A program
wanting this number does not need the app at all.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[CashFlowNPV](CashFlowNPV.md) · [CFData](CFData.md) · [TotalCF](TotalCF.md)
