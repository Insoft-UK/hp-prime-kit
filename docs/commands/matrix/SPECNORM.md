# SPECNORM

The spectral norm: the largest singular value.

| | |
|---|---|
| Syntax | `SPECNORM(matrix)` |
| Group | matrix |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `SPECNORM([[1,2],[3,4]])` | `5.46498570422` | [emulator](../results.tsv) |

## Behaviour

`SPECNORM([[1,2],[3,4]])` answers 5.46498570422 (emulator), and
[SVL](SVL.md) answers `[0.365966190626,5.46498570422]` for the same matrix:
the singular values, of which this is the larger (emulator). The two commands
agree to every digit, which is what says this is the singular value and not
something else.

**Four commands answer a "norm" for this one matrix and no two agree**:
6 from [COLNORM](COLNORM.md), 7 from [ROWNORM](ROWNORM.md), 5.47722557505
from [ABS](ABS.md) and 5.46498570422 here (emulator). Reaching for "the norm"
without naming which one is how a program ends up with a plausible wrong
number.

It is also not [SPECRAD](SPECRAD.md), which answers 5.37228132327 from the
eigenvalues rather than the singular values (emulator).

It answers a plain number, `TYPE` 0 (emulator).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[SVL](SVL.md) · [SPECRAD](SPECRAD.md) · [COLNORM](COLNORM.md) ·
[ABS](ABS.md)
