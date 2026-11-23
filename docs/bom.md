# Nomenclature (BOM)

Liste d'achat de l'électronique, du câblage et du coffret de batterie, établie à partir des choix du dépôt ([README](../README.md), [plans](plans/README.md), [recherches V3](recherches-v3.md)).

**Relevé du 24/11/2026** (entre 0 h et 1 h, heure de Paris) sur les fiches produit. Prix TTC, hors frais de port, et stock affiché à cette heure-là : ils changeront. Rien n'a encore été acheté ni essayé.

Les tableaux chiffrés sont générés depuis [bom.csv](bom.csv) par `python tools/bom.py` ; `python tools/bom.py --check` vérifie qu'ils sont à jour.

## Où acheter

| Marchand | Ce qu'on y prend | Pourquoi |
|---|---|---|
| [Gotronic](https://www.gotronic.fr/) | Carte XIAO, carte SD, LED, barrière, sondes, petits composants, câble, coffret | Tout y est en stock, sauf la batterie et le panneau |
| [Amazon.fr](https://www.amazon.fr/) | Carte de test USB-C (lecture de la batterie) ; options et testeur USB | Aucune carte USB-C mâle donnant accès aux broches SBU trouvée chez Gotronic |
| [AliExpress](https://fr.aliexpress.com/) | Module caméra de repli, seulement si besoin | Variante vendue explicitement « without IR » (sans filtre infrarouge) |
| [Bestpiles](https://bestpiles.fr/) | Rien | Pas de Voltaic ; ses batteries externes (Dudao, etc.) n'annoncent pas de mode Always On, et la plupart des batteries externes s'éteignent à faible consommation |
| [Kiwi Electronics](https://www.kiwi-electronics.com/en/brand-voltaic-systems) (Pays-Bas) | Batterie V75, panneau P110, rallonge, adaptateur | **Hors des quatre sites demandés** : ni la V75 ni le P110 ne sont chez Gotronic, Bestpiles ou AliExpress ; Amazon.fr ne propose que la V50 (48 Wh) à 170,56 €. Kiwi annonce l'envoi en France à partir de 15 € |

## À vérifier avant de commander

1. **Version de la V75 chez Kiwi.** La fiche Kiwi décrit des entrées solaires USB-C (« USB-C Input Solar (Both USB-C ports) »), 15,1 × 7,8 × 2,6 cm, 382 g, coupure de charge à 35 °C. Le fabricant décrit maintenant une [V75 aluminium](https://voltaicsystems.com/v75) avec entrée 3,5 × 1,1 mm, 502 g, coupure à 45 °C. D'où l'adaptateur Voltaic A123 (3,5 × 1,1 femelle → USB-C) de la liste : **un seul en stock**. Si la V75 reçue a une entrée 3,5 × 1,1, la rallonge s'y branche directement. Jamais d'entrée par le port USB-C du dessus : il désactive le mode Always On ([Voltaic](https://blog.voltaicsystems.com/updated-usb-c-pd-and-always-on-for-v25-v50-v75-batteries/)).
2. **Panneau et batterie compatibles :** la [fiche du P110](https://voltaicsystems.com/10-watt-panel-etfe) indique « Compatible with the V25, V50, or V75 USB Battery Pack ».
3. **Stocks faibles :** carte XIAO (8 chez Gotronic), adaptateur A123 (1 chez Kiwi).
4. **Port :** Gotronic l'affiche au panier (point relais à partir de 4,50 €, offert dès 120 €) ; Kiwi à partir de 15 € pour la France avec la batterie.
5. SeeSense, distributeur européen de Voltaic, annonçait la V75 aluminium à 110,70 € TTC dans un résultat de recherche. Sa page est protégée contre les robots : prix et stock non revérifiés, donc non retenus.

## Liste et prix

<!-- BOM:DEBUT (généré par tools/bom.py) -->

### À commander

| Marchand | Réf. | Article | Qté | Prix unit. TTC | Total | Stock relevé | Rôle |
|---|---|---|---:|---:|---:|---|---|
| Gotronic | [39234](https://www.gotronic.fr/art-carte-xiao-esp32s3-sen--soud--47620.htm) | Carte XIAO ESP32-S3 Sense 102010635 (OV3660, micro, microSD), connecteurs soudés | 1 | 17,90 € | 17,90 € | 8 | cerveau, caméra, micro |
| Gotronic | [26870](https://www.gotronic.fr/art-carte-micro-sd-sandisk-32gb-49149.htm) | Carte microSD SanDisk Ultra 32 Go (SDSQUNR-032G-GN3MN), -25 à 85 °C | 1 | 18,50 € | 18,50 € | 153 | clips ; 32 Go maxi sur la XIAO |
| Gotronic | [03458](https://www.gotronic.fr/art-diode-emettrice-tsal6200-22603.htm) | LED IR TSAL6200 940 nm, ±17° | 6 | 0,35 € | 2,10 € | 155 | 4 posées + 2 de rechange |
| Gotronic | [02157](https://www.gotronic.fr/art-transistor-bc337-25-1322.htm) | Transistor NPN BC337-25 (0,8 A) | 2 | 0,15 € | 0,30 € | 240 | commande des LED + 1 de rechange |
| Gotronic | [04024](https://www.gotronic.fr/art-10-resistances-1-4w-100-8486-2565.htm) | Lot de 10 résistances 1/4 W 100 Ω | 1 | 0,20 € | 0,20 € | 1000+ | une par LED (≈ 35 mA) |
| Gotronic | [04028](https://www.gotronic.fr/art-10-resistances-1-4w-220-8486-2568.htm) | Lot de 10 résistances 1/4 W 220 Ω | 1 | 0,20 € | 0,20 € | 1000+ | essai à intensité réduite (≈ 16 mA) |
| Gotronic | [04032](https://www.gotronic.fr/art-10-resistances-1-4w-470-8486-2571.htm) | Lot de 10 résistances 1/4 W 470 Ω | 1 | 0,20 € | 0,20 € | 1000+ | base du BC337 |
| Gotronic | [04044](https://www.gotronic.fr/art-10-resistances-1-4w-4-7k-8486-300.htm) | Lot de 10 résistances 1/4 W 4,7 kΩ | 1 | 0,20 € | 0,20 € | 1000+ | tirage 1-Wire |
| Gotronic | [04048](https://www.gotronic.fr/art-10-resistances-1-4w-10k-8486-19.htm) | Lot de 10 résistances 1/4 W 10 kΩ | 1 | 0,20 € | 0,20 € | 1000+ | rappel base, tirage barrière, série ADC |
| Gotronic | [39178](https://www.gotronic.fr/art-barriere-infrarouge-3mm-47820.htm) | Barrière infrarouge Adafruit 2167 (3 mm, 25 cm) | 1 | 4,90 € | 4,90 € | 200 | détection au trou d'envol |
| Gotronic | [31695](https://www.gotronic.fr/art-sonde-etanche-ds18b20-19339.htm) | Sonde étanche DS18B20 DFRobot DFR0198 (cordon 90 cm) | 2 | 7,95 € | 15,90 € | 250+ | chambre + coffret batterie |
| Gotronic | [12630](https://www.gotronic.fr/art-carte-d-essai-ee3070-21091.htm) | Carte d'essais EE3070 30 × 70 mm | 2 | 0,95 € | 1,90 € | 57 | nichoir + coffret |
| Gotronic | [49114](https://www.gotronic.fr/art-bornier-sc03-5-08-26024.htm) | Bornier à vis SC03/5.08 (3 contacts) | 8 | 0,45 € | 3,60 € | 1000+ | câble, barrière, sondes |
| Gotronic | [04947](https://www.gotronic.fr/art-condensateur-radial-470uf-16v-3386.htm) | Condensateur radial 470 µF / 16 V | 1 | 0,20 € | 0,20 € | 500+ | réserve sur le 5 V au nichoir |
| Gotronic | [15852](https://www.gotronic.fr/art-condensateur-ceramique-100-nf-40054.htm) | Condensateur céramique 100 nF | 2 | 0,10 € | 0,20 € | 1000+ | filtre de la mesure batterie |
| Gotronic | [49204](https://www.gotronic.fr/art-cordon-1-m-usbc-1m-33654.htm) | Cordon USB-A / USB-C 1 m, 3 A | 1 | 4,30 € | 4,30 € | 250+ | coupé en deux : fiche USB-A côté batterie, fiche USB-C côté carte |
| Gotronic | [48415](https://www.gotronic.fr/art-cable-blinde-cb4cr-15162.htm) | Câble blindé CB4CR 4 × 0,28 mm², Ø 4,2 mm (prix au mètre) | 2 | 0,50 € | 1,00 € | 250+ | liaison coffret → nichoir |
| Gotronic | [11345](https://www.gotronic.fr/art-presse-etoupe-pg7b-6376.htm) | Presse-étoupe PG7 (câble 3,5–7 mm, perçage 12,5 mm) | 3 | 1,05 € | 3,15 € | 160 | nichoir + 2 au coffret |
| Gotronic | [11871](https://www.gotronic.fr/art-boitier-etanche-abs-ip207337-6695.htm) | Boîtier étanche ABS IP65, int. 193 × 114 × 51 mm | 1 | 10,90 € | 10,90 € | 36 | coffret de la V75 |
| Gotronic | [08913](https://www.gotronic.fr/art-pochette-de-gaine-thermo-rouge-gt40r-5176.htm) | Pochette de 100 gaines thermorétractables GT100M | 1 | 4,90 € | 4,90 € | 116 | épissures |
| Gotronic | [08770](https://www.gotronic.fr/art-fil-de-cablage-fc25n-5076.htm) | Fil souple 0,20 mm² noir (prix au mètre) | 2 | 0,30 € | 0,60 € | 1000+ | câblage interne |
| Gotronic | [08776](https://www.gotronic.fr/art-fil-de-cablage-fc25r-5082.htm) | Fil souple 0,20 mm² rouge (prix au mètre) | 2 | 0,30 € | 0,60 € | 1000+ | câblage interne |
| Kiwi Electronics | [KW-2936](https://www.kiwi-electronics.com/en/v75-usb-battery-pack-10102) | Voltaic V75 USB Battery Pack 20 100 mAh / 72 Wh | 1 | 105,59 € | 105,59 € | 119 | batterie Always On |
| Kiwi Electronics | [KW-3003](https://www.kiwi-electronics.com/en/10-watt-6-volt-solar-panel-etfe-10924) | Voltaic P110 panneau 10 W 6 V ETFE, 223 × 274 mm, câble 30 cm | 1 | 76,79 € | 76,79 € | 28 | panneau du toit |
| Kiwi Electronics | [KW-2069](https://www.kiwi-electronics.com/en/extension-cable-for-voltaic-solar-panel-300cm-3-5x1-1mm-plug-3367) | Rallonge Voltaic W031 3 m, 3,5 × 1,1 mm étanche | 1 | 12,59 € | 12,59 € | 20 | toit → coffret |
| Kiwi Electronics | [KW-3009](https://www.kiwi-electronics.com/en/female-3-5x1-1mm-usb-c-10930) | Adaptateur Voltaic A123 3,5 × 1,1 mm femelle → USB-C | 1 | 3,95 € | 3,95 € | 1 | entrée solaire USB-C de la V75 (inutile si la V75 reçue a une entrée 3,5 × 1,1) |
| Amazon.fr | [B0H8RP4QQ1](https://www.amazon.fr/dp/B0H8RP4QQ1) | Carte de test USB-C 3.1 mâle 24 broches QIANRENON (SBU sorties) | 1 | 10,19 € | 10,19 € | en stock | lecture de la tension batterie |

### Options

| Marchand | Réf. | Article | Qté | Prix unit. TTC | Total | Stock relevé | Rôle |
|---|---|---|---:|---:|---:|---|---|
| Gotronic | [38058](https://www.gotronic.fr/art-capteur-pir-bs612-36148.htm) | Capteur PIR BS612 (Adafruit 5578), ≤ 11 µA | 1 | 2,70 € | 2,70 € | 21 | détection secondaire |
| Amazon.fr | [B08KJPDPH9](https://www.amazon.fr/dp/B08KJPDPH9) | WEICON Insulation Spray 400 ml (vernis acrylique) | 1 | 20,99 € | 20,99 € | en stock | protection des cartes |
| Amazon.fr | [B0DMLQ1FB2](https://www.amazon.fr/dp/B0DMLQ1FB2) | Toile inox 304 maille 1 mm, 30 × 250 cm | 1 | 10,55 € | 10,55 € | en stock | grilles des deux aérations Ø8 |

### Outillage de mesure

| Marchand | Réf. | Article | Qté | Prix unit. TTC | Total | Stock relevé | Rôle |
|---|---|---|---:|---:|---:|---|---|
| Amazon.fr | [B0FB43CZ9L](https://www.amazon.fr/dp/B0FB43CZ9L) | Testeur USB FNIRSI FNB58 (résolution 0,00001 A annoncée) | 1 | 53,99 € | 53,99 € | 12 | mesures de consommation |

### Seulement si la caméra ne voit pas l’infrarouge

| Marchand | Réf. | Article | Qté | Prix unit. TTC | Total | Stock relevé | Rôle |
|---|---|---|---:|---:|---:|---|---|
| AliExpress | [1005003040149873](https://fr.aliexpress.com/item/1005003040149873.html) | Module caméra OV2640 DVP 24 broches, variante « 21MM-66-without IR » | 1 | 16,99 € | 16,99 € | — | seulement si l'OV3660 ne voit pas les LED 940 nm |

### Totaux (TTC, hors frais de port)

| Statut | Marchand | Total |
|---|---|---:|
| À commander | Gotronic | 91,95 € |
| À commander | Kiwi Electronics | 198,92 € |
| À commander | Amazon.fr | 10,19 € |
| Options | Gotronic | 2,70 € |
| Options | Amazon.fr | 31,54 € |
| Outillage de mesure | Amazon.fr | 53,99 € |
| Seulement si la caméra ne voit pas l’infrarouge | AliExpress | 16,99 € |

**Total à commander : 301,06 € TTC hors port**, soit 27 lignes.

<!-- BOM:FIN -->

## Câblage prévu

Le câble CB4CR relie le coffret au nichoir par ses quatre conducteurs : **+5 V, masse, tension batterie / 2, 1-Wire**. Son blindage est relié à la masse côté nichoir seulement.

**Dans le coffret**

| Depuis | Vers | Remarque |
|---|---|---|
| Port USB-A Always On de la V75 | Moitié USB-A du cordon coupé → +5 V et masse du CB4CR | Brancher une fiche USB-A met la V75 en mode Always On ([Voltaic](https://blog.voltaicsystems.com/updated-usb-c-pd-and-always-on-for-v25-v50-v75-batteries/)) |
| Port USB-C du dessus de la V75 | Carte de test USB-C : broche SBU (A8 ou B8) → conducteur « batterie / 2 » ; masse | Lecture seule : ne rien brancher sur CC ni VBUS. Voltaic : SBU = moitié de la tension des cellules, de 1,6 V (vide) à 2,1 V (pleine). Mesurer A8 et B8 au multimètre à réception |
| Panneau P110 (câble 30 cm) | Rallonge 3 m → adaptateur A123 → USB-C latéral de la V75 | Rallonge coupée à 15 cm de sa fiche mâle, passée dans le presse-étoupe, puis ressoudée conducteur par conducteur (vérifier au multimètre) |
| Sonde DS18B20 n° 2 | +5 V, masse, 1-Wire du CB4CR | Sur le 5 V, la ligne de données tirée à 3,3 V reste lisible : la [fiche DS18B20](https://cdn.sparkfun.com/datasheets/Sensors/Temp/DS18B20.pdf) donne un niveau haut dès 2,2 V |

**Dans le compartiment technique du nichoir**

| Broche XIAO | Branchement | Remarque |
|---|---|---|
| USB-C | Moitié USB-C du cordon coupé, reliée au +5 V et à la masse du CB4CR | Alimentation par le chemin USB normal de la carte ; condensateur 470 µF sur le +5 V |
| D0 (GPIO1) | Conducteur « batterie / 2 » via 10 kΩ, 100 nF vers la masse | Convertisseur ADC1 : utilisable pendant le Wi-Fi |
| D1 (GPIO2) | Sortie de la barrière (fil blanc) + 10 kΩ vers 3,3 V | Collecteur ouvert ; broche de réveil |
| D2 (GPIO3) | Base du BC337 via 470 Ω ; 10 kΩ base-émetteur | Les LED restent éteintes au démarrage ; GPIO3 est une broche de configuration (Seeed) |
| D3 (GPIO4) | Alimentation de l'émetteur de la barrière (fil rouge) | 10 mA sous 3,3 V : allumé par impulsions pour économiser l'énergie |
| D4 (GPIO5) | Bus 1-Wire (deux DS18B20) + 4,7 kΩ vers 3,3 V | Sonde n° 1 alimentée en 3,3 V |
| D5 (GPIO6) | PIR BS612 (option) | Broche de réveil |
| D6 (GPIO43) | Libre | Sortie du port série : la puce y écrit ses messages de démarrage |
| D7 (GPIO44) | Libre | Entrée du port série |
| D8 à D10 | Réservées | Utilisées par le lecteur microSD de la carte Sense |

Brochage d'après le [wiki Seeed](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/) : à relire avant de souder.

**LED** : quatre TSAL6200, chacune avec sa résistance de 100 Ω, du +5 V au collecteur du BC337 (émetteur à la masse). Elles traversent la cloison, tournées vers le nid, derrière un diffuseur (papier calque ou ruban PTFE).

## Calculs

- **LED** : [fiche Vishay](https://www.vishay.com/docs/81010/tsal6200.pdf) : 940 nm, ±17°, 100 mA maxi, 1,35 V typique à 100 mA. Avec 100 Ω sous 5 V : (5 − 1,3 − 0,2) / 100 ≈ 35 mA par LED, 0,12 W dans la résistance (1/4 W) ; environ 140 mA pour les quatre. Avec 220 Ω : environ 16 mA par LED pour un essai moins lumineux.
- **Transistor** : base à (3,3 − 0,8) / 470 ≈ 5 mA, plus de cinq fois les 0,9 mA nécessaires à 140 mA avec le gain minimal de 160 du BC337-25.
- **Câble** : 0,28 mm² de cuivre, environ 0,06 Ω par mètre. Pour 1 m de liaison, aller et retour, 0,12 Ω : environ 0,06 V de chute à 0,5 A. Conducteurs rigides : à fixer, pas à plier souvent.
- **Barrière** : 10 mA sous 3,3 V ([fiche Gotronic](https://www.gotronic.fr/art-barriere-infrarouge-3mm-47820.htm)), soit 33 mW, et jusqu'à 50 mW prélevés au 5 V si le régulateur de la carte est linéaire : 0,8 à 1,2 Wh/j si elle reste allumée. C'est 19 à 38 % du budget V2 de 3,19–4,32 Wh/j : d'où l'allumage par impulsions (temps de réponse annoncé < 2 ms), à valider.
- **Repères de consommation** (à mesurer) : carte Sense en sommeil profond 3 mA, alimentée en 3,8 V avec la carte d'extension ([Seeed](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/)), vidéo 138 mA, photo 341 mA ([Gotronic](https://www.gotronic.fr/art-carte-xiao-esp32s3-sen--soud--47620.htm)) ; LED environ 140 mA pendant la capture ; V75 en mode Always On, environ 7 mA (26 mW).

## Montage

- **Presse-étoupe PG7** : perçage 12,5 mm. Dans la paroi de 20 mm du nichoir, lamer l'intérieur (environ Ø 25) pour que l'écrou prenne : mesurer d'abord la longueur filetée du presse-étoupe reçu.
- **Cordon USB coupé** : repérer au multimètre les fils du +5 V (broche 1) et de la masse (broche 4) de chaque fiche ; isoler D+ et D−.
- **Sonde de la chambre** : trou Ø 6,5 dans la cloison, extrémité de la sonde au ras du plafond ; le cordon reste dans le compartiment (aucun câble dans la chambre).
- **Carte de test USB-C** : elle reste branchée dans la V75 : la caler dans le coffret pour qu'elle ne fasse pas levier sur le port.
- **Vernis** (option) : ni sur l'objectif, ni sur le micro, ni sur le lecteur de carte, les connecteurs et la prise d'antenne.

## Hors électronique (non chiffré, magasin de bricolage)

D'après les [plans](plans/README.md) : planche de 20 mm d'au moins 180 × 2 050 mm ; toit 300 × 250 ; contreplaqué marine de 10 mm (100 × 80) pour la plaque de trappe ; barre de fixation 40 × 600 × 20 ; vis inox 4 × 40, dont deux pivots avec rondelles ; crochet ou vis de blocage de la porte ; couverture EPDM ou tôle ; joint mousse ; silicone neutre ; platine et cales de 10 mm pour le panneau ; fil ou sangle de fixation au support ; huile de lin facultative.

Visserie du panneau : le kit Voltaic « ETFE Panel Screw & Washer Set » est en rupture chez Kiwi ; choisir des vis inox selon les trous du panneau.

## Écartés

| Article | Raison |
|---|---|
| Voltaic V50 sur Amazon.fr (170,56 €) | 48 Wh au lieu de 72, plus cher que la V75 |
| SanDisk High Endurance 32 Go sur Amazon.fr (29,00 €) | La SanDisk Ultra de Gotronic (18,50 €) supporte aussi −25 à 85 °C ; changer de carte si l'usure se manifeste |
| Minuterie TPL5110 (Gotronic 38876, 6,85 €) | Coupe toute la carte entre deux réveils programmés : incompatible avec le réveil par la barrière |
| Connecteur femelle sécable FH050 (Gotronic, 6,30 €) | Les borniers à vis suffisent pour débrancher la barrière |
| Batteries externes Bestpiles | Mode Always On non annoncé |

## Points ouverts

- **Redémarrage matériel de la caméra** (idée de BirdBox) : aucun circuit retenu, et une coupure séparée de la caméra sur la carte Sense n'a pas été étudiée. Redémarrage logiciel seulement pour l'instant.
- **Vision infrarouge de l'OV3660** : test de la télécommande à réception. Si elle échoue, module OV2640 sans filtre IR (2 Mpx ; capteur pris en charge par la carte Sense selon Seeed) : vérifier la longueur et le brochage de la nappe.
- **Éclairage** : faisceau de ±17° étroit pour 14 cm de large ; valider l'éclairage du fond avec le diffuseur, dans le carton d'essai.
- **Toutes les consommations** restent à mesurer au testeur USB.
