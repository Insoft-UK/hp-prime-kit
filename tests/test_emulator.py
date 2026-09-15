# -*- coding: utf-8 -*-
"""Tests for installing into the Virtual Calculator and reading back out.

None of this needs the emulator. A temp folder plays the part of a
calculator through HPPRIME_EMU_ROOT, and the three things that touch the
real machine -- finding it running, closing it, launching it -- are replaced
here, so both branches of "the emulator is open" can be tested on a machine
where it is not installed at all.

What is worth guarding, because both were wrong once:

  - the files are judged BEFORE anything is closed. Shutting somebody's
    emulator and only then saying "that was a .txt" is the wrong order.
  - a copy that fails with --restart still reopens the emulator.

    python tests/test_emulator.py
"""
from __future__ import unicode_literals
import io, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from hpkit import emulator as E
from hpkit import program as P

PASS, FAIL = [0], [0]

SOURCE = 'EXPORT SUMSQ()\nBEGIN\n  RETURN 385;\nEND;'


def ok(cond, msg, detail=''):
    if cond:
        PASS[0] += 1
        print('  ok    %s' % msg)
    else:
        FAIL[0] += 1
        print('  FAIL  %s%s' % (msg, ('  ' + detail) if detail else ''))


def build(path, source=SOURCE):
    """A real .hpprgm, from the template the kit ships."""
    tpl = P.default_template()
    data = P.write(open(tpl, 'rb').read(), source)
    with open(path, 'wb') as f:
        f.write(data)
    return path


