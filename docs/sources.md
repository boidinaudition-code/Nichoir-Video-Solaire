# Sources et limites des références

[Accueil](../README.md) · [Capture](capture.md) · [Énergie](energie.md)

Cette liste reprend les références du dossier. Pour cette correction, la notice V25 2025, les pages fabricant V25/P126, la fiche technique P126 et les README NestBox/BirdSensor_xiao ont été consultés en ligne. Cette lecture ciblée ne revalide ni les autres références, ni les stocks ou prix. « Source » ne signifie pas certification du montage. Les liens externes du vérificateur local sont contrôlés syntaxiquement, pas téléchargés.

## Faune, composants et énergie

- [LPO — nichoirs pour passereaux](https://www.lpo.fr/la-lpo-en-actions/mobilisation-citoyenne/refuges-lpo/tutoriels/nichoirs-pour-passereaux) : référence du dossier pour dimensions utiles, trou et implantation ; ne valide pas la conception électronique.
- [Seeed — XIAO ESP32S3 Sense](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/) : documentation constructeur à consulter pour brochage, variantes et consommation. Confirmer la révision réelle et le PID ; aucune compilation ici.
- [Gotronic — Sense](https://www.gotronic.fr/art-carte-xiao-esp32s3-sense-37063.htm) et [BS612](https://www.gotronic.fr/art-capteur-pir-bs612-36148.htm) : références commerciales déjà retenues ; dessin de brochage à contrôler avant soudure.
- [Voltaic — V25](https://voltaicsystems.com/v25/) et [P126](https://voltaicsystems.com/P126/) : références fabricant à confronter au lot. La [fiche technique P126 datée du 31 août 2026](https://voltaicsystems.com/content/P126_ds.pdf) présente R3C en tête de son historique ; les chiffres revendeur 7,28/8,51 V correspondent aux anciennes R1D/R1E, pas aux valeurs actuelles. Voir les distinctions et précautions dans le [câblage](cablage.md).
- [Notice constructeur V25/V50/V75 2025 (PDF)](https://voltaicsystems.com/content/batteries/V25_50_75_Instructions_2025.pdf) : document dont le titre interne porte 2025-06-02 ; génération V25 6700 mAh / 24,12 Wh, USB-A Always On et entrées DC/USB-C. Ce document n'identifie pas à lui seul la révision de la batterie reçue.
- [Kiwi — V25](https://www.kiwi-electronics.com/en/v25-usb-battery-pack-10076) et [P126](https://www.kiwi-electronics.com/en/solar-panel-6v-2w-etfe-coating-10922) : références du panier prévisionnel, non nouvelle vérification de stock/TVA. Tous les achats et alternatives sont liés dans le README.
- [PVGIS, Commission européenne](https://re.jrc.ec.europa.eu/pvg_tools/en/) : outil proposé pour une étude future ; aucune simulation locale n'a été effectuée.

La notice V25 2025 consultée contient bien l'incohérence 3,5 × 1,1 (repérage des ports) / 3,5 × 1,5 (spécifications). Obtenir la notice du lot et faire lever cette ambiguïté avant achat/branchement. Prix, dimensions et révisions restent à confirmer à réception.

## Comparaison commerciale : Birdfy Nest

[Manuel Birdfy Nest (PDF constructeur)](https://support.birdfy.com/img/products/product-manual/birdfy-nest-manual.pdf).

Référence commerciale pour réfléchir à l'organisation d'un coffre technique et d'un panneau : séparer l'accès à l'électronique de la chambre et protéger les raccordements. Ce produit n'est ni notre plan coté ni une validation de nos dimensions LPO, de la XIAO ou de notre budget énergétique.

Différence importante : un panneau déporté peut être orienté et exposé indépendamment du nichoir, au prix d'un câble et de raccordements supplémentaires. Notre V1 impose le P126 intégralement sur le toit : ombre et orientation du nichoir contraignent donc la production. Ne pas transposer une autonomie commerciale à ce montage ni présenter le manuel comme preuve qu'un panneau fixé sur notre toit suffira. Le coffret batterie arrière séparé et ombragé est notre choix de conception, pas une cote copiée du produit.

## Projets ouverts candidats

| Référence réelle | Usage possible | Ce qui n'est pas établi dans ce dossier |
|---|---|---|
| [s60sc/ESP32-CAM_MJPEG2SD](https://github.com/s60sc/ESP32-CAM_MJPEG2SD) | Piste pour vidéo MJPEG enregistrée en AVI sur SD | Aucun commit figé, licence auditée, portage compilé ou essai XIAO/OV3660/PIR/sommeil réalisé ici |
| [TeTeHacko/chytra-budka](https://github.com/TeTeHacko/chytra-budka) | Piste nichoir avec XIAO | Ne pas présenter le solaire comme réalisé ; aucune preuve d'autonomie solaire ou de conformité à notre chaîne AVI |
| [davidlsparks/NestBox](https://github.com/davidlsparks/NestBox) | Plans de nichoir bois avec caméra, inspiration d'implantation mécanique | Ni validation de nos cotes LPO, ni preuve ou promesse d'autonomie solaire pour notre montage |
| [happychriss/BirdSensor_xiao](https://github.com/happychriss/BirdSensor_xiao) | Piste XIAO ESP32-S3 Sense activée par PIR via coupure d'alimentation TPS22918 | Capture JPEG et envoi Wi-Fi décrits, pas équivalent de notre chaîne AVI sur SD ni de notre réveil RTC ; aucune autonomie transposable, aucun lien établi avec le nom XiaoBird |
| XiaoBird | Nom non identifié de manière fiable | Aucun dépôt ni auteur attribué, aucun lien inventé, aucune fonctionnalité retenue sur cette seule appellation |

Une disponibilité de code n'est pas une preuve de fonctionnement du système retenu. Lire licence, version, configuration et limites avant toute réutilisation. Aucun de ces projets n'est intégré au présent dépôt.
