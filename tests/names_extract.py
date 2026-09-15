# -*- coding: utf-8 -*-
"""Rebuild docs/commands/names.tsv, the list of every PPL name, from HP's
own sources.

    python tests/names_extract.py ct.txt CommandsList.txt release_info.txt \\
        > docs/commands/names.tsv

You only need this when one of the sources changes. The kit reads the
versioned names.tsv and needs nothing but the standard library.

Getting the three inputs, which is the one part that is not Python:

    # 1. HP's built-in help for firmware 13217, dumped to PDF (the same dump
    #    tests/hp_examples_extract.py reads)
    curl -O https://www.hpcalc.org/prime/docs/commandtree.zip
    unzip commandtree.zip
    pdftotext -layout -enc UTF-8 "Command tree 13217.pdf" ct.txt

    # 2. The command tree of firmware 2.1.14181, exported by Frank P
    curl -O https://www.hpcalc.org/prime/docs/commandslist.zip
    unzip commandslist.zip                  # CommandsList.txt, Windows-1252

    # 3. The release notes of every firmware from 13333 to 2.4.15515
    curl -O https://www.hpcalc.org/prime/pc/HP_Prime_Calculator_G2_Firmware_20250915.zip
    unzip HP_Prime_Calculator_G2_Firmware_20250915.zip release_info.txt

What it keeps: from the help, the topic titles and the first line after each
"Syntax:"; from the 2.1 list, each name and its menu path; from the release
notes, the names in NOTES below, which were read by hand because the notes
are prose. No description is copied from any of them: HP's prose stays HP's.
"""
from __future__ import unicode_literals
import io, re, sys
from collections import OrderedDict

# Names neither list has, read by hand from the release notes after
# 2.1.14091: (name, kind, group, the version whose notes name it, what they
# say, in brief).
NOTES = [
    ('UVAL', 'function', 'units', '2.1.14091',
     'added: the value part of a unit object'),
    ('UPART', 'function', 'units', '2.1.14091',
     'added: the unit part of a unit object'),
    ('normald_cdf', 'cas', 'cas', '14566',
     'named: improved precision with negative arguments'),
    ('normald_icdf', 'cas', 'cas', '14566',
     'named: optional arguments left, right, center, tail'),
    ('SeqPlot', 'app variable', 'sequence', '14730',
     'added: a Sequence app variable'),
    ('GET', 'unknown', '', '2.2',
     'named: behaves consistently on outputs of QPI; what it is is not known'),
    ('ListToMat', 'function', 'matrix', '2.4',
     'named: now an error on a list holding a string'),
]

# HP's apps, by the name the help gives them. A title such as "Importing
# from a Statistics App" is a topic, not an app.
APPS = ['Advanced Graphing', 'Data Streamer', 'Explorer', 'Finance',
        'Function', 'Geometry', 'Graph 3D', 'Inference', 'Linear Explorer',
        'Linear Solver', 'Parametric', 'Polar', 'Python',
        'Quadratic Explorer', 'Sequence', 'Solve', 'Spreadsheet',
        'Statistics 1Var', 'Statistics 2Var', 'Triangle Solver',
        'Trig Explorer']

# Sections of the tree that hold the calculator's own variables.
HOME = {'Home', 'Real', 'Complex', 'List', 'Matrix', 'Graphics',
        'Home Settings', 'System', 'CAS', 'User', 'Common', 'Common App',
        'Common Plot View', 'Common Numeric View', 'Common App Mode'}

# One-word menu titles. In the tree they head the next group of names, so
# they end the section before them and are not names themselves.
MENUS = set('''Integer More Strings Drawing Pixels Cartesian Matrix Numbers
Arithmetic Trigonometry Hyperbolic Probability List Special Polynomial Plot
Block Branch Loop Variable Function Units Complex Create Basic Advanced
Factorize Vector Extract Calculus Differential Integral Limits Transform
Rewrite Algebra Density Cumulative Inverse Random Distribution Statistics
Solve Zoom Measure Point Line Polygon Curve Tests'''.split())

KEYWORDS = set('THEN ELSE END DO FROM TO DOWNTO STEP UNTIL DEFAULT'.split())
OVERRIDES = {'AND': ('operator', ''), 'OR': ('operator', ''),
             'NOT': ('operator', ''), 'XOR': ('operator', ''),
             'Ans': ('variable', 'home')}
GROUP_FIX = {'probabiity': 'probability'}      # sic, in the 2.1 export
IDENT = re.compile(r'^[^\W\d][\w→×₀-₉]*$', re.U)
SPECIFIC = ('statement', 'command', 'app function', 'app variable',
            'variable')
