---
phase: 06-home-functions
plan: 04
status: complete
completed: 2026-09-13
key_files:
  - docs/commands/special/*.md
  - docs/commands/hyperbolic/*.md
  - docs/commands/trigonometry/*.md
  - docs/commands/units/*.md
  - docs/topics/ppl.md
commits: ["Hyperbolic, trigonometry, and eight of the nine special functions"]
---

# Plan 04 summary: the four small groups

## What was built

- All 27 names: 9 `special`, 6 `hyperbolic`, 6 `trigonometry`, 6 `units`.
- `ppl.type-codes` gained a measured code 9.

## What this turned up

**The angle mode was read rather than inferred.** `HAngle` answers 0 in the
same batch where `ACOT(1)` answers a quarter of pi, `ASEC(2)` a third and
`ACSC(2)` a sixth. So 0 is the radian mode, on this calculator in this state.
That closes half a question [ARC](../../../docs/commands/drawing/ARC.md) and
`ARG` had both recorded as open, each having measured something that looked
like radians while saying plainly that nobody had read the mode. The other
half -- what a different `HAngle` does to those answers -- is still
unmeasured, and `ACOT` says so.

**The `special` group does not behave alike, and that is its finding.**
`Gamma` computes: `Gamma(5)` is 24, which cross-checks against the `5!` that
answered 120 in the probability group. The other seven answer type 8. `Beta`
gives the exact fraction `1/12`; `Psi` and `Zeta` both give pi squared over
six, from different questions and in different batches; `Ci`, `Ei`, `Si` and
`erf` hand the call straight back unevaluated. `erfc` is the most revealing,
coming back rewritten as `1-erf(1)` -- algebra happening, which is what says
these are symbolic objects rather than names the calculator failed to know.

**Type 9 is measured, five times over.** Every unit-carrying answer is type 9:
`CONVERT`, `MKSA`, `UFACTOR`, `UPART` and `USIMPLIFY`. `TYPE(2_m)` answers 9
directly. It had been one of the codes taken from HP's help and never run, and
an earlier `TEVAL` answer had hinted at it without settling it. `UVAL` is the
contrast: it answers type 0, an ordinary number with the unit gone.

**`UVAL` and `UPART` take a unit value apart** -- 2 and `1_m`, which multiply
back to `2_m` -- the same division of labour `MANT` and `XPON` make for a
plain number. `UPART` answers `1_m` rather than a bare `m`, so there is
nothing there to print as a label without taking it further.

**Pi is the fifth character the calculator writes that nobody can type**,
after the minus sign, the imaginary unit, the exponent glyph and the radical.
`Psi` and `Zeta` both carry it, and both Result cells were built from the
stored row rather than typed.

## Deviations

- **`CONVERT` and `UFACTOR` answer identically** for the pair measured, so one
  example cannot tell them apart. Both entries say that rather than describing
  each as though the difference were known. The probe is a compound unit.
- **`MKSA` and `USIMPLIFY` returned their argument unchanged**, because a
  metre is already a base unit and has nothing to simplify. Those rows measure
  that the call is accepted, not what it does, and both entries say so.
- **Labels went missing again**: eight in one pass, eight in the next, one in
  the last. Two earlier diagnoses blamed batch size and were wrong. The real
  cause is narrower: a label's parentheses must contain no other parentheses,
  and a backticked call such as `ACOSH(2)` inside one breaks it exactly as a
  markdown link does. Applied as a rule, that class produced zero failures in
  the following pass.
- **`Psi.md` failed to write** because `docs/commands/special/` did not exist
  yet and `io.open` does not create parent directories, where the Write tool
  does. Caught by the error, not by a check.
- Appending labels to already-wrapped text left lines over 100 characters
  twice, re-wrapped both times.

## Results

```
special                     9 of 9
hyperbolic                  6 of 6
trigonometry                6 of 6
units                       6 of 6
```
