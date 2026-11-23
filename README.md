# Nichoir vidéo solaire

État : documentation de conception V3. Aucun firmware, aucun essai matériel et aucun déploiement.

## Décisions actuelles

- Caméra : XIAO ESP32-S3 Sense + OV5640 NoIR grand angle, DVP 24 broches. Comparer le brochage du module acheté à la fiche Seeed avant branchement ; la compatibilité n'est pas vérifiée. Le module Seeed standard a un autofocus et un filtre IR-cut : repli pour les essais de jour.
- Éclairage : LED IR 940 nm diffusées, seulement pendant la capture, commandées depuis le 5 V par transistor/MOSFET, jamais directement par GPIO. Référence, nombre et courant restent à choisir et mesurer, sans échauffement de la chambre.
- Capture : clips 720p MJPEG/AVI sur microSD, une photo 5 Mpx au début de chaque événement. Pas de vidéo 5 Mpx.
- Détection : barrière IR au trou d'envol pour les entrées/sorties ; photo toutes les 10 min en journée pour le timelapse. PIR intérieur optionnel ; barrière hors champ, sans éclairer la chambre.
- Solaire : Voltaic P110, 9,54 W ; toit monopente 45° orienté sud, trou d'envol sur la face est. Géométrie du toit à revalider.
- Batterie : Voltaic V75, 72,36 Wh, sortie USB-A Always On 5 V. Prix fabricant : 89 USD, pas un prix France. Batterie dans un coffret séparé, ombragé et protégé de l'eau/condensation ; charge autorisée entre 0 et 45 °C.
- Réseau : Wi-Fi déclaré OK par Romain, sans mesure RSSI documentée. Aucun câble possible : montage autonome solaire. Envois bornés vers une future galerie MP4 sur Unraid, avec ACK durable ; pas de flux continu ni de Frigate.

## Options écartées et pourquoi

| Option | Motif |
|---|---|
| Pi Zero 2 W + Camera Module 3 NoIR Wide + Frigate | Environ 1 W continu, soit 24 Wh/j estimés non mesurés, contre au plus 8,8 Wh/j solaires moyens en décembre à 60° ; Frigate suppose un flux continu |
| Panneau 2 W | Budget hivernal insuffisant avec les envois Wi-Fi |
| Pack maison 5×18650 XTAR et chargeur BQ25185 | Sécurité et complexité ; la V75 certifiée couvre le besoin documentaire |
| Power bank quelconque | La plupart s'éteignent à faible courant ; Always On nécessaire |
| 1080p ou vidéo 5 Mpx | 1080p : probablement plusieurs dizaines de Mo pour 20 s, ordre de grandeur non mesuré incompatible avec le budget Wi-Fi de 10–30 s/clip ; 5 Mpx réservé aux photos |
| PIR seul | Oiseau qui couve peu mobile et détection peu fiable dans 14 cm |

## Prochaines étapes

1. Essai en carton fermé, trou de 32 mm, avec NoIR + LED IR, sans oiseaux.
2. Mesurer les Wh par clip et la veille au wattmètre USB, puis recalculer le budget complet.
3. Vérifier le brochage du module NoIR ; c'est un préalable à son branchement pour l'essai 1.
4. Réaliser le gabarit du toit 45° : prise au vent, débord et fixation.

Éléments à prévoir : XIAO Sense, module NoIR, microSD, LED IR et commande, barrière IR, P110, V75, câbles compatibles, bois, fixations et coffrets. Pas de BOM chiffrée V3 établie.

La faune reste prioritaire : chambre ombragée aux heures chaudes, aucun perchoir, câble libre ou pointe accessible. Aucune intervention sur nichoir occupé, même par trappe technique ; laisser la vidéo arrêtée en cas de panne.

## Documentation et contrôles

- [Recherches V3, sources, PVGIS et calculs](docs/recherches-v3.md)
- [CSV PVGIS des quatre inclinaisons](docs/pvgis-le-havre-inclinaisons.csv)
- [Décision V2 partiellement remplacée ; §2 livraison durable toujours valide](docs/decision-v2.md)
- [Comparatif de 14 projets PIR / OV5640](docs/comparatif-pir-ov5640.md)
- [Archive V1 : ancienne BOM, tableaux et huit pages](docs/archive/v1/README-v1.md)

Depuis la racine : `python -m unittest discover -s tests -v`, `python tools/verifier_dossier.py`, puis `git diff --check`. Les outils et tests de calcul restent V1 : ils ne qualifient pas le matériel V3.