KIND_ORDER = ('statement', 'keyword', 'operator', 'command', 'function',
              'app function', 'app variable', 'variable', 'cas', 'unknown')


def slug(words):
    s = ' '.join(words).lower().replace('/', '')
    s = re.sub(r'[^a-z0-9₀-₉]+', '-', s).strip('-')
    return GROUP_FIX.get(s, s)


def app_of(words):
    """-> the slug of the app a menu path starts with, or ''."""
    text = ' '.join(words)
    for app in sorted(APPS, key=len, reverse=True):
        if text == app or text.startswith(app + ' '):
            return slug([app])
    return ''


# ------------------------------------------------------------------ the help

def streams(text):
    """-> (left titles in order, right-column lines in order).

    A page of the dump is two columns: the tree of topic titles on the left,
    the help text on the right. The left column ends where the page's
    "Help Text" header starts, and a title is separated from the text beside
    it by two or more spaces."""
    bound, left, right = None, [], []
    for line in text.split('\n'):
        line = line.replace('\f', '')
        if 'Help Topics Tree' in line and 'Help Text' in line:
            bound = line.index('Help Text')
            continue
        if bound is None:
            continue
        indent = len(line) - len(line.lstrip(' '))
        if line.strip() and indent < bound - 1:
            parts = re.split(r' {2,}', line.strip(), maxsplit=1)
            left.append(parts[0].strip())
            if len(parts) > 1:
                right.append(parts[1].strip())
        else:
            right.append(line.strip())
    return left, right


def syntaxes(right):
    """-> {name: the first syntax line HP gives for it}."""
    out = {}
    for i, line in enumerate(right):
        if not line.startswith('Syntax:'):
            continue
        form = line[7:].strip() or next((r for r in right[i + 1:i + 4] if r),
                                        '')
        form = re.sub(r'\s+or$', '', form.replace('“', '"').replace('”', '"'))
        m = re.match(r'^([^\W\d][\w→×]*)', form, re.U)
        if m and m.group(1) not in out:
            out[m.group(1)] = form.replace('\t', ' ')
    return out


SECTION = re.compile(r'^(.+?) (Functions|Variables)$')
APP_TITLE = re.compile(r'^(.+?) [Aa]pp$')


def tree_names(left):
    """-> [(name, kind, group)] from the titles, in order. A name inside a
    "... Functions" or "... Variables" section belongs to it; the app is the
    last app title before it."""
    out, app, section = [], None, None
    for title in left:
        m_sec = SECTION.match(title)
        m_app = APP_TITLE.match(title)
        if m_app and not m_sec and m_app.group(1) in APPS:
            app, section = slug([m_app.group(1)]), None
            continue
        if m_sec:
            head, what = m_sec.group(1), m_sec.group(2)
            bare = re.sub(r' App$', '', head)
            kind = 'app function' if what == 'Functions' else 'app variable'
            if head in HOME or bare in HOME or title == 'Variables':
                section = ('variable', slug([bare]))
            elif bare == 'App':
                section = (kind, 'app')
            elif bare in APPS:
                app = slug([bare])
                section = (kind, app)
            else:
                section = (kind, app or slug([bare]))
            continue
        words = title.split()
        if len(words) > 1:
            if all(w.isupper() for w in words) and IDENT.match(words[0]) \
                    and words[0] not in KEYWORDS:
                out.append((words[0], 'statement', ''))
            else:
                section = None
            continue
        if title in MENUS:
            section = None
            continue
        if not IDENT.match(title):
            continue
        if section:
            out.append((title, section[0], section[1]))
        elif title[0].islower():
            out.append((title, 'cas', 'cas'))
        elif title.isupper():
            out.append((title, 'function', 'catalog'))
    return out


# ------------------------------------------------------------ the 2.1 list

def list21(text):
    """-> [(name, menu path)] in the list's order."""
    rows = []
    for line in text.splitlines():
        if line.count('|') < 2 or set(line.strip()) <= set('-|+ '):
            continue
        left = line.split('|')[0]
        m = re.match(r'^\s*(?:\d{1,4}|\+\+\+)?\s*(\S.*)$', left)
        if not m:
            continue
        parts = re.split(r'\s{2,}', m.group(1).strip(), maxsplit=1)
        menu = re.sub(r'\s+', ' ', parts[1]) if len(parts) > 1 else ''
        rows.append((parts[0], menu))
    return rows


