# Comparatif PIR et OV5640 — briques pour le nichoir V2

[Accueil](../README.md) · [Décision V2](decision-v2.md)

> **Décisions courantes : [README](../README.md).** La carte retenue est la XIAO ESP32-S3 Sense avec caméra **OV3660** (Gotronic 39234), et non plus l'OV5640 : clips 720p et photo 3 Mpx. Les fiches de projets ci-dessous restent valables comme inspiration ; les consignes OV5640 et le protocole 5 Mpx sont historiques.

## Périmètre et méthode

Revue documentaire directe de **14 dépôts nommés**, plus un dépôt hors classement. Les README ont été téléchargés en parallèle depuis `raw.githubusercontent.com`, après résolution de `HEAD` par l'API GitHub ; chaque lien ci-dessous fige le commit effectivement consulté. Les arborescences GitHub et certains documents/fichiers complémentaires ont aussi été consultés. Ce classement est une priorité d'étude pour notre besoin, pas une mesure de qualité générale.

Aucun firmware tiers compilé, aucun essai matériel, aucun code copié ou intégré, aucun service installé ou modifié sur Unraid. Les démonstrations, mesures et matériels « attestés » ci-dessous sont **déclarés par leurs auteurs**, pas reproduits ici. « Support » signifie compatibilité annoncée/configurable, pas essai sur notre XIAO et notre lot OV5640. L'absence de preuve dans les sources consultées n'établit pas l'absence absolue d'une fonctionnalité.

Vocabulaire : **photo** = JPEG isolé ou rafale ; **vidéo enregistrée** = séquence conservée dans un fichier, avec conteneur identifié si documenté ; **stream** = flux direct, pas preuve d'archivage. PIR de déclenchement, réveil de sommeil profond et coupure matérielle sont trois mécanismes différents. Un PIR peut être optionnel dans un logiciel et néanmoins rester le déclencheur retenu pour notre V2.

## Consigne caméra courante

La cible est désormais **XIAO ESP32S3 Sense + OV5640, à confirmer par PID à réception**, et non OV3660. [Seeed, source constructeur consultée](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/) annonce la transition, mais prévient que des lots OV3660 circulent encore. Pas de substitution silencieuse : obtenir le lot OV5640 et relever référence, PID, optique et révision.

Selon le [guide Seeed](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started), l'OV5640 **livré avec la Sense est à focale fixe** ; seul le **module long vendu séparément, avec dissipateur, a un autofocus**. La [fiche MJY5OAF-F3M-V1](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/new-res/OV5640_Camera_Module_Specification.pdf) de ce module AF indique les broches 23 AF-GND / 24 AFVDD 2,8 V et un objectif « 4P+IR », « IR Cut ». La V3 retient un NoIR grand angle DVP 24 broches pour le 940 nm, avec brochage à vérifier et mise au point manuelle à 10–15 cm si ce module n'a pas d'AF. La définition maximale annoncée est 2592 × 1944. Cela ne garantit ni vidéo 5 MP, ni cadence 1080p, ni supériorité en faible lumière. Le tableau constructeur laisse les consommations OV5640 à **TBD** : les anciennes valeurs OV3660, les microampères du SoC seul et les courants d'une autre carte ne dimensionnent pas le nichoir complet.

## Vue d'ensemble des 14 dépôts

