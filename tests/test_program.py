# -*- coding: utf-8 -*-
"""Tests for the .hpprgm reader/writer.

Part of this runs anywhere: it uses the code template the kit ships. The
rest needs files written by the Connectivity Kit, and those are specific to
each machine, so if none are found those checks are skipped rather than
failed.

    python tests/test_program.py [calculator_folder]

The default folder is the first calculator in the Connectivity Kit's mirror,
    %USERPROFILE%\\Documents\\HP Connectivity Kit\\<Calculators>\\
where <Calculators> is whatever the Kit calls it in its language
(Calculadoras on a Spanish install).
"""
from __future__ import unicode_literals
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from hpkit import program as P

SAMPLE = """EXPORT SUMSQ(n)
BEGIN
  LOCAL zi, zs;
  zs := 0;
  FOR zi FROM 1 TO n DO
    zs := zs + zi * zi;
  END;
  RETURN zs;
END;"""

ACCENTS = 'EXPORT F()\nBEGIN\n  RETURN "àèóç µ Ω";\nEND;'

# Header words that vary between files and are not lengths: see
# docs/topics/formats.md, the container facts.
VARIABLE_WORDS = ((20, 24), (44, 48))


def find_calculator(given=None):
    if given:
        return given
    # Found by what it holds: the Kit names it in its own language.
    from hpkit import emulator
    base = emulator.find_ck_root()
    if not base or not os.path.isdir(base):
        return None
    for d in sorted(os.listdir(base)):
        p = os.path.join(base, d)
        if os.path.isdir(p) and any(f.endswith('.hpprgm')
                                    for f in os.listdir(p)):
            return p
    return None


def shipped_template_checks():
    """What must hold on a fresh clone, with no calculator anywhere."""
    ok = bad = 0
    path = P.default_template()
    if not path:
        print('  FAIL  templates/code.hpprgm is missing from the repository')
        return 0, 1
    data = open(path, 'rb').read()

    txt, _lens, start, _end = P.read(data)
    if P.has_compiled_block(data, start):
        print('  FAIL  the shipped template carries a compiled block')
        bad += 1
    else:
        print('  ok    the shipped template has no compiled block')
        ok += 1

    if P.write(data, txt) == data:
        print('  ok    the shipped template round-trips identical')
        ok += 1
    else:
        print('  FAIL  the shipped template does not round-trip')
        bad += 1

    for name, src in (('a program', SAMPLE), ('accented text', ACCENTS)):
        out = P.write(data, src)
        if P.read(out)[0] == src:
            print('  ok    %s survives being written into the template' % name)
            ok += 1
        else:
            print('  FAIL  %s came back changed' % name)
            bad += 1

    # Writing twice from the same template must be deterministic, and the
    # result must itself be usable as a template.
    once = P.write(data, SAMPLE)
    if P.write(data, SAMPLE) == once:
        print('  ok    writing the same source twice gives the same bytes')
        ok += 1
    else:
        print('  FAIL  writing is not deterministic')
        bad += 1
    if P.read(P.write(once, ACCENTS))[0] == ACCENTS:
        print('  ok    what was written can serve as a template in turn')
        ok += 1
    else:
        print('  FAIL  the generated file is not reusable as a template')
        bad += 1

    # The sizes at which the reader used to hand back the wrapper instead of
    # the source: the record that contains the source begins with the
    # source's own length, and when the low half of that length reads as a
    # printable character the wrapper looks like text too. 97 lengths in
    # every 32,768 do, and these are the edges of the three runs, measured
    # against the shipped template. A source of any length must read back.
    sizes = (32726, 32737, 32784, 32801, 32848)
    wrong = []
    for n in sizes:
        src = '// ' + 'a' * (n - 3)
        if P.read(P.write(data, src))[0] != src:
            wrong.append(n)
    if wrong:
        print('  FAIL  these lengths do not read back: %s'
              % ', '.join(str(n) for n in wrong))
        bad += 1
    else:
        print('  ok    the %d sizes that used to come back as the wrapper'
              % len(sizes))
        ok += 1

    return ok, bad