def from_menu(menu, name):
    """-> (kind, group) for a menu path of the 2.1 list."""
    w = menu.split()
    if name in OVERRIDES:
        return OVERRIDES[name]
    if w[:2] == ['Program', 'Tmplt']:
        return 'statement', slug(w[2:3]) or 'template'
    if w[:2] == ['Program', 'Cmds']:
        return 'command', slug(w[2:3]) or 'commands'
    if w[:2] == ['Toolbox', 'Math']:
        return 'function', slug(w[2:3]) or 'math'
    if w[:2] == ['Toolbox', 'CAS']:
        return 'cas', 'cas'
    if w[:2] == ['Toolbox', 'App']:
        return 'app function', app_of(w[2:]) or 'app'
    if w[:1] == ['Units']:
        return 'function', 'units'
    if w[:1] == ['Apps']:
        return 'app function', app_of(w[1:]) or 'app'
    if w[:1] in (['Geometry'], ['Spreadsheet'], ['App']):
        return 'app function', app_of(w) or 'app'
    if not w:
        if name in KEYWORDS:
            return 'keyword', ''
        if not IDENT.match(name):
            return 'operator', ''
        if name[0].islower():
            return 'cas', 'cas'
        return 'function', 'catalog'
    return 'unknown', slug(w[:2])


# ------------------------------------------------------------------ merging

def build(ct_text, list_text, notes_text):
    left, right = streams(ct_text)
    syntax = syntaxes(right)
    titles = set(left)
    # The 2.1 export lost every character outside Windows-1252: C→PX is
    # C?PX there. Match those back to the help's spelling.
    shape = {}
    for t in titles:
        shape.setdefault(re.sub(r'[^\x00-\x7f]', '?', t), t)

    names = OrderedDict()

    def add(name, kind, group, menu, source):
        if name in names:
            n = names[name]
            if menu and menu not in n['menu']:
                n['menu'] = ' / '.join(filter(None, [n['menu'], menu]))
            # A name the 2.1 list has only in the Catalog, with no menu, is
            # placed better by the section of the help that holds it.
            if not n['placed'] and kind in SPECIFIC \
                    and n['kind'] in ('function', 'unknown', 'cas'):
                n['kind'], n['group'] = kind, group
            return
        names[name] = {'name': name, 'kind': kind, 'group': group,
                       'menu': menu, 'syntax': syntax.get(name, ''),
                       'source': source, 'placed': bool(menu)}

    for name, menu in list21(list_text):
        if '?' in name:
            if name not in shape:
                continue                # an arrow that cannot be recovered
            name = shape[name]
        words = name.split()
        if len(words) > 1:
            if words[0] in KEYWORDS or not words[0].isupper():
                continue
            name = words[0]             # FOR STEP, IF THEN ELSE: the statement
        kind, group = from_menu(menu, name)
        add(name, kind, group, menu,
            '13217' if name in titles else '2.1.14181')
    for name, kind, group in tree_names(left):
        if name in OVERRIDES:
            kind, group = OVERRIDES[name]
        add(name, kind, group, '', '13217')
    for name, kind, group, version, what in NOTES:
        if name in notes_text:
            add(name, kind, group, '', 'notes %s' % version)
    return names


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    ct = io.open(argv[0], encoding='utf-8').read()
    lst = io.open(argv[1], 'rb').read().decode('cp1252')
    notes = io.open(argv[2], encoding='utf-8-sig').read()
    names = build(ct, lst, notes)
    out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', newline='\n')
    out.write('# Every PPL name in HP\'s help, and those added since, as '
              'data.\n')
    out.write('# Generated by tests/names_extract.py from HP\'s Command Tree '
              '13217, the 2.1.14181\n# commands list and the 2.4.15515 '
              'release notes. Names, menus and syntax only.\n')
    out.write('# ' + '\t'.join(('name', 'kind', 'group', 'menu', 'syntax',
                                'source')) + '\n')
    rows = sorted(names.values(), key=lambda n: (
        KIND_ORDER.index(n['kind']), n['group'], n['name'].lower()))
    for n in rows:
        out.write('\t'.join(n[k] for k in ('name', 'kind', 'group', 'menu',
                                           'syntax', 'source')) + '\n')
    out.flush()
    kinds, sources = OrderedDict(), OrderedDict()
    for n in rows:
        kinds[n['kind']] = kinds.get(n['kind'], 0) + 1
        sources[n['source']] = sources.get(n['source'], 0) + 1
    sys.stderr.write('%d names\n  by kind: %s\n  by source: %s\n' % (
        len(rows), dict(kinds), dict(sources)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
