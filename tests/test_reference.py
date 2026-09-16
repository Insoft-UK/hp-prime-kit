# -*- coding: utf-8 -*-
"""The documentation, held to its format in both directions.

    python tests/test_reference.py

docs/format.md states the format and hpkit/docs.py enforces it. A check that
has only ever passed proves nothing, so this suite breaks a copy of the
documentation on purpose, one way at a time, and requires every break to be
caught. The real documentation has to pass untouched: a check that flags
correct pages gets ignored, which is worse than having none.
"""
from __future__ import unicode_literals
import io, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from hpkit import docs                                        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(errors='replace')


def copy():
    tmp = tempfile.mkdtemp(prefix='hpdocs-')
    shutil.copytree(os.path.join(ROOT, 'docs'), os.path.join(tmp, 'docs'))
    return tmp


def _path(root, rel):
    return os.path.join(root, *rel.split('/'))


def edit(root, rel, old, new):
    path = _path(root, rel)
    text = io.open(path, encoding='utf-8').read()
    if old not in text:
        raise AssertionError('%s does not contain %r' % (rel, old))
    with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text.replace(old, new, 1))


def append(root, rel, extra):
    with io.open(_path(root, rel), 'a', encoding='utf-8', newline='\n') as f:
        f.write(extra)


def entry_named(root, name):
    """A copy of LEFT's entry under another name, in the same folder."""
    text = io.open(_path(root, 'docs/commands/strings/LEFT.md'),
                   encoding='utf-8').read().replace('# LEFT\n', '# %s\n' % name)
    with io.open(_path(root, 'docs/commands/strings/%s.md' % name), 'w',
                 encoding='utf-8', newline='\n') as f:
        f.write(text)


AGAIN = """
<a name="ppl.local-limit"></a>
## The same identifier, twice

| | |
|---|---|
| Identifier | `ppl.local-limit` |
| Kind | rule |
| Known from | G2 |

Stated again.

**Evidence.** None.
"""

# (what is broken, how, and a phrase the report has to contain)
BREAKS = [
    ('a fact identifier used twice',
     lambda r: append(r, 'docs/topics/ppl.md', AGAIN), 'already used'),
    ('a link to a fact that does not exist',
     lambda r: edit(r, 'docs/commands/list/SIZE.md', '#ppl.index-call)',
                    '#ppl.no-such-fact)'), 'names no fact'),
    ('a link to a file that does not exist',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md', '(RIGHT.md)',
                    '(RIGHTS.md)'), 'goes nowhere'),
    ('a page that points at the layer built on it',
     lambda r: append(r, 'docs/commands/strings/LEFT.md', '\nSee SKILL.md.\n'),
     'layer built on it'),
    ('a generated page out of date',
     lambda r: append(r, 'docs/commands/index.md', '\nedited by hand\n'),
     'out of date'),
    ('a generated page nobody produces any more',
     lambda r: append(r, 'docs/commands/gone.md', '# Gone\n'),
     'no folder of entries produces'),
    ('an example with no label',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md',
                    '| `"MOM"` | [emulator](../results.tsv) |',
                    '| `"MOM"` |  |'), 'exactly one label'),
    ('a label that is not one of the four',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md',
                    '| [emulator](../results.tsv) |', '| HP manual |'),
     'exactly one label'),
    ('a behaviour paragraph with no label',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md', 'to mix up (G2).',
                    'to mix up.'), 'says how it is known'),
    ('an example the interpreter contradicts',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md', '| `"MOM"` |',
                    '| `"MOO"` |'), 'the interpreter answers'),
    ('an error the interpreter does not raise',
     lambda r: edit(r, 'docs/commands/strings/MID.md',
                    '| `MID("abcdef", 0, 2)` | *error* |',
                    '| `MID("abcdef", 1, 2)` | *error* |'),
     'where the entry says error'),
    ('a title that is not the file name',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md', '# LEFT\n',
                    '# LEFTX\n'), 'the title is'),
    # The suffix belongs on the file where two names differ only in case, and
    # never in the title: a title carrying it names a command nobody has.
    ('a title wearing the file name suffix',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md', '# LEFT\n',
                    '# LEFT-var\n'), 'the title is'),
    ('a group that is not the folder',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md', '| Group | strings |',
                    '| Group | list |'), 'lives in'),
    ('a field missing',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md',
                    '| Runs on the PC | yes |\n', ''), 'the fields are'),
    ('a section that is not one of the four',
     lambda r: edit(r, 'docs/commands/loop/FOR.md', '## Behaviour',
                    '## Behavior'), 'unknown section'),
    ('a fact whose Identifier is not its anchor',
     lambda r: edit(r, 'docs/topics/ppl.md', '| Identifier | `ppl.index-call` |',
                    '| Identifier | `ppl.indexcall` |'), 'repeats the anchor'),
    ('a fact with no evidence',
     lambda r: edit(r, 'docs/topics/ppl.md', '**Evidence.** A program that runs',
                    'A program that runs'), 'Evidence'),
    ('an entry whose name is not on the list',
     lambda r: entry_named(r, 'NOSUCH'), 'is not on the list of names'),
    ('an entry in a folder the list does not give it',
     lambda r: edit(r, 'docs/commands/names.tsv', 'LEFT\tcommand\tstrings',
                    'LEFT\tcommand\ttext'), 'the list files LEFT under'),
    ('a row of the list with a field missing',
     lambda r: append(r, 'docs/commands/names.tsv', 'BROKEN\tfunction\n'),
     'a row has'),
    ('an example labelled emulator with no stored answer',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md',
                    '| `LEFT("MOMOGUMBO", 3)`',
                    '| `LEFT("xyz", 1)` | `"x"` | [emulator](../results.tsv) |'
                    '\n| `LEFT("MOMOGUMBO", 3)`'),
     'holds no answer'),
    ('a stored answer that differs from the entry',
     lambda r: stored(r, 'LEFT', 'LEFT("abcdef", 3)', '"abd"', '2'),
     'the emulator answers'),
    # COS does not run on the PC, so an example of it with no stored answer
    # and no G2 measurement has been run nowhere.
    ('an example nobody has run',
     lambda r: edit(r, 'docs/commands/catalog/COS.md',
                    '| `COS(1)` | `0.540302305868` | [emulator](../results.tsv) |',
                    '| `COS(1)` | `0.540302305868` | [emulator](../results.tsv) |'
                    '\n| `COS(0)` | `1` | HP help |'),
     'nobody has run'),
    ('the index for models out of date',
     lambda r: append(r, 'docs/llms.txt', '\nedited by hand\n'),
     'out of date'),
    ('the index for models over its budget',
     lambda r: edit(r, 'docs/commands/strings/LEFT.md',
                    'The first n characters of a string.',
                    'The first n characters of a string'
                    + ', said at length' * 7000 + '.'),
     'over its budget'),
]