def main(argv):
    print('-- shipped template (no calculator needed)')
    ok, bad = shipped_template_checks()

    folder = find_calculator(argv[1] if len(argv) > 1 else None)
    if not folder:
        print('\nSKIPPED: no Connectivity Kit folder found; ran the '
              'template checks only')
        print('\nPASS: %d   FAIL: %d' % (ok, bad))
        return 1 if bad else 0

    binaries = []
    for root, _, fs in os.walk(folder):
        for f in sorted(fs):
            if f.endswith(('.hpprgm', '.hpappprgm')):
                binaries.append(os.path.join(root, f))
    if not binaries:
        print('\nSKIPPED: no programs in %s' % folder)
        print('\nPASS: %d   FAIL: %d' % (ok, bad))
        return 1 if bad else 0

    print('\n-- your own binaries, from %s' % folder)
    skipped = crossed = 0
    template = None
    for path in binaries:
        data = open(path, 'rb').read()
        name = os.path.basename(path)
        try:
            txt, _lens, start, _end = P.read(data)
        except P.UnexpectedFormat:
            # a program with no source block is an empty program: the
            # calculator's built-in apps are exactly that. Not a failure.
            skipped += 1
            continue

        # 1) round-trip: rewriting the same text must give the same file
        if P.write(data, txt) == data:
            ok += 1
            print('  ok    %-24s round-trip identical (%d chars)'
                  % (name, len(txt)))
        else:
            bad += 1
            print('  FAIL  %-24s round-trip differs' % name)

        if not P.has_compiled_block(data, start) and template is None:
            template = (name, data)

    # The template the kit ships wins over anything in the CK folder: those
    # files stop being usable the moment the calculator rewrites the program,
    # because from then on they carry their own compiled block.
    fixed = os.environ.get('HP_PRIME_TEMPLATE') or P.default_template()
    if fixed and os.path.isfile(fixed):
        d = open(fixed, 'rb').read()
        try:
            if not P.has_compiled_block(d, P.read(d)[2]):
                template = (os.path.basename(fixed), d)
        except P.UnexpectedFormat:
            pass

    # 2) cross-build: put one program's source into another one's container.
    #    This is the check that really validates the length arithmetic,
    #    because the size changes.
    if template:
        tname, tdata = template
        for path in binaries:
            data = open(path, 'rb').read()
            name = os.path.basename(path)
            if name == tname:
                continue
            try:
                txt, _, start, end = P.read(data)
            except P.UnexpectedFormat:
                continue
            if P.has_compiled_block(data, start):
                continue
            built = P.write(tdata, txt)
            crossed += 1
            # What the writer builds is header + source; the trailer is
            # copied from the template. And the trailer is NOT always the
            # same: it can carry metadata. So what is checked is what the
            # writer actually builds, and the trailer is reported instead of
            # failing.
            # Two words of the header vary between files and are not lengths,
            # so the writer copies them from its template like the trailer:
            # offset 20 (2 in one calculator's programs, 0 elsewhere) and 44
            # (1 to 7 across the programs of one calculator, like an
            # ordinal). Programs written with the template's zeros there run
            # on a G2; what the two words mean has not been measured.
            def masked(b):
                b = bytearray(b[:end])
                for s, e in VARIABLE_WORDS:
                    if e <= len(b):
                        b[s:e] = b'\0\0\0\0'
                return bytes(b)
            if built[:end] == data[:end] or masked(built) == masked(data):
                ok += 1
                notes = []
                if built[:end] != data[:end]:
                    notes.append('header words at 20/44')
                if built[end:] != data[end:]:
                    notes.append('trailer')
                print('  ok    %-24s rebuilt from %s%s'
                      % (name, tname,
                         "  (different %s: the template's are used)"
                         % ' and '.join(notes) if notes else ''))
            else:
                bad += 1
                print('  FAIL  %-24s header or source differs (%d vs %d)'
                      % (name, len(built), len(data)))

    print('\nPASS: %d   FAIL: %d   skipped (empty programs): %d'
          % (ok, bad, skipped))
    if crossed:
        print('cross-builds: %d' % crossed)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