| Priorité d'étude | Dépôt | Photo / enregistrement / stream dans les sources | PIR | Capteur : preuve matérielle ou support seulement |
|---|---|---|---|---|
| 1 | s60sc/ESP32-CAM_MJPEG2SD | JPEG, AVI MJPEG sur SD, direct et relecture MJPEG/RTSP | Optionnel : détection image et manuel aussi | Bench OV2640 décrit ; OV3660/OV5640 et XIAO annoncés compatibles, pas essai de notre combinaison |
| 2 | Remeny-Farm/esp32-photostation | Rafales JPEG + JSON sur SD, upload HTTPS ; pas de clips AVI documentés | Déclencheur de visite | XIAO OV3660 de référence ; OV2640/OV5640 listés en variantes |
| 3 | happychriss/BirdSensor_xiao | JPEG puis upload ; mode serveur MJPEG commandé ; pas d'AVI documenté | Déclenche la mise sous tension | XIAO OV2640/OV3660 décrits ; OV5640 non attesté |
| 4 | Danielson187/BirdWatch | Photo Wi-Fi vers serveur/galerie ; pas de clips ou stream caméra documentés | AM312, réveil profond | AI-Thinker avec OV3660 explicitement dans la BOM |
| 5 | SEspe/BirdBox | Rafales photo SD et galerie, live MJPEG ; pas d'AVI documenté | Optionnel | Référence S3 N16R8 OV2640 ; pas preuve XIAO OV5640 |
| 6 | TeTeHacko/chytra-budka | Photos MQTT, audio stream BirdNET et caméra à la demande ; pas de clips AVI SD établis | Parmi PIR / VAD / MQTT | XIAO OV3660 explicitement décrit |
| 7 | Dyspersja/CameraTrap | Photos SD, consultation et stream web ; pas de vidéo enregistrée documentée | Déclencheur photo | ESP32-CAM OV2640 décrit et montage présenté |
| 8 | jameszah/ESP32-CAM-Video-Telegram | Photo + AVI, PSRAM dans l'ancien descriptif ; SD/hors Internet en v11 ; accès local | Optionnel, désactivable | Ancien descriptif OV2640 ; pas preuve OV5640 |
| 9 | nicklaststop22/esp32-cam-aio | JPEG, AVI MJPEG SD et live MJPEG | Armable/désarmable ; manuel aussi | AI-Thinker OV2640 décrit |
| 10 | pratik001010/ESP32-CAM-Outdoor-Surveillance-System | AVI SD, relecture/direct MJPEG, FTP | Optionnel | Bench OV2640 décrit ; support OV5640, OV3660 explicitement non testé |
| 11 | JJFourie/ESP32Cam-MQTT-SPIFFS-PIR | Photo vers PHP, live web ; SPIFFS pour configuration | AM312, commande MQTT aussi | OV2640 référencé ; pas PID matériel publié dans le README |
| 12 | aquatikz/ESP32-CAM-Live-cat-feeder-camera-Telegram- | Photos SD + Telegram, live MJPEG optionnel ; pas d'AVI documenté | AM312 | AI-Thinker visé ; capteur exact non attesté |
| 13 | OrTarazi/ESP32-CAM_cat_feeder_project | Photo Telegram ; pas d'AVI/SD/stream établi | Réveil EXT1, commande photo aussi | AI-Thinker décrit ; capteur exact non attesté |
| 14 | Hansikajain05/Solar_ai_Scarecrow | Images pour inférence ; pas d'archive vidéo ou stream documenté | Porte d'inférence désactivable | AI-Thinker décrit ; branche OV3660 dans le code ≠ matériel attesté |

## Fiches sourcées

### 1. s60sc/ESP32-CAM_MJPEG2SD — priorité pour le fichier vidéo

