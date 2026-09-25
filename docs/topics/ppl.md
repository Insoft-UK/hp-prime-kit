# PPL: facts about the language

Facts about the language as a whole rather than about one command. Each has an
identifier, says how it is known, and is stated here once; the entries it
concerns link to it.

Reference firmware: G2, 2.4 revision 15515 (2025-09-15). A fact labelled `G2`
was measured on that calculator, one labelled `emulator` on HP's Virtual
Calculator, one labelled `HP help` comes from the built-in help, and one
labelled `unverified` from none of those. New to the Prime? The
[guided path](../start/01-setup.md) teaches; this page records.

## The shape of a program

```ppl
// line comment
/* block */

EXPORT VAR1, VAR2;              // globals, they persist between uses
EXPORT MYDATA:=[[1,2],[3,4]];

EXPORT FUNC(a, b)
BEGIN
  LOCAL x, y;                   // ALL the locals, at the top
  x := a + b;
  RETURN x;
END;                            // the ; after END is required
```

`EXPORT` makes a function visible from other programs and from Home; without
it the function is private to its file. Everything is 1-based, which is the
most common mistake coming from Python. Equality is `==`, assignment `:=`,
not-equal `<>`, and the logicals are `AND`, `OR`, `NOT`.

Control flow: `IF … THEN … ELSE … END;` · `FOR i FROM 1 TO n DO … END;`
(`DOWNTO` and `STEP` too) · `WHILE … DO … END;` · `REPEAT … UNTIL c;` ·
`CASE … DEFAULT … END;` · `IFERR … THEN … END;` · `BREAK` · `CONTINUE` ·
`KILL` · `IFTE(c, a, b)` as an expression.

| What you need | PPL |
|---|---|
| size of a list or string | `SIZE(L)` |
| dimensions of a matrix | `d := DIM(M);` → `d(1)`, `d(2)` |
| append to a list | `L(SIZE(L)+1) := v;` or `L := CONCAT(L, {v});` |
| number → string / string → number | `STRING(x)` / `EXPR(s)` |
| type of a variable | `TYPE(v)` |

There is error trapping and no exceptions of your own: `IFERR statements THEN
statements [ELSE statements] END;` traps a system error and leaves its code in
`Ans`, and `STRINGFROMID` turns that into a message. What does not exist is a
way to raise an error of your own with a value inside, so an API that returns
results still needs a convention: a region code of `-1` with the reason, say,
and `{}` from functions that return lists. `IFERR` hardens one call; it does
not propagate errors.

## Where to look things up

