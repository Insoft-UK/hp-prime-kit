---
phase: 07-app-functions
plan: 01
status: complete
completed: 2026-09-13
key_files:
  - docs/commands/finance/*.md
  - docs/commands/results.tsv
commits: ["The 34 finance functions, and two families that check themselves"]
---

# Plan 01 summary: the finance functions

## What was built

- All 34 names of `finance`, covering the inventory exactly: none missing and
  none written that the list does not carry.
- 36 rows: the 34 calls plus two round trips sent as nested expressions.
- Phase 7 stands at 34 of 179.

## What this turned up

**`PercentMargin` and `PercentMarkup` hold each other's usual meanings.**
With a cost of 60 and a price of 100 the difference is 40; over the price
that is 40 per cent and over the cost it is 66.67. The calculator answers
66.67 to the one called *Margin* and 40 to the one called *Markup*, which is
the opposite of what those two words mean in ordinary accounting. Both
answers are plausible numbers, so a program carries the error silently and
nothing flags it. Each entry has a `Models get wrong` table, because reaching
for the name that sounds right is exactly what a model will do.

**Two families were shown to invert one equation, rather than being described
as though they did.** `BrkEvQuant` handed what `BrkEvProfit` answered comes
back to the hundred units it started from, exactly; `TvmPV` handed what
`TvmFV` answered comes back to −999.999999998, the thousand it started from
to nine figures. The difference between exact and nearly exact is itself
informative: the break-even family rearranges, the money family solves by
iteration. Both round trips were nested into single expressions so they could
travel inside `EXPR` and could not refuse the batch.

**The cash-flow family checks itself five ways.** At ten per cent the present
value is −21.0368144252 and the break-even rate is 8.8963, below the ten
demanded, which agrees. The future value is −28, which is the present value
times 1.1 cubed to every figure printed. The uniform series is −8.4592, the
same money said as three equal payments. The payback is 2.6, two periods plus
three fifths of the third. Each row supports the others.

**The three commands that take dates are the three that were refused.**
`DateDays`, `BondPrice` and `BondYield` all failed with dates written the way
the Prime displays them, while all 31 commands taking plain numbers answered.
That pattern is better evidence about the date shape than about the three
commands, and it is written as a hypothesis with its probe rather than as a
finding.

**`CashFlowMIRR` and `CashFlowFMRR` answered the same number, character for
character.** One example cannot separate them, so neither entry describes a
difference nobody here has measured. The probe is a list that turns negative
again after the outlay, where the two rates would have something to do. Phase
6 met this with two unit commands and answered it the same way.

**`BlackScholes` answers a list of two where every other name here answers a
number**, and its second element is exactly zero, which is worth suspicion
rather than belief. HP's own syntax row is truncated in the inventory, ending
part way through the sixth argument's name, so the full argument list is not
published in the data this kit holds.

**`ChangeNew` and `ChangeOld` do not match any simple reading.** For 100 and
ten per cent the first answers 10, not 110; for 110 the second answers 1100.
Their siblings `ChangePrice` and `ChangeCost` behave as a proper rise and
fall and are inverses of each other. The undocumented third argument, which
HP calls an option, is the suspect, and the entries say so instead of
inventing a rule from one row.

## Deviations

- **One missing label in 34 entries**, in `IntConvEff`, caught by the
  checker. The rate is better than Phase 6's, and the reason is that the
  checker was run at nine entries rather than at thirty-four: a defect in the
  shape would have been repeated twenty-five more times otherwise.
- **`Models get wrong` is a table, not prose.** Written as paragraphs first
  and corrected once the checker named the format.
- **Two regenerations were needed**, because editing an entry after
  `docs.build` leaves the group page stale. A suite run was started against
  that stale state and stopped rather than reported, since its verdict would
  have meant nothing.
- **The batch expired twice before it ran.** The harness waits thirty
  minutes, a watcher waited fifty-five more, and both gave up before the
  keypresses happened. Nothing was lost either time: the state file holds the
  cases and collection needs no resend.

## What this batch did NOT settle

The longest answer was 17 characters and nothing was cut, so no name in this
plan came near the harness's 160-character width.

**Corrected 2026-09-13.** This section first said the width question was open.
It is not: Phase 6 measured it. `SVD([[1,2],[3,4]])` came back truncated and
its row says so, 184 characters stored once the marker is counted, and
`matrix/SVD.md` and `matrix/SVL.md` document it. `QR`, `LQ`, `SCHUR` and
`EIGENVV` sit just under the limit at 152, 139, 124 and 107. What is true here
is narrower: nothing in phase 7 has yet produced an answer long enough to
reach it, so the risk has not recurred, not that the behaviour is unknown.

## Results

```
finance                     34 of 34
phase 7                     34 of 179
checker                     0 problems
suite                       6276 passed, 0 failed
```
