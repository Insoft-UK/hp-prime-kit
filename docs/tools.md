# The tools

Every command in one place. Python 3.7 or newer, no dependencies, nothing to
install.

```bash
hpprime <command> [arguments]
```

Run it from the repository folder. How you type `hpprime` depends on your
shell: `.\hpprime` in PowerShell, where the `.\` is required, `hpprime` in
cmd.exe, and `./hpprime` on macOS and Linux. `python hpprime.py` works
everywhere and is the one to fall back on.

Every command exits 0 on success and non-zero on failure, so they all work as
gates in a script.

---

## doctor

```bash
hpprime doctor
```

Reports what works on this machine: the Python version, whether the code
template and the app templates are there and valid, whether a Connectivity Kit
folder exists, where the emulator is and which calculators it has, whether it
is running, which `install` cares about, and an end-to-end self test (source →
`.hpprgm` → source, and the PPL runs). Anything wrong comes with what to do
about it.

Run it first, and again whenever something behaves strangely.

## new

```bash
hpprime new NAME              # a PPL program: NAME.txt
hpprime new NAME --python     # a Python app: NAME/main.py
```

Writes a starter that already compiles and runs, and prints the commands to
take it to the calculator. The name is what it will be called there: letters
and digits, no spaces.

## lint

```bash
hpprime lint FILE.txt
hpprime lint ppl/ --quiet          # errors only, no warnings
hpprime lint A.txt B.txt --set     # also: names that would collide
```

Catches, before you compile, what the Prime's compiler will not explain. The
output is compiler-shaped, `file:line: level: rule: message [fact, label]`,
and it exits 1 if there is any error. What is in brackets is the identifier
of the fact the rule comes from, so a message can be checked rather than
believed, and how that finding is known, in [format.md](format.md)'s words.

```
prog.txt:5: ERROR: index-call: cannot index the result of a call (SIZE(...)(...)): store it first, d := DIM(M); d(1) [ppl.index-call, G2]
prog.txt:9: WARN: one-based: index 0 into L: PPL lists and matrices start at 1. What 0 does on a list or a matrix has not been measured [ppl.one-based, unverified]
```

A rule is an error only as far as its measurement reaches. What was measured
for `index-call` is `SIZE(M)(1)`, so a call indexed where it is produced is an
error, labelled `G2`; a name the file does not define, which may be a
function or a list, is a warning labelled `unverified`; and a list indexed
twice, `L(2)(1)`, is not flagged at all. The same split runs through the rest.
`local-limit` is an error from 13 variables, which failed, and a warning from
9 to 12, which nobody has run. `export-multiple` is an error from 7
initialised variables. `local-first` is an error for a `LOCAL` half way down a
function, and a warning for one inside a nested block. `end-semicolon` is an
error for a block's `END` and a warning for a function's. `single-end` is an
error for `ENDIF`, `ENDFOR` and `ENDWHILE`. `one-based` is only ever a
warning: what failed was `MID` with a 0, and an index of 0 into a list or a
matrix has not been measured. A 0 passed to a function the file defines is an
argument, and is not flagged. When somebody measures one of these cases, it
becomes an error with its evidence. `tests/test_lint.py` fails on an error
whose label is not `G2` or `emulator`.

Twelve rules, and each one says where it comes from. Ten name a fact in
[docs/topics/](topics/ppl.md), every one of them measured on a G2 or on the
emulator: too many variables in one `LOCAL` (`local-limit`), indexing the
result of a call (`index-call`), `ENDIF` and friends (`single-end`), index 0
(`one-based`), a `LOCAL` after code (`local-first`), several initialised
variables in one `EXPORT` (`export-multiple`), an `END` without its semicolon
(`end-semicolon`), `EXPR` without a guard (`expr-empty`), duplicate exported
names (`export-clash`, with `--set`), and `TEXTOUT_P` without its width
(`textout-width`).

There were thirteen. A rule called `equality` flagged a single `=` in a
condition as an error, and on 2026-09-12 the calculator settled it: `IF a = 2
THEN` compiles and compares, exactly as `==` does. The rule was removed
rather than softened, because a linter that flags legal, correct code is
worse than one rule short. `ppl.equality-operators` holds the measurement,
and the one question it leaves open -- what a bare `=` does as a statement,
where `a = 2;` might silently do nothing in place of `a := 2;` -- is waiting
for a measurement rather than for a rule.

`unbalanced` names no fact, because an unclosed block is something the
compiler reports itself and no fact about the platform is involved.

The twelfth, `unknown-name`, knows every PPL name. A call to a name that is
not on the documentation's [list of names](commands/names.tsv), and that the
program does not define, is flagged: the command a model invents, `STRLEN(s)`
for `SIZE(s)`, caught before the calculator answers *syntax error*. It knows
the calculator's own variables too (`A` to `Z`, `L0` to `L9`, `M0` to `M9`,
`G0` to `G9`, `Z0` to `Z9`), and it compares the calculator's names without
regard to case, so that it never flags a spelling the calculator might accept.
Whether the calculator itself ignores case in its names has not been measured.
It names no fact either: it comes from the list of names, which is an
inventory rather than something measured about the platform.
`tests/test_lint.py` fails if any rule names a fact no topic page defines, or
names none and gives no reason.

Warnings come in two kinds. `local-limit` at 7 and 8 variables, `expr-empty`
and `textout-width` carry a measured fact: the code compiles and runs, and
what they flag is a hazard rather than a mistake. The `unverified` ones are
the cases above, where a rule reaches past its measurement. `unknown-name` is
a warning for a file on its own, because the file may be calling a function
that another program exports, and an error with `--set`. Every other finding
is an error, and only an error exits 1. `--quiet` hides the warnings.

What it does not flag matters as much. `RETURN` inside a `FOR` is legal; locals
like `L12` or `r2` are legal; several locals with initial values on one line
are legal. Each was checked on hardware, and they are listed in the source so
that nobody puts the false rule back.

`--set` is for files that go to the calculator together: it adds a check for
exported names that would collide as globals, and it makes `unknown-name` an
error, because with every file in view nothing else could supply the name.

## run

```bash
hpprime run FILE.txt --call "AREA(2)"
hpprime run lib.txt data.txt --call "LOAD(1)" --call "F(3,350)"
```

Runs the PPL, on your PC. Not a reimplementation: the same file you install.

From Python:

```python
from hpkit import interp
m = interp.Machine()
m.load_file('ppl/LIB.hpprgm')
r = m.call('F', 3.0, 350.0)
```

What it covers: numbers, strings and the string functions, lists, 1-based
matrices, `IF`/`CASE`/`FOR`/`WHILE`/`REPEAT`/`IFERR`, `EXPORT` functions,
globals and locals, matrices passed by value, and the native matrix algebra:
`MAKEMAT`, `MAKELIST`, `RREF`, `TRN`, `DET`, `INVERSE`, `IDENMAT`.

What it records instead of drawing: `TEXTOUT_P`, `RECT`, `INPUT`, `CHOOSE`,
`WAIT`, `MSGBOX` and `GETKEY`, including `GETKEY` written bare, without
parentheses, which is how PPL writes it. Each goes into `machine.io` and
returns a neutral value, so a program with an interface still runs end to end.

`GETKEY`'s neutral value is "no key pressed", so a loop that waits for one can
never finish here. That is the shape of every wait helper in this kit. Rather
than spin, a loop that has run a million times stops with a message naming the
cause: a tool that hangs with no output is worse than one that refuses.

What it does not cover raises, and never an invented result. If you need a
command, add it to `BUILTINS` with its case in `tests/test_interp.py`, and
measure it on the calculator first.

That promise is checked against a source outside this repository.
`tests/hp_examples.txt` holds the worked examples from HP's own built-in help,
and `test_hpdocs.py` runs every one that applies. A command may answer HP's
number or refuse; answering a different number fails the suite. It found six on
its first run -- `ROUND` with a negative n, `MIN`/`MAX` over a list, `LOG` with
a base, `SORT` with a second argument, and `SIZE` of a matrix -- all since
corrected.

`LEFT`, `RIGHT`, `MID`, `INSTRING` and `SORT` are covered, every case measured
on a G2, including the trap that `LEFT(s,0)` and `RIGHT(s,0)` return the whole
string while `MID(s,start,0)` returns an empty one. What the calculator raises
on, this raises on, including a `MID` start below 1 and a `SORT` of a list
mixing numbers with strings, both of which are errors there.

One fidelity gap worth knowing: `M := GZ`, assigning a global matrix to a
local, aliases here and copies on the Prime. The way never to be bitten is not
to do it: work on the global.

## write / read / verify

```bash
hpprime write source.txt -o PROG.hpprgm     # build the binary
hpprime read PROG.hpprgm -o source.txt      # pull the source back out
hpprime verify PROG.hpprgm                  # round-trip check
hpprime verify MYAPP.hpappdir *.py          # app folder check
```

`write` uses `templates/code.hpprgm`, which the kit ships, unless you pass
`-t`. It reads back what it wrote before reporting success, and it refuses a
template that carries a compiled block, because changing the source would leave
that block out of step.

`read` works on anything with the container's magic, including the
`.hpappprgm` inside an app. Use it to compare what is installed with your
repository:

```bash
hpprime read ".../Calculators/HP Prime/MYPROG.hpprgm" -o installed.txt
diff installed.txt ppl/MYPROG.txt
```

`verify` takes either a `.hpprgm`, which it rebuilds and compares, or an app
folder, which it compares with what a build would produce. That is how you
catch the calculator having rewritten the wrappers.

It works out which kind of app it is looking at, because the two are not
compared the same way: a PPL app is built from the blank descriptor and its
`.hpappprgm` is supposed to differ from the empty skeleton. Give it the sources
too and it checks those as well; otherwise it says which parts it did not
compare.

```bash
hpprime verify MYAPP.hpappdir src/*.py     # a Python app
hpprime verify MYAPP.hpappdir app.txt      # a PPL app, program included
```

## build

```bash
hpprime build MYAPP src/*.py --icon icon.png   # a Python app
hpprime build MYAPP app.txt --ppl              # a PPL app
```

Builds a `.hpappdir`: the three wrappers, plus your files. The wrappers are
rebuilt from the templates every time, on purpose. The calculator rewrites them
when you leave the app, and that state must not survive into your repository.

It also deletes `__pycache__`, which holds CPython `.pyc` files MicroPython
would not read, warns if a Python app has no `main.py`, and warns about imports
MicroPython does not have, which on the calculator show up as the app closing
at startup, silently. Use `--allow a,b` for modules you know are there.

## install / pull

```bash
hpprime install CIRCLE.hpprgm --restart      # into the emulator, and open it
hpprime install MYAPP.hpappdir M1.hpmat      # apps and matrices too
hpprime pull                                 # what has it actually got?
hpprime pull CIRCLE --diff ppl/CIRCLE.txt    # is that my code? exits 1 if not
```

`install` copies into the Virtual Calculator's own folder, which, unlike the
Connectivity Kit's, is read by the emulator when it starts, so copying into it
installs. Measured end to end: the program appears in the Program Catalogue,
compiles, and runs.
[deploy.emulator-folder](topics/deploy.md#deploy.emulator-folder)
has the evidence and the three rules that follow from it.

It takes `.hpprgm` programs, `.hpappdir` folders and `.hpmat` matrices, and
refuses everything else, including a `.txt` source, because a calculator takes
that file without a word and then has nothing to run. A `.hpprgm` is opened and
parsed before it is copied, so a file that is not really one is caught here
rather than on the calculator.

Because the folder is read at startup, `install` also refuses to copy into a
running emulator: the copy would appear to work and change nothing. `--restart`
closes it, with a window-close request rather than a kill, so the calculator
saves itself, then copies and opens it again. With more than one calculator,
`--calc NAME` says which, and `hpprime doctor` lists them.

`pull` reads back what is really installed. The calculator rewrites each
program with its compiled block, so this is the state of the machine and not a
copy of what you meant to send. With no arguments it lists; with a name it
prints the source, or writes it with `-o`; with `--diff` it compares against
one of your files and exits 1 if they have drifted apart.

For a physical calculator neither of these applies. That is still a drag in the
CK window:
[deploy.ck-mirror](topics/deploy.md#deploy.ck-mirror).

## emu

```bash
hpprime emu list                  # every calculator, and which are clones
hpprime emu new LAB --from Prime  # one to experiment on
hpprime emu reset LAB             # back to how `new` left it
hpprime emu remove LAB
```

Calculators to burn, so that the one you care about is not the one you are
testing on. `new` clones a calculator that has been used -- the machine and its
built-in apps, none of your programs -- and gives it its own identity in
`settings`. It has to be cloned from a working one: a folder the emulator
created but never finished setting up asks for a language on every unlock and
never gets past it.

`reset` is the one that earns its place. A test that starts from a calculator
in a known state means something; one that starts from wherever you left it
last does not.

`remove` refuses a calculator it did not make, unless you pass `--force`.

Which calculator the emulator opens is not yours to choose. It takes the first
instance not already in use, in an order of its own: measured, with everything
free it opened `Prime` and not a clone called `LAB`, so it is not alphabetical.
`install --restart` says so when it is about to open a different one from the
one you installed into, and `compare` sidesteps it by sending to whichever one
the emulator does open.

## compare

```bash
hpprime compare lib.txt --call "AREA(2)" --call "F(3,350)"
hpprime compare --collect          # if you did not wait the first time
```

Runs the same calls here and on the calculator, and puts the two columns side
by side. `hpprime run` is not the Prime's interpreter, and the only way to find
where they disagree is to ask both.

The results come back as a file rather than off the screen: a generated wrapper
stores each result into `M9`, the emulator writes `M9.hpmat` into its
calculator folder when it closes, and
[formats.md](topics/formats.md) is already able to decode that. So the loop
is: it installs, you type `HPKCMP` on the calculator and close the emulator,
and the table appears.

```
call       here               calculator
---------  -----------------  -----------------  ------------
AREA(2)    12.56636           12.56636           same
F(3,350)   1050.0             1050.0             same
```

It exits 1 if any row disagrees, so it works as a gate.

What to know:

- Numbers only. A matrix cell holds one, so a call whose answer is a string or
  a list is recorded as "did not give a number" on both sides. That is a real
  answer, since both refusing counts as agreement, but it is not the value.
- One keypress is yours. Nothing on the Prime starts a program by itself, so
  the wrapper has to be run once by hand. Whether an app's `START` hook fires
  at boot, which would remove even that, is not measured.
- The generated program goes through the linter before it is sent, and an
  error stops it. The wrapper passes: `AREA(0)` in it calls a function your
  code defines, so the 0 is an argument and not an index.
- `--mat N` if `M9` is in use, `--tol X` for how close counts as the same
  (default 1e-9, relative), `--keep` to leave the wrapper on the calculator.

## matrix

```bash
hpprime matrix read  M1.hpmat -o data.csv
hpprime matrix write data.csv -o M0.hpmat
hpprime matrix nums  PROG.hpprgm
```

`.hpmat` files are the `M0`..`M9` matrices, and the file name decides which
one. This lets a whole matrix reach the calculator as a file, with nothing
pasted.

`nums` walks a program's compiled block and reports every symbol in it, with
the matrices decoded and other types named but not read. It is for looking, not
for writing: whether a calculator accepts a block you generate is unmeasured.
The grammar is in
[formats.md](topics/formats.md#formats.symbol-table).

Complex matrices raise an explicit error rather than returning invented
numbers.

## examples

```bash
hpprime examples LEFT RIGHT            # these entries' examples, one batch
hpprime examples --all                 # every entry's examples
hpprime examples LEFT --probe 'LEFT=LEFT("abc", -2)'   # and a call no entry states
hpprime examples --collect             # read a batch you did not wait for
hpprime examples --relabel             # HP help or unverified -> emulator where it agrees
```

Runs the documentation's examples on the Virtual Calculator and keeps what it
answers in `docs/commands/results.tsv`. What that file means for an entry is
in [format.md](format.md).

Every call goes into one generated program, `HPKDOC`, inside `IFERR`, and its
answer comes back through `M9`, one row per call: whether it answered, `TYPE`,
the number when it is one, and `STRING` of the answer as character codes, so
text, lists and matrices come back as well as numbers. The first row holds
what the calculator says `VERSION` is, and every result is stored with it.

The batch runs on a calculator called `Prime_1`, cloned from yours the first
time and reset before every batch, so every answer comes from the same state
and your own calculator is not touched. The name is the emulator's choice, not
the kit's: the first window opens `Prime`, the second `Prime_1`, and no window
opens a calculator with any other name
([deploy.emulator-folder](topics/deploy.md#deploy.emulator-folder)).
So the command launches only when the next window will be `Prime_1`, which it
reads from the emulator's lock files, and otherwise says what to open or close
first: usually, open your own calculator in the emulator before you run it. A
`Prime_1` the kit did not make is moved into the kit's own folder, never
deleted. When that window closes, the saved state of `Prime_1` has to have
moved, or nothing is read.

Your part is three steps in that emulator, and the command prints them and
waits: compile `HPKDOC` once (`Check` in its editor, since a program copied as
a file is not live on Home until then), run it from Home, and close the
window.

## docs

```bash
hpprime docs            # check the entries, then regenerate the pages made from them
hpprime docs --check    # change nothing; exit 1 if anything is wrong
```

The documentation under `docs/commands/` and `docs/topics/` follows one
format, stated in [format.md](format.md), and this command holds it to that
format. Every entry has its fields in order; every example and every
behaviour paragraph carries a label saying how it is known; names and fact
identifiers are unique, and every link to one resolves; nothing in it
points at the layer built on top of it; and nothing speaks of how it was
built, such as a phase of the work or "this kit".

For a command that `hpprime run` implements, every example goes through the
interpreter and has to give the result the entry states. An example the
interpreter does not cover is listed as a note rather than failed, for the
same reason `run` raises instead of guessing. Every example also has to have
been run somewhere: an answer stored from the Virtual Calculator, a
measurement on a G2, or the interpreter. One that has none fails.

The group pages, `docs/commands/<group>.md`, the two indexes and
`docs/llms.txt`, the index a model loads first, are generated from the
entries and the facts. `--check` fails when one of them is out of date or
`docs/llms.txt` passes its budget of 100,000 bytes, and so does
`tests/test_reference.py`.

## templates

```bash
hpprime templates "C:\Users\you\Documents\HP Connectivity Kit\Calculators"
```

Says which of your `.hpprgm` files can act as a template for `write`. You need
this only if the shipped template ever fails you, and it is not obvious by eye,
because the mirror folder holds files that have been through the calculator,
which adds a compiled block to everything it saves. Measured on one machine: 2
of 58 qualified.

---

## Testing the kit itself

```bash
python tests/run_all.py
```

Thirteen suites, and none of them needs a calculator. Two use one if it is there:
the `.hpprgm` reader against your own binaries, and the number format against
your own data. They skip what they cannot find rather than failing.

| Suite | What it covers |
|---|---|
| `test_lint.py` | that the linter catches, and that it does not raise false alarms |
| `test_interp.py` | the interpreter's subset, and that it fails where it must |
| `test_program.py` | the shipped template, and round trips over your binaries |
| `test_appdir.py` | building an app, and what `verify` sees |
| `test_numbers.py` | the internal number format, against real encodings |
| `test_cli.py` | the whole `hpprime` path a newcomer walks |
| `test_examples.py` | the starters and examples, so the first thing anybody copies still works |
| `test_docs.py` | every relative link in the documentation resolves |
| `test_hpdocs.py` | the interpreter against the examples in HP's own help |
| `test_emulator.py` | installing into the emulator and reading back, with a temp folder standing in for a calculator |
| `test_compare.py` | the generated wrapper, and the comparison, against a matrix written as the calculator would have left it |
| `test_reference.py` | the documentation's format, held in both directions: each way of breaking it is caught, and the real pages pass |
| `test_examples_run.py` | `hpprime examples` without the emulator: the program it generates, the answers read back, `results.tsv`, relabelling, and a stand-in that writes the matrix as the calculator would |

## Using the modules directly

Every command is a thin front over a module you can import:

```python
from hpkit import lint, interp, program, appdir, numbers, emulator, compare, docs, examples
```

| Module | Main entry points |
|---|---|
| `lint` | `check_source(path, text)`, `check_files(paths)` |
| `interp` | `Machine()`, `.load_file()`, `.call()`, `.io` |
| `program` | `read(data)`, `write(template, source)`, `default_template()` |
| `appdir` | `build()`, `check()`, `put_ppl_program()`, `check_imports()` |
| `numbers` | `decode()`, `encode()`, `read_hpmat()`, `write_hpmat()` |
| `emulator` | `find_root()`, `instances()`, `pick()`, `install()`, `contents()`, `source_of()`, `create()`, `reset()` |
| `compare` | `harness()`, `here()`, `there()`, `verdicts()` |
| `examples` | `cases()`, `harness()`, `decode()`, `read_results()`, `write_results()`, `run()`, `collect()`, `relabel()` |
