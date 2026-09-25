# The file formats

Facts about the files the calculator reads and writes, rather than about one
command. Each has an identifier, says how it is known, and is stated here
once.

This is the most technical page here and the one you least need in order
to start: writing your first program needs none of it, and the
[guided path](../start/02-first-program.md) does that in three commands. Come
here when something does not add up, when you want to move a lot of data, or
out of curiosity.

None of it is documented by HP. It was worked out by measuring real files
written by the Connectivity Kit and by the calculator, and checked by
rebuilding them byte for byte. The practical conclusion is that the PPL source
sits inside verbatim, as UTF-16LE: not compressed, not encrypted, so a program
can be read and written from the PC. Mind the last step, which has traps of
its own: see [deploy.md](deploy.md).

## How this is verified

A round trip is not enough on its own: reading and writing with the same
mistake gives a perfect round trip and a wrong answer. That happened here --
an early version carried 88 bytes of header along as though they were source,
and the round trip came out identical anyway. What verifies it is rebuilding a
program from a **different-sized** template and comparing with what the
Connectivity Kit wrote, because that exercises the length arithmetic:

| Test | Result |
|---|---|
| Round trip of a code program (37 KB) | identical |
| Round trip of a data program (1 MB, with compiled block) | identical |
| Round trip of an `.hpappprgm` | identical |
| Round trip of the factory apps (with CRLF) | identical |
| An 11,918-character program rebuilt from an 18,007-character template | byte for byte equal to the CK's file |
| A 579-character factory app from the same template | byte for byte equal |

