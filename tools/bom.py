#!/usr/bin/env python3
"""Nomenclature (BOM) : docs/bom.csv → tableaux et totaux de docs/bom.md.

    python tools/bom.py          # régénère la partie chiffrée de docs/bom.md
    python tools/bom.py --check  # vérifie qu'elle est à jour (tests)

Les prix sont des relevés datés, pas des engagements : la partie générée
évite seulement les erreurs de recopie et d'addition.
"""
import csv
import sys
from collections import OrderedDict
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / 'docs' / 'bom.csv'
MD = ROOT / 'docs' / 'bom.md'
DEBUT, FIN = '<!-- BOM:DEBUT (généré par tools/bom.py) -->', '<!-- BOM:FIN -->'

STATUTS = OrderedDict([
    ('ferme', 'À commander'),
    ('option', 'Options'),
    ('outil', 'Outillage de mesure'),
    ('conditionnel', 'Seulement si la caméra ne voit pas l’infrarouge'),
])
COLONNES = ['id', 'statut', 'marchand', 'reference', 'designation', 'qte',
            'prix_unitaire_ttc', 'url', 'stock_releve', 'role']


def lire(chemin=CSV):
    with open(chemin, encoding='utf-8', newline='') as f:
        lignes = list(csv.DictReader(f, delimiter=';'))
    for n, l in enumerate(lignes, 2):
        if list(l) != COLONNES:
            raise ValueError(f'{chemin.name}:{n} colonnes inattendues')
        if l['statut'] not in STATUTS:
            raise ValueError(f'{chemin.name}:{n} statut inconnu {l["statut"]!r}')
        if not l['url'].startswith('https://'):
            raise ValueError(f'{chemin.name}:{n} URL non HTTPS')
        l['qte'] = int(l['qte'])
        l['prix'] = Decimal(l['prix_unitaire_ttc'])
        if l['qte'] <= 0 or l['prix'] <= 0:
            raise ValueError(f'{chemin.name}:{n} quantité ou prix invalide')
        l['total'] = l['prix'] * l['qte']
    ids = [l['id'] for l in lignes]
    if len(ids) != len(set(ids)):
        raise ValueError('identifiants en double dans bom.csv')
    return lignes


def eur(x):
    return f'{x:.2f}'.replace('.', ',') + ' €'


def totaux(lignes):
    par = OrderedDict()
    for l in lignes:
        cle = (l['statut'], l['marchand'])
        par[cle] = par.get(cle, Decimal(0)) + l['total']
    return par


def generer(lignes):
    out = [DEBUT, '']
    for statut, titre in STATUTS.items():
        sel = [l for l in lignes if l['statut'] == statut]
        if not sel:
            continue
        out += [f'### {titre}', '',
                '| Marchand | Réf. | Article | Qté | Prix unit. TTC | Total | Stock relevé | Rôle |',
                '|---|---|---|---:|---:|---:|---|---|']
        for l in sel:
            out.append(f"| {l['marchand']} | [{l['reference']}]({l['url']}) | {l['designation']} | "
                       f"{l['qte']} | {eur(l['prix'])} | {eur(l['total'])} | {l['stock_releve']} | {l['role']} |")
        out.append('')
    t = totaux(lignes)
    out += ['### Totaux (TTC, hors frais de port)', '',
            '| Statut | Marchand | Total |', '|---|---|---:|']
    for (statut, marchand), v in t.items():
        out.append(f'| {STATUTS[statut]} | {marchand} | {eur(v)} |')
    ferme = sum((v for (s, _), v in t.items() if s == 'ferme'), Decimal(0))
    out += ['', f'**Total à commander : {eur(ferme)} TTC hors port**, '
                f'soit {sum(1 for l in lignes if l["statut"] == "ferme")} lignes.', '', FIN]
    return '\n'.join(out)


def section_actuelle(texte):
    i, j = texte.find(DEBUT), texte.find(FIN)
    if i < 0 or j < i:
        raise ValueError('marqueurs BOM absents de docs/bom.md')
    return i, j + len(FIN)


def main(argv):
    lignes = lire()
    texte = MD.read_text(encoding='utf-8')
    i, j = section_actuelle(texte)
    attendu = generer(lignes)
    if '--check' in argv:
        if texte[i:j] != attendu:
            print('docs/bom.md n’est pas à jour : lancer python tools/bom.py')
            return 1
        print('BOM à jour')
        return 0
    MD.write_text(texte[:i] + attendu + texte[j:], encoding='utf-8')
    print('docs/bom.md régénéré')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
