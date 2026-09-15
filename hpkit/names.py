# -*- coding: utf-8 -*-
"""The list of every PPL name, as the documentation keeps it.

docs/commands/names.tsv is built by tests/names_extract.py from HP's own
sources: the Command Tree of firmware 13217, the command tree of 2.1.14181,
and the release notes up to 2.4.15515. This module reads it. The
documentation builds its index from it, and the linter uses it to know which
names exist.

    from hpkit import names
    everything = names.load()          # OrderedDict: name -> Name
    names.known(everything)            # every name, lower case
"""
from __future__ import unicode_literals
import io, os
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PATH = os.path.join(ROOT, 'docs', 'commands', 'names.tsv')

FIELDS = ('name', 'kind', 'group', 'menu', 'syntax', 'source')
KINDS = ('statement', 'keyword', 'operator', 'command', 'function',
         'app function', 'app variable', 'variable', 'cas', 'unknown')

# The kinds that get an entry of their own. Keywords belong to the entry of
# their statement, operators to the language's topic page, and CAS is out of
# scope: those are known to the linter and not documented one by one.
DOCUMENTED = ('statement', 'command', 'function', 'app function',
              'app variable', 'variable', 'unknown')


class Name(object):
    def __init__(self, line, name, kind, group, menu, syntax, source):
        self.line = line
        self.name = name
        self.kind = kind
        self.group = group
        self.menu = menu
        self.syntax = syntax
        self.source = source

    @property
    def documented(self):
        return self.kind in DOCUMENTED


def read(path=PATH):
    """-> ([Name], [(line, problem)]). Comment lines start with #."""
    out, problems, seen = [], [], set()
    if not os.path.isfile(path):
        return out, [(0, 'there is no list of names at %s' % path)]
    for n, line in enumerate(io.open(path, encoding='utf-8'), 1):
        line = line.rstrip('\n').rstrip('\r')
        if not line.strip() or line.startswith('#'):
            continue
        cells = line.split('\t')
        if len(cells) != len(FIELDS):
            problems.append((n, 'a row has %d fields: %s'
                             % (len(FIELDS), ', '.join(FIELDS))))
            continue
        name = Name(n, *cells)
        if name.kind not in KINDS:
            problems.append((n, 'unknown kind "%s"' % name.kind))
        if name.name in seen:
            problems.append((n, '%s is listed twice' % name.name))
        seen.add(name.name)
        out.append(name)
    return out, problems


def load(path=PATH):
    """-> OrderedDict {name: Name}, the first row winning."""
    out = OrderedDict()
    for name in read(path)[0]:
        out.setdefault(name.name, name)
    return out


def known(everything=None):
    """-> the set of every listed name, lower case.

    The linter compares the calculator's names without regard to case, so
    that it never flags a spelling the calculator might accept (sin for
    SIN). Whether the calculator itself ignores case in its own names has
    not been measured. A program's own names are compared exactly."""
    if everything is None:
        everything = load()
    return set(n.lower() for n in everything)
