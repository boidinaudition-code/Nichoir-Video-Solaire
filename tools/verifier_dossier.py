#!/usr/bin/env python3
"""Vérification des calculs V1 archivés et des liens, sans validation matérielle."""
import re
from decimal import Decimal
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    from .dimensionnement import calcul
except ImportError:
    from dimensionnement import calcul


ROOT = Path(__file__).resolve().parents[1]


def lignes_table(texte):
    return [tuple(c.strip().replace('**', '') for c in ligne.strip('|').split('|'))
            for ligne in texte.splitlines() if ligne.startswith('|')]


def euros(texte):
    return Decimal(texte.replace(',', '.'))


def verifier(root=ROOT):
    root = Path(root).resolve()
    erreurs = []
    rapports = []

    def exiger(condition, message):
        if not condition:
            erreurs.append(message)

    requis = ['README.md', '.gitignore', 'tools/dimensionnement.py',
              'tools/verifier_dossier.py', 'tests/test_dimensionnement.py']
    requis += ['docs/archive/v1/README-v1.md']
    requis += [f'docs/archive/v1/{nom}.md' for nom in
               ('architecture', 'cablage', 'bois', 'energie', 'capture', 'essais',
                'sources', 'revue')]
    for nom in requis:
        exiger((root / nom).is_file(), f'Fichier manquant : {nom}')
    if erreurs:
        return erreurs, rapports

    archive = root / 'docs/archive/v1'
    readme = (archive / 'README-v1.md').read_text(encoding='utf-8')
    energie = (archive / 'energie.md').read_text(encoding='utf-8')
    exiger(readme.splitlines()[0] == '# Nichoir vidéo solaire — conception V1',
           'Titre de l’archive V1 inattendu')
    exiger((root / 'README.md').read_text(encoding='utf-8').splitlines()[0]
           == '# Nichoir vidéo solaire', 'Titre public inattendu')

    locaux = externes = 0
    for fichier in [root / 'README.md', *sorted((root / 'docs').rglob('*.md'))]:
        texte = fichier.read_text(encoding='utf-8')
        # Liens inline du dossier ; les URL nues ne sont pas téléchargées non plus.
        liens = re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', texte)
        nus = re.findall(r'https?://[^\s<>`)]+', texte)
        for cible in dict.fromkeys(liens + [u.rstrip('.,;') for u in nus]):
            url = urlsplit(cible)
            if url.scheme or url.netloc:
                externes += 1
                exiger(url.scheme == 'https' and bool(url.hostname)
                       and not url.username and not url.password,
                       f'URL HTTPS invalide dans {fichier.name} : {cible}')
            else:
                locaux += 1
                chemin = (fichier.parent / unquote(url.path)).resolve() if url.path else fichier
                exiger(chemin.is_relative_to(root) and chemin.is_file(),
                       f'Lien local absent/hors dépôt dans {fichier.name} : {cible}')
                # Le dossier ne contient pas de liens à ancre : refuser plutôt
                # que prétendre avoir validé un fragment non contrôlé.
                exiger(not url.fragment and not url.query,
                       f'Fragment/requête locale non pris en charge : {cible}')
    rapports.append(f'Liens : {locaux} locaux, {externes} externes (syntaxe uniquement, sans HTTP)')

    lignes = lignes_table(readme)
    debut = next(i for i, r in enumerate(lignes) if r[0].startswith('Élément /'))
    fin = next(i for i, r in enumerate(lignes) if r[0] == 'Total complet prévisionnel')
    achats = lignes[debut + 2:fin]
    exiger(len(achats) == 15, 'BOM : 15 lignes d’achat attendues')
    fixe = Decimal(0)
    mini = Decimal(0)
    maxi = Decimal(0)
    for ligne in achats:
        prix = ligne[1]
        if not re.fullmatch(r'\d+(?:,\d{2})?(?:–\d+(?:,\d{2})?)?', prix):
            erreurs.append(f'Prix BOM invalide : {prix}')
            continue
        bornes = [euros(p) for p in prix.split('–')]
        exiger(bornes[0] <= bornes[-1], f'Intervalle BOM inversé : {prix}')
        mini += bornes[0]
        maxi += bornes[-1]
        if len(bornes) == 1:
            fixe += bornes[0]
    annonce = '–'.join(f'{p:.2f}'.replace('.', ',') for p in (mini, maxi))
    exiger(lignes[fin][1] == annonce, f'Total BOM erroné : attendu {annonce}')
    # Les prix HT sont ceux du dossier, pas un nouveau panier marchand.
    for reference, ht in (('V25 KW-2655', '43.99'), ('P126 KW-3001', '20.49'),
                           ('Joint de fixation P126', '3.29')):
        ligne = next(r for r in achats if reference in r[0])
        ttc = (Decimal(ht) * Decimal('1.20')).quantize(Decimal('0.01'))
        exiger(euros(ligne[1]) == ttc, f'Conversion TVA incorrecte : {reference}')
    rapports.append(f'BOM : fixe {fixe:.2f} €, total {mini:.2f}–{maxi:.2f} € TTC hors port')

    scenarios = [calcul(clips=n) for n in (10, 100, 500)]
    scenarios.append(calcul(clips=1, duree_s=86400, latence_s=0, actif_ma=140))
    cles = ['actif_s_j', 'charge_usb_wh_j', 'propre_wh_j', 'besoin_cellule_wh_j',
            'bilan_wh_j', 'hsp_min', 'jours_sans_soleil', 'jours_avant_reserve_epuisee']
    details = [r for r in lignes_table(energie)
               if r[0] in ('10 clips de20 s', '100 clips de20 s', '500 clips de20 s', 'Continu140 mA')]
    synthese = [r for r in lignes if r[0] in
                ('10 clips/j', '100 clips/j', '500 clips/j', 'Continu 140 mA, comparaison')]
    exiger(len(details) == len(synthese) == 4, 'Quatre scénarios attendus dans chaque tableau énergie')
    for numero, (r, detail, resume) in enumerate(zip(scenarios, details, synthese), 1):
        attendu = [str(r[cles[0]])] + [f'{r[k]:.{2 if k.startswith("jours_") else 3}f}'.replace('.', ',')
                                       for k in cles[1:]]
        exiger(list(detail[1:]) == attendu, f'Énergie détaillée : scénario {numero} erroné')
        court = [f'{r[k]:.{2 if k.startswith("jours_") else 3}f}'.replace('.', ',')
                 for k in ('besoin_cellule_wh_j', 'hsp_min', 'jours_sans_soleil')]
        exiger(list(resume[1:]) == court, f'Énergie README : scénario {numero} erroné')
        # Recalcul indépendant de la fonction, pour ne pas comparer seulement
        # le document à une éventuelle régression du même modèle.
        actif = (10, 100, 500)[numero - 1] * 23 if numero < 4 else 86400
        courant = 350 if numero < 4 else 140
        usb = Decimal(5) * (courant * actif + 5 * (86400 - actif)) / Decimal(3600000)
        besoin = usb / Decimal('0.85') + Decimal('0.026') * 24
        exiger(abs(r['besoin_cellule_wh_j'] - float(besoin)) < 1e-10,
               f'Formule énergie : scénario {numero} incohérent')
    exiger(abs(calcul()['reserve_wh'] - 19.296) < 1e-10, 'Réserve énergétique incohérente')
    exiger(calcul(ombre=0)['hsp_min'] is None, 'Ombre totale : seuil impossible attendu')
    exiger(calcul(ombre=0.5)['hsp_min'] == 2 * calcul()['hsp_min'],
           'Ombre 50 % : seuil doublé attendu')
    rapports.append('Calculs : quatre scénarios README/énergie, TVA, réserve et ombre contrôlés')

    bois = (archive / 'bois.md').read_text(encoding='utf-8')
    geometrie = [
        (f'{250 - 20}', '230'),
        (f'{(200 - 136) / 2:g}', '32'),
        (f'{(230 - 112) / 2:g}', '59'),
        (f'{170 - 32 / 2:g}', '154'),
        (f'{310 + 30 * 20 / 180:.2f}'.replace('.', ','), '313,33'),
        (f'{310 + 30 * 160 / 180:.2f}'.replace('.', ','), '336,67'),
        (f'{310 + 30 * 20 / 170:.2f}'.replace('.', ','), '313,53'),
        (f'{310 + 30 * 150 / 170:.2f}'.replace('.', ','), '336,47'),
    ]
    for calcule, publie in geometrie:
        exiger(calcule == publie and publie in bois, f'Cote bois incohérente : {publie}')
    rapports.append('Bois : huit valeurs numériques recalculées et présentes dans le texte ; libellés, plan et montage non validés')
    return erreurs, rapports


def main():
    try:
        erreurs, rapports = verifier()
    except (ValueError, IndexError, StopIteration, OSError) as exc:
        print(f'ÉCHEC : dossier illisible ou structure inattendue : {exc}')
        return 1
    for rapport in rapports:
        print(rapport)
    for erreur in erreurs:
        print(f'ÉCHEC : {erreur}')
    if not erreurs:
        print('OK — cohérence locale uniquement ; matériel et liens distants non validés.')
    return int(bool(erreurs))


if __name__ == '__main__':
    raise SystemExit(main())
