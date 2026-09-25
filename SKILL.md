---
name: hp-prime
description: Write, review and deploy programs, apps and interfaces for HP Prime calculators (G1/G2), in PPL or MicroPython. Use whenever .hpprgm, .hpappdir, .hpapp or .hpappprgm files appear, or PPL code (EXPORT/BEGIN/END, LOCAL, TEXTOUT_P, INPUT, CHOOSE, DRAWMENU, GETKEY), or Prime Python (import hpprime, hpprime.eval, fillrect), or the HP Connectivity Kit or Virtual Calculator, or when data, calculation or an interface has to go onto an HP Prime.
---

# HP Prime

PPL is thinly documented, and its compiler reports only `syntax error` and a
line number. This kit removes the two things that waste the most time: guessing
the syntax, and the paste-and-compile cycle in the Connectivity Kit.

## Start here

Load [`docs/llms.txt`](docs/llms.txt). It is the index of the documentation:
every fact and every command entry on one line, with its link and a one-line
summary, small enough to load whole. Every claim behind those links says how
it is known -- `G2`, `emulator`, `HP help` or `unverified` -- and you cite it
by its identifier, such as `ppl.local-limit`.

Then read [`AGENTS.md`](AGENTS.md). It is the operating contract for this
repository: what to read before writing PPL, the two gates every program goes
through, what you must not claim, and what only the human can do. It is short,
and everything below assumes it.

Then read [`docs/topics/ppl.md`](docs/topics/ppl.md) before writing a
line: the limits that break compilation, and the five facts marked
`refuted hypothesis`, restrictions that look reasonable and do not exist.

## The loop, in three commands

```bash
hpprime lint FILE.txt                  # what the compiler will not explain
hpprime run  FILE.txt --call "F(2)"    # run the real file, here, no calculator
hpprime write FILE.txt -o PROG.hpprgm  # build the binary
```

Onto the emulator you can install it yourself:

```bash
hpprime install PROG.hpprgm --restart  # copies, and reopens the emulator
hpprime pull PROG --diff FILE.txt      # what is really on there
```

To find where the PC interpreter and the real one disagree:

```bash
hpprime compare lib.txt --call "F(2)"  # the human types HPKCMP once and
                                       # closes the emulator; the numbers
                                       # come back as a file
```

Onto a physical calculator you cannot: that is the human dragging the file onto
the calculator in the Connectivity Kit window, and copying into the CK's mirror
folder does not work. See [`docs/topics/deploy.md`](docs/topics/deploy.md).

`hpprime doctor` checks the machine, `hpprime new NAME` writes a starter that
already runs, `hpprime build` makes an app and `hpprime verify` checks one.
Every command is in [`docs/tools.md`](docs/tools.md).

## If the user has never programmed a Prime

Send them to [`docs/start/01-setup.md`](docs/start/01-setup.md) before anything
else. It is a six-step path from an empty folder to something running on the
calculator, and step 6 is about working with you.

## Installing this skill

```bash
git clone https://github.com/JordiRigau/hp-prime-kit ~/.claude/skills/hp-prime
```

The repository is the skill: `SKILL.md` sits at its root, so any session that
touches `.hpprgm` files or PPL code has the measured rules in front of it
instead of improvising syntax.
