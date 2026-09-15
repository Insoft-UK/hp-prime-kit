---
phase: 04-facts-carried-over
verified: 2026-09-12
status: approved
---

# Phase 4 verification: Facts carried over

## Success criteria

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| 1 | A migration list maps every fact in today's seven reference pages to its new home, with none left out | VERIFIED | `MIGRATION.md` has a row for each of the 53 sections of the seven pages, and no row is blank. A destination is a fact identifier, a named prose section, or the entry that already held it. The one thing with no home yet -- `INSTRING`'s trap, whose entry is Phase 6 -- is written out in full in the list, so deleting the page could not lose it |
| 2 | The false hypotheses and the unverified items are entries with their own status | VERIFIED | Five facts carry `Kind: refuted hypothesis` (`ppl.return-in-loop`, `ppl.letter-digit-names`, `ppl.local-m-matrices`, `ppl.locals-initialised-one-line`, `ppl.global-index-other-program`), each stated as what is true. What was not measured is a fact labelled `unverified` that says what would settle it, rather than a sentence in prose that reads like a rule: `formats.header-words`, `formats.matrix-flag`, `micropython.eval-parentheses`, `interface.wait-minus-one`, `libraries.published` and the rest |
| 3 | Every lint message names the fact identifier it comes from, and a test checks that every rule has one | VERIFIED | `hpkit/lint.py`: `FACTS` maps eleven rules to a fact, `NO_FACT` says what the other two come from, and `__str__` prints `[identifier]`. `tests/test_lint.py` reads the rules out of the linter's own source and fails on a rule that names a fact no topic page defines, on one that names none and gives no reason, and on a mapping for a rule that is never emitted: "every rule names its fact, or says what it comes from" |
| 4 | The deploy page explains the send from the Connectivity Kit's content library, marked as done once | VERIFIED | `deploy.content-library-send`: copy into the content library (`Contenido` on a Spanish install), right-click → *Send*. Done once, 2026-09-09, with `TAULES.hpappdir`, driven through Windows UI Automation, verified by reading the source back -- identical, 409,575 characters -- in five attempts, and the fact says nothing beyond that one run is measured |
| 5 | The mistakes models are known to make appear in the entries they concern | VERIFIED | `SIZE` (an AI-written interpreter returned the element count until HP's examples caught it) and `LEFT` (it followed HP's wording for a negative count until the emulator refused it, 2026-09-12). No other entry has a record, and the format forbids a guessed section |

## Requirements

| ID | Status | Evidence |
|---|---|---|
| FACT-01 | VERIFIED | the seven pages are gone and `MIGRATION.md` says where each section went |
| FACT-02 | VERIFIED | 106 facts, each with an identifier, one label, a statement and its evidence, and `hpprime docs --check` holds every one to that |
| FACT-03 | VERIFIED | criterion 2 |
| FACT-04 | VERIFIED | a fact about the platform is in its topic page; a fact about one command is in that command's entry, and the migration list names the phase that will move the ones whose entries do not exist yet |
| FACT-05 | VERIFIED | criterion 4 |
| CMD-06 | VERIFIED | criterion 5 |
| TOOL-02 | VERIFIED | criterion 3 |
| CHECK-04 | PARTLY | the first half holds: every rule is tied to a fact or says what it comes from, and a test enforces it. The second half -- every fact that can be caught from a PC has a rule or says why not -- has not been done: 106 facts against 13 rules, with no audit of which of the rest a linter could see |

## Tests

```
python tests/run_all.py     724 passed, 0 failed, across 13 suites
hpprime docs --check        5 entries, 106 facts, 25 examples run: 0 problems
docs/reference/             empty
```

## The gap, and what would close it

One pass over the 106 facts, marking each as caught by a rule, invisible from
a PC, or catchable and not caught. The third list is the useful output: it is
the backlog of lint rules worth writing, and it is what CHECK-04 asks for.
It is a phase of its own rather than a task at the end of this one, and it
wants the entries of Phases 5 to 8 in place first, because most of what a
linter could catch is about commands that have no entry yet.

## What this phase changed about the documentation

Prose let a measurement, an inference and a guess sit in the same paragraph.
The format does not, and moving 2,180 lines through it turned up:

- two lint rules stricter than their evidence (`equality`, `end-semicolon`),
  now citing facts that say what would settle them;
- a claim in `docs/tools.md` and `README.md` that twelve of the thirteen rules
  came from errors measured on a G2, which was not true;
- items that read like rules and rest on a published tutorial or on somebody
  else's source: locals initialised on one line, the touch layer, half of
  `micropython`;
- a finding that had never reached the documentation at all: the content
  library send, which was in `PROJECT.md` and is now a fact.

## Human approval

- [x] Phase 4 approved to close — the user, 2026-09-12, with the two unverified lint rules to be measured in the next emulator batch
