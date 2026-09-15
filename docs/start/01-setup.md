# 1. What you are getting into

You have an HP Prime and you want it to do something of your own. This page
covers what the machine is, what the words mean and what to install. It takes
about fifteen minutes, and then you write a program.

---

## The machine

The HP Prime is a graphing calculator with a 320 × 240 touch screen, and a
small computer you can program. There are two generations, G1 and G2. They
share firmware; the G2 is faster and has more memory. Everything measured in
this kit was measured on a G2.

It is programmed in two languages, and the choice is worth making deliberately:

| | **PPL** | **Python** |
|---|---|---|
| What it is | the calculator's own language | MicroPython, a reduced Python |
| Since when | always | firmware from 2021 on |
| Looks like | Pascal / BASIC | Python, with less library |
| Good for | calculation, libraries other programs use | interfaces, long logic, reusing PC code |
| Official documentation | thin | none |

You do not have to pick one. From Python you can run PPL and get the result
back, so the usual arrangement is heavy calculation or data in PPL and the
interface in Python, or everything in PPL if it is small.

This path starts with PPL, because it is the native language and because half
of what is measured here is about it. Python comes in [step 5](05-python.md).

If you come from programming on a PC, one difference matters more than the
rest:

> There is no debugger, no useful error message and no console. The PPL
> compiler says `syntax error` and points at a line without saying what is
> wrong with it. A Python app that does something it dislikes closes by itself,
> silently.

That is the problem this kit exists to solve: checking things without the
calculator, so that you do not depend on the paste-compile-look-repeat loop.

## Program or app: what each one is

| | **Program** | **App** |
|---|---|---|
| What it is | a file with functions in it | a folder with its own icon |
| Where it lives | the program catalogue | the `[Apps]` key |
| How it opens | `[Shift][Program]`, navigate, `[Enter]` | `[Apps]` and touch the icon: two presses |
| The file | `MYPROG.hpprgm` | `MYAPP.hpappdir/`, a folder |

An app does not compute better. It opens faster and has somewhere to keep its
things. Start as a program and wrap it as an app at the end, once it works:
iterating on a program is much faster, and converting it afterwards is
packaging rather than rewriting.

## What to install

| | |
|---|---|
| HP Connectivity Kit (CK) | the PC program that talks to the calculator: <https://hpcalcs.com/download/> |
| HP Virtual Calculator | a Prime inside your PC, to try things without the physical one. It comes with the CK |
| Python 3.7 or newer | for this kit's tools. Nothing else: no pip, no libraries |

A physical calculator is not required to start. The Virtual Calculator behaves
the same for almost everything.

Then clone this repository and check the setup:

```bash
git clone https://github.com/JordiRigau/hp-prime-kit
cd hp-prime-kit
python hpprime.py doctor
```

`doctor` reports what works on your machine and what to do about anything that
does not. It should end with "Everything the kit needs is in place."

Run these in a terminal, with the repository folder as the current directory,
which is what the `cd` above does. Every command in these pages is written the
short way, `hpprime doctor`, and how you type that depends on your shell:

| Shell | Type |
|---|---|
| Windows PowerShell | `.\hpprime doctor` — the leading `.\` is required |
| Windows cmd.exe | `hpprime doctor` |
| macOS, Linux | `./hpprime doctor` |
| anywhere, always works | `python hpprime.py doctor` |

If in doubt, use the last one. It is the same program either way.

## The vocabulary you need

The reference pages use these seven words without explaining them:

| Word | What it means |
|---|---|
| PPL | the Prime's own language (*Prime Programming Language*) |
| CK | the Connectivity Kit, the PC program |
| `.hpprgm` | a program's file. It is binary, with the code as text inside |
| `.hpappdir` | an app's folder |
| template | an existing `.hpprgm` whose header is reused to make another. It is needed because the format cannot be generated from nothing. The kit ships one |
| compiled block | a chunk the calculator adds before the code, with numbers already in its internal format. It makes the file bigger and the program open instantly |
| the mirror | the folder `Documents\HP Connectivity Kit\Calculators\<your calculator>\`. It is not a drop box: it is a copy the CK writes *from* the calculator |

Two more appear in the interface pages: a grob is an image in memory that you
draw onto (`G0` is the screen), and a soft key is one of the six buttons in the
bottom row, whose labels your program sets.

---

Next: [2. Your first program](02-first-program.md), from an empty file to
something running on the calculator.