`python tests/test_program.py` repeats it against whatever binaries are on
your machine, and `python tests/test_numbers.py` does the same for the
numbers. A program built this way runs on a G2
([deploy.writer-on-hardware](deploy.md#deploy.writer-on-hardware)),
which is what makes the container facts below `G2` rather than a theory about
bytes.

Reading and writing from the command line:

```bash
hpprime read  PROG.hpprgm -o source.txt
hpprime write source.txt -o PROG.hpprgm
hpprime matrix read  M1.hpmat -o data.csv
hpprime matrix write data.csv -o M0.hpmat
hpprime matrix nums PROG.hpprgm
```

---

<a name="formats.container"></a>
## The .hpprgm is a nested TLV container

| | |
|---|---|
| Identifier | `formats.container` |
| Kind | rule |
| Known from | G2 |

All little-endian. Every record is a 4-byte length followed by that many
bytes; inside the payload, some records carry a 4-byte tag before their
children and some do not, which is why walking the tree by taking the last
child does not work.

```
offset  contents
------  ----------------------------------------------------------
0       7C 61 8A B2                       magic
4       FE FF FF FF   00 00 00 00         preamble
12      [u32 length][length bytes]        records, nested
...     (optional) compiled block
...     [u32 length][u32 tag][UTF-16LE source][NUL]
...     trailer
```

**Evidence.** Measured on real files from a G2's Connectivity Kit mirror and
rebuilt byte for byte, including a rebuild from a different-sized template;
the resulting program runs on a G2 with firmware 2.4.15515.

<a name="formats.source-record"></a>
## The source record is found by its shape, innermost first

| | |
|---|---|
| Identifier | `formats.source-record` |
| Kind | rule |
| Known from | G2 |

The source record is `[u32 length][u32 tag][UTF-16LE text][NUL]`. To find it:
walk the offsets **byte by byte**, not in steps of 4, keep the blocks that
decode as UTF-16LE, end in NUL and are nearly all printable, take the largest,
and then, of the ones ending where that one ends, take the **innermost**. The
records to patch when the text changes are the ones that end exactly where it
ends.

The sweep is byte by byte because a compiled block sitting before the source
is not a multiple of 4 bytes long, so the source record ends up unaligned: in
one data program it starts at an odd offset.

**Evidence.** The rule recovers the source of every binary in the mirror, and
the writer built on it produces files the Connectivity Kit's own output
matches byte for byte.

<a name="formats.wrapper-trap"></a>
## A record that wraps the source can read as text too

| | |
|---|---|
| Identifier | `formats.wrapper-trap` |
| Kind | rule |
| Known from | G2 |

Taking the largest text-like candidate on its own is wrong. The wrapper starts
eight bytes ahead of the source record, so its payload begins with that
record's own header: four bytes of length, four of tag. When the low half of
the length lands on `<printable ASCII> 00`, the wrapper decodes as text as
well, it is bigger, it wins, and what comes back is those header bytes with
the source glued behind them. 97 source lengths in every 32,768 do it, one in
340, and the file is not at fault: one character more or less in the source
and it passes. This is what
[formats.source-record](#formats.source-record)'s innermost rule exists for --
a record that ends where another ends and starts before it contains it rather
than sitting beside it.

**Evidence.** Found on a generated app source whose length changes with its
data, refused because what had just been written did not read back.
`tests/test_program.py` writes the five edge lengths every run: 32,726;
32,737; 32,784; 32,801; 32,848.

<a name="formats.trailer-varies"></a>
## The trailer is not constant, so it is copied rather than built

| | |
|---|---|
| Identifier | `formats.trailer-varies` |
| Kind | rule |
| Known from | G2 |

It is 1,008 bytes in most files, the factory apps contradict even that, and it
can carry metadata inside: between two files with the same source, 15 bytes of
difference appeared there, with UTF-16 text in them. So nothing is assumed.
What follows the source is preserved as it is when rewriting, and when
generating, the template's trailer is copied. The calculator accepts the
result, which does mean generating is not byte-exact for an arbitrary file: it
is exact for the lengths and the source, which is what the writer builds.

**Evidence.** Measured across the programs of a G2's mirror, and the generated
files run on a G2.

<a name="formats.header-words"></a>
## Two header words vary between files, and nobody knows what they mean

| | |
|---|---|
| Identifier | `formats.header-words` |
| Kind | rule |
| Known from | unverified |

| Offset | Values seen |
|---|---|
| 20 | 2 in the three programs of one calculator; 0 in the other nine, and in the shipped template |
| 44 | 0 to 7, a different value for most programs of the same calculator; 0 in the shipped template. In the symbol table it is 0 in a program with no globals and 1, 2, 4, 5, 7, 8, 9, 11 or 12 in ones that have them, with no relation to how many |

Neither is a length: the sizes add up either way. Programs written from the
shipped template, with 0 in both, run on a G2, so the calculator does not need
them to hold anything else. The writer copies them from its template.

**Evidence.** Read from the twelve programs of one Connectivity Kit mirror,
not measured on a calculator. `tests/test_program.py` reports them rather than
failing on them.

<a name="formats.line-endings"></a>
## The stored source has LF endings and no trailing newline

| | |
|---|---|
| Identifier | `formats.line-endings` |
| Kind | rule |
| Known from | G2 |

The Connectivity Kit stores the editor's buffer. A normal PC text file does
have a trailing newline, so generating has to drop one to come out byte for
byte as the CK would write it. HP's factory apps carry CRLF inside, and the
container accepts both.

**Evidence.** Measured on the mirror's files; the round trip of the factory
apps, CRLF included, is identical.

<a name="formats.source-offset-152"></a>
## Source at offset 152 means no compiled block, which is what a template needs

| | |
|---|---|
| Identifier | `formats.source-offset-152` |
| Kind | rule |
| Known from | G2 |

A program with only code, as the Connectivity Kit writes it, is header +
source + trailer, with the source starting at offset 152 exactly. Anything
above 152 is compiled block, and that is the test for whether a file can act
as a template. A looser threshold lets through the small blocks the calculator
adds, of 96, 184 and 360 bytes, and then what you generate comes out exactly
that many bytes short.

**Evidence.** Measured across a mirror's programs; `hpprime templates` applies
the test, and on one machine 2 of 58 files qualified.

<a name="formats.two-producers"></a>
## The calculator adds a compiled block to anything it saves

| | |
|---|---|
| Identifier | `formats.two-producers` |
| Kind | rule |
| Known from | G2 |

| Written by | What it puts in | Same source, measured |
|---|---|---|
| The Connectivity Kit | the source only | 38,888 B |
| The calculator, on saving | source + its compiled block | 42,078 B (3,190 of block) |

So the block is not only in data programs. Both read equally well and both
round-trip exactly, but a template has to be a Connectivity Kit file: the
calculator's carry a block that would stop matching the new source, and the
writer rejects them for that reason.

**Evidence.** The same source written both ways on a G2 with firmware
2.4.15515, and the two files measured.

<a name="formats.block-is-a-cache"></a>
## The compiled block is a cache the calculator rebuilds

| | |
|---|---|
| Identifier | `formats.block-is-a-cache` |
| Kind | rule |
| Known from | G2 |

A program that declares large matrices carries a block before the source, with
the numbers already in the calculator's internal format: 367 KB of it in a data
program whose source is 632 KB. That block is what makes a data program open
instantly on the calculator that receives it. It does not have to be
generated: write the matrices as literals in the source and build the program
like any other.

When the rebuild happens -- on arrival or on the first run -- is not
established, and it is not a manual compile. How long a large one takes to
compile on receipt has not been timed: two small matrices are instant, and
hundreds of kilobytes nobody has measured. That is also the limit on how large
a generated data program can usefully be.

**Evidence.** Measured on a G2 with firmware 2.4.15515: a program was
installed with one number in its block changed and its source left alone; it
answered with the source's value, and the copy that came back had the block
rebuilt.

<a name="formats.block-not-byte-stable"></a>
## The same source compiled twice gives different blocks

| | |
|---|---|
| Identifier | `formats.block-not-byte-stable` |
| Kind | rule |
| Known from | G2 |

The blocks differ in the padding byte beside a matrix's type, so a block is
never compared byte for byte to decide whether two programs are the same.

**Evidence.** Two compiles of one source on a G2 with firmware 2.4.15515.

<a name="formats.number"></a>
## A number is 8 bytes of BCD with a 12-bit exponent

| | |
|---|---|
| Identifier | `formats.number` |
| Kind | rule |
| Known from | G2 |

Little-endian; read as a 64-bit integer:

```
bits  0..11   decimal exponent, 12-bit two's complement
bits 12..59   12 BCD mantissa digits, most significant at the top
bits 60..63   sign: 0 positive, 9 negative     (the usual BCD convention)

value = d1.d2d3...d12 x 10^exponent            and zero is all zeros
```

| Word | Sign | Mantissa | Exp | Value |
|---|---|---|---|---|
| `9760000000000001` | 9 | `760000000000` | 1 | −76 |
| `0600000000000FFC` | 0 | `600000000000` | −4 | 0.0006 |
| `0205991225000002` | 0 | `205991225000` | 2 | 205.991225 |
| `0915550000000000` | 0 | `915550000000` | 0 | 9.1555 |

**Evidence.** Worked out with a Rosetta stone rather than by guessing: a data
program carries its compiled block before the source, and the source is the
same numbers written in decimal, so one file gives tens of thousands of
(bytes, value) pairs nobody chose. 56 of 56 matrices located, 44,718 numbers
decoded and compared exactly, 44,718 re-encoded byte for byte, and 1,616
negatives inside that comparison -- the negatives are what fix the sign
nibble at 9 rather than 1, which a sample without them cannot tell.

<a name="formats.number-infinity"></a>
## Infinity is marked by a sign nibble of its own

| | |
|---|---|
| Identifier | `formats.number-infinity` |
| Kind | rule |
| Known from | emulator |

Negative infinity is sign nibble 2 and positive infinity sign nibble 6, each
with exponent 499 and a mantissa of twelve nines:

```
F3 91 99 99 99 99 99 29     -Inf     sign 2, mantissa 999999999999, exp 499
F3 91 99 99 99 99 99 69     +Inf     sign 6, the same otherwise
```

The exponent and the mantissa are those of the largest real, so the sign
nibble is the only thing that tells infinity from it. A reader that knows
only 0 and 9 refuses both, and `hpkit.numbers` reads exactly these two
patterns and nothing wider: another nibble, or 2 or 6 with anything else
around them, is still refused, because nothing has been measured there.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15, on
2026-09-13, by reading the cells of two batches' `M9.hpmat` that the decoder
had refused. `valuation(X^2+X)` gave the first word, and `STRING` of the same
call answered `"-Inf"` while `TYPE` answered 0, an ordinary real
([results.tsv](../commands/results.tsv)); `Dirac(0)` gave the second, and
`STRING` answered `"+Inf"`. In the same batch
[MAXREAL](../commands/catalog/MAXREAL.md) decoded as 9.99999999999E499: the
same exponent and mantissa with sign 0.

<a name="formats.hpmat"></a>
## An .hpmat is that number format with a 16-byte header

| | |
|---|---|
| Identifier | `formats.hpmat` |
| Kind | rule |
| Known from | G2 |

```
00  01 00      constant in everything observed
02  14 xx      TYPE IS THE LOW BYTE: 14 real, 94 complex (16 bytes per
               element). The high byte varies -- 00, 04 and 80 all appear
               across 20 real files for the same kind of matrix -- so a
               reader that matches on the pair rejects good files
04  u32        rank: 2 = matrix, 1 = vector
08  u32        rows
12  u32        columns
16  ...        the elements, row by row, 8 bytes each
```

With that, a whole matrix goes to the calculator as a file, with nothing
pasted and no program source involved. The file name decides: `M0.hpmat` is
the matrix `M0`. Complex matrices are reported as an explicit error rather
than as invented numbers: they are not covered.

**Evidence.** Nine real `.hpmat` files from a G2 read and rewritten byte for
byte identical, header included.

<a name="formats.hpmat-vector"></a>
## A vector is the same file with rank 1 and one row

| | |
|---|---|
| Identifier | `formats.hpmat-vector` |
| Kind | rule |
| Known from | emulator |

After the rank come 1 and the number of elements, so a vector reads as a
matrix of one row. The writer always writes rank 2, so a vector read and
written again comes back as a 1×n matrix: the numbers survive, the bytes do
not.

**Evidence.** Measured on 2026-09-11 on the Virtual Calculator 2.4, build
2025-09-15, by storing `[1,2,3]` in `M1` from a program and reading the file
back: 40 bytes, the two words after the rank 1 and 3, the elements 1, 2 and 3.
The single-element vectors found in the `M1` and `M2` of two mirrored
calculators, where both words are 1, agree with it.

<a name="formats.symbol-table"></a>
## The compiled block is the program's symbol table, and Main is an entry in it

| | |
|---|---|
| Identifier | `formats.symbol-table` |
| Kind | rule |
| Known from | G2 |

That is the thing to hold on to, because it explains the rest: the source
record is nested inside the `Main` entry, a code program's table has one
entry, and what looks like a block in front of the source is the globals
coming before `Main` in that table.

```
[u32 len][u32 tag]                 the symbol table
   [entry]  a global               name tag 0040018B
   [entry]  a global
   ...
   [entry]  Main                   name tag 0040008B
              its value contains [u32 len][u32 tag][source UTF-16LE][NUL]
```

The entries are in the order the source declares them, and there are three
shapes, told apart by the tag in their name record:

| Tag | What it is | Shape |
|---|---|---|
| `0040018B` | a variable | the name record comes first |
| `0040020B` | a function | wrapped in one more record, so the name record is 8 bytes further in |
| `0040008B` | `Main` | like a variable's, and its value holds the source |

Each entry is three TLV records, the same shape as the container around them,
and a real matrix value follows the `.hpmat` layout:

```
[u32 total]                                  everything below this field
  [u32 68][u32 0040018B][name UTF-16LE, zero-padded to 64 bytes]
  [u32 8][u32 00800185][u32 9]               9 in every entry measured
  [u32 len][u32 00C0018C][value]

[u16 flag][u16 0014][u32 rank=2][u32 rows][u32 cols][rows*cols numbers]
```

The name field is fixed at 64 bytes, so a name shorter than 32 characters is
padded with zeros. `hpprime matrix nums PROG.hpprgm` reports every symbol,
with the matrices decoded.

**Evidence.** The walk is run over a 367 KB block from end to end: 72 entries,
finishing exactly where the source record begins, recovering the same 72 names
the source declares, in the same order. A grammar that is wrong does not land
on the last byte. In a code program the source record ends exactly where the
`Main` entry ends, and both end where the table's own record does.

<a name="formats.matrix-type-byte"></a>
## A matrix value's type is one byte, and its neighbour is uninitialised

| | |
|---|---|
| Identifier | `formats.matrix-type-byte` |
| Kind | rule |
| Known from | G2 |

The type is the single byte at offset 2 of the value, `0x14`. Reading the two
bytes as a 16-bit type rejects perfectly good matrices.

**Evidence.** One file measured has `0xCD` in the byte beside it, which is
uninitialised memory.

<a name="formats.value-types-undecoded"></a>
## The value types other than a matrix are not decoded

| | |
|---|---|
| Identifier | `formats.value-types-undecoded` |
| Kind | rule |
| Known from | unverified |

Matrices are `0014`. Lists, strings and numbers come out as `0012`, `001F`,
`0100` and `FF16` in the files measured, and their payloads are reported but
not read. Which is which is not established.

**Evidence.** None beyond the tags seen. Each is one Rosetta stone away: a
program declaring one global of that type, installed and read back.

<a name="formats.matrix-flag"></a>
## The flag before a matrix value's type is not the rank

| | |
|---|---|
| Identifier | `formats.matrix-flag` |
| Kind | rule |
| Known from | unverified |

It is 1 in some values and 2 in others. Both appear on 2-D real matrices, so
it is not the rank, and what it means is unknown. Two files written by the
Virtual Calculator on 2026-09-11 agree with that: a 2×2 matrix in `M1` and a
1×3 vector both carry flag 2, and a 1×1 matrix in `M0` carries 1.

**Evidence.** Read from real files only; nothing was changed and read back to
see what moves it.

<a name="formats.entry-splice"></a>
## Where a new symbol entry would be spliced in is not established

| | |
|---|---|
| Identifier | `formats.entry-splice` |
| Kind | rule |
| Known from | unverified |

Building an entry is solved -- `numbers.symbol_entry()` does it and the tests
read them back -- but an entry inserted ahead of `Main` sits inside the table
record and outside the `Main` one, and which enclosing lengths that changes
has not been worked out. Nobody needs it: the calculator rebuilds the block
from the source anyway
([formats.block-is-a-cache](#formats.block-is-a-cache)).

**Evidence.** None. It would take one program rebuilt with an entry added and
read back by the calculator.

<a name="formats.other-files"></a>
## What else is in the folder, and what the tools refuse to read

| | |
|---|---|
| Identifier | `formats.other-files` |
| Kind | rule |
| Known from | G2 |

| | What it is | Read by the tools? |
|---|---|---|
| `.hpprgm` | a program | yes |
| `.hpappdir/` | an app | yes, and its `.hpappprgm` as a program |
| `.hpmat` | one of the `M0`..`M9` matrices | yes (the real ones) |
| `.hplist` | one of the `L0`..`L9` lists | no: a different header (`FE FF 16 00`) and variable-size elements with a type tag. An empty list is 8 bytes |
| `.hpsettings`, `settings` | settings; `settings` carries the calculator's identifier, which for a physical calculator is its serial number | no |
| `.hpexammode` | an exam mode | no |

None of these starts with the `7C 61 8A B2` magic, so the reader rejects them
at once instead of inventing anything.

**Evidence.** Read from the mirrors of the calculators on this machine. The
`.hplist` format is not worked out because every one seen is empty, and a
format is not guessed from empty files.