Source : [README au commit 18f6e84](https://github.com/s60sc/ESP32-CAM_MJPEG2SD/blob/18f6e84b051da8741b70a0c41d2ac7c3da332fad/README.md).

- **Force :** enregistrement JPEG multiplexés dans de vrais AVI sur SD, relecture, transferts FTP/HTTPS/WebDAV et configurations S3/XIAO. PIR optionnel, détection image ou commande manuelle possibles. L'application ne se résume donc pas à du streaming.
- **Faiblesse / énergie :** application riche, pression mémoire et nombreuses fonctions non nécessaires. Le README réserve les définitions au-dessus de FHD aux photos pour raisons mémoire, tout en publiant une table de cadences hautes définitions : cette tension documentaire interdit d'en déduire un mode 5 MP vidéo fiable. Détection image limitée au-delà de SXGA. Ses FPS OV2640/Freenove et sa table OV5640 ne sont pas une promesse XIAO en basse lumière ; son avertissement thermique concerne des montages caméra et alimentations à qualifier, pas toute Sense indistinctement. PIR ne prouve pas notre cycle profond/radio bornée.
- **À transposer :** étudier tamponnement, écritures SD alignées, finalisation/index AVI et distinction enregistrement/relecture pour les clips de 20 s, avec l'audio PDM dans l'AVI (décision V3, voir [inspirations et audio](inspirations-audio.md)). Désactiver lampes, direct permanent et rotation destructrice. Le transfert proposé ne remplace pas notre ACK durable avec empreinte et déduplication.

### 2. Remeny-Farm/esp32-photostation — priorité pour la file hors ligne

Sources : [README au commit ca7bb61](https://github.com/Remeny-Farm/esp32-photostation/blob/ca7bb61b6cf3b93efdc18518aeb3be4328a16800/README.md), [architecture](https://github.com/Remeny-Farm/esp32-photostation/blob/ca7bb61b6cf3b93efdc18518aeb3be4328a16800/docs/architecture.md), [matériel](https://github.com/Remeny-Farm/esp32-photostation/blob/ca7bb61b6cf3b93efdc18518aeb3be4328a16800/docs/hardware.md), [contrat HTTPS](https://github.com/Remeny-Farm/esp32-photostation/blob/ca7bb61b6cf3b93efdc18518aeb3be4328a16800/docs/protocol.md).

- **Force :** jusqu'à cinq photos par visite PIR, JPEG et JSON en file SD, reprise réseau avec backoff, serveur propre et logique testable sur hôte. Référence matérielle XIAO OV3660, une carte vérifiée selon l'auteur ; OV5640 est une variante supportée, pas un banc attesté.
- **Faiblesse / énergie :** secteur USB en V1, **sans batterie, deep sleep ni solaire** ; scan BLE continu et heartbeats. « Wakes » dans le README n'est pas ici une preuve de réveil profond. L'identification par balise de poule ne convient pas à des oiseaux sauvages. La mention autofocus OV5640 ne prouve pas l'optique d'un module NoIR générique ; seul le module Seeed long vendu séparément a un autofocus, celui livré avec la Sense est à focale fixe.
- **À transposer :** file persistante avec temporaires, identité de visite, photos avant manifeste et uploads hors capture ; adapter aux AVI clos. Ajouter explicitement empreinte, persistance serveur et ACK V2, réessais bornés et arrêt SD pleine. Ni équiper les oiseaux de BLE, ni importer éclairage constant et scan permanent.

### 3. happychriss/BirdSensor_xiao — priorité pour borner le cycle actif

Source : [README au commit 5e45dfd](https://github.com/happychriss/BirdSensor_xiao/blob/5e45dfd40d9500b8bc6efa0a6cce32d15df38069/README.md).

- **Force :** XIAO, JPEG SXGA puis POST serveur ; PIR Parallax et TPS22918 coupent réellement l'alimentation entre événements. Auto-maintien, watchdog de cycle et attente bornée de retombée PIR sont décrits. Un mode serveur MJPEG peut maintenir la carte allumée.
- **Faiblesse / énergie :** photo, pas chaîne AVI SD. OV2640/OV3660 décrits, OV5640 non attesté. Les ~130 µA de veille, pics ~300 mA, cycles ~15–20 s et « des mois » sur LiPo sont des annonces de ce montage, pas une autonomie pour nos clips, notre régulation USB et notre trafic. Coupure matérielle ≠ réveil RTC.
- **À transposer :** deadline globale et garde anti-redéclenchement pour éviter de vider la batterie en cas de panne. Le power-gating reste une option électronique distincte à qualifier avec fermeture SD ; ne pas recopier son raccordement BAT dans notre architecture USB.

### 4. Danielson187/BirdWatch — priorité pour la télémétrie et le mode dégradé

Source : [README au commit 7e2837f](https://github.com/Danielson187/BirdWatch/blob/7e2837f562e3c400c68d843f30e4dae35fb17d33/README.md).

- **Force :** PIR → photo → Wi-Fi → sommeil profond, serveur local, galerie et Home Assistant. BOM explicite AI-Thinker/OV3660, solaire CN3065, pack protégé 1S2P et INA219 ; ce n'est pas une attestation OV5640/XIAO.
- **Faiblesse / énergie :** photographie et analyse serveur, pas clip AVI. L'auteur précise que les relevés INA219 sont pris seulement à l'éveil : les Wh estimés ne constituent **pas un comptage continu**. Aucune autonomie de ce système ne valide notre panneau ou notre pack. Licences non commerciales déclarées : pas de réutilisation automatique.
- **À transposer :** visualiser état batterie, incidents et mode de survie dans la future galerie ; mesurer réellement l'énergie entre événements. Ne pas reprendre assemblage de cellules, Docker ou IA pour cette mise à jour documentaire.

### 5. SEspe/BirdBox — priorité pour la lisibilité de la galerie

Source : [README au commit 1643f8b](https://github.com/SEspe/BirdBox/blob/1643f8b72a8438b6ee4b93df1c81dd77e0106c3f/README.md).

- **Force :** rafales photo SD regroupées par visite, galerie, statistiques, quarantaine des premières images au boot et diagnostics de file ; stream MJPEG séparé. PIR explicitement **optionnel**. Matériel de référence déclaré S3 N16R8 OV2640, pas XIAO OV5640.
- **Faiblesse / énergie :** serveur et réseau résidents, pas démonstration d'un budget sommeil/solaire ni d'AVI. La reconnaissance embarquée historique a été abandonnée : identification désormais **en ligne via iNaturalist**, avec cloud payant optionnel. « No cloud » ne veut pas dire aucune sortie Internet.
- **À transposer :** statut par visite, raison d'échec, file visible et quarantaine d'exposition, pour la future galerie MP4 hors carte. Ne pas importer le stream permanent, les suppressions automatiques ou la dépendance IA externe dans la chaîne de conservation V2.

### 6. TeTeHacko/chytra-budka — retour d'expérience énergie, pas solaire acquis

Source : [README au commit f6216ed](https://github.com/TeTeHacko/chytra-budka/blob/f6216edb1e54a96c61e50aef8275f8df72dbe260/README.md).

- **Force :** montage XIAO OV3660, photos PIR/VAD/MQTT, audio BirdNET, télémétrie et modes de puissance ; l'auteur distingue matériel déployé et travaux prévus.
- **Faiblesse / énergie :** unités sur USB/powerbank ; essai intermédiaire panneau pliant rechargeant une powerbank, mais **aucun nœud solaire autonome déployé**, étage charge solaire/batterie non construit. ~1,1 W en modes toujours actifs et ~0,40 W en Safe light-sleep sont rapportés par l'auteur. Les modes automatiques ne passent pas réellement en sommeil profond ; hibernation sur commande distincte. Audio stream/vidéo à la demande ne prouvent pas AVI SD. SDIO annoncé dans son schéma ne valide pas le bus SPI réel de notre extension.
- **À transposer :** consigner les mesures par état et distinguer conception, banc et terrain. Ne pas reprendre son flux audio pour BirdNET (la V3 enregistre le son seulement avec les clips), ni ses indicateurs lumineux ni sa qualification « invisible aux oiseaux ». La V3 retient son propre éclairage 940 nm à qualifier, sans intervention occupée.

### 7. Dyspersja/CameraTrap — référence photo SD simple

Source : [README au commit 1342e46](https://github.com/Dyspersja/CameraTrap/blob/1342e4689f6bc2c7d0c938016cd7fe82b57ad439/README.md).

- **Force :** ESP32-CAM OV2640 avec PIR, photo sur microSD, liste et aperçu pleine résolution ; démonstrations de montage et stream navigateur présentées par l'auteur.
- **Faiblesse / énergie :** le direct `/stream` n'est **pas** un fichier vidéo ; pas d'AVI, sommeil profond ou bilan solaire établi dans le README. Le serveur Wi-Fi n'est pas assimilable à notre veille.
- **À transposer :** contrôle au banc de la séparation capture, fichier stocké et affichage, avec consultation des originaux ; pas une base démontrée pour nos clips OV5640.

### 8. jameszah/ESP32-CAM-Video-Telegram — distinguer les générations

Sources : [README au commit 2beec59](https://github.com/jameszah/ESP32-CAM-Video-Telegram/blob/2beec59cd2c91ec7eed1ecd134555fa2484a2836/README.md), [documentation installateur v11](https://github.com/jameszah/ESP32-CAM-Video-Telegram/blob/2beec59cd2c91ec7eed1ecd134555fa2484a2836/installer/README11.md).

- **Force :** véritables AVI et photos, déclencheur PIR/radar optionnel ou requête. Le descriptif ancien enregistre en PSRAM (~3 Mo), mais l'annonce 2024 et l'installateur v11 ajoutent **SD, fonctionnement hors Internet et téléchargement local**. Ne pas qualifier tout le dépôt de « sans SD ».
- **Faiblesse / énergie :** README mêlant générations. Les 25/8/2 FPS et durées associées concernent l'ancien mode, avec vitesse de lecture parfois différente de la capture ; ils ne valent pas pour XIAO OV5640. Envoi d'un clip de 3 Mo annoncé jusqu'à une minute ; Telegram n'est ni notre archive locale ni notre ACK durable. Pas de budget solaire démontré.
- **À transposer :** distinguer FPS acquis, FPS du conteneur et timelapse ; éprouver la lecture indépendante des AVI. Retenir le fonctionnement local plutôt que Telegram obligatoire et les clips limités à la RAM.

### 9. nicklaststop22/esp32-cam-aio — petite alternative DVR

Source : [README au commit 5af1cba](https://github.com/nicklaststop22/esp32-cam-aio/blob/5af1cbac0dc1c742ccc6fbe1170e470435473073/README.md).

- **Force :** AI-Thinker OV2640, AVI MJPEG FAT32, photos, live et commandes d'arrêt/finalisation ; PIR armable, manuel possible. Arduino natif sans dépendances externes annoncé.
- **Faiblesse / énergie :** clips PIR de deux minutes et serveur résident, pas notre sommeil court. Pics jusqu'à 500 mA annoncés avec Wi-Fi/flash, pas courant moyen ni budget OV5640. MMC 1 bit libérant GPIO13 concerne l'AI-Thinker, **pas un brochage XIAO à recopier**. Lecture AVI annoncée dans les navigateurs à vérifier : notre galerie garde une conversion MP4 qualifiée.
- **À transposer :** étudier la commande arrêt → index AVI et contrôler l'absence d'éclairage pendant SD. Pas de flash, de stream permanent ou de durée deux minutes imposée au nichoir.

### 10. pratik001010/ESP32-CAM-Outdoor-Surveillance-System — référence secondaire

Source : [README au commit 8a0062e](https://github.com/pratik001010/ESP32-CAM-Outdoor-Surveillance-System/blob/8a0062eab44b2e9ab7fa5201bc6b5b3030a26ef0/README.md).

- **Force :** AVI SD, direct/relecture MJPEG et FTP ; PIR optionnel face à la détection image. README de génération MJPEG2SD 8.x, présentation de montage pan/tilt et données de banc OV2640.
- **Faiblesse / énergie :** support OV5640/OV3660 annoncé, mais **OV3660 explicitement non testé**. Ancienne chaîne Arduino, tableau hautes définitions et limite de décodage à ne pas interpréter comme validation 5 MP sur XIAO ; aucune mesure de notre énergie ni preuve de sommeil PIR. Les ressemblances avec MJPEG2SD ne constituent pas un deuxième benchmark indépendant.
- **À transposer :** liste des interactions SD, qualité JPEG, détection et débit, à tester ensemble. Préférer la source s60sc pour l'étude courante ; exclure servos, lampe et FTP non sécurisé de la prescription V2.

### 11. JJFourie/ESP32Cam-MQTT-SPIFFS-PIR — télémétrie configurable

Source : [README au commit 42c7a12](https://github.com/JJFourie/ESP32Cam-MQTT-SPIFFS-PIR/blob/42c7a12f4b737a6401831edfabe3e47ebf8cc16e/README.md).

- **Force :** AM312, photo uploadée vers PHP, événements MQTT, température DS18B20, réglages caméra persistants et live web. OV2640 est la référence documentaire, pas un PID matériel attesté.
- **Faiblesse / énergie :** SPIFFS conserve surtout les **configurations JSON**, pas une preuve de vidéothèque SD. Pas d'AVI ni de sommeil/solaire établi ; MQTT et stream supposent une disponibilité réseau contraire à une radio éteinte entre fenêtres.
- **À transposer :** télémétrie d'incidents et version de réglages jointe aux futurs clips, sans garder MQTT en permanence et sans confondre publication d'événement avec réception durable du média.

### 12. aquatikz/ESP32-CAM-Live-cat-feeder-camera-Telegram- — conserver la photo avant notification

Sources : [README au commit 2620420](https://github.com/aquatikz/ESP32-CAM-Live-cat-feeder-camera-Telegram-/blob/2620420a8c93f0e1e3754affe4080dda11331978/README.md), [sketch consulté](https://github.com/aquatikz/ESP32-CAM-Live-cat-feeder-camera-Telegram-/blob/2620420a8c93f0e1e3754affe4080dda11331978/Cat_feeder_camera.ino).

- **Force :** AM312 → photo, stockage SD `/catcam`, notification Telegram et stream MJPEG **optionnel**. AI-Thinker est la cible de compilation ; aucun PID ne prouve le capteur livré.
- **Faiblesse / énergie :** photos, pas clips AVI ; live toujours actif en option ≠ autonomie. Aucun bilan sommeil/solaire documenté. Le sketch contient `setInsecure()` : transport sans validation du certificat à ne pas reprendre.
- **À transposer :** média local distinct de sa notification ; notre rétention doit aller plus loin et interdire l'effacement avant ACK durable. Pas de Telegram ni de stream requis pour la capture V2.

### 13. OrTarazi/ESP32-CAM_cat_feeder_project — réveil simple, périmètre limité

Sources : [README au commit fb67a7c](https://github.com/OrTarazi/ESP32-CAM_cat_feeder_project/blob/fb67a7c65fd8e23080933b32b2ac00016638b130/README.md), [implémentation consultée](https://github.com/OrTarazi/ESP32-CAM_cat_feeder_project/blob/fb67a7c65fd8e23080933b32b2ac00016638b130/cat_feeder.cpp).

- **Force :** AI-Thinker, PIR sur GPIO13, réveil EXT1 puis photo Telegram et sommeil profond ; appels de réveil/sommeil présents dans le code. Capteur exact non attesté, pas preuve OV5640.
- **Faiblesse / énergie :** ni AVI SD ni galerie locale établie ; « ultra-low power » et case profiling cochée sans Wh de cycle exploitables. README contradictoire sur servo prévu ou déjà disponible, chemin `firmware/cat_feeder.cpp` cité alors que le fichier est à la racine. `setInsecure()` présent : pas validation TLS.
- **À transposer :** scénario de test réveil → capture → fin de cycle, et contrôle du PIR resté haut. Ne pas reprendre servomoteur, flash, effarouchement ni accès Telegram supposé disponible pendant le sommeil.

### 14. Hansikajain05/Solar_ai_Scarecrow — contre-exemple pour la faune

Sources : [README au commit 43725b5](https://github.com/Hansikajain05/Solar_ai_Scarecrow/blob/43725b51f0bf3ce2747e2e725201fc7848f3ab67/README.md), [sketch consulté](https://github.com/Hansikajain05/Solar_ai_Scarecrow/blob/43725b51f0bf3ce2747e2e725201fc7848f3ab67/scarecrow.ino).

- **Force :** déclenchement PIR puis jusqu'à trois images pour confirmation `bird/no_bird`, avec seuil explicite. La porte PIR est désactivable (`USE_PIR_GATE`). AI-Thinker décrit ; traitement conditionnel OV3660 dans le code ne prouve pas ce capteur matériel.
- **Faiblesse / énergie :** modèle entraîné non inclus ; captures pour inférence, pas archive vidéo/stream. Titre « Solar » mais prescription générique panneau/chargeur/batterie/boost seulement, aucune autonomie mesurée démontrée par les sources consultées. Buzzer et LED visent à chasser les oiseaux : **incompatibles avec un nichoir**.
- **À transposer :** uniquement l'idée d'une confirmation multi-image évaluée hors ligne sur scènes vides, jamais comme condition de suppression des originaux. Aucun dispositif d'effarouchement, aucun seuil IA pris comme vérité terrain.

## Hors classement

- **themanyone/esp32_trailcam** : [README au commit 33e2492](https://github.com/themanyone/esp32_trailcam/blob/33e249203516599a13473d4e70791fc86b11ea91/README.md). Détection par comparaison d'images après réveil périodique, **sans PIR**, photos XGA sur SD avec flash. Pas de vidéo enregistrée ni serveur web livré selon le README (web futur). Utile pour comparer coût des réveils périodiques et faux positifs d'ombres, mais peut manquer un passage entre réveils et consomme pour vérifier une scène vide. Ni le flash ni l'autonomie « low power » non chiffrée ne sont transposés.
- **XiaoBird** : nom non identifié de manière fiable. Aucun auteur, dépôt, capteur, PIR ou résultat énergétique attribué ; ne pas l'assimiler à BirdSensor_xiao, BirdBox ou chytra-budka.

## Corrections par rapport aux résumés antérieurs

La comparaison actuelle prime sur les formulations historiques V1 ; celles-ci restent archivées, pas réécrites comme si elles avaient visé l'OV5640.

1. **OV3660 → OV5640** pour la consigne V2 ; PID et lot à vérifier. Support d'un pilote ≠ montage testé ; autofocus et filtre dépendent du module acheté.
2. **Photo / fichier / flux** : CameraTrap, BirdBox, BirdSensor_xiao, photostation, BirdWatch et les projets photo Telegram ne sont pas des preuves de notre enregistrement AVI. Le flux audio BirdNET n'est pas une vidéo nichoir enregistrée.
3. **PIR optionnel** dans MJPEG2SD, BirdBox, les DVR et jameszah ; porte PIR désactivable dans Scarecrow. Un déclencheur lu sur une carte allumée ne prouve ni sommeil profond ni power-gating. Photostation n'est pas un prototype sur batterie.
4. **jameszah** : « uniquement PSRAM et sans SD » ne décrit que l'ancien texte ; la v11 documente SD et accès local hors Internet. Ne pas fusionner les FPS/limites des versions.
5. **Solaire** : chytra-budka distingue essais USB/powerbank et futur nœud autonome ; Scarecrow ne fournit pas une preuve d'autonomie par son nom. BirdWatch décrit du solaire, mais ses relevés INA219 à l'éveil n'intègrent pas toute la journée.
6. **IA** : BirdBox utilise actuellement iNaturalist en ligne, non le modèle local abandonné ; XiaoBird reste non attribué. Aucun résultat IA, FPS ou durée de batterie tiers ne valide notre faible lumière.
7. **Conservation et sécurité** : SD, FTP, MQTT, Telegram ou HTTP réussi ne prouvent pas ACK durable. Les exemples désactivant la validation TLS ne sont pas des recettes V2. La SD XIAO SPI ne se câble pas comme la MMC AI-Thinker.
8. **Précision V3 autofocus** : l'OV5640 livré avec la Sense est bien à focale fixe ; seul le module long vendu séparément a un autofocus, et sa fiche indique un filtre IR-cut. Un NoIR générique peut être sans AF ; comparer son brochage avant connexion et régler alors manuellement la netteté à 10–15 cm.

## Briques retenues et exclusions — historique V2

Ordre proposé pour un futur prototype, sans assembler aujourd'hui les firmwares :

1. **Capture locale d'abord** : s60sc pour étudier JPEG→AVI, tampons, index et fermeture. Garder uniquement les fonctions nécessaires au clip, vérifier licence/configuration/commit avant toute intégration.
2. **File persistante et réseau différé** : photostation pour l'organisation des temporaires/manifeste et l'idempotence ; compléter selon la décision V2 avec SHA-256, identité persistante, authentification TLS validée, sync serveur, ACK durable et absence d'effacement sans ACK. Le mock serveur tiers n'est pas un backend de production.
3. **Activité bornée** : BirdSensor_xiao pour deadline/réarmement ; BirdWatch pour mode dégradé et télémétrie, sans copier leur électronique. Réveil profond BS612 reste la solution initiale ; coupure TPS22918 seulement si besoin établi par mesures et circuit qualifié.
4. **Galerie future sur serveur** : BirdBox pour visites, diagnostics et distinction en attente/échec, sans IA ou serveur vidéo permanent sur la carte. Le MP4 reste un dérivé de l'AVI conservé selon rétention explicite, pas un import Frigate.

Exclusions V2 : éclairage/IR/flash, audio et servos, effarouchement, BLE sur oiseaux, exposition Internet directe, cloud obligatoire, rotation des clips non acquittés, et toute promesse de cadence ou d'autonomie. La V3 lève les exclusions de l'éclairage IR et de l'audio (son enregistré avec chaque clip) et remplace le déclenchement PIR principal par la barrière IR. Cette revue n'est pas un audit exhaustif de sécurité/licences ; aucun code tiers repris.

## Essai exploratoire V2 archivé : 5 MP contre 1080p, sans oiseaux

**Protocole non exécuté.** Nichoir vide ou boîte de banc aux mêmes géométrie, distance et matériaux, mire texturée et objet mobile inerte. Ni animal attiré/enfermé, ni intervention occupée, ni ajout d'éclairage au nichoir. Au banc seulement, faire varier une source externe reproductible et relever l'éclairement au plan de la mire ; inclure le noir pour constater la limite, sans promettre une image exploitable.

- Identifier lot/PID OV5640, autofocus ou réglage manuel selon module, distance de netteté, carte/PSRAM, microSD, alimentation, firmware/commit, pilote, XCLK, qualité JPEG, gain/exposition et température. Même matériel et scène pour les deux modes ; consigner tout réglage différent. Vérifier LEDs caméra/SD et absence d'éclairage parasite avant pose.
- Comparer **photo 2592 × 1944 (5 MP)** et **photo 1920 × 1080**, à qualité JPEG fixée puis à taille de fichier comparable ; comparer détails utiles, bruit, couleur, zones saturées et flou sur objet mobile. Le cadrage 4:3 contre 16:9 change : comparer aussi la zone commune, pas seulement l'image affichée redimensionnée. Plus de pixels ne garantit pas plus de détails utilisables dans l'obscurité.
- Tester ensuite des **clips AVI de 20 s en 1080p**, avec VGA comme témoin de repli. N'essayer une séquence 5 MP que si le pilote et le firmware la permettent sans dépassement mémoire ; sinon noter « non supporté/échec », pas inventer des FPS. Le conseil s60sc au-dessus de FHD vise les photos : le 5 MP photo n'est pas notre exigence vidéo. Les 10 images/s historiques sont une cible à vérifier, pas une cadence promise en 1080p.
- Répéter au moins dix cycles par condition, après cold boot et après réveil PIR simulé au banc ; alterner l'ordre des modes. Mesurer temps PIR→première image **utilisable**, stabilisation d'exposition, capture, fermeture/sync SD, association Wi-Fi, upload et ACK. Rapporter dispersion et échecs, pas seulement meilleur résultat. Les fenêtres réseau restent bornées ; un dépassement est un échec de livraison à conserver en file, pas une permission radio illimitée.
- Mesurer **FPS réellement acquis = images valides / durée réelle de capture**, pertes et intervalles entre images, puis contrôler durée/FPS/index du fichier avec un décodeur indépendant. Une lecture accélérée/timelapse n'améliore pas la cadence acquise. Relever taille JPEG/AVI, débit SD, mémoire libre/minimale, resets et température après séries.
- Intégrer les **Wh par phase et par cycle complet**, y compris veille réelle de la carte + caméra + SD + PIR, démarrage/exposition, capture, finalisation, radio/réessais et retour au sommeil. Instrument adapté aux faibles courants et aux pics, consommation propre connue ; ne pas mélanger Wh USB et Wh cellule ni recompter les pertes. Rejouer panne Wi-Fi/serveur, ACK perdu et SD pleine pour mesurer le pire scénario borné. Aucun effacement de média non acquitté.

Fiche brute à remplir pour chaque répétition : condition lumineuse et température ; mode/dimensions/qualité ; images valides et durée réelle ; FPS acquis et du conteneur ; latence première image utile ; temps par phase ; octets ; Wh USB et, si instrumentés séparément, Wh cellule ; courant de veille/pics ; résultat de décodage/ACK ; anomalie. **Aucune valeur matérielle n'est disponible aujourd'hui.**

Retenir le mode le moins coûteux qui donne des détails utiles et une vidéo décodable dans les conditions observées. Si 1080p ou 5 MP dégradent exposition, mémoire, durée active ou température, réduire définition/cadence ou rester en photo ; si le noir est inexploitable, accepter l'absence d'image. Toute modification de durée, résolution, débit ou politique radio impose de **remesurer l'énergie**, puis de refaire besoins/jour, réserve, panneau et marges hivernales. Les tableaux V2 hérités sont des sensibilités de calcul, pas une qualification OV5640.

## Vérification documentaire reproductible

Depuis la racine : `python -m unittest discover -s tests -v`, `python tools/verifier_dossier.py`, puis `git diff --check`. Les outils et tests restent V1, avec chemins d'archives adaptés dans le vérificateur : ils vérifient leurs calculs historiques et les liens, pas le fonctionnement des dépôts externes ou de l'OV5640. Contrôler en plus les 14 fiches distinctes et leurs liens GitHub figés ; les deux exclusions ne comptent pas parmi les 14.

Résultats exécutés pour cette rédaction : **8 tests V1 réussis**, vérificateur de cohérence locale réussi, contrôle arithmétique V2 du CSV 12 mois/besoins/réserve réussi. Le contrôle documentaire a compté **14 fiches uniques**, chacune avec force/faiblesse/transposition, et vérifié **22 liens GitHub à SHA complet** contre les arborescences effectivement téléchargées ; 15 README récupérés au total, dont celui de trailcam hors classement. `git diff --check` sans erreur. Ces succès ne valident ni compilation tierce, ni matériel, ni performance ou autonomie. Commit local uniquement, pas de push ni de modification d'Unraid.
