#!/usr/bin/env python3
"""Dimensionnement indicatif V1 archivé, pas une validation V3 ni un firmware."""
import argparse
import json
import math


def calcul(*, clips=100, duree_s=20, latence_s=3, actif_ma=350,
           veille_ma=5, propre_w=0.026, rendement_usb=0.85,
           capacite_wh=24.12, fraction_utile=0.8, panneau_w=2,
           rendement_solaire=0.5, hsp=1, ombre=1):
    valeurs = locals().copy()
    for nom, valeur in valeurs.items():
        if not isinstance(valeur, (int, float)) or not math.isfinite(valeur) or valeur < 0:
            raise ValueError(f"{nom}: valeur finie positive ou nulle attendue")
    for nom in ('rendement_usb', 'fraction_utile', 'rendement_solaire'):
        if not 0 < valeurs[nom] <= 1:
            raise ValueError(f"{nom}: attendu dans ]0, 1]")
    if not 0 <= ombre <= 1 or hsp > 24:
        raise ValueError('ombre dans [0, 1], hsp dans [0, 24]')
    if not isinstance(clips, int):
        raise ValueError('clips doit être entier')
    secondes_actives = clips * (duree_s + latence_s)
    if secondes_actives > 86400:
        raise ValueError('temps actif supérieur à une journée')
    charge_wh = 5 * (actif_ma * secondes_actives + veille_ma * (86400 - secondes_actives)) / 3600000
    propre_wh = propre_w * 24
    besoin_wh = charge_wh / rendement_usb + propre_wh
    gain_par_hsp = panneau_w * rendement_solaire * ombre
    solaire_wh = gain_par_hsp * hsp
    reserve_wh = capacite_wh * fraction_utile
    deficit_wh = besoin_wh - solaire_wh
    return {
        'actif_s_j': secondes_actives, 'charge_usb_wh_j': charge_wh,
        'propre_wh_j': propre_wh, 'besoin_cellule_wh_j': besoin_wh,
        'solaire_cellule_wh_j': solaire_wh, 'bilan_wh_j': -deficit_wh,
        'hsp_min': besoin_wh / gain_par_hsp if gain_par_hsp else None,
        'reserve_wh': reserve_wh,
        'jours_sans_soleil': reserve_wh / besoin_wh if besoin_wh else None,
        'jours_avant_reserve_epuisee': reserve_wh / deficit_wh if deficit_wh > 0 else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--clips', type=int, default=100)
    parser.add_argument('--hsp', type=float, default=1)
    parser.add_argument('--ombre', type=float, default=1, help='fraction solaire restante, 0 à 1')
    parser.add_argument('--veille-ma', type=float, default=5)
    parser.add_argument('--propre-w', type=float, default=0.026)
    parser.add_argument('--panneau-w', type=float, default=2)
    args = parser.parse_args()
    try:
        resultat = calcul(**vars(args))
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(resultat, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
