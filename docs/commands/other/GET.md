# GET

On HP's list of names, and refused in every form tried.

| | |
|---|---|
| Syntax | `GET` |
| Group | other |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `EXPR("GET")` | *error* | [emulator](../results.tsv) |
| `EXPR("GET(1)")` | *error* | [emulator](../results.tsv) |
| `EXPR("GET(QPI(0.5))")` | *error* | [emulator](../results.tsv) |

## Behaviour

**It is on the list because the release notes of 2.2 name it** (HP help),
saying it behaves consistently on what [QPI](../catalog/QPI.md) answers. No
source says what it is, and the list gives it no group, which is why its
entry sits in `other`.

**Bare, with a number, and with `QPI`'s answer, all three were refused**
(emulator). A form with a string, `GET("A")`, was not tried: a quote inside
a string in `EXPR` needs a way of writing it nobody here has measured.

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[QPI](../catalog/QPI.md)