def main():
    tmp = tempfile.mkdtemp(prefix='hpemu_')
    saved = (os.environ.get('HPPRIME_EMU_ROOT'), E.running, E.close, E.launch,
             os.environ.get('HPPRIME_KIT_STATE'))
    try:
        root = os.path.join(tmp, 'Calculators')
        one = os.path.join(root, 'Prime')
        os.makedirs(one)
        os.environ['HPPRIME_EMU_ROOT'] = root
        # Nothing this suite does may land in the real home folder.
        os.environ['HPPRIME_KIT_STATE'] = os.path.join(tmp, 'state')

        # ------------------------------------------------------- finding it
        ok(E.find_root() == root, 'HPPRIME_EMU_ROOT is what find_root uses')
        ok(E.instances(root) == ['Prime'], 'the one calculator is listed')
        ok(E.pick(root) == one, 'with one calculator, none has to be named')

        # The Connectivity Kit names its folders in its own language:
        # Calculadoras on a Spanish install. A name nobody has seen is found
        # by what the folder holds, and a content library, which holds apps
        # rather than calculators, is not taken for it.
        ck = os.path.join(tmp, 'HP Connectivity Kit')
        es = os.path.join(ck, 'Calculadoras', 'HP Prime')
        os.makedirs(es)
        os.makedirs(os.path.join(ck, 'Contenido', 'APP.hpappdir'))
        open(os.path.join(es, 'calc.hpsettings'), 'wb').close()
        ok(E.calculators_in(ck) == os.path.join(ck, 'Calculadoras'),
           'a Spanish Connectivity Kit: Calculadoras is found')
        other = os.path.join(tmp, 'CK2')
        seen_never = os.path.join(other, 'Rechner', 'Prime')
        os.makedirs(seen_never)
        os.makedirs(os.path.join(other, 'Aaa', 'APP.hpappdir'))
        open(os.path.join(seen_never, 'calc.hpsettings'), 'wb').close()
        ok(E.calculators_in(other) == os.path.join(other, 'Rechner'),
           'a name never seen is found by what the folder holds, and a '
           'folder of apps ahead of it in name order is passed over')
        ok(E.calculators_in(os.path.join(tmp, 'no-such-folder')) is None,
           'no folder, no answer')
        os.environ['HPPRIME_CK_ROOT'] = os.path.join(ck, 'Calculadoras')
        ok(E.find_ck_root() == os.path.join(ck, 'Calculadoras'),
           'HPPRIME_CK_ROOT is what find_ck_root uses')
        del os.environ['HPPRIME_CK_ROOT']

        two = os.path.join(root, 'Prime_1')
        os.makedirs(two)
        try:
            E.pick(root)
            ok(False, 'with two calculators it refuses to guess')
        except E.EmulatorError as e:
            ok('--calc' in str(e), 'with two calculators it refuses to guess',
               str(e))
        ok(E.pick(root, 'Prime_1') == two, '--calc names the calculator')
        try:
            E.pick(root, 'Nope')
            ok(False, 'an unknown calculator name is an error')
        except E.EmulatorError as e:
            ok('Prime' in str(e),
               'an unknown name says which ones there are', str(e))

        # ------------------------------------------ what may be copied over
        prog = build(os.path.join(tmp, 'SUMSQ.hpprgm'))
        mat = os.path.join(tmp, 'M1.hpmat')
        with open(mat, 'wb') as f:
            from hpkit import numbers
            f.write(numbers.write_hpmat([[1.0, 2.0]]))
        app = os.path.join(tmp, 'MYAPP.hpappdir')
        os.makedirs(app)
        open(os.path.join(app, 'MYAPP.hpapp'), 'wb').write(b'\x7c\x61\x8a\xb2')

        for good in (prog, mat, app):
            try:
                E._check_one(good)
                ok(True, '%s is accepted' % os.path.basename(good))
            except E.EmulatorError as e:
                ok(False, '%s is accepted' % os.path.basename(good), str(e))

        txt = os.path.join(tmp, 'SUMSQ.txt')
        with io.open(txt, 'w', encoding='utf-8') as f:
            f.write(SOURCE)
        try:
            E._check_one(txt)
            ok(False, 'a .txt source is refused, not copied')
        except E.EmulatorError as e:
            ok('hpprime write' in str(e),
               'a .txt source is refused, and says to build it first', str(e))

        try:
            E._check_one(os.path.join(tmp, 'NOPE.hpprgm'))
            ok(False, 'a missing file is refused')
        except E.EmulatorError:
            ok(True, 'a missing file is refused')

        # A file with the right name and the wrong insides is the one the
        # calculator would take in silence and then not run.
        fake = os.path.join(tmp, 'FAKE.hpprgm')
        with open(fake, 'wb') as f:
            f.write(b'not a program at all')
        try:
            E._check_one(fake)
            ok(False, 'a .hpprgm that is not one is refused')
        except E.EmulatorError:
            ok(True, 'a .hpprgm that is not one is refused')

        broken = os.path.join(tmp, 'BROKEN.hpappdir')
        os.makedirs(broken)
        try:
            E._check_one(broken)
            ok(False, 'an app folder with no .hpapp is refused')
        except E.EmulatorError as e:
            ok('hpprime build' in str(e),
               'an app folder with no .hpapp says to build it', str(e))

        # --------------------------------------------------- installing it
        done = E.install([prog, app, mat], two)
        ok(sorted(n for n, _ in done) ==
           ['M1.hpmat', 'MYAPP.hpappdir', 'SUMSQ.hpprgm'],
           'a program, an app and a matrix all go in')
        ok(os.path.isfile(os.path.join(two, 'SUMSQ.hpprgm')),
           'the program lands in the calculator folder')
        ok(os.path.isdir(os.path.join(two, 'MYAPP.hpappdir')),
           'the app lands as a folder')

        programs, apps = E.contents(two)
        ok(programs == ['SUMSQ'], 'the program is listed by name')
        ok(apps == ['MYAPP'], 'the app is listed by name')

        # The calculator's own apps are stored with a leading &, and they
        # are not yours.
        os.makedirs(os.path.join(two, '&Function.hpappdir'))
        ok(E.contents(two)[1] == ['MYAPP'],
           "the calculator's built-in apps are not listed as yours")

        ok(P.normalize_source(E.source_of(two, 'SUMSQ')) ==
           P.normalize_source(SOURCE),
           'the source read back is the source that went in')
        try:
            E.source_of(two, 'GHOST')
            ok(False, 'reading a program that is not there is an error')
        except E.EmulatorError:
            ok(True, 'reading a program that is not there is an error')

        # An install over the top replaces, rather than merging into, an app
        # folder: a file you deleted must not survive on the calculator.
        open(os.path.join(two, 'MYAPP.hpappdir', 'stale.py'), 'w').write('x')
        E.install([app], two)
        ok(not os.path.isfile(os.path.join(two, 'MYAPP.hpappdir', 'stale.py')),
           'reinstalling an app clears what is no longer in it')

        # ---------------------------------------------------- the two clis
        calls = []
        E.running = lambda: []
        E.close = lambda timeout=20: calls.append('close') or 1
        E.launch = lambda exe=None: calls.append('launch') or 'HPPrime.exe'

        rc = E.cli_pull(['--calc', 'Prime_1'])
        ok(rc == 0, 'pull with no name lists what is there')

        out = os.path.join(tmp, 'back.txt')
        rc = E.cli_pull(['SUMSQ', '--calc', 'Prime_1', '-o', out])
        ok(rc == 0 and io.open(out, encoding='utf-8').read().strip()
           == SOURCE.strip(), 'pull -o writes the source out')

        rc = E.cli_pull(['SUMSQ', '--calc', 'Prime_1', '--diff', txt])
        ok(rc == 0, 'pull --diff exits 0 when they match')

        other = os.path.join(tmp, 'other.txt')
        with io.open(other, 'w', encoding='utf-8') as f:
            f.write('EXPORT SUMSQ()\nBEGIN\n  RETURN 1;\nEND;')
        rc = E.cli_pull(['SUMSQ', '--calc', 'Prime_1', '--diff', other])
        ok(rc == 1, 'pull --diff exits 1 when the calculator has something '
                    'else')

        # With the emulator shut, install just copies.
        del calls[:]
        prog2 = build(os.path.join(tmp, 'OTHER.hpprgm'))
        rc = E.cli_install([prog2, '--calc', 'Prime_1'])
        ok(rc == 0 and 'OTHER' in E.contents(two)[0],
           'install copies when the emulator is not running')
        ok(calls == [], 'nothing is closed or launched when it was not open')

        # With it open and no --restart: refuse, and touch nothing.
        E.running = lambda: [1234]
        del calls[:]
        rc = E.cli_install([prog2, '--calc', 'Prime_1'])
        ok(rc == 1, 'install refuses while the emulator is running')
        ok(calls == [], 'and it does not close the emulator to say so')

        # The order that was wrong once: a bad file must not cost you your
        # emulator.
        del calls[:]
        rc = E.cli_install([txt, '--calc', 'Prime_1', '--restart'])
        ok(rc == 1, 'a .txt is still refused with --restart')
        ok(calls == [], 'the emulator is not closed before the files are '
                        'judged', str(calls))

        # And --restart does the whole cycle.
        del calls[:]
        rc = E.cli_install([prog2, '--calc', 'Prime_1', '--restart'])
        ok(rc == 0 and calls == ['close', 'launch'],
           'install --restart closes, copies, and opens it again',
           str(calls))

        # A copy that fails after the close still leaves it open.
        del calls[:]
        real_install = E.install
        E.install = lambda p, c: (_ for _ in ()).throw(
            E.EmulatorError('disk full'))
        try:
            rc = E.cli_install([prog2, '--calc', 'Prime_1', '--restart'])
        finally:
            E.install = real_install
        ok(rc == 1, 'a failed copy exits non-zero')
        ok('launch' in calls, 'a failed copy still reopens the emulator',
           str(calls))

        # ------------------------------------- calculators made to be burnt
        E.running = lambda: []
        lab = E.create(root, 'LAB', 'Prime')
        ok(os.path.isdir(lab), 'emu new makes a calculator')
        ok('LAB' in E.made(), 'and remembers having made it')
        ok(E.contents(lab) == ([], []),
           'a clone starts with none of your programs or apps')

        # The built-in apps do come along: they are part of the machine.
        os.makedirs(os.path.join(one, '&Function.hpappdir'))
        open(os.path.join(one, 'HERS.hpprgm'), 'wb').write(b'x')
        lab2 = E.create(root, 'LAB2', 'Prime')
        ok(os.path.isdir(os.path.join(lab2, '&Function.hpappdir')),
           "the calculator's own apps are part of the clone")
        ok(not os.path.isfile(os.path.join(lab2, 'HERS.hpprgm')),
           'a program that was already on it is not')

        try:
            E.create(root, 'LAB', 'Prime')
            ok(False, 'emu new refuses a name already taken')
        except E.EmulatorError:
            ok(True, 'emu new refuses a name already taken')
        try:
            E.create(root, 'no spaces here', 'Prime')
            ok(False, 'emu new refuses a name a calculator could not have')
        except E.EmulatorError:
            ok(True, 'emu new refuses a name a calculator could not have')

        # The identity in `settings` is what tells two calculators apart, so
        # a clone must not keep the original's.
        ident = E.SETTINGS_MAGIC + b'\x00' * 76 + b'\x04\x00\x00\x00'
        ident += b'6340C3C41AC1B93' + b'\x00' * 65
        with open(os.path.join(one, 'settings'), 'wb') as f:
            f.write(ident)
        lab3 = E.create(root, 'LAB3', 'Prime')
        after = open(os.path.join(lab3, 'settings'), 'rb').read()
        ok(len(after) == len(ident), 'the settings file keeps its size')
        ok(b'6340C3C41AC1B93' not in after,
           'a clone does not claim to be the calculator it came from')
        ok(after[:4] == ident[:4], 'and it is still a settings file')

        # A settings file this has never seen is left alone rather than
        # scribbled on.
        ok(E._reserialize(b'not a settings file', 'X') is None,
           'a file without the magic is not rewritten')

        # reset is the point of the whole thing: back to a known calculator.
        E.install([prog], lab)
        ok(E.contents(lab)[0] == ['SUMSQ'], 'something is installed on it')
        E.reset(root, 'LAB')
        ok(E.contents(lab) == ([], []), 'emu reset puts it back as it was')

        try:
            E.reset(root, 'Prime')
            ok(False, 'reset refuses a calculator it did not make')
        except E.EmulatorError:
            ok(True, 'reset refuses a calculator it did not make')
        try:
            E.remove(root, 'Prime')
            ok(False, 'remove refuses a calculator it did not make')
        except E.EmulatorError as e:
            ok('--force' in str(e),
               'remove refuses a calculator it did not make', str(e))
        ok(os.path.isdir(one), 'and it is still there')

        E.remove(root, 'LAB2')
        ok(not os.path.isdir(os.path.join(root, 'LAB2')),
           'remove deletes one it did make')
        ok('LAB2' not in E.made(), 'and forgets it')

        ok(E.cli_emu(['list']) == 0, 'emu list runs')
        ok(E.cli_emu(['new', 'LAB4', '--from', 'Prime']) == 0, 'emu new runs')
        ok(E.cli_emu(['reset', 'LAB4']) == 0, 'emu reset runs')
        ok(E.cli_emu(['remove', 'LAB4']) == 0, 'emu remove runs')
        ok(E.cli_emu(['nonsense', 'X']) == 2, 'an unknown emu word is usage')

        # ------------------------------- which calculator the emulator opens
        # It is not the tool's choice and not alphabetical, so the only
        # honest answer comes from watching which calculator's saved state
        # moves. That state is written when the emulator closes.
        stamps = E._stamps(root)
        ok(set(stamps) <= set(E.instances(root)),
           'the stamps are per calculator')
        ok(E._changed(root, stamps) is None, 'nothing has moved yet')
        settings = os.path.join(two, 'calc.hpsettings')
        open(settings, 'wb').write(b'state')
        ok(E._changed(root, stamps) == 'Prime_1',
           'a calculator whose state appears is the one that was open')

        ok(E.remembered_open(root) is None,
           'with nothing remembered it does not guess')
        state = os.environ['HPPRIME_KIT_STATE']
        if not os.path.isdir(state):
            os.makedirs(state)
        with open(os.path.join(state, 'opens.txt'), 'w') as f:
            f.write(','.join(E.instances(root)) + chr(10) + 'Prime_1')
        ok(E.remembered_open(root) == 'Prime_1', 'and it remembers')
        E.create(root, 'LAB5', 'Prime')
        ok(E.remembered_open(root) is None,
           'a new calculator makes the remembered answer stale, not wrong')
        E.remove(root, 'LAB5')
    finally:
        for var, was in (('HPPRIME_EMU_ROOT', saved[0]),
                         ('HPPRIME_KIT_STATE', saved[4])):
            os.environ.pop(var, None)
            if was is not None:
                os.environ[var] = was
        E.running, E.close, E.launch = saved[1], saved[2], saved[3]
        shutil.rmtree(tmp, ignore_errors=True)

    print('\nPASS: %d   FAIL: %d' % (PASS[0], FAIL[0]))
    return 1 if FAIL[0] else 0


if __name__ == '__main__':
    sys.exit(main())