| Source | What it is good for |
|---|---|
| **The `[Help]` key, on the calculator** | HP's own entry for the command you are on: syntax, a sentence, and worked examples. The first place to look, and the one nobody mentions |
| **Command Tree 13217** ([hpcalc.org](https://www.hpcalc.org/prime/docs/commandtree.zip)) | that same help, dumped to a 239-page PDF: how to read it without a calculator, and how an agent reads it at all |
| *HP Prime Programming Reference* (HP) | looking up one command, not for learning |
| **hpmuseum.org/forum**, HP Prime subforum | complete code and real behaviour |
| **hpcalc.org** | a program archive: read code that already works before writing any |
| **en.hpprime.club** (E. Shore / H. Klaver) | tutorials with examples that run |
| **udel.edu/~mm/hp/primePython** | the closest thing to a reference for Python on the Prime |

HP's help gets further than this repository once assumed: `LEFT`'s zero case,
`MOD` as a Euclidean remainder and the `TYPE` codes are all in it, and reading
it corrected four answers this documentation had wrong. What it does not do is cover the
edges evenly -- `RIGHT` and `MID` get no sentence about theirs -- or say
anything about the limits below that break compilation. Look it up first, and
measure the rest. Its examples are the interpreter's test data:
`tests/hp_examples.txt` holds every one that applies to a command the
interpreter implements, and `python tests/test_hpdocs.py` runs them.

Direct links:
[undocumented limits](https://www.hpmuseum.org/cgi-bin/archv021.cgi?read=254706) ·
[E. Shore's tutorial](https://literature.hpcalc.org/community/hpprime-prog-tutorial.pdf) ·
[G2 firmware 2.4.15515](https://www.hpcalc.org/details/7783) ·
[Python libraries](https://udel.edu/~mm/hp/primePython/upython.html) ·
[Python Activities Book](https://literature.hpcalc.org/community/hpprime-python-activities.pdf)

> If you are an AI agent reading this: hpmuseum.org is protected against
> automated access and answers with a challenge you cannot pass. Do not try.
> The source that does allow reading is hpcalc.org, and downloading somebody's
> program and reading it is worth more than any tutorial.

---

<a name="ppl.local-limit"></a>
## One LOCAL statement holds at most 8 variables

| | |
|---|---|
| Identifier | `ppl.local-limit` |
| Kind | rule |
| Known from | G2 |

A `LOCAL` statement with 9 or more variables does not compile, and the
compiler reports only *syntax error* on its line. Several `LOCAL` statements
in a row do work, so declare the variables in groups of 6.

**Evidence.** Measured against programs that compile on the same calculator, a
G2 with firmware 2.4.15515: one that declares 8 compiles, and three others
stop at 7. The functions that failed declared 13, 16 and 18. Between the two,
9, 10, 11 and 12 were measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must: none compiled ([results.tsv](../commands/results.tsv)). `hpprime lint` catches
9 and more as an error.

<a name="ppl.locals-at-top"></a>
## Every local is declared at the top of the BEGIN

| | |
|---|---|
| Identifier | `ppl.locals-at-top` |
| Kind | rule |
| Known from | G2 |

A `LOCAL` statement half way down a function does not compile. All of them go
together, first thing inside `BEGIN`. One at the top of a block nested inside
the function, after code, does compile and work.

**Evidence.** A compile error on a G2 with firmware 2.4.15515, recorded in the
table of limits that break compilation. The nested block was measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must:
`LOCAL zb;` opening an `IF` block after `za := 1;` compiled, and the
function answered 3 ([results.tsv](../commands/results.tsv)). `hpprime lint` catches the first and leaves the
second alone.

<a name="ppl.index-call"></a>
## The result of a call cannot be indexed where it is produced

| | |
|---|---|
| Identifier | `ppl.index-call` |
| Kind | rule |
| Known from | G2 |

`SIZE(M)(1)` does not compile, and neither does the same shape on a
function a program defines, in its own file or in another program. Assign the
result to a variable and index the variable: `d := DIM(M);` and then
`d(1)`.

**Evidence.** A compile error on a G2 with firmware 2.4.15515, recorded in the
table of limits that break compilation. The programs' own functions were
measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must: a function returning `{10,20,30}`, called and indexed with `(2)`
where it is produced, did not compile whether it was defined in the same
file or in a program compiled before it ([results.tsv](../commands/results.tsv)). `hpprime lint` catches it as
`index-call`.

<a name="ppl.export-initialised"></a>
## Initialise one exported global per line

| | |
|---|---|
| Identifier | `ppl.export-initialised` |
| Kind | rule |
| Known from | G2 |

`EXPORT A:=1, B:=2, …;` failed with seven initialised variables on one line;
two, four and six compile. One declaration per line compiles.

**Evidence.** A compile error on a G2 with firmware 2.4.15515, recorded in the
table of limits that break compilation. Two, four and six on one line were
measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must, and all three compiled ([results.tsv](../commands/results.tsv)); three and five were not tried, and
one per line avoids the question.

<a name="ppl.no-end-keywords"></a>
## END closes everything: there is no ENDIF or ENDFOR

| | |
|---|---|
| Identifier | `ppl.no-end-keywords` |
| Kind | rule |
| Known from | G2 |

`ENDIF`, `ENDFOR`, `ENDWHILE`, `ENDCASE` and `ENDFUNC` do not exist in PPL.
Every block ends with `END`, and a function's `END` carries a `;`.

**Evidence.** A compile error on a G2 with firmware 2.4.15515, recorded in the
table of limits that break compilation, for the first three. `ENDCASE`
closing a `CASE` and `ENDFUNC` closing a function were measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must, and
neither compiled ([results.tsv](../commands/results.tsv)). `ENDPROC` was not tried. `hpprime lint` catches them,
and the names are not on the list of names in `docs/commands/names.tsv`.

<a name="ppl.minus-sign"></a>
## The calculator writes a negative with the mathematical minus sign

| | |
|---|---|
| Identifier | `ppl.minus-sign` |
| Kind | rule |
| Known from | emulator |

What comes back from the calculator is U+2212, the minus sign, and not the
ASCII hyphen U+002D that you type on a keyboard. Source is a different
matter: a program is written with the hyphen and the calculator accepts it.

This documentation writes results with the hyphen, because an entry is read
by people who have to type what they read, and `hpprime docs` treats the two
characters as the same sign when it compares an entry with what the emulator
answered.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15: the
`IFERR` example of [IFERR](../commands/branch/IFERR.md) answered a negative
one whose codepoints are `0x2212 0x31`, stored in
[results.tsv](../commands/results.tsv).

<a name="ppl.one-based"></a>
## Lists, strings and matrices are indexed from 1

| | |
|---|---|
| Identifier | `ppl.one-based` |
| Kind | rule |
| Known from | G2 |

Lists, strings and matrices start at 1: the first element is element 1. A 0
is never the first element, and what it is depends on where it goes:

| | |
|---|---|
| a position in a string, `MID(s, 0, 2)` | an error |
| a list read at 0, `L(0)` | its **last** element |
| a list assigned at 0, `L(0) := v` | `v` added at the end |
| an empty list read at 0 | an error |
| a string read at 0, `S(0)` | an error |
| a matrix read at 0, `M(0)` or `M(0, 1)` | an error |

The list is the trap. Coming from Python, `L(0)` means the first element,
and here it answers the last one with no error; when the index is computed,
nothing in the source shows it.

**Screen coordinates are the exception: they count from 0.** A point of the
screen or of a grob starts at `(0,0)`, and a drawing command takes it without
complaint. So a 0 is correct in a drawing call and wrong in a list, and the
two live in the same program. `hpprime lint` flags a literal 0 only where the
name is not one of the calculator's own, which is what keeps
`LINE(G1,0,0,9,4,RGB(0,0,255))` out of its way.

**Evidence.** `MID("abcdef", 0, 2)` is an error on a G2 with firmware
2.4.15515 and on the Virtual Calculator 2.4, build 2025-09-15
([results.tsv](../commands/results.tsv)), while every measured example that
indexes from 1 answers. HP's help says the same. The list and matrix rows
were measured on the same build on 2026-09-24, with the 0 held in a variable
so that the program compiled whatever the answer: `{10,20,30}` read at 0
answered 30, assigned 40 at 0 became `{10,20,30,40}`, and `[[1,2],[3,4]]`
read at 0, with one index or two, was refused; so were an empty list and
the string `"abc"` read at 0 ([results.tsv](../commands/results.tsv)). A
literal 0 written in the source, `zl(0)`, compiles too, and answered 30,
measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must. `hpprime lint` warns on a
literal 0 passed to a name the file does not define, which may be a list, as
`one-based`, labelled `emulator`.

The exception is measured on the same build: `C→PX(0,0)` answers `{160,109}`,
`GETPIX(G1,0,0)` answers a colour, and `LINE`, `RECT` and `TRIANGLE` all draw
with a 0 among their corners
([results.tsv](../commands/results.tsv)).

<a name="ppl.string-index-code"></a>
## A string indexed answers a character code, not a character

| | |
|---|---|
| Identifier | `ppl.string-index-code` |
| Kind | rule |
| Known from | emulator |

A string held in a variable can be indexed like a list, and what comes back
is the code of the character, a number: `"abc"` at 2 answers 98, not `"b"`.
[ASC](../commands/strings/ASC.md) answers the same codes for the whole
string, and [MID](../commands/strings/MID.md) is how to get the character as
text. A comparison against `"b"` fails, with no error, because the two are
not the same type.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15, on
2026-09-24: `LOCAL zs, zi; zs := "abc"; zi := 2; RETURN zs(zi);` answered 98,
a real ([results.tsv](../commands/results.tsv)). The index was held in a
variable so that the program compiled whatever the answer. Until then the
interpreter on the PC answered `"b"`.

<a name="ppl.names-ignore-case"></a>
## The calculator reads a command's name without regard to case

| | |
|---|---|
| Identifier | `ppl.names-ignore-case` |
| Kind | rule |
| Known from | emulator |

`alog(2)` and `Alog(2)` answer 100, as `ALOG(2)` does, and `xpon(1000)`
answers 3: a name HP writes in capitals is found in any case. It is the
assumption `hpprime lint` was built on, which never flags a spelling that
differs from the list only in case.

It does not make case irrelevant everywhere. A lower-case name can also be a
CAS command of its own, and those were kept out of the measurement: both
names tried exist on HP's list in capitals only.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15, on
2026-09-24, with each call inside `EXPR`, so through Home's reading of an
expression; a program's source compiled with the name in lower case was not
tried ([results.tsv](../commands/results.tsv)).

<a name="ppl.equality-operators"></a>
## == compares, := assigns, <> is not-equal

| | |
|---|---|
| Identifier | `ppl.equality-operators` |
| Kind | rule |
| Known from | emulator |

`==` compares, `:=` assigns and `<>` is not-equal (HP help). What was assumed
here for a long time, and is false, is that a single `=` in a condition does
not compile: **it does**. `IF a = 1 THEN … END;` passed the editor's `Check`.

And it **compares**, exactly as `==` does. Two functions asked it from
different directions and agreed: `IF a = 2` with `a` at 1 took the `ELSE`,
and the same test left `a` unchanged rather than setting it to 2. So a single
`=` inside a condition is not a trap at all: it is legal and it means what a
reader would think.

`hpprime lint` called it an error until this was measured, and the rule was
removed rather than softened: a linter that flags legal, correct code is
worse than one rule short.

**As a statement it is a trap.** `za = 2;` compiles, and assigns nothing: it
compares `za` with 2 and throws the answer away. Written where `za := 2;` was
meant, the program runs, raises nothing, and keeps the old value.
`hpprime lint` warns on it as `equality-statement`.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15, on
2026-09-12, with programs written by hand because the harness lints what it
sends and would not send this one. That it compiles: `Check` on a program
holding `IF a = 1 THEN RETURN 5; ELSE RETURN 6; END;` reported its only error
further down, in a function about
[ppl.end-semicolon](#ppl.end-semicolon), so everything above compiled. That
it compares: `IF a = 2 THEN RETURN 5; ELSE RETURN 6; END;` with `a` at 1
answered 6, and `IF a = 2 THEN a := 99; END; RETURN a;` answered 1. The
statement was measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must: `LOCAL za; za := 1; za = 2; RETURN za;` compiled
and answered 1 ([results.tsv](../commands/results.tsv)).

<a name="ppl.end-semicolon"></a>
## END carries a semicolon

| | |
|---|---|
| Identifier | `ppl.end-semicolon` |
| Kind | rule |
| Known from | emulator |

It is `END;`, both for a function and for a block inside one. A missing
semicolon does not compile. On a block's `END` the error is reported on the
**next** line: the compiler carries on past the `END`, swallows what follows
and fails there, so the line the calculator names is not the line to fix. On
a function's own `END` it does not compile either, even when that `END` is
the last line of the file.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15, on
2026-09-12, with a program written by hand for the question. Its second
function held `IF 1 == 1 THEN z := 2; END` on line 12 and `RETURN z;` on line
13, and the editor's `Check` answered *syntax error* on line 13. The first
function of the same program, which compiled, is the evidence for
[ppl.equality-operators](#ppl.equality-operators). A function's own `END`
without its `;` was measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must: last in the file, and with another function
after it, neither compiled ([results.tsv](../commands/results.tsv)). `hpprime lint` catches a line that is exactly
`END` as `end-semicolon`.

<a name="ppl.global-index-other-program"></a>
## Indexing a global from another program is not a compile error

| | |
|---|---|
| Identifier | `ppl.global-index-other-program` |
| Kind | refuted hypothesis |
| Known from | G2 |

This page used to state, as a rule, that indexing a global declared in a
different program fails, because the compiler reads `NAMES(1)` as a call to a
function called `NAMES`. That is too broad. A list declared `EXPORT
L:={"a","b",…}`, with contents, is indexed from another program and passed to
`SIZE` in an app in daily use. What did fail was a list declared `EXPORT
L:={};`, empty, indexed from another program.

What separates the two is not established. Two hypotheses, neither measured:
the declaration's contents, since an empty list may leave the compiler nothing
to infer a type from; or the order they were installed in, since a program
only sees another's functions if it was compiled afterwards, and the same may
hold for knowing a global's type. Four small programs would settle it: a
global declared empty and one declared full, each indexed from a second
program, installed in both orders.

Until somebody runs that, copying to a local first is the safe move: `zn :=
NAMES;` and then `zn(1)`. It costs one line and works in both cases. That is a
precaution, not a rule, and `hpprime lint` does not flag it: `TS1(1)` and
`AREA(3,350)` are written the same way, so one file cannot tell them apart.

**Evidence.** Both programs are on the same G2 with firmware 2.4.15515: one
indexing an empty exported list failed, one indexing a filled exported list
runs.

<a name="ppl.return-in-loop"></a>
## RETURN inside a loop is allowed

| | |
|---|---|
| Identifier | `ppl.return-in-loop` |
| Kind | refuted hypothesis |
| Known from | G2 |

The hypothesis was that `RETURN` cannot appear inside `FOR` or `REPEAT`. It is
false: `RETURN` works inside a loop, and leaves the function from there.

**Evidence.** A program that runs on a G2 has two `RETURN` statements inside
loops.

<a name="ppl.letter-digit-names"></a>
## A letter followed by a digit is a usable name

| | |
|---|---|
| Identifier | `ppl.letter-digit-names` |
| Kind | refuted hypothesis |
| Known from | G2 |

The hypothesis was that names like `r2` or `y1` are reserved, because the
calculator has variables spelled that way. It is false for locals: a program
that compiles uses `L12`, `L13`, `L14`, `L15` as local names.

**Evidence.** A program on a G2 with firmware 2.4.15515 that compiles and
runs. What was not tested is a local named exactly like a calculator variable
in use, such as `M1` or `L1`, so the safe habit of prefixing locals stands.

<a name="ppl.local-m-matrices"></a>
## A local called m does not clash with the M0..M9 matrices

| | |
|---|---|
| Identifier | `ppl.local-m-matrices` |
| Kind | refuted hypothesis |
| Known from | G2 |

The hypothesis was that `LOCAL m` collides with the built-in matrices. It is
false: what was failing in the program that started the hypothesis was the
number of locals in one statement, which is
[ppl.local-limit](#ppl.local-limit).

**Evidence.** The same program compiles once the `LOCAL` statement is split,
with the name unchanged, on a G2 with firmware 2.4.15515.

<a name="ppl.locals-initialised-one-line"></a>
## Locals can be initialised on one line

| | |
|---|---|
| Identifier | `ppl.locals-initialised-one-line` |
| Kind | refuted hypothesis |
| Known from | emulator |

The hypothesis was that a `LOCAL` statement cannot give initial values to
several variables at once, and it is false: `LOCAL za := 2, zb := 3;`
compiles, and both values are there when the function runs, and so does
three, as published tutorial code writes it. Exported globals are different:
see [ppl.export-initialised](#ppl.export-initialised).

**Evidence.** Run on the Virtual Calculator 2.4, build 2025-09-15, in the
batch stored on 2026-09-12: `LOCAL za := 2, zb := 3; RETURN za + zb;`,
compiled as the body of a function in a program that passed the editor's
`Check`, answered 5. The three-variable form, which a tutorial published by
E. Shore uses, was measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must: `LOCAL za := 1, zb := 2, zc := 3;` compiled
and the function answered 6 ([results.tsv](../commands/results.tsv)).

<a name="ppl.i-e-as-locals"></a>
## i and e work as local names

| | |
|---|---|
| Identifier | `ppl.i-e-as-locals` |
| Kind | rule |
| Known from | emulator |

`i` is the imaginary unit and `e` Euler's number, and a local of either name
compiles and holds what it is given: inside the function the local is the
number, not the constant. Prefixed names (`zi`, `ze`) still read better next
to arithmetic that uses the constants.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must: `LOCAL i; i := 2; RETURN i * 3;` answered 6, and
`LOCAL e; e := 2; RETURN e + 1;` answered 3 ([results.tsv](../commands/results.tsv)).

---

<a name="ppl.imaginary-unit"></a>
## The imaginary unit goes in as `i` and comes back as a private-use glyph

| | |
|---|---|
| Identifier | `ppl.imaginary-unit` |
| Kind | rule |
| Known from | emulator |

A complex number may be typed either as `3+4*i`, with the ASCII letter, or as
the pair `(3,4)`. Both are accepted. What the calculator answers is neither:
the imaginary unit comes back as U+E003, a character in Unicode's private use
area, so `CONJ(3+4*i)` reads as `3-4*` followed by that glyph.

This is the same shape as [ppl.minus-sign](#ppl.minus-sign): the calculator
takes ASCII on input and answers with a character of its own. Unlike the
minus sign, nothing here normalises it, so a program comparing an
answer against text it wrote itself will not match, and a result stored in
`results.tsv` carries the glyph literally.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15:
`RE(3+4*i)` and `RE((3,4))` both answer 3, `IM(3+4*i)` answers 4, and
`CONJ(3+4*i)` answers a `TYPE` 3 value whose text holds U+E003
([results.tsv](../commands/results.tsv)).

---

<a name="ppl.exponent-glyph"></a>
## Scientific notation comes back with a glyph of the calculator's own

| | |
|---|---|
| Identifier | `ppl.exponent-glyph` |
| Kind | rule |
| Known from | emulator |

A number in scientific notation is not written with an `E`. The exponent is
marked with U+1D07, the small capital E, and the exponent's sign is the
mathematical minus U+2212, so machine epsilon reads as `2.22044604925ᴇ−16`
rather than `2.22044604925E-16`.

This is the third character the calculator answers with that nobody can type:
the minus sign, [ppl.minus-sign](#ppl.minus-sign), the imaginary unit,
[ppl.imaginary-unit](#ppl.imaginary-unit), and this one. The pattern is worth
holding on to -- what goes in is ASCII and what comes back is the
calculator's own typography -- because a program comparing an answer against
text it wrote itself will not match, and only the minus sign is normalised
anywhere here.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15:
`LQ([[1,2],[3,4]])` and `SCHUR([[1,2],[3,4]])` both answer decompositions
holding very small numbers, and in both the exponent marker is U+1D07 and its
sign U+2212 ([results.tsv](../commands/results.tsv)).

---

<a name="ppl.exact-answers"></a>
## Some commands answer exactly, and an exact answer is not a number

| | |
|---|---|
| Identifier | `ppl.exact-answers` |
| Kind | rule |
| Known from | emulator |

A command may answer a value the calculator keeps in exact form rather than as
a decimal. `l2norm([1,2,3])` answers the square root of 14, written with
U+221A and held as `TYPE` 8 -- the same type `CAS` answers with -- while its
two siblings `l1norm` and `maxnorm` answer the plain numbers 6 and 3, of
`TYPE` 0.

So a program cannot tell from the family a command belongs to whether it will
get a number back. Arithmetic on the exact value works, but a comparison
against text, or an assumption that the answer has digits, will not.

U+221A is also the fourth character the calculator writes that nobody can
type, after [ppl.minus-sign](#ppl.minus-sign),
[ppl.imaginary-unit](#ppl.imaginary-unit) and
[ppl.exponent-glyph](#ppl.exponent-glyph).

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15:
`l2norm([1,2,3])` answers U+221A followed by 14 with `TYPE` 8, where
`l1norm([1,2,3])` answers 6 and `maxnorm([1,2,3])` answers 3, both `TYPE` 0
([results.tsv](../commands/results.tsv)).

<a name="ppl.type-codes"></a>
## What TYPE answers

| | |
|---|---|
| Identifier | `ppl.type-codes` |
| Kind | rule |
| Known from | emulator |

`TYPE(v)` answers 0 for a real, 1 for an integer, 2 for a string, 3 for a
complex, 4 for a matrix, 5 for an error, 6 for a list, 8 for a function, 9 for
a unit, and 14.x for a CAS object. Watch 3 and 4: this documentation had them the other
way round until HP's help was read, and `IF TYPE(v) == 3` then branches on
complex numbers instead of matrices.

**Evidence.** 0, 1, 2, 3, 4, 6, 8 and 9 are measured on the Virtual Calculator 2.4,
build 2025-09-15. Four by a call of their own: `TYPE(3)` is 0, `TYPE("a")` is
2, `TYPE([[1,2],[3,4]])` is 4 and `TYPE({1,2})` is 6. The fifth comes from
what other commands answer: `RGB(255,0,0)`, `SETBITS(12)` and `R→B(12)` all
come back as `#` integers of type 1, which is what HP's help calls an
integer and what an ordinary number is not. All of it is in
[results.tsv](../commands/results.tsv). Every other answer the batches bring
back carries its `TYPE` too, and none has contradicted those four. Type 8
is measured on what `CAS` answers: `CAS("1/2+1/3")` and `CAS(1/2+1/3)` both
come back as `5/6` with `TYPE` 8, 2026-09-12, and `l2norm([1,2,3])`
answers a square root of 14 with the same `TYPE` 8 and no `CAS` call
around it, 2026-09-13. That is worth reading twice,
because HP's help calls 8 a function and keeps 14.x for a CAS object, so what
the CAS hands back arrives as 8 and not as 14.x. Which of the two namings is
right is not something those two rows settle, and a program branching on
`TYPE` should follow the 8 that was measured. Type 3 is measured too: `CONJ(3+4*i)` answers a complex number and its
`TYPE` is 3, 2026-09-13, so the help's warning about 3 and 4 being easy to
swap is now settled on one side. Type 9 is measured too: `TYPE(2_m)` answers 9, 2026-09-13, which is
what HP's help calls a unit. An earlier `TEVAL` answer had come back
as 9 without settling it; a value carrying a unit settles it. The
codes still unmeasured here are 5 and 14.x, which come from HP's
built-in help. A `TEVAL` answer came back as type 9, a unit,
which agrees with the help's 9 without settling it.

<a name="ppl.function-always-answers"></a>
## A function always answers something

| | |
|---|---|
| Identifier | `ppl.function-always-answers` |
| Kind | rule |
| Known from | G2 |

There is no way to write a function that returns nothing. Without a `RETURN`,
a function answers with the value of the last statement that produced one, and
an assignment produces the value assigned. That matters because Home prints
what a program answers: you choose what the number is, not whether there is
one.

| The body ends in | It answers |
|---|---|
| `z := 1;` | 1 -- an assignment produces the value assigned |
| `FOR zi FROM 1 TO 2 DO z := zi; END;` | 2 -- the last value the body produced |
| an `IF` whose condition is false | 0 -- the value from before it, unchanged |
| a call to another function | what that function answered |
| `RETURN;`, bare and with no value | 0 -- and it does compile |

**Evidence.** Measured on a G2 with firmware 2.4.15515, one function per
ending, with no `RETURN` in any of them except the last.

<a name="ppl.home-no-parentheses"></a>
## On Home a function with no arguments is called without parentheses

| | |
|---|---|
| Identifier | `ppl.home-no-parentheses` |
| Kind | rule |
| Known from | G2 |

`MYFUNC` runs it; `MYFUNC()` answers *syntax error*. Inside PPL source the
parentheses are correct and required. With arguments the two agree:
`CIRCAREA(2)` everywhere. It is the same convention the built-in `GETKEY`
follows in PPL, generalised to your own functions: an empty pair of
parentheses is not how the Home parser reads a call.

**Evidence.** Measured on a G2 with firmware 2.4.15515: typing `SELF3()` on
Home answers *syntax error*, and `SELF3` returns 1. That same program's source
contains `IF SELF1() == 385 AND SIZE(SELF2()) == 23`, and it compiled and
returned 1, so the parentheses are right in source and wrong on Home, not
wrong everywhere.

<a name="ppl.getkey-no-parentheses"></a>
## GETKEY takes no parentheses in PPL, and does across the bridge

| | |
|---|---|
| Identifier | `ppl.getkey-no-parentheses` |
| Kind | rule |
| Known from | G2 |

In PPL source it is `zk := GETKEY;`. From Python, across the bridge, it is
`eval('GETKEY()')`.

**Evidence.** Both forms are in programs that run on a G2 with firmware
2.4.15515.

<a name="ppl.matrices-by-value"></a>
## Matrices are passed by value

| | |
|---|---|
| Identifier | `ppl.matrices-by-value` |
| Kind | rule |
| Known from | G2 |

Handing a big matrix to a function copies it. With large data, reach for a
global instead of an argument.

**Evidence.** Recorded in a table of run-time traps, measured on a G2
with firmware 2.4.15515. The record does not name the program, and the cost
was not timed.

<a name="ppl.expr-empty"></a>
## EXPR of an empty string fails

| | |
|---|---|
| Identifier | `ppl.expr-empty` |
| Kind | rule |
| Known from | G2 |

`EXPR("")` is an error, so check `SIZE(s) > 0` before evaluating whatever came
out of a field.

**Evidence.** Recorded in a table of run-time traps, measured on a G2
with firmware 2.4.15515.

<a name="ppl.expr-dynamic-access"></a>
## EXPR is how a name is resolved at run time, and it is not free

| | |
|---|---|
| Identifier | `ppl.expr-dynamic-access` |
| Kind | rule |
| Known from | G2 |

`EXPR("NAME")` gives the variable whose name was built on the fly. Do it once
at load time, never once per element.

**Evidence.** Recorded in a table of run-time traps, measured on a G2
with firmware 2.4.15515. How much slower it is than a direct reference was not
timed; what was measured is that a per-element loop was the part that had to
be changed.

<a name="ppl.global-namespace"></a>
## Exported names share one namespace with Home

| | |
|---|---|
| Identifier | `ppl.global-namespace` |
| Kind | rule |
| Known from | G2 |

An `EXPORT`ed name is visible from Home and from every other program, so two
programs exporting `AREA` collide, and so does a program exporting a name an
app already uses. Prefix them.

**A program's name hides an app's function of the same name.** A program
exporting `AREA`, which is the Function app's, compiled, and `AREA(2)` on
Home then answered 12.5663706144, the program's, with the Function app
active. So a program that exports an app's name takes that function away
from Home for as long as it is installed.

**Evidence.** Recorded in a table of run-time traps, measured on a G2
with firmware 2.4.15515. The collision with an app's function was measured
on the Virtual Calculator 2.4, build 2025-09-15, on 2026-09-24, by `hpprime examples --compile`, with its two controls coming out as they must, `AREA(2)` read through `EXPR` ([results.tsv](../commands/results.tsv)).

<a name="ppl.decimal-point"></a>
## The decimal point in source is always a dot

| | |
|---|---|
| Identifier | `ppl.decimal-point` |
| Kind | rule |
| Known from | G2 |

Even on a calculator that displays `,` as the decimal separator, source is
written with `.`.

**Evidence.** Recorded in a table of run-time traps, measured on a G2
with firmware 2.4.15515.

<a name="ppl.compilation-order"></a>
## A program only sees another's functions if it was compiled afterwards

| | |
|---|---|
| Identifier | `ppl.compilation-order` |
| Kind | rule |
| Known from | G2 |

Install in dependency order -- data, then engine, then app -- or recompile the
one that depends on the other.

**Evidence.** Measured on a G2 with firmware 2.4.15515. It is the same
mechanism the open question in
[ppl.global-index-other-program](#ppl.global-index-other-program) asks about
for globals.

<a name="ppl.check-last-error"></a>
## Which bad line Check names depends on what is wrong with it

| | |
|---|---|
| Identifier | `ppl.check-last-error` |
| Kind | rule |
| Known from | emulator |

When the editor's Check refuses a program with several bad lines, it names
one of them, and which one depends on the kind of error. With two plain
syntax errors far apart, it named the **first**. With calls it could not
read, it named the **last**, and fixing each moved the report backwards
through the program. So the named line is a place to start, not a promise
about the lines above or below it: a program with several bad lines takes one
round per bad line to clear, in either order.

**Evidence.** Measured on the Virtual Calculator 2.4, build 2025-09-15, with
three generated programs that differed only in a few calls. Their bad lines
were 31, 33 and 35 in the first, 31 and 33 in the second and 31 alone in the
third, and Check named 35, then 33, then 31. Which calls were bad was settled
separately by running each one inside `EXPR`, where a bad call is a value on
its row instead of a refusal of the whole program. The first-line case was
measured on the same build on 2026-09-24: a program with `za := za + ;` on
lines 4 and 12 and nothing else wrong, and Check named line 4, read off the
screen by the person pressing it.

<a name="ppl.speed-anchor"></a>
## The one speed figure there is

| | |
|---|---|
| Identifier | `ppl.speed-anchor` |
| Kind | rule |
| Known from | G2 |

PPL is interpreted and HP publishes no figure for what an operation costs. The
one measurement on physical hardware: an inverse lookup by bisection, 60
iterations, each a double interpolation over matrices, is "noticeable, but
under a second".

That is an order of magnitude to reason with. A 53x49 Gauss-Jordan is about
45,000 floating-point operations, two orders of magnitude past that bisection,
and a loop that calls it multiplies the count. If an algorithm is past that,
measure it on the calculator as soon as it compiles, not at the end. Moving
the heavy computation into Python is a real option rather than a detour: the
bridge crossing costs 0.2 ms, which is nothing next to this.

**Evidence.** The bisection was timed by hand on a G2 with firmware 2.4.15515.
MicroPython's own speed on the Prime has not been measured; only the bridge
crossing has.


<a name="ppl.mu-zero-spelling"></a>
## One name on the list cannot be typed as the list spells it

| | |
|---|---|
| Identifier | `ppl.mu-zero-spelling` |
| Kind | rule |
| Known from | emulator |

The Inference app's null-hypothesis mean is on HP's list as `μ₀`,
spelled with GREEK SMALL LETTER MU, U+03BC. The calculator refuses that name
and answers to the same two glyphs spelled with MICRO SIGN, U+00B5. The two
are indistinguishable on screen.

**Evidence.** Both were read in the same app, with Inference active. U+03BC
followed by U+2080 was refused, twice, in two different batches. U+00B5
followed by U+2080 answered 0.5. Every other Greek name in the same sweep
answered as the list spells it -- `π₀`, `σ₁` and
`σ₂` among them -- so this is one name's spelling and not a rule
about Greek letters.

**What it costs.** The linter compares a program's names against the list, so
it accepts the spelling the calculator refuses and flags the one that works
as an invented name. A person reading HP's documentation, or a model trained
on it, types the refused one. `docs/commands/names.tsv` is generated from
HP's Command Tree and is not edited by hand, so the list keeps HP's spelling
and this fact carries the correction.
