# Recherches et décisions V3

[Accueil](../README.md) · [Décision V2](decision-v2.md) · [Comparatif des projets](comparatif-pir-ov5640.md) · [Archive V1](archive/v1/README-v1.md)

Décisions confirmées par Romain le 23/11/2026. Documentation uniquement : aucun firmware, essai matériel ou déploiement. Les sources ci-dessous étayent les choix, pas une qualification du montage.

## 1. Autonomie et réseau

Romain déclare le Wi-Fi OK à l'emplacement du nichoir ; aucune mesure RSSI n'est documentée. Aucun câble n'est possible : montage autonome solaire autour de la XIAO ESP32-S3 Sense.

L'option Raspberry Pi Zero 2 W + Camera Module 3 NoIR Wide + Frigate est écartée. Environ 1 W continu donne 24 Wh/j, estimation non mesurée supérieure à la production hivernale moyenne du P110, au plus 8,8 Wh/j en décembre même à 60°.

Frigate n'est pas retenu : pas de flux continu possible. La galerie MP4 future sur Unraid et la spécification d'ACK durable de la décision V2 §2 restent valides. Conserver AVI original, identité persistante, SHA-256, réception authentifiée TLS, persistance avant ACK, déduplication, réessais bornés et aucune suppression SD avant ACK persistant. La photo d'événement et les photos timelapse devront aussi recevoir une politique de livraison durable explicite ; aucun service Unraid n'est livré ici.

## 2. Caméra : focale fixe ou autofocus, choisir NoIR

Seeed distingue deux modules : l'OV5640 **livré avec la carte Sense est à focale fixe** ; seul le **module OV5640 long vendu séparément, avec dissipateur, a un autofocus**. La mention V2 « Sense à focale fixe » était donc juste ; une version intermédiaire de ce dossier l'avait corrigée à tort.

Sources primaires :

- [Guide Seeed XIAO ESP32S3](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started) : « The OV5640 shipped with the Sense expansion board is a fixed-focus version; only the standalone long OV5640 module (sold separately, with heat sink) supports auto-focus (AF) » ; lots OV3660/OV5640 mixtes pendant la transition.
- [Fiche du module Seeed OV5640](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/new-res/OV5640_Camera_Module_Specification.pdf) : module MJY5OAF-F3M-V1, broches 23 AF-GND et 24 AFVDD 2,8 V, objectif « 4P+IR », « IR Cut ». Les broches AF indiquent que cette fiche décrit le module autofocus ; la présence d'un filtre IR-cut sur le module fixe livré avec la Sense n'est pas documentée ici, mais reste probable pour un module grand public.

Un module à filtre IR-cut bloque largement le 940 nm. Choix V3 : OV5640 NoIR, sans filtre IR-cut, grand angle et connecteur DVP 24 broches. La compatibilité de brochage avec le connecteur Sense n'est pas vérifiée : comparer toute la table de broches du module acheté à la fiche Seeed avant branchement, pas seulement le nombre de broches.

Un module NoIR générique peut être sans autofocus ; prévoir alors un réglage manuel de mise au point à environ 10–15 cm. Le module fixe livré avec la Sense reste le repli pour les essais de jour ; le module AF séparé est une alternative pour la netteté, mais avec filtre IR-cut. Contrôler référence, lot, PID, optique, révision et champ réel à réception.

