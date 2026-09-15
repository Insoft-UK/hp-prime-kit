---
phase: 07-app-functions
status: approved
verified: 2026-09-14
requirements: [CMD-10]
---

# Phase 7 verification: App functions

The criteria are counted here, not asserted. Every number was measured by
reading `docs/` and `results.tsv` on 2026-09-14, after the last build and
after the rounds run with each app active.

## Criterion 1: every app function on the list has an entry in the fixed format

| | |
|---|---|
| names the inventory files as `app function` | 179 |
| of those, with an entry | **179** |
| entries in a folder the list does not give them | 0 |
| problems reported by `docs.check` | **0** |
| suite | **9098 passed, 0 failed** |

Complete, and the format is enforced by the checker rather than by reading.

## Criterion 2: every example has a result on file, or says why it cannot

| | |
|---|---|
| examples across those 179 entries | 213 |
| labelled `emulator`, each with its row in `results.tsv` | **208** |
| labelled `G2`, measured by hand with the evidence in the entry | **4** |
| marked `*no value*` with the reason written out | **1** |
| with no result and no reason | **0** |

The `*no value*` is `randNorm`, whose answer differs on every run, so a stored
row would record one draw and hold every later run to it.

The four `G2` rows were read off the user's own calculator, firmware
2.4.15515, after the batches had run. `results.tsv` is written by
`hpprime examples` and never edited by hand, which is why a hand-read result
takes the `G2` label and carries its evidence in the entry instead.

## What the count does not say

**130 of the 179 names answered something; 49 did not.** By group:

```
geometry          71 of  84      statistics-1var   3 of   6
finance           30 of  34      statistics-2var   1 of   5
spreadsheet        4 of  22      explorer          4 of   4
inference          6 of   9      linear-solver     1 of   3
triangle-solver    5 of   6      solve             0 of   1
function           5 of   5
```

**One group still answers nothing: `solve`, which has one name.** It was two
groups before these rounds; `LinSolve` moved `linear-solver` off that list by
answering `{2,1}`.

**Of the 49 silent names, 22 were retried with their own app active and
refused anyway** -- 18 in `spreadsheet`, `DoSolve`, `Solve2×2`, `Solve3×3` and
`Solve`. Those are measured negatives. The other 27, in `geometry`,
`finance`, `inference`, `statistics-1var` and `statistics-2var`, were never
retried that way, and their entries say so rather than assuming the rule
would not have helped.

## What the hand measurements changed

**The phase's main finding came from four keypresses, not from a batch.** An
app's functions answer only while its app is active; the command does not
have to be typed inside the app, and selecting it is enough. With the
Triangle Solver active, `SSS(3,4,5)` answers on Home; with the Spreadsheet
active, `SUM({1,2,3})` answers 6; with the Function app active and `X^2-4`
entered in its editor, `ROOT(F1,1)` answers 2. All three are refused
otherwise. Recorded as
[apps.function-needs-active-app](../../../docs/topics/apps.md#apps.function-needs-active-app).

**The rule then survived into the batches, which is what the last rounds
tested.** The user selected an app by hand and the harness ran as usual: the
functions answered from inside the program, so what the keypresses reached
one call at a time, a batch reached forty at a time. That produced 39 rows
and turned 31 refusals from a defect into a condition.

**It is necessary but not sufficient, and the fact says so.** Eighteen of the
twenty-two `spreadsheet` names still refuse with the app open, most of them
statistics names wanting data in cells that an empty sheet does not hold.

**Three names do not follow the rule at all**: `Solve`, refused in five
forms, and `Solve2×2` and `Solve3×3`, refused in two each. Each was retried
with its own app active -- `Solve( )`, `Solve2×2( )`, `Solve3×3( )` -- and
refused there too. `LinSolve` answered from that same batch with that same app
open, so the conditions were demonstrably working when the refusals came --
which is what makes them negatives rather than silence. `Solve2×2` is a
*syntax error* by hand as well: not a refusal after reading the name, but a
name the calculator does not read.

**A second finding came free and is worth more than its size.** The Triangle
Solver answers in **degrees**, while everything else this documentation has
measured is in radians: `SSS(3,4,5)` gives `{36.8698976458,53.1301023542,90}`,
which matches degrees to ten figures and sums to 180. A program feeding those
angles into a trigonometric function is wrong by a factor near 57 and nothing
raises. Recorded as
[apps.triangle-solver-degrees](../../../docs/topics/apps.md#apps.triangle-solver-degrees),
with a `Models get wrong` table in `SSS`.

## Corrections made during the phase

Eight claims of this documentation were wrong and were corrected rather than
quietly dropped:

1. That `NTHROOT` was refused in both forms. The line map had been assumed
   rather than read.
2. That reporting a failure as text was `residue`'s own behaviour. Seven
   geometry commands do it, in three types.
3. That the 160-character width was untested. Phase 6 had measured it.
4. That the `function` group was unreachable. It computes; the probe saying
   otherwise never checked its own setup.
5. That the cause of the `spreadsheet` refusals was not established, and that
   `SAS` had been sent degrees on a radian calculator.
6. That the refusal was shared by all twenty-two `spreadsheet` names. Four of
   them answer. The sentence stood in 17 entries and the checker could not
   catch it: it was well-formed, correctly labelled, and only wrong.
7. That `AAS` and `ASA` could not be told apart. With the app active they
   answer different triangles, by arithmetic rather than by wording.
8. That `linear-solver` answered nothing. `LinSolve` solves a system when the
   coefficients arrive as one matrix with the right-hand side as its last
   column.

**Two arithmetic predictions written into entries before the rows arrived
were wrong, and the calculator was right both times**: `ISECT` was predicted
to answer 2 and answered 2.56155281281, and the linear system was predicted
to give `y = −1` and gave `{2,1}`. Both misses are recorded in the entries
instead of being replaced by the measured value, because a prediction is only
worth making if a miss is admitted.

Each correction came from measuring something that had been assumed, which is
the practice this phase should be judged on as much as on the count.

## Approval

- [x] Phase 7 approved to close -- the user, 2026-09-14
