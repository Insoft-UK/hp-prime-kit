# IFTE

Answers one of two values, depending on a test.

| | |
|---|---|
| Syntax | `IFTE(Expr, TrueClause, FalseClause)` |
| Group | catalog |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("IFTE(1<2,10,20)")` | `10` | [emulator](../results.tsv) |

## Behaviour

`IFTE(1<2,10,20)` answers 10 (emulator): the test holds, so the second
argument is the answer. It is a plain real, type 0,
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes).

**It is an expression, where `IF` is a statement** (emulator). This can sit
inside a larger formula and give it a value, which a branch cannot do. That
is the reason to reach for it rather than for [IF](../branch/IF.md).

**It is the two-case form of [PIECEWISE](PIECEWISE.md)** (emulator), which
takes up to eight test-and-value pairs and answers the first that holds.
Where a program has exactly one condition, this is the shorter spelling of
the same thing.

Whether both clauses are evaluated before the test decides, or only the one
that wins, was not measured (unverified). It matters when a clause is
expensive or changes something.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[PIECEWISE](PIECEWISE.md) · [IF](../branch/IF.md) ·
[ppl.type-codes](../../topics/ppl.md#ppl.type-codes)
