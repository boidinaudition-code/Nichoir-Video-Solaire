# Nouvelles inspirations et ajout de l'audio

[Accueil](../README.md) · [Recherches V3](recherches-v3.md) · [Comparatif des 14 projets](comparatif-pir-ov5640.md)

Sources lues le 23 novembre 2026. Documentation seulement : aucun code ni fichier 3D tiers copié dans ce dépôt, aucun essai matériel.

## 1. BirdWatch (Danielson187)

Source : [README au commit 7e2837f](https://github.com/Danielson187/BirdWatch/blob/7e2837f562e3c400c68d843f30e4dae35fb17d33/README.md).

Ce que fait le projet, selon son auteur : station solaire d'observation des oiseaux (fixation sur rambarde de balcon) à ESP32-CAM avec caméra OV3660 et PIR AM312. Au mouvement, la carte se réveille, prend **une photo**, l'envoie en Wi-Fi au serveur et se rendort. Le pack est un 1S2P de 18650 protégé, chargé par un module CN3065 depuis deux panneaux 5 V / 3 W d'environ 100 × 100 mm.

Idées retenues :

| Idée | Ce que l'on en fait pour le nichoir |
|---|---|
| Mesure de la batterie (INA219 sur le chemin de la batterie) envoyée avec chaque observation | Envoyer la tension batterie, le RSSI Wi-Fi et la température de la carte avec chaque clip. L'auteur précise que ses Wh sont des **estimations** à partir de mesures prises pendant les réveils, pas un compteur continu. |
| Mode survie quand la batterie est basse | Seuils à définir : moins de clips, envois regroupés et espacés, puis photos seules. |
| Heures actives configurables | Plage horaire réglable. Dans un nichoir, la nuit compte (couvaison, dortoir) : ne pas la couper par défaut, la limiter si l'énergie manque. |
| Portail Wi-Fi de configuration au premier démarrage, aucun réglage codé en dur | À reprendre : identifiants Wi-Fi et adresse du serveur hors du firmware et hors Git. |
| Identifiant unique par appareil, serveur multi-appareils | Compatible avec l'identité persistante de la [livraison durable](decision-v2.md). |
| Serveur Docker avec base de données, tableau de bord, archive, statistiques de visites et d'énergie | Modèle pour la galerie sur Unraid. |
| Intégration Home Assistant native (batterie, signal, dernière photo) | Utile chez Romain : capteurs batterie, dernière visite et nombre de visites. |
| Détection d'oiseau par IA (YOLO) et classification d'espèce | La détection de présence peut servir à **trier les faux déclenchements**. La classification d'espèce est peu utile dans un nichoir à mésanges. Optionnel, côté Unraid uniquement. |
| Panneaux collés sur le toit et larmier arrière pour limiter les entrées d'eau | Principe à reprendre pour le compartiment technique. |

Non retenu : l'électronique de charge et le pack 18650 (remplacés par la V75 certifiée), l'ESP32-CAM AI-Thinker.

**Licence :** logiciel sous PolyForm Noncommercial 1.0.0 ; documentation et fichiers 3D sous CC BY-NC-SA 4.0. Un usage personnel non commercial avec attribution est possible ; toute adaptation des fichiers 3D doit garder la même licence.

## 2. Naturebytes

Sources : [Our Tech](https://naturebytes.org/our-tech/), [Conservation](https://naturebytes.org/conservation/).

Ce que disent les pages : la NestBox utilise une technologie similaire à leur Wildlife Cam Kit, lui-même alimenté par un Raspberry Pi, pour diffuser en direct, filmer, photographier et suivre la nidification. Elle a été déployée avec le Muséum des sciences naturelles de Belgique dans un projet éducatif national (« Xperibird ») ; les observations sont saisies sur un portail en ligne. Selon [l'étude d'impact de 2017](https://drive.google.com/file/d/13e6Tcm3k3meYt6jEoQe6_RHLcHpRFHc2/view) liée depuis la page, XperiBIRD.be suit la nidification des mésanges dans des écoles belges. Naturebytes déploie aussi des enregistreurs audio AudioMoth (full spectrum, jusqu'aux ultrasons) pour suivre les paysages sonores.

Les pages publiques ne détaillent **ni le matériel exact, ni l'éclairage, ni l'alimentation** de la NestBox. Le document lié depuis « More information » est une étude d'impact éducatif de 2017 sans détails techniques.

Idées retenues :

- **Carnet de nidification** dans la galerie : construction du nid, ponte, éclosion, envol, plus le nombre d'œufs (ajout de notre part). La vidéo sert à remplir ce carnet.
- Combiner images et **données de contexte**, comme le concept de station météo de Naturebytes : température dans la chambre et à l'extérieur.
- L'audio a une vraie valeur de suivi (AudioMoth). Un enregistreur full spectrum dédié reste hors périmètre ; le micro de la Sense suffit pour une V1 audio (§4).

Non retenu : la diffusion en direct (technologie du Cam Kit à Raspberry Pi, incompatible avec le budget solaire et sans câble, voir le README).

## 3. Boîtier de piège photo ESP32-CAM sur Printables (Karl132)

Source : [modèle 520378](https://www.printables.com/model/520378-case-for-esp32_cam-trail-camera-pir-sensor-18650-b). Page web protégée par Cloudflare ; description lue via l'API publique de Printables.

Ce que décrit l'auteur : boîtier imprimé pour ESP32-CAM, PIR et deux 18650 en série, photos sur SD sans Wi-Fi. Un MOSFET commandé par la sortie du PIR **coupe totalement l'alimentation** de l'ESP32 entre deux déclenchements. Latence annoncée : 1,5 à 2 s, contre environ 1 s avec le sommeil profond. Le potentiomètre du PIR maintient l'alimentation environ 15 s.

Idées retenues :

- **Couper l'alimentation de la caméra et des LED IR** entre deux événements, plutôt que de compter sur la seule veille. À comparer par la mesure au sommeil profond : plus de latence, moins de veille. La V75 consomme de toute façon environ 26 mW en Always On.
- **Étanchéité** : silicone autour de la caméra et des passages, vernis de protection sur les cartes et connecteurs, **un orifice bas laissé ouvert** pour évacuer l'humidité.
- **Impression** en PETG ou ABS : l'auteur indique que le PLA se dégrade dehors en un à deux ans. Utile pour le compartiment technique, imprimable par Romain.

Non retenu : deux 18650 en série sans régulateur ni chargeur intégré.

## 4. Audio

Demande de Romain : récupérer aussi le son.

Ce que permettent les sources :

- La carte Sense intègre un **micro numérique PDM** (GPIO 41 données, GPIO 42 horloge). Seeed indique que l'ESP32-S3 n'accepte que le **mono 16 bits**, et ses exemples enregistrent en **16 kHz**. Source : [Seeed, micro de la Sense](https://wiki.seeedstudio.com/xiao_esp32s3_sense_mic/).
- `ESP32-CAM_MJPEG2SD` gère les micros PDM sur ESP32-S3, avec des broches prédéfinies pour la XIAO Sense. L'audio est enregistré en **PCM 16 bits mono à 16 kHz** et stocké **dans le fichier AVI** ; l'auteur indique que cela fonctionne bien sur ESP32-S3. Source : [README au commit 18f6e84](https://github.com/s60sc/ESP32-CAM_MJPEG2SD/blob/18f6e84b051da8741b70a0c41d2ac7c3da332fad/README.md).

Décision :

- **Son enregistré avec chaque clip**, dans le même AVI, avec le micro de la Sense. Pas de micro supplémentaire en V1.
- **Volume** : 16 000 échantillons × 2 octets × 20 s = **640 ko par clip**, peu par rapport à la vidéo. Consommation du micro à mesurer avec le reste.
- **Limite** : à 16 kHz, le son est coupé au-dessus de 8 kHz. Les aigus des cris de passereaux peuvent donc être en partie perdus. À écouter lors des essais.
- **Galerie** : le MP4 produit sur Unraid doit contenir la piste audio. Seeed signale que beaucoup de lecteurs vidéo lisent mal ses WAV. La conversion MP4 sur Unraid devrait régler ce point : à tester.
- **Placement** : la Sense est dans le compartiment technique, au-dessus de la chambre. Prévoir un petit passage acoustique vers la chambre, protégé de l'eau et sans bord coupant. À tester.
- **Vie privée** : le son n'est enregistré que pendant les clips déclenchés par une activité dans le nichoir, jamais en continu. Le micro peut capter des voix proches : éviter de placer le nichoir près d'une terrasse ou d'un passage.

Écarté pour l'instant : l'écoute continue pour déclencher sur les cris des oisillons (coût énergétique de l'écoute permanente) et un enregistreur full spectrum de type AudioMoth.

À vérifier : la qualité réelle du micro intégré à travers la cloison, le bruit de la carte et des LED, et la synchronisation son/image.
