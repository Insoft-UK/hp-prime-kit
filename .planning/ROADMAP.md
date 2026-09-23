# Roadmap: hp-prime-kit

## Overview

Milestone 1 builds the documentation. First comes the format, with the tests
that hold every entry to it. Then three foundations: the list of every PPL
name, a way to run examples on the Virtual Calculator, and the facts measured
so far carried over. With those in place the entries are written group by
group (statements and program commands, Home functions, app functions, app
variables, then the variables of Home and the system), every example run on
the emulator, and the milestone closes with
the guided path, the index for models and the README. Milestone 2, the agent
kit, is planned once this one is done.

## Milestones

- 🚧 **Milestone 1: the documentation** — Phases 1-9 (in progress)
- 📋 **Milestone 2: the agent kit** — planned after milestone 1 (KIT-01 to KIT-11 in `REQUIREMENTS.md`)

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): planned milestone work
- Decimal phases (2.1, 2.2): urgent insertions (marked INSERTED)

- [x] **Phase 1: Entry format and checks** - One format for commands, facts and examples, and the tests that hold every entry to it (completed 2026-09-11)
- [x] **Phase 2: Command inventory** - Every PPL name as data, reconciled with 2.4.15515, and a linter that flags invented commands (completed 2026-09-11)
- [x] **Phase 3: Evidence on the Virtual Calculator** - Examples run in batches on the emulator, with any kind of answer brought back (completed 2026-09-12)
- [x] **Phase 4: Facts carried over** - Everything measured so far, in the new format, with lint messages that cite it (completed 2026-09-12)
- [x] **Phase 5: Statements and program commands** - Entries for the part of PPL every program uses (completed 2026-09-12)
- [x] **Phase 6: Home functions** - Entries for math, lists, matrices, statistics and the rest (completed 2026-09-13)
- [x] **Phase 7: App functions** - Entries for the functions of HP's apps that a program can call (completed 2026-09-14)
- [ ] **Phase 8: App variables** - Entries for the app variables a program can read or set
- [ ] **Phase 8.1: Home and system variables** (INSERTED) - Entries for the 65 variables of Home, the system and the settings every app shares, and `GET`
- [ ] **Phase 9: Guided path, index and README** - The way in, for a person and for a model

## Phase Details

### Phase 1: Entry format and checks
**Goal**: A fixed, documented format for a command entry, a fact and an example, and tests that reject anything that does not follow it
**Depends on**: Nothing (first phase)
**Requirements**: CMD-03, CMD-04, CMD-07, READ-02, CHECK-01, CHECK-03, CHECK-05
**Success Criteria** (what must be TRUE):
  1. One page explains the format of an entry, a fact and an example, and the four ways each can state how it is known
  2. A handful of real entries (for example `LEFT`, `SIZE` and `FOR`) and facts (for example the `LOCAL` limit) exist in the final format and pass the tests
  3. The tests fail on a duplicate identifier, a reference that does not resolve, a documentation page that mentions the kit, and a broken link
  4. For a command the interpreter implements, its entry's examples also run through `hpprime run` in the tests
**Plans**: 2 plans

Plans:
- [x] 01-01: The format, and real content in it
- [x] 01-02: The checks and the generator

### Phase 2: Command inventory
**Goal**: The complete list of PPL names lives in the repository as data, and the linter uses it
**Depends on**: Phase 1
**Requirements**: CMD-01, CMD-02, CMD-05, TOOL-01
**Success Criteria** (what must be TRUE):
  1. The list holds every statement, command, Home function, app function and app variable in HP's help, with its category and syntax; a first count of the help's titles puts the upper-case names at about 280
  2. Names added or removed after firmware 13217 are identified from a second source, and every name says where it came from
  3. An index by name and one by HP's grouping are generated from the list
  4. `hpprime lint` flags `STRLEN(s)` as a name that does not exist, and stays quiet on the program's own functions, locals and globals
**Plans**: 2 plans

Plans:
- [x] 02-01: The list of names, and the index over all of it
- [x] 02-02: The linter that reads the list

### Phase 3: Evidence on the Virtual Calculator
**Goal**: The examples of any batch of entries run on the Virtual Calculator with one keypress, and every kind of answer comes back as a file
**Depends on**: Phase 1. Checkpoint before it starts: the user installs the Virtual Calculator 2.4 and opens it once (done on 2026-09-11: 2.4 r15515)
**Requirements**: EVID-01, EVID-02, EVID-03, EVID-04, TOOL-03
**Success Criteria** (what must be TRUE):
  1. `hpprime doctor` finds the Spanish Connectivity Kit (`Calculadoras`) and the Virtual Calculator, and says which folders it used
  2. A batch of examples is sent, run with one keypress on the emulator and read back, strings, lists, matrices and errors included
  3. Each result is stored with the firmware it came from, and one that differs from HP's stated result is flagged
  4. The reader's wrong pick between two source records ending at the same offset is reproduced in a test and fixed
**Plans**: 3 plans

Plans:
- [x] 03-01: The localised folders, and what the real mirror showed
- [x] 03-02: The batch runner, and results.tsv
- [x] 03-03: The first real batch, on the emulator, with the user

### Phase 4: Facts carried over
**Goal**: Everything the current reference establishes is in the new format, stated once, and the linter points at it
**Depends on**: Phase 1
**Requirements**: FACT-01, FACT-02, FACT-03, FACT-04, FACT-05, CMD-06, TOOL-02, CHECK-04
**Success Criteria** (what must be TRUE):
  1. A migration list maps every fact in today's seven reference pages to its new home, with none left out
  2. The false hypotheses and the unverified items are entries with their own status
  3. Every lint message names the fact identifier it comes from, and a test checks that every rule has one
  4. The deploy page explains the send from the Connectivity Kit's content library, marked as done once
  5. The mistakes models are known to make appear in the entries they concern
