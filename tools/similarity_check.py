#!/usr/bin/env python3
"""Prüft, wie ähnlich sich die Branchenseiten im sichtbaren Text sind.

Faustregel: über 60 % wird es kritisch (Doorway-Pages-Muster),
über 80 % ist es ein akutes Problem.
"""
import difflib
import itertools
import pathlib
import re

PUB = pathlib.Path(__file__).resolve().parent.parent / 'public'


def sichtbarer_text(pfad):
    s = pfad.read_text(encoding='utf-8')
    s = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', '', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def main():
    seiten = sorted(p for p in PUB.glob('*.html') if p.name != 'index.html')
    texte = {p.name: sichtbarer_text(p) for p in seiten}

    print(f'{len(seiten)} Branchenseiten geprüft\n')
    for name, t in texte.items():
        print(f'  {name:34s} ~{len(t.split())} Wörter')

    werte = []
    schlimmste = None
    for a, b in itertools.combinations(seiten, 2):
        r = difflib.SequenceMatcher(None, texte[a.name], texte[b.name]).ratio()
        werte.append(r)
        if schlimmste is None or r > schlimmste[0]:
            schlimmste = (r, a.name, b.name)

    if not werte:
        return
    schnitt = sum(werte) / len(werte)
    print(f'\nÄhnlichkeit: Durchschnitt {schnitt*100:.1f} %, '
          f'Maximum {schlimmste[0]*100:.1f} % ({schlimmste[1]} / {schlimmste[2]})')
    if schlimmste[0] > 0.8:
        print('AKUT: Seiten sind praktisch Kopien voneinander.')
    elif schlimmste[0] > 0.6:
        print('WARNUNG: zu ähnlich, bitte inhaltlich weiter differenzieren.')
    else:
        print('In Ordnung.')


if __name__ == '__main__':
    main()
