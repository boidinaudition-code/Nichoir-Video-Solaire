#!/usr/bin/env python3
"""Plan du nichoir en bois : cotes, débit et dessins SVG (bibliothèque standard).

Toutes les cotes sont en millimètres. Repère :
  x : largeur, de la face sud (x=0, côté bas du toit) à la face nord (x=180) ;
  y : profondeur, de la façade est (y=0, trou d'envol) au dos ouest (y=180) ;
  z : hauteur, depuis le dessous du fond (z=0).
Le toit monopente descend vers le sud à 45° ; la pente est donc visible de face.

Usage : python tools/plan_nichoir.py        (régénère docs/plans/)
        python tools/plan_nichoir.py --check (vérifie sans écrire)
"""
import argparse
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SORTIE = ROOT / 'docs' / 'plans'

# --- Paramètres --------------------------------------------------------------
E = 20                    # épaisseur des planches (LPO : 2 cm conseillé)
INT = 140                 # fond intérieur 14 × 14 cm (charbonnière, LPO)
H_CHAMBRE = 230           # hauteur intérieure 23 cm (LPO)
TROU = 32                 # charbonnière 32 mm ; 28 mm pour réserver aux mésanges bleues
TROU_AXE = 170            # axe du trou au-dessus du dessus du fond (LPO : 17 cm)
PENTE = 45                # degrés
H_SUD = 310               # hauteur extérieure de la façade côté sud (bas du toit)
JEU_PORTE = 3             # côté sud raccourci pour pivoter sous le toit
JEU_LATERAL = 1           # jeu de la porte de chaque côté (bois qui gonfle)
Z_PIVOT = 290             # axe des vis pivots de la porte, à E/2 du bord sud
TRAPPE = (70, 150, 285, 345)  # trappe technique en FAÇADE : x de 70 à 150, z de 285 à 345
MARGE_PLAQUE = 10            # la plaque de fermeture déborde de 10 tout autour
AERATION_FACADE = (145, 400)  # trous Ø8 grillagés (x, z)
AERATION_DOS = (60, 330)
Z_BLOC_HAUT = 190 + 45        # haut du bloc d'entrée (90 × 90 centré sur le trou)
MARGE_DEBIT = 40          # équerrage et reprises
TOIT_L, TOIT_P = 300, 250  # toit : longueur dans la pente × largeur (est-ouest)
DEBORD_SUD = 30           # débord du toit en bas de pente
PANNEAU = (274, 223, 4)   # Voltaic P110 : long, large, épaisseur
CALE_PANNEAU = 10         # entretoises sous le panneau
TRAIT_SCIE = 3

EXT = INT + 2 * E                         # 180 : largeur et profondeur extérieures
Z_FOND = E                                # dessus du fond
Z_PLAFOND = Z_FOND + H_CHAMBRE            # 250 : dessous de la cloison
Z_CLOISON = Z_PLAFOND + E                 # 270 : dessus de la cloison
Z_TROU = Z_FOND + TROU_AXE                # 190
T = math.tan(math.radians(PENTE))


def z_toit(x):
    """Dessous du toit à l'abscisse x (plan passant par les arêtes hautes extérieures)."""
    return H_SUD + x * T


H_NORD = z_toit(EXT)                      # 490


def angle_ouverture_porte():
    """Angle (degrés) auquel la porte sud touche l'arête du débord sud du toit."""
    u = math.radians(PENTE)
    ex, ez = -DEBORD_SUD * math.cos(u), H_SUD - DEBORD_SUD * math.sin(u)   # arête basse du toit
    xp, zp = E / 2, Z_PIVOT
    h = z_toit(E) - JEU_PORTE
    for deg in range(0, 91):
        a = math.radians(deg)
        # point de l'arête ramené dans le repère de la porte (rotation inverse)
        dx, dz = ex - xp, ez - zp
        x = xp + dx * math.cos(a) - dz * math.sin(a)
        z = zp + dx * math.sin(a) + dz * math.cos(a)
        if 0 <= x <= E and 0 <= z <= h:
            return deg
    return 90


