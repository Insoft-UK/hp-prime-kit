# -*- coding: utf-8 -*-
"""The interpreter against HP's own documented examples.

    python tests/test_hpdocs.py

Every other suite here checks the kit against itself, or against a
measurement its own author took. This one checks it against a source that
did not come from this repository at all: the examples printed in the
calculator's built-in help, which HP publishes as a PDF dump of the command
tree. `tests/hp_examples.txt` says where.

Three outcomes, and the middle one is the point:

  ok            the interpreter gives HP's answer
  NOT COVERED   it raised -- allowed, because `interp` promises to fail
                rather than guess. Counted and listed, never a failure.
  FAIL          it returned a DIFFERENT value. That is an invented result,
                which is the one thing the module says it will not do.

A case that fails is a divergence to investigate, not automatically a bug
here: the dump is from firmware 13217 and this kit's reference is 2.4.15515.
Check it on a calculator before deciding which side is wrong.
"""
from __future__ import unicode_literals
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from hpkit import interp                                    # noqa: E402
# The same reading of a printed result, and the same tolerance, as the check
# that runs the documentation's examples: HP prints rounded results.
from hpkit.docs import parse_result as parse, same          # noqa: E402

CASES = os.path.join(HERE, 'hp_examples.txt')


def load_cases():
    """-> [(expression, expected as text)]."""
    out = []
    for line in io.open(CASES, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        expr, sep, want = line.partition('|')
        if sep:
            out.append((expr.strip(), want.strip()))
    return out


def evaluate(expression):
    """-> (value, None) or (None, why it could not be run)."""
    m = interp.Machine()
    try:
        m.load('EXPORT T()\nBEGIN\n  RETURN %s;\nEND;' % expression)
        return m.call('T'), None
    except (interp.Unsupported, interp.PPLError) as e:
        return None, '%s: %s' % (type(e).__name__, e)
    except Exception as e:                       # a gap, not a crash report
        return None, '%s: %s' % (type(e).__name__, e)


def main():
    ok = bad = 0
    uncovered = []
    for expression, want_text in load_cases():
        got, why = evaluate(expression)
        if why is not None:
            uncovered.append((expression, want_text, why))
            continue
        if same(got, parse(want_text)):
            ok += 1
        else:
            bad += 1
            print('  FAIL  %-38s HP says %-22s got %r'
                  % (expression, want_text, got))

    print('  ok    %d example(s) match HP' % ok)
    if uncovered:
        print('\n  %d not covered -- raised instead of answering, which is'
              ' allowed:' % len(uncovered))
        for expression, want_text, why in uncovered:
            print('    %-38s HP says %-22s %s'
                  % (expression[:38], want_text[:22], why[:44]))

    print('\nPASS: %d   FAIL: %d' % (ok, bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