def stored(root, entry, call, answer, type_):
    """Write one row into results.tsv, as hpprime examples would."""
    from collections import OrderedDict
    from hpkit import examples
    examples.write_results(root, [OrderedDict([
        ('entry', entry), ('call', call), ('answer', answer),
        ('type', type_), ('firmware', 'test'), ('date', '2026-09-11')])])

# A call the interpreter says it does not cover: MID with four arguments
# raises Unsupported, and an entry that states a result for it has to be
# listed rather than failed.
UNCOVERED = ('| `MID("abcdef", 2, 3)` | `"bcd"` |',
             '| `MID("abcdef", 2, 3, 4)` | `"bcd"` | unverified |\n'
             '| `MID("abcdef", 2, 3)` | `"bcd"` |')


def quiet_when_uncovered():
    """An example the interpreter does not cover is listed, not failed: the
    interpreter is a subset, and says so instead of guessing. It still has to
    have been run somewhere, so the copy stores the emulator's answer."""
    root = copy()
    try:
        edit(root, 'docs/commands/strings/MID.md', *UNCOVERED)
        stored(root, 'MID', 'MID("abcdef", 2, 3, 4)', '"bcd"', '2')
        docs.build(root)
        problems, notes = docs.check(root)
        if problems:
            return False, 'it failed: %s' % '; '.join(str(p) for p in problems)
        if not notes:
            return False, 'the example was not listed as uncovered'
        return True, ''
    finally:
        shutil.rmtree(root, ignore_errors=True)


def index_for_models():
    """docs/llms.txt has one line for every entry and every fact, each with
    the link a model follows, and fits its budget."""
    entries, facts, _ = docs.load(ROOT)
    text = io.open(os.path.join(ROOT, 'docs', docs.LLMS),
                   encoding='utf-8').read()
    lines = set(text.split('\n'))
    missing = ['%s' % e.name for e in entries
               if not any(l.startswith('- [%s](commands/%s/%s.md): '
                                       % (e.name, e.folder, e.stem))
                          for l in lines)]
    for f in facts:
        page = os.path.basename(f.path)
        if '- [%s](topics/%s#%s): %s' % (f.ident, page, f.ident,
                                         f.title) not in lines:
            missing.append(f.ident)
    size = len(text.encode('utf-8'))
    if missing:
        return False, 'no line for %s' % ', '.join(missing[:5])
    if size > docs.LLMS_BUDGET:
        return False, '%d bytes, over %d' % (size, docs.LLMS_BUDGET)
    return True, '%d entries and %d facts in %d bytes of %d' % (
        len(entries), len(facts), size, docs.LLMS_BUDGET)


def main():
    ok = bad = 0
    problems, notes = docs.check(ROOT)
    if problems:
        bad += 1
        print('  FAIL  the documentation as it is has %d problem(s):'
              % len(problems))
        for p in problems:
            print('          %s' % p)
    else:
        ok += 1
        entries, facts, _ = docs.load(ROOT)
        print('  ok    the documentation as it is passes: %d entries, %d facts'
              % (len(entries), len(facts)))

    entries = docs.load(ROOT)[0]
    _, _, ran = docs.run_examples(ROOT, entries)
    if ran:
        ok += 1
        print('  ok    %d example(s) ran through the interpreter and agree'
              % ran)
    else:
        bad += 1
        print('  FAIL  no example ran through the interpreter')

    good, why = index_for_models()
    if good:
        ok += 1
        print('  ok    the index for models lists %s' % why)
    else:
        bad += 1
        print('  FAIL  the index for models: %s' % why)

    good, why = quiet_when_uncovered()
    if good:
        ok += 1
        print('  ok    an example the interpreter does not cover is listed, '
              'not failed')
    else:
        bad += 1
        print('  FAIL  an uncovered example: %s' % why)

    for name, breaker, expect in BREAKS:
        root = copy()
        try:
            breaker(root)
            found, _ = docs.check(root)
            if [p for p in found if expect in p.message]:
                ok += 1
                print('  ok    catches %s' % name)
            else:
                bad += 1
                print('  FAIL  missed %s; the report was: %s'
                      % (name, '; '.join(str(p) for p in found) or 'nothing'))
        finally:
            shutil.rmtree(root, ignore_errors=True)

    print('\nPASS: %d   FAIL: %d' % (ok, bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