def x_max_porte_ouverte():
    """Abscisse maximale atteinte par le haut de la porte pendant l'ouverture."""
    xp, zp = E / 2, Z_PIVOT
    coins = [(0, H_SUD - JEU_PORTE), (E, z_toit(E) - JEU_PORTE)]
    xmax = 0
    for deg10 in range(0, angle_ouverture_porte() * 10 + 1):
        a = math.radians(deg10 / 10)
        for x, z in coins:
            xmax = max(xmax, xp + (x - xp) * math.cos(a) + (z - zp) * math.sin(a))
    return xmax


def pieces():
    """Liste des pièces finies. 'h_haute'/'h_basse' : biseau à 45° en tête."""
    return [
        dict(nom='Façade (est)', qte=1, l=EXT, h=H_NORD, ep=E,
             note=f'trapèze : {H_SUD:g} côté sud, {H_NORD:g} côté nord ; trou Ø{TROU} axe à {Z_TROU} du bas ; trappe technique et aération'),
        dict(nom='Dos (ouest)', qte=1, l=EXT, h=H_NORD, ep=E,
             note='même trapèze que la façade ; aération ; côté support, rien ne dépasse'),
        dict(nom='Côté sud (porte pivotante)', qte=1, l=INT - 2 * JEU_LATERAL, h=z_toit(E) - JEU_PORTE, ep=E,
             note=f'biseau 45° en tête : {z_toit(E) - JEU_PORTE:g} face intérieure, {H_SUD - JEU_PORTE:g} face extérieure'),
        dict(nom='Côté nord', qte=1, l=INT, h=H_NORD, ep=E,
             note=f'biseau 45° en tête : {H_NORD:g} face extérieure, {z_toit(EXT - E):g} face intérieure ; passe-câble vers la batterie'),
        dict(nom='Fond', qte=1, l=INT, h=INT, ep=E, note='4 trous Ø5 près des angles'),
        dict(nom='Cloison (plafond de la chambre)', qte=1, l=INT, h=INT, ep=E,
             note='passages caméra, LED IR et micro'),
        dict(nom='Toit', qte=1, l=TOIT_L, h=TOIT_P, ep=E,
             note='panneau 250 de large : planche large ou deux planches collées, couverture étanche'),
        dict(nom='Bloc d’entrée', qte=1, l=90, h=90, ep=E,
             note=f'trou Ø{TROU} aligné ; logement de la barrière IR'),
        dict(nom='Plaque de trappe', qte=1, l=TRAPPE[1] - TRAPPE[0] + 2 * MARGE_PLAQUE,
             h=TRAPPE[3] - TRAPPE[2] + 2 * MARGE_PLAQUE, ep=10,
             note='contreplaqué marine ou planche de 10 ; encoche 6 × 6 en bas pour le câble de la barrière'),
        dict(nom='Barre de fixation', qte=1, l=40, h=600, ep=E, note='vissée au milieu du dos (LPO)'),
    ]


def debit():
    """Débit dans une planche brute de 20 × 180 mm minimum, plus le toit à part.

    Façade et dos : un seul flan 180 × (H_SUD + H_NORD), coupé en diagonale à 45°.
    """
    flan = H_SUD + H_NORD + TRAIT_SCIE * math.sqrt(2)  # trait de scie d'une coupe à 45°
    p = {x['nom']: x for x in pieces()}
    autres = [p['Côté sud (porte pivotante)']['h'], p['Côté nord']['h'],
              p['Fond']['h'], p['Cloison (plafond de la chambre)']['h'], 90]
    longueur = flan + sum(autres) + TRAIT_SCIE * len(autres) + MARGE_DEBIT
    plaque = p['Plaque de trappe']
    return dict(flan_facade_dos=math.ceil(flan), longueur_planche_180=math.ceil(longueur),
                planche_toit=(TOIT_L, TOIT_P), barre=(40, 600), plaque_10mm=(plaque['l'], plaque['h']))


