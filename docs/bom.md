# Nomenclature (BOM)

Liste d'achat de l'électronique, de l'alimentation et du coffret des accus, établie à partir des choix du dépôt ([README](../README.md), [plans](plans/README.md), [recherches V3](recherches-v3.md)).

**Relevé du 24/11/2026** (de 0 h à 2 h, heure de Paris) sur les fiches produit. Prix TTC, hors frais de port, et stock affiché à cette heure-là : ils changeront. Rien n'a encore été acheté ni essayé.

Les tableaux chiffrés sont générés depuis [bom.csv](bom.csv) par `python tools/bom.py` ; `python tools/bom.py --check` vérifie qu'ils sont à jour.

## Choix de Romain (24/11/2026)

- **Pas d'infrarouge** : ni LED IR ni barrière IR. La détection passe par un **capteur PIR**.
- **Pas de sondes de température** pour la télémétrie.
- **Batterie** : 4 accus [XTAR 18650 4000 mAh](https://bestpiles.fr/piles-rechargeables-18650/1663-pile-rechargeable-18650-xtar-lithium-37v-4000mah-10a-6952918302384.html) en parallèle (1S4P), une carte de charge solaire et une sortie 5 V. La Voltaic V75 est abandonnée.
- **Panneau** : le plus grand panneau 6 V qui tient sur le toit, marque indifférente.

## Le panneau : le P110 reste le meilleur choix vérifié

Le toit mesure 300 mm dans la pente sur 250 mm. Le [Voltaic P110](https://voltaicsystems.com/10-watt-panel-etfe) (223 × 274 mm, 9,54 W crête, Vmp 5,71 V) y tient avec 13 mm de marge. Aucun panneau 6 V plus puissant et compatible avec le toit n'a été trouvé :

| Panneau examiné | Dimensions | Pourquoi non |
|---|---|---|
| [AliExpress 6 V « 12 W »](https://fr.aliexpress.com/item/1005012287230935.html), 52,39 € | 345 × 215 mm | Plus long que le toit (300) |
| [AliExpress 6 V « 10 W »](https://fr.aliexpress.com/item/1005006173787287.html) | 320 × 160 mm | Plus long que le toit, plus petit en surface |
| [Gotronic SOL10P](https://www.gotronic.fr/art-panneau-solaire-10-w-sol10p-26488.htm) et [SM10P](https://www.gotronic.fr/art-panneau-solaire-10w-sol10w-13063.htm) | 356 × 253 et 354 × 251 mm | Trop grands, et panneaux 18 V |
| Panneaux « 10 W 6 V » de 165 × 165 mm (Amazon.fr) | 165 × 165 mm | 10 W sur 0,027 m² demanderaient 37 % de rendement : puissance annoncée non crédible |

Un panneau de 300 × 250 mm affleurerait les bords du toit, sans marge pour l'eau et la fixation.

## Où acheter

| Marchand | Ce qu'on y prend |
|---|---|
| [Gotronic](https://www.gotronic.fr/) | Carte XIAO, carte SD, PIR, chargeur solaire, régulateur 5 V, petits composants, câble, coffret |
| [Bestpiles](https://bestpiles.fr/) | Les 4 accus XTAR et un chargeur XTAR pour les préparer |
| [Amazon.fr](https://www.amazon.fr/) | Options et testeur USB |
| [Kiwi Electronics](https://www.kiwi-electronics.com/en/brand-voltaic-systems) (Pays-Bas) | Panneau P110 et sa rallonge. **Hors des quatre sites demandés** : le P110 n'est ni chez Gotronic, ni chez Bestpiles, ni sur AliExpress, ni sur Amazon.fr. Envoi en France à partir de 15 € |
| Mouser ou DigiKey | Supports d'accus (voir plus bas). **Hors liste**, prix non relevé |

AliExpress n'est plus utilisé : le module caméra sans filtre IR n'a plus d'objet.

## Liste et prix

<!-- BOM:DEBUT (généré par tools/bom.py) -->

### À commander

| Marchand | Réf. | Article | Qté | Prix unit. TTC | Total | Stock relevé | Rôle |
|---|---|---|---:|---:|---:|---|---|
| Gotronic | [39234](https://www.gotronic.fr/art-carte-xiao-esp32s3-sen--soud--47620.htm) | Carte XIAO ESP32-S3 Sense 102010635 (OV3660, micro, microSD), connecteurs soudés | 1 | 17,90 € | 17,90 € | 8 | cerveau, caméra, micro |
| Gotronic | [26870](https://www.gotronic.fr/art-carte-micro-sd-sandisk-32gb-49149.htm) | Carte microSD SanDisk Ultra 32 Go (SDSQUNR-032G-GN3MN), -25 à 85 °C | 1 | 18,50 € | 18,50 € | 153 | clips ; 32 Go maxi sur la XIAO |
| Gotronic | [38058](https://www.gotronic.fr/art-capteur-pir-bs612-36148.htm) | Capteur PIR BS612 (Adafruit 5578), ≤ 11 µA | 1 | 2,70 € | 2,70 € | 21 | détection des entrées et sorties (seule détection) |
| Gotronic | [37263](https://www.gotronic.fr/art-chargeur-d-accu-lipo-3-7-vcc-ada4755-33478.htm) | Chargeur solaire Li-ion Adafruit 4755 (bq24074), entrée 5–10 V, charge 1 A, sortie ≤ 4,4 V | 1 | 17,90 € | 17,90 € | 28 | charge des accus par le panneau |
| Gotronic | [32784](https://www.gotronic.fr/art-regulateur-5-v-s7v8f5-21748.htm) | Régulateur 5 V Pololu S7V8F5 (2123), entrée 2,7–11,8 V, 500 mA à 1 A | 1 | 9,60 € | 9,60 € | 67 | sortie 5 V pour la carte |
| Gotronic | [05339](https://www.gotronic.fr/art-thermistance-ctn-10k-8486-3739.htm) | Thermistance CTN 10 kΩ (B = 4300, ±10 %) | 1 | 0,80 € | 0,80 € | 182 | coupe la charge par froid ou chaleur (entrée THERM du chargeur) |
| Gotronic | [09341](https://www.gotronic.fr/art-fusible-temporise-2-a-5484.htm) | Fusible temporisé 2 A 5 × 20 mm | 2 | 0,25 € | 0,50 € | 250+ | sortie du pack (+ 1 de rechange) |
| Gotronic | [09402](https://www.gotronic.fr/art-porte-fusible-pf3-5544.htm) | Porte-fusible PF3 pour circuit imprimé, 5 × 20 mm, 10 A | 1 | 0,30 € | 0,30 € | 250+ | fusible du pack |
| Gotronic | [04060](https://www.gotronic.fr/art-10-resistances-1-4w-100k-8486-20.htm) | Lot de 10 résistances 1/4 W 100 kΩ | 1 | 0,20 € | 0,20 € | 500+ | pont diviseur de la mesure batterie |
| Gotronic | [15852](https://www.gotronic.fr/art-condensateur-ceramique-100-nf-40054.htm) | Condensateur céramique 100 nF | 2 | 0,10 € | 0,20 € | 1000+ | filtre de la mesure batterie |
| Gotronic | [04947](https://www.gotronic.fr/art-condensateur-radial-470uf-16v-3386.htm) | Condensateur radial 470 µF / 16 V | 1 | 0,20 € | 0,20 € | 500+ | réserve sur le 5 V au nichoir |
| Gotronic | [12630](https://www.gotronic.fr/art-carte-d-essai-ee3070-21091.htm) | Carte d'essais EE3070 30 × 70 mm | 2 | 0,95 € | 1,90 € | 57 | nichoir + coffret |
| Gotronic | [49114](https://www.gotronic.fr/art-bornier-sc03-5-08-26024.htm) | Bornier à vis SC03/5.08 (3 contacts) | 6 | 0,45 € | 2,70 € | 1000+ | câble, PIR, pack et panneau |
| Gotronic | [49204](https://www.gotronic.fr/art-cordon-1-m-usbc-1m-33654.htm) | Cordon USB-A / USB-C 1 m, 3 A | 1 | 4,30 € | 4,30 € | 250+ | moitié USB-C seulement : alimentation de la carte |
| Gotronic | [48415](https://www.gotronic.fr/art-cable-blinde-cb4cr-15162.htm) | Câble blindé CB4CR 4 × 0,28 mm² rigide, Ø 4,2 mm (prix au mètre) | 2 | 0,50 € | 1,00 € | 250+ | liaison coffret → nichoir (5 V, masse, batterie / 2, réserve) |
| Gotronic | [11345](https://www.gotronic.fr/art-presse-etoupe-pg7b-6376.htm) | Presse-étoupe PG7 (câble 3,5–7 mm, perçage 12,5 mm) | 3 | 1,05 € | 3,15 € | 160 | nichoir + coffret (câble et panneau) |
| Gotronic | [11871](https://www.gotronic.fr/art-boitier-etanche-abs-ip207337-6695.htm) | Boîtier étanche ABS IP65, int. 193 × 114 × 51 mm | 1 | 10,90 € | 10,90 € | 36 | coffret des accus et du chargeur |
| Gotronic | [08913](https://www.gotronic.fr/art-pochette-de-gaine-thermo-rouge-gt40r-5176.htm) | Pochette de 100 gaines thermorétractables GT100M | 1 | 4,90 € | 4,90 € | 116 | épissures |
| Gotronic | [08770](https://www.gotronic.fr/art-fil-de-cablage-fc25n-5076.htm) | Fil souple 0,20 mm² noir (prix au mètre) | 2 | 0,30 € | 0,60 € | 1000+ | câblage interne |
| Gotronic | [08776](https://www.gotronic.fr/art-fil-de-cablage-fc25r-5082.htm) | Fil souple 0,20 mm² rouge (prix au mètre) | 2 | 0,30 € | 0,60 € | 1000+ | câblage interne |
| Gotronic | [08940](https://www.gotronic.fr/art-fil-de-cablage-fc50n-5199.htm) | Fil souple 0,50 mm² noir (prix au mètre) | 1 | 0,40 € | 0,40 € | 1000+ | câblage du pack |
| Gotronic | [08946](https://www.gotronic.fr/art-fil-de-cablage-fc50r-5203.htm) | Fil souple 0,50 mm² rouge (prix au mètre) | 1 | 0,40 € | 0,40 € | 1000+ | câblage du pack |
| Bestpiles | [6952918302384](https://bestpiles.fr/piles-rechargeables-18650/1663-pile-rechargeable-18650-xtar-lithium-37v-4000mah-10a-6952918302384.html) | Accu 18650 XTAR 4000 mAh protégé, + en relief | 4 | 8,03 € | 32,12 € | disponible | pack 1S4P |
| Bestpiles | [6952918340744](https://bestpiles.fr/chargeur-de-piles-et-batteries/1084-chargeur-de-piles-xtar-mc2-plus-6952918340744.html) | Chargeur XTAR MC2 Plus, 2 baies, coupure 4,20 V ± 0,05 V | 1 | 6,95 € | 6,95 € | disponible | charger chaque accu avant la mise en parallèle |
| Kiwi Electronics | [KW-3003](https://www.kiwi-electronics.com/en/10-watt-6-volt-solar-panel-etfe-10924) | Voltaic P110 panneau 10 W 6 V ETFE, 223 × 274 mm, câble 30 cm | 1 | 76,79 € | 76,79 € | 28 | panneau du toit |
| Kiwi Electronics | [KW-2069](https://www.kiwi-electronics.com/en/extension-cable-for-voltaic-solar-panel-300cm-3-5x1-1mm-plug-3367) | Rallonge Voltaic W031 3 m, 3,5 × 1,1 mm étanche | 1 | 12,59 € | 12,59 € | 20 | toit → coffret, coupée et soudée sur le chargeur |

### Options

| Marchand | Réf. | Article | Qté | Prix unit. TTC | Total | Stock relevé | Rôle |
|---|---|---|---:|---:|---:|---|---|
| Amazon.fr | [B08KJPDPH9](https://www.amazon.fr/dp/B08KJPDPH9) | WEICON Insulation Spray 400 ml (vernis acrylique) | 1 | 20,99 € | 20,99 € | en stock | protection des cartes |
| Amazon.fr | [B0DMLQ1FB2](https://www.amazon.fr/dp/B0DMLQ1FB2) | Toile inox 304 maille 1 mm, 30 × 250 cm | 1 | 10,55 € | 10,55 € | en stock | grilles des deux aérations Ø8 |

### Outillage de mesure

| Marchand | Réf. | Article | Qté | Prix unit. TTC | Total | Stock relevé | Rôle |
|---|---|---|---:|---:|---:|---|---|
| Amazon.fr | [B0FB43CZ9L](https://www.amazon.fr/dp/B0FB43CZ9L) | Testeur USB FNIRSI FNB58 (résolution 0,00001 A annoncée) | 1 | 53,99 € | 53,99 € | 12 | mesures de consommation |

### Totaux (TTC, hors frais de port)

| Statut | Marchand | Total |
|---|---|---:|
| À commander | Gotronic | 99,65 € |
| À commander | Bestpiles | 39,07 € |
| À commander | Kiwi Electronics | 89,38 € |
| Options | Amazon.fr | 31,54 € |
| Outillage de mesure | Amazon.fr | 53,99 € |

**Total à commander : 228,10 € TTC hors port**, soit 26 lignes.

<!-- BOM:FIN -->

**À ajouter, non chiffré : 4 supports MPD BH-18650-W** (un par accu). Les XTAR protégées mesurent 69,2 ± 0,5 mm, soit jusqu'à 69,7 mm, et ont une capacité minimale de 3 800 mAh (fabricant : [tableau XTAR](https://www.xtar.cc/18650-battery.html) et fiche technique ; ces deux valeurs ne figurent pas sur la page Bestpiles). Les supports de Gotronic n'acceptent que 65 mm (indiqué sur leurs fiches) et le Keystone 1042 au plus 67 mm ([Cell Supply](https://cell-supply.co.nz/product/18650holder)). MPD indique que le [BH-18650-W](https://www.batteryholders.com/part.php?pn=BH-18650-W) est conçu pour les 18650 protégées à téton. Il est distribué par Mouser et DigiKey, dont les pages bloquent les relevés automatiques : prix et stock à vérifier à la commande. Essayer un accu dans le premier support reçu avant de câbler : il doit accepter 69,7 mm.

## Les accus : règles de montage

1. **Quatre accus identiques**, achetés ensemble.
2. **Avant la mise en parallèle**, charger chacun au chargeur XTAR MC2 Plus (coupure 4,20 V ± 0,05 V), puis mesurer leurs tensions au multimètre : elles doivent être quasi égales (règle prudente : moins de 0,05 V d'écart). Sinon, des courants forts circulent d'un accu à l'autre au branchement.
3. **Jamais de soudure sur un accu** : uniquement des supports.
4. Les XTAR ont chacune leur protection intégrée (Bestpiles) ; le fusible de 2 A protège en plus le câblage du pack.

## Câblage prévu

Le câble CB4CR relie le coffret au nichoir par ses quatre conducteurs : **+5 V, masse, tension batterie / 2, réserve**. Son blindage est relié à la masse côté nichoir seulement.

**Dans le coffret**

| Depuis | Vers | Remarque |
|---|---|---|
| Panneau P110 → rallonge 3 m | VBUS et GND du chargeur | La rallonge est coupée, passée dans le presse-étoupe et soudée. VBUS est la ligne de la prise jack et de l'USB-C ([Adafruit](https://learn.adafruit.com/adafruit-bq24074-universal-usb-dc-solar-charger-breakout/pinouts)) : entrée 5 à 10 V. Repérer le + au multimètre avant de souder. Ne jamais brancher l'USB-C du chargeur en même temps |
| 4 accus en parallèle (supports) | Fusible 2 A → borne LIPO du chargeur ; − → GND | Fil de 0,5 mm² |
| Thermistance CTN 10 kΩ | Entre THERM et GND du chargeur, collée contre les accus | Couper le pont THERM de la carte (Adafruit) |
| Sortie OUT du chargeur (au plus 4,4 V) | Entrée du régulateur S7V8F5 → +5 V du câble | Masse commune |
| Pont 100 kΩ / 100 kΩ entre LIPO et GND | Point milieu → conducteur « batterie / 2 » | 4,2 V → 2,1 V ; 3,0 V → 1,5 V ; environ 21 µA |

**Dans le compartiment technique du nichoir**

| Broche XIAO | Branchement | Remarque |
|---|---|---|
| USB-C | Moitié USB-C du cordon coupé, reliée au +5 V et à la masse du câble | Chemin d'alimentation normal de la carte ; condensateur 470 µF sur le +5 V |
| D0 (GPIO1) | Conducteur « batterie / 2 », 100 nF vers la masse | Convertisseur ADC1 : utilisable pendant le Wi-Fi |
| D1 (GPIO2) | Sortie du PIR BS612 (alimenté en 3,3 V) | Broche de réveil |
| D2 à D5 | Libres | |
| D6 (GPIO43), D7 (GPIO44) | Libres | Port série : la puce écrit sur D6 au démarrage |
| D8 à D10 | Réservées | Lecteur microSD de la carte Sense |

Brochage d'après le [wiki Seeed](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/) : à relire avant de souder.

## Calculs

- **Chargeur** : bq24074. [Adafruit](https://www.adafruit.com/product/4755) le dit « presque MPPT » : il réduirait le courant quand la tension du panneau descend sous 4,5 V. Mais la [fiche TI](https://www.ti.com/lit/ds/symlink/bq24074.pdf) ne spécifie cette régulation de la tension d'entrée qu'en modes USB100 et USB500 (EN2 au niveau bas). Par défaut, la carte Adafruit est en mode EN1 bas / EN2 haut : courant d'entrée limité par une résistance de 1 kΩ, sans régulation de tension d'entrée spécifiée. Deux possibilités, à départager par un essai par soleil faible : garder le réglage par défaut, ou passer en USB500 (EN1 haut, EN2 bas), qui active la régulation à 4,5 V mais limite l'entrée à 500 mA, soit au plus 2,9 W tirés du panneau. Charge réglée à 1 A (réglable de 0,5 à 1,5 A). C'est un chargeur linéaire : en plein soleil, il dissipe jusqu'à (5,7 − 3,7) V × 1 A ≈ 2 W pendant la charge. Le poser à distance des accus dans le coffret.
- **Froid et chaleur** : le bq24074 suspend la charge hors de 0–50 °C avec une thermistance 10 kΩ de courbe 103AT ([fiche TI](https://www.ti.com/lit/ds/symlink/bq24074.pdf), seuils 2,1 V et 0,3 V sous 75 µA, soit 28 kΩ et 4 kΩ). La CTN de Gotronic (B = 4300) atteint ces valeurs vers +5 °C et +45 °C (calcul, ±10 % de tolérance) : fenêtre plus étroite, donc plus prudente. Avec l'hystérésis de 300 mV de TI, la charge reprend vers 1,8 V, soit 24 kΩ et environ +8 °C. **La charge sera donc coupée sous environ +5 °C et ne reprendra que vers +8 °C**, fréquent au Havre en hiver. Option : une résistance d'environ 110 kΩ en parallèle sur la CTN abaisserait le seuil vers 0 °C (calcul, non retenu dans la liste).
- **Régulateur 5 V** : 500 mA à 1 A selon la tension d'entrée, moins de 0,2 mA à vide ([Pololu](https://www.pololu.com/product/2123)). Pointe de la carte en photo : 341 mA ([Gotronic](https://www.gotronic.fr/art-carte-xiao-esp32s3-sen--soud--47620.htm)).
- **Réserve** : 4 × 3,8 Ah (capacité minimale XTAR) × 3,6 V = 54,7 Wh ; 80 % utilisables = 43,8 Wh.
- **Besoin** : formule de la [décision V2](decision-v2.md) pour 100 clips/j, sans les 0,62 Wh/j consommés par la V75, plus environ 0,02 Wh/j pour le régulateur et le pont diviseur : 2,59 Wh/j (10 s d'envoi par clip) à 3,71 Wh/j (30 s). Soit **environ 12 à 17 jours sans soleil** depuis le pack plein. Hypothèses V2 (veille 5 mA, actif 350 mA, rendement de conversion 85 %) à remesurer.
- **Production** : P110 à 45° en décembre, environ 8 Wh/j avec 50 % de rendement global ([PVGIS](pvgis-le-havre-inclinaisons.csv)). Avec un chargeur linéaire, ces 50 % restent à vérifier, et la coupure par froid (ci-dessus) réduira encore la production réelle d'hiver.
- **Câble** : 0,28 mm² de cuivre, environ 0,06 Ω par mètre ; pour 1 m de liaison, 0,06 V de chute à 0,5 A. Conducteurs rigides : à fixer, pas à plier. Deux mètres commandés : coffret à 1 m au plus du nichoir, avec la marge des boucles d'égouttement. La chute de tension sur la masse fausse un peu la mesure de la batterie : l'étalonnage en deux points la compense.

## Sans éclairage

L'intérieur d'un nichoir est sombre, même de jour : la lumière n'entre que par le trou d'envol et les aérations. Sans LED, les images de la chambre risquent d'être sombres ou bruitées, et la nuit n'est pas filmée. À évaluer dès l'essai dans le carton fermé. Si besoin : une petite fenêtre en plexiglas dépoli sur un côté ombragé (à ajouter aux plans).

## Montage

- **Presse-étoupe PG7** : perçage 12,5 mm. Dans la paroi de 20 mm du nichoir, lamer l'intérieur (environ Ø 25) pour que l'écrou prenne : mesurer d'abord la longueur filetée du presse-étoupe reçu.
- **Cordon USB coupé** : seule la moitié USB-C sert. Repérer au multimètre les fils du +5 V et de la masse ; isoler D+ et D−.
- **PIR** : sous la cloison, lentille dans une fenêtre tournée vers la chambre ; le câble reste dans le compartiment.
- **Coffret** : ombragé, entrées de câbles par le dessous, accus calés.
- **Vernis** (option) : ni sur l'objectif, ni sur le micro, ni sur le lecteur de carte, les connecteurs et la prise d'antenne.

## Hors électronique (non chiffré, magasin de bricolage)

D'après les [plans](plans/README.md) : planche de 20 mm d'au moins 180 × 2 050 mm ; toit 300 × 250 ; contreplaqué marine de 10 mm (100 × 80) pour la plaque de trappe ; barre de fixation 40 × 600 × 20 ; vis inox 4 × 40, dont deux pivots avec rondelles ; crochet ou vis de blocage de la porte ; couverture EPDM ou tôle ; joint mousse ; silicone neutre ; platine et cales de 10 mm pour le panneau ; fil ou sangle de fixation au support ; huile de lin facultative.

Visserie du panneau : le kit Voltaic « ETFE Panel Screw & Washer Set » est en rupture chez Kiwi ; choisir des vis inox selon les trous du panneau.

## Écartés

| Article | Raison |
|---|---|
| Voltaic V75 (105,59 € chez Kiwi) | Remplacée par les 4 XTAR, à la demande de Romain |
| Module UPS 5 V 18650 (Gotronic, 5,50 €) | Une seule cellule, entrée 5 V et non solaire, pas de thermistance annoncée |
| Shield chargeur solaire Seeed (Gotronic, 16,15 €) | Sortie limitée à 600 mA, entrée solaire 4,8 à 6 V alors que le P110 monte à 6,94 V à vide |
| Supports 18650 de Gotronic | Accus de 65 mm seulement |
| LED IR, barrière IR, sondes DS18B20, carte de test USB-C (lecture de la V75) | Abandonnés le 24/11/2026 |

## Points ouverts

- **Supports d'accus** : prix, stock et ajustement des BH-18650-W à vérifier.
- **Luminosité** dans la chambre sans éclairage : essai dans le carton.
- **PIR dans 14 cm** : un oiseau qui couve bouge peu, et la fiabilité du PIR dans un si petit volume n'est pas démontrée ; la photo toutes les 10 min en journée reste le filet de sécurité.
- **Reprise après décharge complète** : la protection des accus coupe en fin de décharge ; vérifier au banc que le chargeur relance la charge au retour du soleil. Si la broche TMR de la carte reste en l'air (non vérifié), la fiche TI prévoit des minuteries de précharge (30 min) et de charge (5 h) : après une décharge profonde du pack de 15 Ah, la reprise pourrait demander plusieurs journées de soleil.
- **Redémarrage matériel de la caméra** (idée de BirdBox) : aucun circuit retenu.
- **Toutes les consommations** restent à mesurer.
