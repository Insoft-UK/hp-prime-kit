---
phase: 08-app-variables
plan: 04
status: complete
completed: 2026-09-16
key_files:
  - docs/commands/finance/*.md
  - docs/topics/apps.md
  - docs/commands/inference/*.md
  - docs/commands/triangle-solver/*.md
  - .planning/STATE.md
commits: []
---

# Plan 04 summary: the Finance app, which split three ways

## What was built

- **97 rows** from two batches: 73 with no app selected -- all 68 Finance
  variables and five Inference lists as controls -- then 24 with Finance
  selected. None overwrote a stored row: every call text was generated
  against the stored keys, and a diff against the last commit confirmed it.
- **68 entries written**, the Finance app's whole variable group.
- **One new fact**, `apps.finance-shows-two-decimals`, and a paragraph added
  to `apps.function-needs-active-app` narrowing what it says about variables.
- **16 entries corrected**, two of them for two reasons: `Xlist` and its five
  sibling lists, `AngleA` and `SideA`, four Triangle Solver entries that declared an assignment nobody had
  measured, `Alpha` and `Ylist` which had measured one and did not declare it,
  and eight Inference entries that labelled a name's meaning `(HP help)`.

## What this turned up

**Neither outcome the plan prepared for.** It expected Finance's variables to
answer from any app or to refuse; they did both, and then some refused even
with Finance selected. Three classes, cleanly separated:

| class | count | names |
|---|---|---|
| answer from any app | 50 | everything but the eighteen below |
| need Finance selected | 9 | `NbPmt`, `IPYR`, `PV`, `PMT`, `FV`, `PPYR`, `CPYR`, `BEG`, `GSize` |
| refuse either way | 9 | `NPV`, `NFV`, `NUS`, `IRR`, `MIRR`, `FMRR`, `Payback`, `DiscPayback`, `BSPut` |

**A name clash does not explain the split.** No name on either side collides
with another name on HP's list, which was the first thing checked.

**The nine that need Finance are the time-value-of-money names**, and five of
them have a twin function -- `TvmPV` and its siblings -- that answered in
Phase 7 without the app. So in this app the functions are free and the
variables they correspond to are not.

**The nine that refuse either way are probably refusing an empty question.**
Eight are results of the cash flows, and `CFData`, the list of cash flows,
read `{}` in both batches, while `TotalCF`, their plain sum, answered 0. A sum
of nothing is 0; a present value or a payback period of nothing has none. The
entries say "likeliest" and name the probe: fill `CFData`, read `NPV` again.
`BSPut` is the one without that excuse: its twin `BSCall` answers 0 with the
same inputs, all 0.

**With Finance active, every number comes back with two decimals.** `CFPYR`
was `12` with the Function app active and `12.00` with Finance; `BSCall` and
`TotalCF` went from `0` to `0.00`. The harness makes each answer's text with
`STRING` on the calculator, so this is what a program doing the same would
get: text that depends on which app is active. It was not being looked for.

**A program can set a time-value variable.** `PV:=1000` answered `1000.00`
and a later read answered the same.

**`Xlist` is not alone.** All five of the Inference app's other lists answered
`{}` with the Function app active. Its entry had called it the single
exception on file.

**The rule about variables was too broad, in three places.** `STATE.md`, the
fact, and the `AngleA` and `SideA` entries all said, in effect, that an app's
variables need the app. The Triangle Solver's and the Function app's do. Most
of Finance's do not, and the Inference app's lists do not. The fact now says
it holds variable by variable, and no entry inherits it without a row.

## Deviations

- **The first recount was wrong, by my script.** `strip('EXPR(")')` strips
  those *characters* from both ends, not the prefix, and ate letters from
  names like `PV`, `IRR` and `PPYR`; only 53 of 68 matched. The number did not
  add up, the parsing was rewritten, and the count came out 50 and 18.
- **Three prose errors survived the generator and the checker.** The nine
  time-value entries listed their names with mixed separators and linked each
  entry to itself; the cash-flow entries called a present value "a rate of
  return"; five date entries labelled `(emulator)` the claim that 2017.0101
  is a date. Found by reading four generated entries in full, and fixed in
  all twenty-two.
- **Two consistency rules were broken in entries already committed**, and are
  now stated in `STATE.md` so they hold from here: a `:=` form appears in
  Syntax only where an assignment was measured, and a name's meaning is
  `(unverified)` where HP's list gives only the name.

## Results

```
rows added                              97   (none overwritten)
app variables with an entry            130 of 172
entries                                598
new facts                                1   (apps.finance-shows-two-decimals)
entries corrected                       16
checker                                  0 problems
```