def verifications():
    """Contrôles chiffrés : retourne une liste de (libellé, ok, détail)."""
    res = []
    res.append(('Fond intérieur ≥ 12 × 12 cm (LPO)', INT >= 120, f'{INT} × {INT}'))
    res.append(('Hauteur intérieure 23 cm (LPO)', Z_PLAFOND - Z_FOND == 230, f'{Z_PLAFOND - Z_FOND}'))
    bas_trou = Z_TROU - TROU / 2 - Z_FOND
    res.append(('Bas du trou ≥ 15 cm au-dessus du fond (LPO)', bas_trou >= 150, f'{bas_trou:g}'))
    res.append(('Trou sous la cloison', Z_TROU + TROU / 2 < Z_PLAFOND - 20,
                f'haut du trou {Z_TROU + TROU / 2:g}, cloison {Z_PLAFOND}'))
    res.append(('Trou dans la façade côté sud (hauteur mini)', Z_TROU + TROU / 2 < H_SUD, ''))
    tech_sud = z_toit(E) - Z_CLOISON
    res.append(('Compartiment technique ≥ 40 mm au point bas', tech_sud >= 40, f'{tech_sud:g}'))
    res.append(('Pivot de la porte entre cloison et toit', Z_CLOISON < Z_PIVOT < H_SUD - JEU_PORTE - 10,
                f'pivot {Z_PIVOT}, cloison {Z_CLOISON}, haut de porte {H_SUD - JEU_PORTE}'))
    x1, x2, z1, z2 = TRAPPE
    res.append(('Trappe technique en façade, au-dessus de la cloison, ≥ 25 de bois sous le toit',
                E < x1 < x2 < EXT - E and z1 > Z_CLOISON + 5 and z2 <= z_toit(x1) - 25,
                f'{x2 - x1} × {z2 - z1}, haut {z2}, toit à {z_toit(x1):g} au-dessus'))
    m = MARGE_PLAQUE
    res.append(('Plaque de trappe sous le débord du toit et au-dessus du bloc d’entrée',
                z2 + m <= z_toit(x1 - m) - 10 and z1 - m > Z_BLOC_HAUT and x2 + m <= EXT,
                f'plaque {x2 - x1 + 2 * m} × {z2 - z1 + 2 * m}, de x {x1 - m} à {x2 + m}, z {z1 - m} à {z2 + m}'))
    xm = x_max_porte_ouverte()
    for nom, (xa, za) in {'façade': AERATION_FACADE, 'dos': AERATION_DOS}.items():
        ok = E + 4 < xa < EXT - E - 4 and Z_CLOISON + 4 < za < z_toit(xa) - 15
        if nom == 'façade':
            ok = ok and not (x1 - m - 4 < xa < x2 + m + 4 and z1 - m - 4 < za < z2 + m + 4)
        res.append((f'Aération Ø8 du {nom} dans le compartiment, sous le toit', ok, f'x {xa}, z {za}'))
    res.append(('Trappe et plaque hors de la zone balayée par la porte', x1 - m > xm + 5,
                f'porte jusqu’à x {xm:.1f}, plaque dès x {x1 - m}'))
    a = angle_ouverture_porte()
    res.append(('Porte ouvrable d’au moins 60°', a >= 60, f'butée sur le débord du toit vers {a}°'))
    pente_box = EXT / math.cos(math.radians(PENTE))
    debord_nord = TOIT_L - DEBORD_SUD - pente_box
    res.append(('Toit couvre la boîte dans la pente', debord_nord >= 10,
                f'longueur boîte {pente_box:.1f}, débords sud {DEBORD_SUD} / nord {debord_nord:.1f}'))
    res.append(('Toit déborde à l’est et à l’ouest', TOIT_P > EXT, f'{(TOIT_P - EXT) / 2:g} de chaque côté'))
    ml, mp = (TOIT_L - PANNEAU[0]) / 2, (TOIT_P - PANNEAU[1]) / 2
    res.append(('Panneau P110 entièrement sur le toit', ml >= 10 and mp >= 10,
                f'marges {ml:g} (pente) et {mp:g} (largeur)'))
    return res


