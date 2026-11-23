# Nichoir vidéo solaire

Nichoir en bois pour mésanges, autonome au solaire : détection des passages par capteur PIR, clip vidéo avec son, envoi en Wi-Fi vers une galerie sur Unraid.

État : conception. Plans du nichoir ([docs/plans](docs/plans/README.md)) et liste d'achat ([BOM](docs/bom.md)) prêts ; rien n'est acheté, aucun firmware, aucun essai matériel.

## Matériel retenu

Références, prix et câblage : **[BOM](docs/bom.md)**. Environ 228 € TTC hors port au 24/11/2026, dont 89 € pour le panneau et sa rallonge, plus quatre supports d'accus à chiffrer.

| Élément | Choix | Remarque |
|---|---|---|
| Carte et caméra | [Gotronic 39234](https://www.gotronic.fr/art-carte-xiao-esp32s3-sen--soud--47620.htm) : XIAO ESP32-S3 Sense 102010635, connecteurs soudés, caméra **OV3660** (2048 × 1536), micro, lecteur microSD (32 Go maxi), antenne | Consommation annoncée : 138 mA en vidéo, 341 mA en prise de photo. Carte SanDisk Ultra 32 Go |
| Détection | Capteur PIR BS612 sous la cloison + photo toutes les 10 min en journée | Pas d'infrarouge actif : ni LED ni barrière. Un oiseau qui couve bouge peu : la photo périodique sert de filet |
| Panneau | Voltaic P110, 9,54 W, 223 × 274 mm | Sur le toit à 45° orienté sud ; rallonge de 3 m jusqu'au coffret |
| Batterie | 4 accus XTAR 18650 4000 mAh protégés en parallèle (environ 55 Wh), chargeur solaire Adafruit bq24074, régulateur 5 V Pololu | Coffret IP65 séparé et ombragé ; charge coupée hors d'environ +5 à +45 °C par une thermistance ; tension du pack lue par la carte |
| Liaison | Câble 4 conducteurs coffret → nichoir : 5 V, masse, tension batterie / 2, réserve | Presse-étoupe PG7 aux deux bouts |

**Sans éclairage, la chambre est sombre** même de jour (lumière du seul trou d'envol) : qualité d'image à évaluer dans le carton d'essai, et pas d'images la nuit. Voir la [BOM](docs/bom.md).

## Fonctionnement prévu

- **Capture :** clip 720p de 20 s sur microSD (AVI), plus une photo pleine définition (3 Mpx) au début de chaque événement.
- **Son :** enregistré pendant chaque clip par le micro de la carte, dans le même fichier (mono, 16 kHz, environ 640 ko par clip). Aigus coupés au-dessus de 8 kHz. Jamais d'enregistrement continu.
- **Envoi :** en Wi-Fi vers Unraid après chaque clip. Le clip reste sur la SD tant qu'Unraid n'a pas confirmé l'avoir enregistré ([règles de livraison](docs/decision-v2.md)).
- **Galerie sur Unraid :** clips convertis en MP4 avec son, regroupés par visite. Réception et analyse séparées : une panne de l'analyse ne perd aucun clip. Calendrier de la nichée (construction, ponte, couvaison, nourrissage, envol) avec compteur de jours ; une étape n'est validée qu'après deux observations ; une image douteuse (trop sombre) donne « incertain », jamais « nid vide ». Capteurs Home Assistant par MQTT (batterie, dernière visite, nombre de visites, file d'envoi). Bouton « pause » avant de s'approcher. Pas de flux en direct ni de Frigate.
- **Télémétrie :** tension des accus et signal Wi-Fi envoyés avec chaque clip ; mode survie quand la batterie baisse (moins de clips, puis photos seules). Réglages Wi-Fi et serveur par un portail de configuration, hors firmware et hors Git.
- **Fiabilité :** mises à jour à distance avec retour automatique à l'ancienne version, jamais batterie basse ; redémarrage logiciel si la caméra se bloque (aucun circuit de coupure matérielle retenu pour l'instant) ; chaque échec enregistre sa raison.
- **Énergie :** au Havre en décembre, le P110 incliné à 45° produit environ 8 Wh/j en moyenne ([données PVGIS](docs/pvgis-le-havre-inclinaisons.csv)). Réserve utile d'environ 44 Wh, soit 12 à 17 jours sans soleil avec les hypothèses de consommation V2. Consommation réelle à mesurer.