**Plans**: 3 plans

Plans:
- [x] 04-01: The language and the formats
- [x] 04-02: The screen, the apps and Python
- [x] 04-03: Deploy, libraries, and the linter's sources

### Phase 5: Statements and program commands
**Goal**: Every statement and program command has a complete entry whose examples have been run
**Depends on**: Phases 2, 3 and 4
**Requirements**: CMD-08
**Success Criteria** (what must be TRUE):
  1. Every name the inventory files under statements and program commands has an entry in the fixed format
  2. Every example in those entries has a Virtual Calculator result on file, or says why it cannot have one
  3. The tests pass with the new entries included
**Plans**: 5 plans

Plans:
- [x] 05-01: The language itself
- [x] 05-02: Strings and integers
- [x] 05-03: Matrices, and the mixed bag under `more`
- [x] 05-04: The commands that talk to a person
- [x] 05-05: The 35 that paint

### Phase 6: Home functions
**Goal**: Every Home function has a complete entry whose examples have been run
**Depends on**: Phase 5
**Requirements**: CMD-09
**Success Criteria** (what must be TRUE):
  1. Every name the inventory files under the Home functions has an entry in the fixed format
  2. Every example in those entries has a Virtual Calculator result on file, or says why it cannot have one
  3. Where HP's stated result and the emulator's answer differ, the entry says so
**Plans**: 6 plans

Plans:
- [x] 06-01: Ten Home functions, and the guard for the one answer never kept
- [x] 06-02: Integers, bits and the rest of arithmetic
- [x] 06-03: The matrices and the lists
- [x] 06-04: The four small groups
- [x] 06-05: The mathematics of catalog
- [x] 06-06: The machine names of catalog

### Phase 7: App functions
**Goal**: Every app function a program can call has a complete entry whose examples have been run
**Depends on**: Phase 6
**Requirements**: CMD-10
**Success Criteria** (what must be TRUE):
  1. Every app function on the list has an entry in the fixed format, with the app it belongs to
  2. Every example in those entries has a Virtual Calculator result on file, or says why it cannot have one
**Plans**: 7, all complete

### Phase 8: App variables
**Goal**: Every app variable a program can read or set has an entry
**Depends on**: Phase 7
**Requirements**: CMD-11
**Success Criteria** (what must be TRUE):
  1. Every app variable on the list has an entry in the fixed format, with its app, what it holds, and whether a program can set it
  2. Every example in those entries has a Virtual Calculator result on file, or says why it cannot have one
**Plans**: 4 complete so far (08-01 to 08-04), one round on the emulator at a time; 42 variables in six apps remain

### Phase 8.1: Home and system variables (INSERTED)
**Goal**: Every variable a program reads or sets outside one app has an entry: Home's settings, the system's, and the plot and numeric settings every app shares
**Depends on**: Phase 8. Inserted on 2026-09-16: Phase 5 deferred these 65 names to Phases 6, 7 and 8, none of those phases took them, and `GET` was never assigned
**Requirements**: CMD-12
**Success Criteria** (what must be TRUE):
  1. Every name the list files as `variable` has an entry in the fixed format, with what it holds and whether a program can set it
  2. `GET` has an entry, which says what it is, or that the sources do not say
  3. Every example in those entries has a Virtual Calculator result on file, or says why it cannot have one
**Plans**: TBD

### Phase 9: Guided path, index and README
**Goal**: A person can learn from zero and a model can find any entry, both on the finished reference
**Depends on**: Phases 5, 6, 7, 8 and 8.1. It runs ahead of 8 and 8.1, at the user's choice on 2026-09-16: what it builds is generated from the entries or links to them, and its verification is counted again when 8.1 closes
**Requirements**: READ-01, READ-03, READ-04, READ-05, READ-06, CHECK-02
**Success Criteria** (what must be TRUE):
  1. The guided path takes somebody from an empty folder to a program running on the calculator, linking to entries rather than restating them
  2. One index, within its size budget, lists every entry and topic with its identifier and a one-line summary
  3. The README presents the documentation first, and `AGENTS.md` and `SKILL.md` point at the new documentation until milestone 2 replaces them
  4. The tests confirm that every example in the documentation has been run or says why not
**Plans**: 4, approved on 2026-09-16; 3 complete

Plans:
- [x] 09-01: The model index, and the check for examples nobody ran
- [x] 09-02: Planning language out of the documentation
- [x] 09-03: The guided path
- [ ] 09-04: The README, and the pages above the documentation

## Progress

**Execution Order:**
Phases run in numeric order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 8.1 → 9. Phase 4 depended only on Phase 1, so it could move ahead of Phase 3 while the emulator was not ready. Phase 9 runs ahead of 8 and 8.1 at the user's choice, since nothing it builds waits for their entries.

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Entry format and checks | 2/2 | Complete | 2026-09-11 |
| 2. Command inventory | 2/2 | Complete | 2026-09-11 |
| 3. Evidence on the Virtual Calculator | 3/3 | Complete | 2026-09-12 |
| 4. Facts carried over | 3/3 | Complete | 2026-09-12 |
| 5. Statements and program commands | 5/5 | Complete | 2026-09-12 |
| 6. Home functions | 6/6 | Complete | 2026-09-13 |
| 7. App functions | 7/7 | Complete | 2026-09-14 |
| 8. App variables | 4/TBD | In progress: 130 of 172 | - |
| 8.1. Home and system variables | 0/TBD | Not started (INSERTED) | - |
| 9. Guided path, index and README | 3/4 | In progress | - |