# --- SVG ---------------------------------------------------------------------
STYLE = ('<style>text{font-family:sans-serif;font-size:9px;fill:#222}'
         '.t{font-size:12px;font-weight:bold}.bois{fill:#e8cfa0;stroke:#5a3d1a;stroke-width:1}'
         '.vide{fill:#fff;stroke:#5a3d1a;stroke-width:1}.cache{fill:none;stroke:#5a3d1a;stroke-dasharray:4 3}'
         '.pv{fill:#25456b;stroke:#111}.cote{stroke:#c0392b;stroke-width:.6;fill:none}'
         '.cotet{fill:#c0392b}.trou{fill:#fff;stroke:#111}</style>')


def svg(w, h, corps, titre):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" '
            f'viewBox="0 0 {w} {h}">{STYLE}<rect width="{w}" height="{h}" fill="#fff"/>'
            f'<text class="t" x="10" y="16">{titre}</text>{corps}</svg>\n')


def cote(x1, y1, x2, y2, texte, d=0):
    """Ligne de cote avec texte au milieu ; d décale le texte."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    return (f'<line class="cote" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'
            f'<text class="cotet" x="{mx + d:.1f}" y="{my - 2:.1f}" text-anchor="middle">{texte}</text>')


def poly(points, cls):
    return f'<polygon class="{cls}" points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in points)}"/>'


def vue_facade():
    """Élévation de la façade est, avec intérieur en pointillés, toit et panneau."""
    ox, oy = 90, 620          # origine (x=0, z=0) dans le dessin
    P = lambda x, z: (ox + x, oy - z)
    c = []
    c.append(poly([P(0, 0), P(EXT, 0), P(EXT, H_NORD), P(0, H_SUD)], 'bois'))
    # intérieur caché : chambre, fond, cloison
    for x1, z1, x2, z2 in [(E, 0, EXT - E, Z_FOND), (E, Z_PLAFOND, EXT - E, Z_CLOISON)]:
        (a, b), (cx, d) = P(x1, z2), P(x2, z1)
        c.append(f'<rect class="cache" x="{a}" y="{b}" width="{cx - a}" height="{d - b}"/>')
    c.append(f'<line class="cache" x1="{P(E,0)[0]}" y1="{P(E,0)[1]}" x2="{P(E,z_toit(E))[0]}" y2="{P(E,z_toit(E))[1]:.1f}"/>')
    c.append(f'<line class="cache" x1="{P(EXT-E,0)[0]}" y1="{P(EXT-E,0)[1]}" x2="{P(EXT-E,z_toit(EXT-E))[0]}" y2="{P(EXT-E,z_toit(EXT-E))[1]:.1f}"/>')
    tx, tz = P(EXT / 2, Z_TROU)
    c.append(f'<circle class="trou" cx="{tx}" cy="{tz}" r="{TROU / 2}"/>')
    c.append(f'<rect fill="none" stroke="#5a3d1a" x="{tx - 45}" y="{tz - 45}" width="90" height="90"/>')
    x1, x2, z1, z2 = TRAPPE
    m = MARGE_PLAQUE
    (a1, b1), (a2, b2) = P(x1 - m, z2 + m), P(x2 + m, z1 - m)
    c.append(f'<rect fill="#d9b980" stroke="#5a3d1a" x="{a1}" y="{b1}" width="{a2 - a1}" height="{b2 - b1}"/>')
    (a1, b1), (a2, b2) = P(x1, z2), P(x2, z1)
    c.append(f'<rect class="cache" x="{a1}" y="{b1}" width="{a2 - a1}" height="{b2 - b1}"/>')
    c.append(f'<text x="{a1 + 4}" y="{(b1 + b2) / 2 + 3}">trappe</text>')
    # toit (dessous sur le plan z = H_SUD + x), épaisseur E vers le haut
    u = (math.cos(math.radians(PENTE)), math.sin(math.radians(PENTE)))
    n = (-u[1], u[0])
    base = (0 - DEBORD_SUD * u[0], H_SUD - DEBORD_SUD * u[1])
    a = base
    b = (a[0] + TOIT_L * u[0], a[1] + TOIT_L * u[1])
    c.append(poly([P(*a), P(*b), P(b[0] + E * n[0], b[1] + E * n[1]), P(a[0] + E * n[0], a[1] + E * n[1])], 'bois'))
    off = E + CALE_PANNEAU
    m = (TOIT_L - PANNEAU[0]) / 2
    pa = (a[0] + m * u[0] + off * n[0], a[1] + m * u[1] + off * n[1])
    pb = (pa[0] + PANNEAU[0] * u[0], pa[1] + PANNEAU[0] * u[1])
    c.append(poly([P(*pa), P(*pb), P(pb[0] + PANNEAU[2] * n[0], pb[1] + PANNEAU[2] * n[1]),
                   P(pa[0] + PANNEAU[2] * n[0], pa[1] + PANNEAU[2] * n[1])], 'pv'))
    # cotes
    c.append(cote(*P(0, -25), *P(EXT, -25), f'{EXT}'))
    c.append(cote(*P(-30, 0), *P(-30, H_SUD), f'{H_SUD}', -14))
    c.append(cote(*P(EXT + 30, 0), *P(EXT + 30, H_NORD), f'{H_NORD:g}', 16))
    c.append(cote(*P(EXT - E - 8, Z_FOND), *P(EXT - E - 8, Z_PLAFOND), f'{H_CHAMBRE}', -14))
    c.append(cote(*P(E + 8, Z_FOND), *P(E + 8, Z_TROU), f'axe {TROU_AXE}', 20))
    c.append(f'<line class="cote" x1="{P(E + 8, Z_TROU)[0]}" y1="{P(0, Z_TROU)[1]}" x2="{tx}" y2="{tz}"/>')
    t = [f'Trou Ø{TROU} (28 pour la mésange bleue)', 'Bloc d’entrée 90 × 90 devant le trou', f'Trappe technique {TRAPPE[1] - TRAPPE[0]} × {TRAPPE[3] - TRAPPE[2]} (pointillés) sous sa plaque',
         f'Chambre {INT} × {INT} × {H_CHAMBRE}', f'Cloison {Z_PLAFOND}–{Z_CLOISON}, compartiment technique au-dessus',
         f'Toit {TOIT_L} × {TOIT_P}, pente {PENTE}°, panneau P110 sur cales {CALE_PANNEAU}',
         'Sud à gauche (bas du toit), nord à droite']
    for i, s in enumerate(t):
        c.append(f'<text x="340" y="{360 + 14 * i}">{s}</text>')
    return svg(640, 660, ''.join(c), 'Vue de face (façade est) — cotes en mm')


def vue_debit():
    """Débit : flan façade + dos coupé à 45°, puis pièces de 140 de large."""
    c, y0 = [], 40
    flan = H_SUD + H_NORD
    flan_reel = debit()['flan_facade_dos']
    s = 0.6  # échelle
    X = lambda v: 20 + v * s
    c.append(f'<text x="20" y="{y0 - 6}">Planche 20 × 180 (mini) — façade + dos dans un flan de 180 × {flan_reel}, une coupe à 45°</text>')
    c.append(poly([(X(0), y0), (X(H_SUD), y0), (X(H_NORD), y0 + EXT * s), (X(0), y0 + EXT * s)], 'bois'))
    c.append(poly([(X(H_SUD), y0), (X(flan), y0), (X(flan), y0 + EXT * s), (X(H_NORD), y0 + EXT * s)], 'bois'))
    c.append(f'<text x="{X(120)}" y="{y0 + 60}">Façade</text><text x="{X(600)}" y="{y0 + 60}">Dos</text>')
    c.append(cote(X(0), y0 + EXT * s + 12, X(flan), y0 + EXT * s + 12, f'{flan_reel} (trait de scie à 45° compris)'))
    y1 = y0 + EXT * s + 50
    x = 0
    c.append(f'<text x="20" y="{y1 - 6}">Pièces refendues : porte sud à 138, les autres à 140</text>')
    for p in pieces()[2:6]:
        w = p['h'] * s
        c.append(f'<rect class="bois" x="{X(x)}" y="{y1}" width="{w:.1f}" height="{INT * s}"/>')
        c.append(f'<text x="{X(x) + 3}" y="{y1 + 14}">{p["nom"].split(" (")[0]}</text>')
        c.append(f'<text x="{X(x) + 3}" y="{y1 + 26}">{p["l"]:g} × {p["h"]:g}</text>')
        x += p['h'] + TRAIT_SCIE
    d = debit()
    c.append(f'<text x="20" y="{y1 + INT * s + 26}">Longueur totale de planche 180 : ≈ {d["longueur_planche_180"]} mm (bloc d’entrée compris), + toit {TOIT_L} × {TOIT_P} et barre 40 × 600 ; plaque de trappe {d["plaque_10mm"][0]} × {d["plaque_10mm"][1]} en 10 mm.</text>')
    return svg(740, int(y1 + INT * s + 50), ''.join(c), 'Débit des pièces — cotes en mm')


def vue_cloison():
    """Cloison vue de dessus : caméra, LED IR, micro."""
    o, c = 40, []
    c.append(f'<rect class="bois" x="{o}" y="{o}" width="{INT}" height="{INT}"/>')
    m = o + INT / 2
    c.append(f'<circle class="trou" cx="{m}" cy="{m}" r="7"/><text x="{m + 10}" y="{m + 3}">objectif Ø14 (à ajuster)</text>')
    for dx, dy in [(-30, -30), (30, -30), (-30, 30), (30, 30)]:
        c.append(f'<circle class="trou" cx="{m + dx}" cy="{m + dy}" r="2.75"/>')
    c.append(f'<circle class="trou" cx="{m + 45}" cy="{m - 55}" r="2"/><text x="{m + 20}" y="{o - 6}">micro Ø4, position selon la carte</text>')
    c.append(f'<text x="{o}" y="{o + INT + 16}">4 LED IR Ø5,5 sur un carré de 60</text>')
    c.append(cote(o, o + INT + 30, o + INT, o + INT + 30, f'{INT}'))
    return svg(260, 250, ''.join(c), 'Cloison vue de dessus')


def vue_toit():
    """Toit vu de dessus avec l'emprise du panneau."""
    s, o, c = 0.8, 30, []
    c.append(f'<rect class="bois" x="{o}" y="{o}" width="{TOIT_L * s}" height="{TOIT_P * s}"/>')
    ml, mp = (TOIT_L - PANNEAU[0]) / 2, (TOIT_P - PANNEAU[1]) / 2
    c.append(f'<rect class="pv" x="{o + ml * s}" y="{o + mp * s}" width="{PANNEAU[0] * s}" height="{PANNEAU[1] * s}"/>')
    c.append(cote(o, o + TOIT_P * s + 14, o + TOIT_L * s, o + TOIT_P * s + 14, f'{TOIT_L} (dans la pente, sud → nord)'))
    c.append(cote(o + TOIT_L * s + 14, o, o + TOIT_L * s + 14, o + TOIT_P * s, f'{TOIT_P}', 14))
    c.append(f'<text x="{o + 10}" y="{o + TOIT_P * s / 2}" fill="#fff" style="fill:#fff">P110 {PANNEAU[0]} × {PANNEAU[1]}, marges {ml:g} et {mp:g}</text>')
    return svg(320, 260, ''.join(c), 'Toit vu de dessus')


def fichiers():
    return {'vue-facade.svg': vue_facade(), 'debit.svg': vue_debit(),
            'cloison.svg': vue_cloison(), 'toit.svg': vue_toit()}


def main():
    ap = argparse.ArgumentParser(description='Plan du nichoir en bois')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    ko = [v for v in verifications() if not v[1]]
    for lib, ok, det in verifications():
        print(('OK ' if ok else 'KO ') + lib + (f' — {det}' if det else ''))
    print('Débit :', debit())
    ecart = []
    for nom, contenu in fichiers().items():
        f = SORTIE / nom
        if a.check:
            if not f.exists() or f.read_text(encoding='utf-8') != contenu:
                ecart.append(nom)
        else:
            SORTIE.mkdir(parents=True, exist_ok=True)
            f.write_text(contenu, encoding='utf-8')
    if ecart:
        print('SVG à régénérer :', ', '.join(ecart))
    sys.exit(1 if ko or ecart else 0)


if __name__ == '__main__':
    main()
