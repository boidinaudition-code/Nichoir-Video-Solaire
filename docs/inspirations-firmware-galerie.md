# Inspirations : firmware, galerie et suivi de la nichée

[Accueil](../README.md) · [Inspirations précédentes et audio](inspirations-audio.md) · [Comparatif des 14 projets](comparatif-pir-ov5640.md)

Cinq dépôts lus le 23 novembre 2026, au commit indiqué. Documentation seulement : aucun code tiers copié.

| Dépôt | Ce que c'est | Licence |
|---|---|---|
| [NestNinja.open](https://github.com/CraigHutchinson/NestNinja.open/blob/a52b0e2bf9c955fbcb388ec3bcd1f0796fa754b5/README.md) | Nichoir connecté ESP32-P4 + ESP32-C6, caméra OV5647, vidéo H.264. **Code pas encore publié** : le dépôt ne contient que de la documentation (sortie annoncée au 3ᵉ trimestre 2026) | GPL-3.0 annoncée |
| [BirdNest](https://github.com/VorosEgyes/BirdNest/blob/0fd1f7e31f77f7be80f5b14e9bd0c7a7387bb24d/README.md) | ESP32-CAM sur batterie : photos programmées vers Telegram, MQTT, sommeil profond, mises à jour à distance, carte électronique KiCad | MIT |
| [birdnest-ai](https://github.com/bali0019/birdnest-ai/blob/77303ef6dd78d19a14bc1949ecb09e2161854e49/README.md) | Surveillance d'un nid de cardinal avec une caméra Blink et l'IA Claude, alertes Discord | aucune licence : tous droits réservés |
| [BirdBox](https://github.com/SEspe/BirdBox/blob/1643f8b72a8438b6ee4b93df1c81dd77e0106c3f/README.md) ([spécification](https://github.com/SEspe/BirdBox/blob/1643f8b72a8438b6ee4b93df1c81dd77e0106c3f/FSD_BirdBox.md)) | Caméra de nichoir ou de mangeoire ESP32-S3 (ESP-IDF), photos sur microSD, galerie et statistiques sur la carte, Home Assistant | MIT |
| [birdcam](https://github.com/nbokdam/birdcam/blob/f79f6578aa11f21328073e274bba0cbe9b0d59b4/README.md) | Nichoirs à Raspberry Pi, vidéo et son en direct dans le navigateur, seulement quand quelqu'un regarde | AGPL-3.0 |

## Idées retenues

### Caméra et éclairage

- **Les LED IR exigent un capteur sans filtre IR-cut.** La spécification de BirdBox le dit explicitement pour son option LED IR. Cela confirme le test de la télécommande prévu à la réception de la carte.
- **Mode « nichoir »** (BirdBox) : mise au point rapprochée, éclairage IR, visites rares mais longues. Réglages distincts d'une mangeoire.
- **Grand angle** : NestNinja annonce un objectif fisheye 160° avec LED IR pour l'intérieur du nichoir. À garder en tête si l'objectif de l'OV3660 ne couvre pas tout le fond.
- **Jeter les premières images** après l'allumage de la caméra, le temps que l'exposition se règle (BirdNest : 4 images ; BirdBox ignore aussi les détections pendant une courte période après le démarrage).
- **Coupure de l'alimentation de la caméra** : BirdBox constate qu'un capteur OV2640 peut cesser de fournir des images après plusieurs heures ; le seul remède garanti est de couper son alimentation. Aucun circuit de coupure n'est retenu dans la [BOM](bom.md) : la minuterie TPL5110 couperait la carte entre deux réveils programmés, incompatible avec le réveil par la barrière. Point ouvert.

### Fiabilité du firmware

- **Mises à jour à distance sûres** (BirdNest, BirdBox) : deux partitions, vérification SHA-256 et retour automatique à l'ancienne version si la nouvelle ne démarre pas. BirdNest refuse la mise à jour sous 3,60 V de batterie. À reprendre : **jamais de mise à jour quand la batterie est basse**, et jamais pendant la nidification sans nécessité.
- **Un seul firmware pour tous les nichoirs** (BirdNest) : nom de l'appareil enregistré dans la carte, par défaut dérivé de l'adresse MAC.
- **Portail Wi-Fi de secours** (BirdNest, BirdBox) : se rouvre après plusieurs échecs de connexion, sans bloquer la carte ; BirdBox continue d'essayer le réseau en parallèle, car un nichoir peut être en limite de portée.
- **Les erreurs disent pourquoi** (BirdBox, BirdNest) : chaque échec d'envoi enregistre une raison courte (`wifi`, `tls`, `timeout`…) au lieu d'un simple « erreur ».
- **Blocage = réinitialisation bornée** : après trois relances logicielles ratées, BirdBox signale un défaut au lieu de boucler.

### Énergie et nuit

- **Nuit détectée par l'image, pas par l'heure** (BirdBox) : le contraste de l'image s'effondre dans le noir, alors que la luminosité moyenne reste trompeuse. Réveil par une courte mesure toutes les 10 minutes. Garde-fou : réveil forcé après 14 h de sommeil, au cas où un oiseau ou une feuille masquerait l'objectif. Pour nous, avec les LED IR, la nuit ne coupe pas la vidéo : elle sert à **passer en mode IR**.
- **Tension batterie calibrée en deux points** (BirdNest). Notre carte est alimentée en 5 V régulé par la V75 : elle ne voit pas la tension de la batterie. Depuis le 24/11/2026, la V75 est remplacée par un pack de 4 accus 18650 dont la carte lit directement la tension, via un pont diviseur ([BOM](bom.md)) : l'étalonnage en deux points reste utile.
- **Température** par sonde DS18B20 (BirdNest) : non retenu le 24/11/2026. La sécurité de charge repose sur la thermistance du chargeur ([BOM](bom.md)).

### Galerie, Home Assistant et suivi de la nichée

- **Séparer la capture de l'analyse** (birdnest-ai) : un service reçoit et stocke sans jamais s'arrêter ; un autre analyse la file à son rythme. Une panne de l'analyse ne fait perdre aucun clip. C'est le même principe que notre livraison durable vers Unraid.
- **Calendrier de la nichée** (birdnest-ai) : six étapes déduites des observations (construction, ponte, couvaison, nourrissage, envol, vide), avec un compteur « couvaison, jour 4 sur environ 12 ». Une éclosion n'est validée qu'après **deux observations distinctes** à quelques heures d'intervalle, pour éviter les fausses alertes. Durées à adapter aux mésanges.
- **Ne pas conclure « nid vide » sur une image IR** (birdnest-ai) : en noir et blanc, l'oiseau se confond avec le nid ; dans le doute, « incertain ».
- **Comptage des œufs** : birdnest-ai le désactive faute de vue plongeante. Notre caméra regarde le nid **par-dessus** : le comptage devient envisageable, à vérifier sur les images réelles.
- **Visite = rafale** (BirdBox) : regrouper les images et clips d'une même visite ; confirmer ou corriger d'un clic ; filtrer les faux déclenchements.
- **Diagnostics publiés dans Home Assistant par MQTT** (BirdBox, BirdNest) : disponibilité avec dernier message automatique (« hors ligne »), version du format des messages, signal Wi-Fi, température, batterie, file d'envoi.
- **Bouton « pause »** avant de s'approcher du nichoir (birdnest-ai) : on suspend les captures le temps du passage.
- **Images IR affichées en niveaux de gris** et **accès protégé par identifiant** dans la galerie (birdcam). Pas d'accès depuis Internet sans VPN (BirdBox, BirdWatch).

## Idées écartées

| Idée | Raison |
|---|---|
| Vidéo en direct à la demande (birdcam, BirdBox) | La carte devrait rester connectée en Wi-Fi en permanence : incompatible avec le budget solaire |
| ESP32-P4 avec encodage H.264 (NestNinja) | Fichiers bien plus légers que le MJPEG, mais autre carte que celle retenue et code pas encore publié. À reconsidérer pour une V2 du matériel |
| Reconnaissance d'espèce (BirdBox, birdnest-ai) | Peu utile dans un nichoir à mésanges ; BirdBox a d'ailleurs abandonné son modèle embarqué faute de précision |
| Analyse de chaque image par une IA payante (birdnest-ai) | L'auteur cite 180 à 270 $ par mois ; une analyse locale sur Unraid suffit pour les faux déclenchements |
| Envoi vers Telegram ou Discord | Galerie locale sur Unraid et Home Assistant |
