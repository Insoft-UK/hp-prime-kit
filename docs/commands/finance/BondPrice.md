# BondPrice

The price of a bond, refused in the form tried here.

| | |
|---|---|
| Syntax | `BondPrice(settlement_date,maturity_date,coupon_percent,call_value,yield_percent,semi_annual,cal360)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BondPrice(1.012024,1.012034,5,100,6,2,0)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), with all seven arguments in the published
order: two dates, a coupon of five per cent, a call value of a hundred, a
yield of six, semi-annual coupons and an ordinary calendar.

**It shares its refusal with the other two commands that take dates**
(emulator): [DateDays](DateDays.md) and [BondYield](BondYield.md) were
refused in the same batch with dates written the same way, while every
finance command taking only plain numbers answered. That pattern points at
the dates rather than at the bond arithmetic, and [DateDays](DateDays.md)
carries the account and the probe.

**Nothing here measures the other six arguments** (unverified). If the date
shape is what is wrong, the rest of the list may be right as published; if it
is not, everything after the first two arguments is still untested. This
entry does not choose between those.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BondYield](BondYield.md) · [DateDays](DateDays.md)