L'autofocus (module long séparé uniquement) est utile à 10–15 cm. Le [forum Seeed sur l'AF OV5640](https://forum.seeedstudio.com/t/ov5640-camera-for-xiao-esp32s3-sense-how-to-use-autofocus/272485?page=2) évoque la possibilité de figer la focale par registre VCM, à valider sur le module et le pilote réels.

## 3. Éclairage et capture

Version LED infrarouge validée. LED IR 940 nm diffusées, allumées seulement pendant la capture, alimentées depuis le 5 V et commandées par transistor/MOSFET, jamais directement par un GPIO. Référence, nombre et courant restent à choisir et mesurer ; aucun échauffement de la chambre n'est acceptable. Les caméras de nichoir du commerce éclairent en IR ; cela ne qualifie pas notre intensité ni notre montage.

Clips 720p MJPEG dans un conteneur AVI sur microSD, avec une photo 5 Mpx au début de chaque événement. La durée de travail héritée est 20 s, avec cadence réelle à mesurer. Pas de vidéo 5 Mpx. Le 1080p est écarté : un clip de 20 s pèserait probablement plusieurs dizaines de Mo, ordre de grandeur non mesuré incompatible avec le budget V2 de 10–30 s de Wi-Fi total par clip.

## 4. Détection

Barrière infrarouge au trou d'envol pour déclencher sur les entrées/sorties, plus une photo toutes les 10 min en journée pour le timelapse. PIR intérieur optionnel : un oiseau qui couve bouge peu, et le PIR est peu fiable dans 14 cm. Aucune référence de barrière n'est encore choisie.

La caméra NoIR verra l'IR de la barrière : placer celle-ci hors champ et vérifier qu'elle n'éclaire pas la chambre. Mesurer aussi sa consommation continue et les faux déclenchements ; les besoins hérités ne les qualifient pas.

## 5. Panneau, toit et PVGIS

[Voltaic P110](https://voltaicsystems.com/9-watt-panel/) : 9,54 W, 223 × 274 × 4 mm, Vmp 5,71 V, Voc 6,94 V. Le nom commercial « 10 W » ne remplace pas la valeur 9,54 W utilisée pour le calcul.

Toit monopente à 45° orienté sud ; trou d'envol sur la face est. Le toit proposé de 250 × 300 mm sur rampant doit être revalidé à 45° : prise au vent, débord, fixation, sortie câble et ventilation. Aucun nouveau débit bois n'est établi.

### Provenance et méthode

[CSV fourni, valeurs conservées](pvgis-le-havre-inclinaisons.csv). API PVGIS MRcalc v5.3, latitude 49.49, longitude 0.10, 2005–2023, PVGIS-SARAH3, aspect 0 = sud, angles 9/30/45/60°. Pour chaque mois : moyenne sur les années de H(i)_m divisée par le nombre de jours du mois, années bissextiles comprises. Les kWh/m²/j donnent numériquement les HSP/j ; ne pas utiliser H(h)_m à leur place.

[Requête MRcalc de référence à 45°](https://re.jrc.ec.europa.eu/api/v5_3/MRcalc?lat=49.49&lon=0.10&startyear=2005&endyear=2023&raddatabase=PVGIS-SARAH3&horirrad=1&optrad=0&selectrad=1&angle=45&aspect=0&outputformat=json) ; remplacer seulement angle par 9, 30 ou 60 pour les autres séries. [Documentation API JRC](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/getting-started-pvgis/api-non-interactive-service_en). La provenance est celle du CSV joint au brief ; aucune nouvelle interrogation API n'est revendiquée ici.

Production calculée : `Wh/j = 9,54 × 0,50 × HSP`. Le rendement global 50 % est une hypothèse de conversion/charge/câblage, pas une mesure ; ombre locale et blocage de charge au gel restent supplémentaires.

| Mois | HSP 9° | HSP 30° | HSP 45° | HSP 60° | Wh/j à 45° |
|---|---:|---:|---:|---:|---:|
| Janvier | 1,128 | 1,533 | 1,730 | 1,833 | 8,25 |
| Février | 1,953 | 2,490 | 2,722 | 2,807 | 12,99 |
| Mars | 3,195 | 3,710 | 3,857 | 3,803 | 18,40 |
| Avril | 4,966 | 5,352 | 5,309 | 4,990 | 25,33 |
| Mai | 5,382 | 5,413 | 5,137 | 4,619 | 24,51 |
| Juin | 5,883 | 5,773 | 5,379 | 4,747 | 25,66 |
| Juillet | 5,878 | 5,843 | 5,484 | 4,885 | 26,16 |
| Août | 4,997 | 5,206 | 5,055 | 4,661 | 24,11 |
| Septembre | 3,880 | 4,371 | 4,462 | 4,320 | 21,28 |
| Octobre | 2,404 | 2,942 | 3,151 | 3,193 | 15,03 |
| Novembre | 1,402 | 1,880 | 2,107 | 2,219 | 10,05 |
| Décembre | 1,023 | 1,473 | 1,703 | 1,837 | 8,12 |

Décembre : 9° → 4,88 Wh/j ; 45° → 8,12 Wh/j ; 60° → 8,76 Wh/j. Passer de 9° à 45° apporte environ 66 % en décembre. Juin : 5,883 HSP à 9° contre 5,379 à 45°.

Moyenne annuelle HSP annoncée dans le brief : 3,508 à 9° et 3,842 à 45°. La moyenne simple des 12 valeurs mensuelles arrondies du CSV donne 3,508 et 3,841 ; cet écart de dernière décimale est conservé explicitement, sans modifier les données. À 30°, cette même moyenne vaut 3,832 : 45° est le meilleur compromis hivernal, quasi identique à 30° en annuel. Ces moyennes supposent l'absence d'ombre locale ; elles ne garantissent ni une journée minimale ni l'autonomie hivernale.

## 6. Batterie : Voltaic V75

La V75 remplace le pack 1S5P maison et l'option « n'importe quelle power bank ». La plupart des power banks s'arrêtent à faible courant : [explication Always On Voltaic](https://voltaicsystems.com/always-on-batteries/).

Sources : [fiche V75 fabricant](https://voltaicsystems.com/v75) et [notice V25/V50/V75 2025](https://voltaicsystems.com/content/batteries/V25_50_75_Instructions_2025.pdf).

| Caractéristique | Valeur documentaire |
|---|---|
| Capacité nominale | 20 100 mAh / 72,36 Wh cellule, pas à 5 V USB |
| Sorties retenues | 2 × USB-A Always On 5 V |
| Consommation propre Always On | Environ 7 mA / 26 mW internes, soit 0,624 Wh/j |
| Entrée solaire | 5–6 V / 2 A, USB-C latéral ou DC 3,5 × 1,1 mm |
| MPP | 5,2 V |
| Coupure entrée | 0 °C et 45 °C |
| Coupure sortie | −15 °C et 60 °C |
| Reprise | Automatique après décharge et défauts de température |
| Conformité indiquée | IEC 62133, UN 38.3, CE |
| Encombrement et masse | 15,5 × 8,2 × 2,4 cm ; 502 g |
| Prix fabricant | 89 USD ; ni prix France ni total livré |
| Charge au panneau 10 W | 9 h selon la notice, pas un résultat local |

Ne pas utiliser le port USB-C PD du dessus en mode Always On. La notice indique 3,5 × 1,5 mm dans la ligne de spécifications, contre 3,5 × 1,1 ailleurs : vérifier connecteur, polarité et notice du lot à réception. Faire confirmer la compatibilité du P110 avec l'entrée V75, notamment Voc à froid et tolérances, avant connexion ; jamais de panneau brut sur la XIAO.

Coffret séparé de la chambre, ombragé, protégé de l'eau et de la condensation, jamais sous le panneau chaud. Tester au banc USB stable à faible charge, charge/alimentation simultanées et reprise après interruptions selon un protocole fabricant sûr. Aucun raccordement aux pastilles BAT XIAO ni batterie supplémentaire en parallèle de l'USB.

### Réserve et autonomie théorique

`Réserve = 0,80 × 72,36 = 57,888 Wh`, soit 57,89 Wh. Besoins hérités de V2 pour 100 clips/j : 3,19 et 4,32 Wh/j, selon 10 ou 30 s de réseau total par clip. Avec les valeurs non arrondies V2, cela donne environ 18,1 et 13,4 jours sans soleil depuis la réserve pleine.

Ces besoins restent à remesurer : ils ne prennent en compte ni les LED IR ni le 720p, et ne qualifient pas la barrière ni le timelapse. Ne pas recompter la consommation propre si elle est déjà incluse dans la mesure complète. Froid, vieillissement et rendement réel réduisent la réserve disponible.

Les cinq XTAR en DIY et le chargeur BQ25185 sont écartés pour sécurité et complexité : la V75 certifiée couvre le besoin documentaire sans assemblage de cellules.

## 7. Essais et points ouverts

Tous les essais matériels restent non exécutés. Avant tout branchement NoIR : comparer brochage, tensions et orientation de nappe à la fiche Seeed.

1. Carton fermé avec trou de 32 mm, mire à 10–15 cm, NoIR + LED 940 nm : champ, netteté, exposition, décodage AVI 720p et photo 5 Mpx, température et lumière parasite de la barrière. Pas d'oiseaux.
2. Wattmètre USB adapté à la veille et aux pics : Wh/clip, photo, LED, barrière, timelapse, démarrage, fermeture, radio et réessais ; noter la consommation de l'instrument. Refaire budget journalier et solaire.
3. Simuler entrées/sorties et oiseau immobile avec objets inertes ; mesurer latence, faux déclenchements et réarmement borné.
4. Gabarit toit 45° : débord, vent, fixation indépendante du panneau, étanchéité, ventilation et maintien de la chambre utile. Dimensionner le coffret pour la V75 et les courbures de câbles.
5. Rejouer les pannes SD/réseau et toutes les exigences de livraison durable V2 §2, sans effacement de média non acquitté ; tester protections et reprise thermique sans charge gel réelle, surcharge ni court-circuit provoqués.
6. Avant pose active : au moins 72 h sans solaire et une semaine au site vide, pluie/condensation et températures chambre/coffret relevées.

Pas de perchoir, de vis saillante ou de câble accessible ; chambre ombragée aux heures chaudes. Aucune intervention pendant l'occupation, même pour mise au point ou retrait SD. Si une porte reste ouverte, nichoir passif ou vidéo arrêtée.

Les outils et tests Python restent V1 ; seules leurs références d'archives sont adaptées. Les contrôles logiciels se rejouent depuis la racine avec `python -m unittest discover -s tests -v`, `python tools/verifier_dossier.py` et `git diff --check`. Ils ne remplacent aucun essai matériel.
