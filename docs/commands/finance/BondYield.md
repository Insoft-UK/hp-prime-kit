# BondYield

The yield of a bond, refused in the form tried here.

| | |
|---|---|
| Syntax | `BondYield(settlement_date,maturity_date,price,coupon_percent,call_value,semi_annual,cal360)` |
| Group | finance |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("BondYield(1.012024,1.012034,95,5,100,2,0)")` | *error* | [emulator](../results.tsv) |

## Behaviour

**The call is refused** (emulator), with the seven arguments in the published
order: two dates, a price of ninety-five, a coupon of five per cent, a call
value of a hundred, semi-annual coupons and an ordinary calendar.

**It is the inverse of [BondPrice](BondPrice.md)**, which takes a yield and
answers a price where this takes a price and answers a yield (HP help). Both
were refused in the same batch, so neither could be used to check the other,
which is the round trip that would have settled the argument order the way
the `Tvm` and `BrkEv` families were settled.

**The dates are the shared suspect** (emulator): this, [BondPrice](BondPrice.md)
and [DateDays](DateDays.md) are the three finance commands taking dates and
the three that were refused, while the plain-number commands all answered.
[DateDays](DateDays.md) carries the account and names the probe.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[BondPrice](BondPrice.md) · [DateDays](DateDays.md)
