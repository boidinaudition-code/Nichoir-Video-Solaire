# Câblage — vérifier le lot avant branchement

> **ARCHIVE V1 OBSOLÈTE.** Voir la [décision V2](decision-v2.md) pour les options d'alimentation ; le couple P126/V25 ci-dessous n'est pas un câblage V2 validé. Conserver les précautions électriques et vérifier les révisions avant branchement.

[Accueil](../README.md) · [Sources](sources.md) · [Essais](essais.md)

## Alimentation retenue, génération V25 2025/actuelle

P126 câble mâle DC **3,5 × 1,1 mm** vers entrée solaire DC V25 **3,5 × 1,1 mm**. Vérifier dimension, emboîtement et polarité au multimètre/notice du lot avant connexion ; aucun forçage ni adaptateur 5,5 × 2,1. Connexion à garder dans le coffret sec : le panneau IP67 ne rend pas la batterie ou tous les raccordements IP67.

La [notice 2025](https://voltaicsystems.com/content/batteries/V25_50_75_Instructions_2025.pdf), titre interne daté du 2 juin 2025, indique 3,5 × 1,1 dans le repérage des ports mais **3,5 × 1,5 dans sa ligne de spécifications**, incohérence confirmée à la lecture et à signaler au fournisseur. La fiche fabricant V25 actuelle et la fiche UE convergent sur 3,5 × 1,1 : c'est le choix de conception, à confirmer sur la pièce reçue. Notice : panneaux Voltaic 5–7 V ; entrée spécifiée 5–6 V/2 A.

Le [P126 constructeur](https://voltaicsystems.com/P126/) est commercialisé comme panneau « 6 V / 2 W ». Sa [fiche technique du 31 août 2026](https://voltaicsystems.com/content/P126_ds.pdf) présente la révision **R3C** : Vmp nominal **7,48 V**, Voc nominal **8,74 V**, puissance nominale 2,62 W ; valeurs « Expected » après pertes de fabrication : **7,21 V / 8,48 V / 2,21 W**. Les **7,28 V / 8,51 V** recopiés de la fiche revendeur correspondent aux anciennes **R1D/R1E** de l'historique constructeur : ils ne prouvent pas la révision vendue. Relever révision et lot à réception. La page commerciale indique encore 2,7 mm d'épaisseur, contre **3,1 mm** dans la fiche technique : contrôler aussi l'encombrement réel avant fixation. Le modèle énergétique conserve prudemment 2 W, sans gain d'autonomie revendiqué.

Vmp est une tension au point de puissance maximale **en charge**, Voc une tension **à vide** ; aucune n'est une sortie USB régulée. La compatibilité doit être celle du couple Voltaic, pas déduite du seul intitulé 6 V. Faire confirmer par écrit P126 de la révision livrée + V25 actuelle, notamment au regard de l'entrée annoncée 5–6 V/2 A ; mesurer en charge et ne jamais appliquer ces tensions directement à la XIAO ou au port USB-C d'un autre power bank. Le rendement solaire global du calcul est une hypothèse, pas une qualification des pertes loin du MPP (V25 MPP annoncé 5,2 V).

V25 : **USB-A Always On -> câble USB-A/USB-C -> XIAO USB-C 5 V**. Le port USB-C PD supérieur de la V25 n'est pas Always On ; ne l'utiliser ni en entrée ni en sortie pendant ce mode. Recharge solaire par DC ou USB-C latéral uniquement. Double appui bouton V25 arrête les sorties ; simple appui les réactive. Prévoir bouton protégé des appuis accidentels, puis tester reprise automatique après décharge/protection température. Recharge initiale sur table, au sec et hors gel.

**Ne rien brancher aux pastilles BAT de la XIAO.** Pas de lithium nu ni de chargeur solaire en cascade. Pas d'alimentation simultanée par broche 5 V et USB de PC ; pour le banc, déconnecter V25 avant USB PC. GND commun interne XIAO/PIR. Ne pas dépasser 3,3 V sur une E/S.

### Anciennes générations

Des V25 anciennes sont annoncées 6400 mAh / environ 23 Wh et peuvent utiliser une entrée micro-USB plutôt que le DC/USB-C actuel. Ne pas réutiliser leurs dimensions, comportement Always On ou adaptateur comme preuve pour la génération 6700 mAh. Si ancienne reçue : suspendre montage, relever notice et ports exacts, puis revoir budget/connectique. Le [micro-USB Voltaic A101](https://voltaicsystems.com/A101/) est un exemple de référence historique, **pas un achat de la V1 actuelle**. Les USB-C latéral solaire et supérieur PD ne sont pas interchangeables fonctionnellement. La fiche Kiwi affiche 23 g, contre 230 g fabricant : retenir fabricant et contrôler, pas dimensionner la fixation sur 23 g.

## PIR BS612 — câbler selon les noms, pas la position supposée

Lire le dessin « dimensions/brochage » et la fiche technique depuis la page Gotronic 38058 avant soudure ; ne pas compter les pattes à partir d'une photo inversée.

| BS612 | Connexion V1 |
|---|---|
| VDD | 3V3 XIAO, alimentation continue y compris veille |
| GND | GND XIAO |
| REL | D0 = GPIO1, entrée RTC, réveil EXT0 niveau haut |
| OEN | 3V3 (activation permanente) |
| SENSE | GND (configuration recommandée Gotronic) |
| ONTIME | GND : impulsion annoncée 2 s, pas 1 h |

Consommation annoncée ≤ 11 µA, alimentation 2,7–3,7 V. Une résistance de tirage faible charge (par exemple 100 kΩ à la masse sur REL) n'est à monter qu'après contrôle du type de sortie et de ses niveaux ; réserver sa place. Contrôler sortie haute ≤ 3,3 V, basse franche, pas flottante. GPIO1 libre du bus caméra/SD et RTC sur ESP32-S3, confirmer `rtc_gpio_is_valid_gpio(GPIO_NUM_1)` dans le firmware de banc. Réactiver correctement le mode GPIO après réveil RTC (`rtc_gpio_deinit`). D1/GPIO2 réservé au bouton service vers GND avec tirage adapté ; ne pas utiliser GPIO3 de strapping.

Le PIR n'émet pas d'IR mais doit voir le mouvement thermique : **ne voit pas à travers bois ou vitre ordinaire**. Lentille d'origine conservée, passage à travers cloison ajusté sans bord coupant, sans autre vitre devant. Essayer à courte distance dans le volume réel ; la portée 5 m n'est pas une qualification pour mésange à 15 cm, ni preuve de détection sous plumage chaud/froid.

## Pins réservées et conflits

| Fonction | GPIO ESP32-S3 |
|---|---|
| microSD Sense SPI | CS 21, SCK 7 (D8), MISO 8 (D9), MOSI 9 (D10) |
| Caméra XCLK ; SCCB SDA/SCL | 10 ; 40/39 |
| Caméra D0..D7 | 15, 17, 18, 16, 14, 12, 11, 48 |
| Caméra VSYNC/HREF/PCLK | 38/47/13 |
| Micro PDM non utilisé | 41/42, laisser les ponts intacts |
| PIR | GPIO1 / D0 |

Voir Seeed pin multiplexing. **GPIO21 sert au CS SD** : ne pas reprendre aveuglément un exemple de LED utilisateur sur ce GPIO pendant les accès SD. Masquer les voyants avec un écran opaque extérieur à la chambre, sans isoler thermiquement carte/radiateurs ; ne pas couper des pistes au hasard. Audio désactivé. Pas de servomoteur, flash ni autre périphérique sur les pins réservées. Bus SD SPI de la Sense, pas brochage SD_MMC d'une AI Thinker copié tel quel.

Fils courts, soudures isolées, anti-arrachement. Débouchés de câbles vers le bas avec goutte d'eau. Tenir USB et lecteur SD hors zone humide ; les radiateurs inclus ne doivent toucher aucun fil. Vérifier 5 V au plus près de la carte pendant démarrage/écriture SD, pas seulement à vide sur la V25.
