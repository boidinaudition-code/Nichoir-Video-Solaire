# Nichoir vidéo solaire

Nichoir en bois pour mésanges, autonome au solaire : détection des entrées et sorties, clip vidéo avec son, envoi en Wi-Fi vers une galerie sur Unraid.

État : conception. Plans du nichoir ([docs/plans](docs/plans/README.md)) et liste d'achat ([BOM](docs/bom.md)) prêts ; rien n'est acheté, aucun firmware, aucun essai matériel.

## Matériel retenu

Références, prix et câblage : **[BOM](docs/bom.md)**. Environ 301 € TTC hors port au 24/11/2026, dont 199 € pour la batterie et le panneau.

| Élément | Choix | Remarque |
|---|---|---|
| Carte et caméra | [Gotronic 39234](https://www.gotronic.fr/art-carte-xiao-esp32s3-sen--soud--47620.htm) : XIAO ESP32-S3 Sense 102010635, connecteurs soudés, caméra **OV3660** (2048 × 1536), micro, lecteur microSD (32 Go maxi), antenne | Consommation annoncée : 138 mA en vidéo, 341 mA en prise de photo. Carte SanDisk Ultra 32 Go |
| Éclairage | 4 LED IR Vishay TSAL6200 (940 nm, ±17°), environ 35 mA chacune, allumées seulement pendant la capture, commandées par un BC337 depuis le 5 V | Derrière un diffuseur ; intensité à régler en essai |
| Détection | Barrière IR Adafruit 2167 au trou d'envol + photo toutes les 10 min en journée | Émetteur allumé par impulsions (10 mA en continu sinon) ; PIR BS612 en option |
| Panneau | Voltaic P110, 9,54 W, 223 × 274 mm | Sur le toit à 45° orienté sud ; rallonge de 3 m jusqu'au coffret |
| Batterie | Voltaic V75, 72,36 Wh, sortie USB Always On | Coffret IP65 séparé et ombragé. Tension des cellules lue par la carte sur les broches SBU du port USB-C (moitié de la tension, 1,6 à 2,1 V) |
| Températures | 2 sondes DS18B20 : chambre et coffret | Sonde de la chambre affleurante sous la cloison |
| Liaison | Câble 4 conducteurs coffret → nichoir : 5 V, masse, tension batterie, 1-Wire | Presse-étoupe PG7 aux deux bouts |

**À vérifier dès réception : la caméra voit-elle l'infrarouge ?** Si l'OV3660 du kit a un filtre IR-cut, les LED 940 nm l'éclaireront mal. Test simple : filmer la LED d'une télécommande de télé pendant un appui. Si la caméra ne la voit pas, il faudra un module caméra NoIR (sans filtre) compatible avec le connecteur de la Sense, ou renoncer aux images dans le noir.

## Fonctionnement prévu

- **Capture :** clip 720p de 20 s sur microSD (AVI), plus une photo pleine définition (3 Mpx) au début de chaque événement.
- **Son :** enregistré pendant chaque clip par le micro de la carte, dans le même fichier (mono, 16 kHz, environ 640 ko par clip). Aigus coupés au-dessus de 8 kHz. Jamais d'enregistrement continu.
- **Envoi :** en Wi-Fi vers Unraid après chaque clip. Le clip reste sur la SD tant qu'Unraid n'a pas confirmé l'avoir enregistré ([règles de livraison](docs/decision-v2.md)).
- **Galerie sur Unraid :** clips convertis en MP4 avec son, regroupés par visite. Réception et analyse séparées : une panne de l'analyse ne perd aucun clip. Calendrier de la nichée (construction, ponte, couvaison, nourrissage, envol) avec compteur de jours ; une étape n'est validée qu'après deux observations ; une image IR douteuse donne « incertain », jamais « nid vide ». Capteurs Home Assistant par MQTT (batterie, dernière visite, nombre de visites, file d'envoi). Bouton « pause » avant de s'approcher. Pas de flux en direct ni de Frigate.
- **Télémétrie :** tension des cellules de la V75, signal Wi-Fi et température (chambre et coffret de batterie) envoyés avec chaque clip ; mode survie quand la batterie baisse (moins de clips, puis photos seules). Réglages Wi-Fi et serveur par un portail de configuration, hors firmware et hors Git.
- **Fiabilité :** mises à jour à distance avec retour automatique à l'ancienne version, jamais batterie basse ; redémarrage logiciel si la caméra se bloque (aucun circuit de coupure matérielle retenu pour l'instant) ; chaque échec enregistre sa raison.
- **Énergie :** au Havre en décembre, le P110 incliné à 45° produit environ 8 Wh/j en moyenne ([données PVGIS](docs/pvgis-le-havre-inclinaisons.csv)). Consommation réelle à mesurer.

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

1. Commander selon la [BOM](docs/bom.md) et vérifier la vision infrarouge (test de la télécommande) ; vérifier aussi la version de V75 reçue et la tension SBU au multimètre.
2. Essai dans un carton fermé percé d'un trou de 32 mm, avec les LED IR : image, son, netteté à 15–20 cm.
3. Mesurer au wattmètre USB la consommation par clip et en veille ; comparer veille et coupure d'alimentation entre deux événements.
4. Montage à blanc du nichoir, puis passages de la caméra, des LED et du micro dans la cloison.
5. Écrire le firmware (base d'étude : `ESP32-CAM_MJPEG2SD`) et la galerie Unraid.

## Options écartées

| Option | Raison |
|---|---|
| Raspberry Pi, flux en direct, Frigate | Aucun câble possible jusqu'au nichoir ; un Raspberry Pi consomme trop pour le solaire |
| Panneau 2 W | Trop faible en hiver |
| Pack 18650 fait maison, power bank quelconque | Sécurité ; la plupart des power banks s'éteignent à faible consommation |
| Vidéo 1080p ou pleine définition | Fichiers trop lourds à envoyer en Wi-Fi |
| PIR seul | Un oiseau qui couve bouge peu |
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