## Le nichoir en bois

Plans, débit et montage : **[docs/plans](docs/plans/README.md)**.

- Chambre 140 × 140 × 230 mm, trou Ø32 (28 pour réserver aux mésanges bleues), selon le tableau LPO.
- Planche de 20 mm, environ 2,05 m de long pour la caisse, plus le toit de 300 × 250.
- Compartiment technique au-dessus de la chambre, sous le toit à 45° qui porte le panneau.
- Côté sud pivotant pour le nettoyage d'automne ; trappe en façade, au-dessus du trou d'envol, pour l'électronique et la carte SD.

![Vue de face](docs/plans/vue-facade.svg)

Pièces imprimées éventuelles (supports, coffret) : PETG ou ABS plutôt que PLA. Silicone autour des passages, vernis de protection sur les cartes, petit orifice bas pour évacuer l'humidité.

La faune passe avant les images : chambre ombragée aux heures chaudes, aucun perchoir, aucun câble ni pointe dans la chambre. **Aucune intervention sur un nichoir occupé** ; en cas de panne, la vidéo reste arrêtée jusqu'à l'automne.

## Prochaines étapes

1. Commander selon la [BOM](docs/bom.md) ; charger les 4 accus séparément et vérifier leurs tensions avant de les mettre en parallèle.
2. Essai dans un carton fermé percé d'un trou de 32 mm : luminosité, image, son, netteté à 15–20 cm, déclenchement du PIR.
3. Mesurer au wattmètre USB la consommation par clip et en veille ; comparer veille et coupure d'alimentation entre deux événements.
4. Montage à blanc du nichoir, puis passages de la caméra, du micro et du PIR dans la cloison.
5. Écrire le firmware (base d'étude : `ESP32-CAM_MJPEG2SD`) et la galerie Unraid.

## Options écartées

| Option | Raison |
|---|---|
| Raspberry Pi, flux en direct, Frigate | Aucun câble possible jusqu'au nichoir ; un Raspberry Pi consomme trop pour le solaire |
| Panneau 2 W | Trop faible en hiver |
| Power bank quelconque | La plupart des power banks s'éteignent à faible consommation |
| Éclairage et barrière infrarouges, sondes de température | Abandonnés le 24/11/2026 |
| Vidéo 1080p ou pleine définition | Fichiers trop lourds à envoyer en Wi-Fi |
| Écoute audio continue | Trop d'énergie |

## Documentation

- [Plans du nichoir](docs/plans/README.md)
- [BOM : composants, prix, câblage](docs/bom.md)
- [Recherches V3 : éclairage, toit, batterie, PVGIS](docs/recherches-v3.md)
- [Inspirations BirdWatch, Naturebytes, Printables et audio](docs/inspirations-audio.md)
- [Inspirations NestNinja, BirdNest, birdnest-ai, BirdBox, birdcam : firmware, galerie, suivi de la nichée](docs/inspirations-firmware-galerie.md)
- [Comparatif de 14 projets ESP32 + caméra + PIR](docs/comparatif-pir-ov5640.md)
- [Décision V2 : règles de livraison des clips](docs/decision-v2.md)
- [Archive V1](docs/archive/v1/README-v1.md)

Contrôles : `python -m unittest discover -s tests -v`, `python tools/plan_nichoir.py --check`, `python tools/bom.py --check` et `python tools/verifier_dossier.py`.
