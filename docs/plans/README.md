# Plans du nichoir en bois

[Accueil](../../README.md) · Générateur : [`tools/plan_nichoir.py`](../../tools/plan_nichoir.py)

Plan propre à ce projet : nichoir « boîte à lettres » de la LPO, agrandi pour loger l'électronique au-dessus de la chambre et porter le panneau solaire sur un toit à 45°. Cotes en mm. **Non encore construit** : faire un montage à blanc avant de visser.

Référence : les dimensions de la chambre et du trou suivent le [tableau de la LPO](https://www.lpo.fr/la-lpo-en-actions/mobilisation-citoyenne/refuges-lpo/tutoriels/nichoirs-pour-passereaux) et son [tuto PDF 2025](https://www.lpo.fr/media/read/47921/file/Nichoirs%20pour%20passereraux-mis%20%C3%A0%20jour%202025.pdf) (plans © LPO, consultables sur leur site, non recopiés ici). Pour un nichoir simple sans électronique, leur plan « boîte à lettres » suffit.

| Critère LPO | Ce plan |
|---|---|
| Fond intérieur ≥ 12 × 12 cm ; 14 × 14 cm pour la charbonnière | 140 × 140 |
| Hauteur intérieure 23 cm | 230 |
| Trou : 32 mm charbonnière, 26–28 mm mésange bleue | 32 (ou 28 pour réserver le nichoir aux petites mésanges) |
| Bas du trou ≥ 15 cm au-dessus du fond ; trou à 17 cm | axe à 170, bas du trou à 154 |
| Bois plein 2 cm, brut à l'intérieur, pas d'aggloméré | planche 20 mm, mélèze, pin ou chêne |
| 2 trous de 5 mm dans le fond | 4 trous Ø5 |
| Une partie amovible pour le nettoyage | côté sud pivotant |
| Trou à l'est ou au sud-est, jamais face aux vents dominants | façade est ; toit en pente vers le sud |

## Dessins

![Vue de face](vue-facade.svg)

![Débit](debit.svg)

![Cloison](cloison.svg) ![Toit](toit.svg)

## Liste des pièces

| Pièce | Qté | Cotes finies (mm) | Remarque |
|---|---:|---|---|
| Façade (est) | 1 | 180 de large, 310 côté sud → 490 côté nord | trapèze, trou Ø32 centré (axe à 190 du bas), trappe technique 80 × 60 |
| Dos (ouest) | 1 | même trapèze | aération ; côté support |
| Côté sud (porte) | 1 | 138 × 327, biseau 45° en tête (307 face extérieure) | 1 mm de jeu de chaque côté, raccourci de 3 mm pour pivoter sous le toit |
| Côté nord | 1 | 140 × 490, biseau 45° en tête (470 face intérieure) | passe-câble vers la batterie |
| Fond | 1 | 140 × 140 | 4 trous Ø5 près des angles |
| Cloison | 1 | 140 × 140 | dessous à 250 du bas : caméra, LED IR, micro |
| Toit | 1 | 300 dans la pente × 250 | planche large ou deux planches collées |
| Bloc d'entrée | 1 | 90 × 90 | trou Ø32 aligné, logement de la barrière IR |
| Plaque de trappe | 1 | 100 × 80 × 10 | contreplaqué marine ou planche de 10 ; vissée sur la façade, joint mousse ; encoche 6 × 6 en bas |
| Barre de fixation | 1 | 40 × 600 × 20 | verticale, vissée au milieu du dos |

Débit : une planche de 20 mm d'au moins 180 de large et environ **2,05 m** de long (traits de scie et équerrage compris), plus le toit, la barre et une chute de 10 mm pour la plaque de trappe. Façade et dos sortent d'un seul flan de 180 × 805 coupé en diagonale à 45°. Côté nord, fond et cloison sont refendus à 140, la porte sud à 138.

## Montage

1. **Débit.** Couper le flan 180 × 805 en diagonale (45°) : on obtient façade et dos. Refendre à 140 le côté nord, le fond et la cloison, à 138 la porte sud. Biseauter à 45° le haut des deux côtés.
2. **Trou d'envol.** Scie cloche Ø32 dans la façade : centré, axe à 190 du bas. Percer le bloc d'entrée au même diamètre. Rainures horizontales à l'intérieur sous le trou si le bois est lisse.
3. **Fond.** 4 trous Ø5. Laisser le bois brut à l'intérieur.
4. **Caisse.** Visser le côté nord, le fond (de 0 à 20) et la cloison (dessous à 250, cale de 230 posée sur le fond) entre façade et dos. Vis inox 4 × 40, avant-trous Ø3. Le fond et la cloison ne sont **pas** vissés au côté sud.
5. **Porte sud.** Deux vis pivots 4 × 40 à travers façade et dos, dans le chant de la porte, **à 290 du bas et à 10 du bord sud** (milieu de l'épaisseur) : au-dessus de la cloison, sous le toit. Une rondelle entre porte et façade, une entre porte et dos. En bas, un crochet ou une vis de blocage. La porte s'ouvre d'environ 70° avant de buter sur le débord du toit, assez pour nettoyer. Un joint mousse ou une brosse ferme la fente de 3 mm sous le toit (insectes).
6. **Trappe technique.** Avant l'assemblage, découper dans la **façade** une ouverture de 80 × 60 : de 70 à 150 depuis le bord sud, de 285 à 345 du bas. Il reste au moins 35 mm de bois au-dessus, sous le toit. Elle se ferme par une plaque extérieure de 100 × 80 × 10 (de 60 à 160, de 275 à 355), vissée avec un joint mousse ; la plaque reste sous le débord du toit et au-dessus du bloc d'entrée. C'est l'accès à l'électronique et à la carte SD, sans décrocher le nichoir ni démonter le toit.
7. **Électronique** (voir [README](../../README.md)). Percer la cloison après réception de la carte : passage d'objectif, 4 LED IR (Ø5), trou micro au droit du micro de la carte, trou Ø6,5 pour la sonde de température, à affleurer sous la cloison ([BOM](../bom.md)). La carte repose sur la cloison, objectif vers le bas. **Ne rien placer à moins de 50 mm du bord sud extérieur** dans le compartiment : le haut de la porte y rentre quand elle s'ouvre.
8. **Passages.** Côté nord, dans le compartiment technique (vers 350 du bas, au milieu) : presse-étoupe PG7 (perçage Ø12,5 ; lamage intérieur d'environ Ø25 pour l'écrou, selon le filetage reçu) pour le câble du coffret de la batterie, boucle d'égouttement. Rien ne dépasse du dos, qui s'appuie sur le support. Aération : un trou Ø8 grillagé en façade (vers 145 depuis le bord sud, 400 du bas, au-dessus de la plaque) et un au dos (vers 60 depuis le bord sud, 330 du bas), sous le débord du toit. Câble de la barrière IR : dans une baguette sur la façade, du bloc d'entrée jusque sous la plaque de trappe ; il passe par une encoche de 6 × 6 au bas de la plaque et entre dans le compartiment par l'ouverture de la trappe. Un connecteur dans le compartiment permet de retirer la plaque. Joint silicone autour de l'encoche. Aucun câble dans la chambre.
9. **Toit.** Vissé sur façade, dos et côté nord, jamais sur la porte, **avant** la pose du panneau : ses vis tombent sous l'emprise du panneau, le toit reste donc fixe. Couverture étanche (EPDM ou tôle). Panneau P110 sur une platine démontable, elle-même sur cales de 10, marges de 13 mm.
10. **Pose.** Barre de fixation au milieu du dos, qui écarte le nichoir de 20 mm du support. Nichoir légèrement penché vers l'avant (LPO), à 2 m au moins, solidement fixé, cales entre tronc et fil de fixation. Huile de lin facultative (LPO), à l'extérieur uniquement (choix du projet).

La porte sud ouvre la chambre ; la trappe en façade ouvre le compartiment technique. **Ni l'une ni l'autre pendant la nidification** : nettoyage et maintenance en automne, nichoir vide.

## À vérifier au montage à blanc

- Hauteur totale : environ 515 mm avec le toit et le panneau. Prise au vent et fixation à adapter au support.
- Le champ de la caméra à 15–20 cm du nid : l'objectif de l'OV3660 doit couvrir les 140 × 140 du fond ; mise au point à régler.
- La porte pivote sans frotter ; le loquet ne laisse pas de jour.
- Étanchéité de la couverture et des passages ; ventilation sans courant d'air sur le nid.

## Régénérer les plans

```sh
python tools/plan_nichoir.py          # contrôles + régénération des SVG
python tools/plan_nichoir.py --check  # contrôle seul (utilisé par les tests)
```

Les paramètres (épaisseur, trou, pente, toit, panneau) sont en tête du script. Le script vérifie les critères LPO, la place du compartiment technique et le panneau sur le toit.
