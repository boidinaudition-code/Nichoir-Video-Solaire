# Sources et limites des références

[Accueil](../README.md) · [Capture](capture.md) · [Énergie](energie.md)

Cette liste reprend les références du dossier et les liens explicitement fournis pour sa finalisation, sans nouvelle recherche web. « Source » ne signifie pas certification du montage. Aucun nouveau contrôle HTTP, de stock, de prix ou de contenu distant n'est revendiqué ici. Les liens externes du vérificateur sont contrôlés syntaxiquement, pas téléchargés.

## Faune, composants et énergie

- [LPO — nichoirs pour passereaux](https://www.lpo.fr/la-lpo-en-actions/mobilisation-citoyenne/refuges-lpo/tutoriels/nichoirs-pour-passereaux) : référence du dossier pour dimensions utiles, trou et implantation ; ne valide pas la conception électronique.
- [Seeed — XIAO ESP32S3 Sense](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/) : documentation constructeur à consulter pour brochage, variantes et consommation. Confirmer la révision réelle et le PID ; aucune compilation ici.
- [Gotronic — Sense](https://www.gotronic.fr/art-carte-xiao-esp32s3-sense-37063.htm) et [BS612](https://www.gotronic.fr/art-capteur-pir-bs612-36148.htm) : références commerciales déjà retenues ; dessin de brochage à contrôler avant soudure.
- [Voltaic — V25](https://voltaicsystems.com/v25/) et [P126](https://voltaicsystems.com/2-watt-6-volt-solar-panel/) : références fabricant à confronter au lot et à sa notice. Les caractéristiques recopiées dans le dossier ne remplacent pas la confirmation de compatibilité demandée dans le câblage.
- [Kiwi — V25](https://www.kiwi-electronics.com/en/v25-usb-battery-pack-10076) et [P126](https://www.kiwi-electronics.com/en/solar-panel-6v-2w-etfe-coating-10922) : références du panier prévisionnel, non nouvelle vérification de stock/TVA. Tous les achats et alternatives sont liés dans le README.
- [PVGIS, Commission européenne](https://re.jrc.ec.europa.eu/pvg_tools/en/) : outil proposé pour une étude future ; aucune simulation locale n'a été effectuée.

La notice V25 2025 évoquée dans le dossier n'a pas d'URL précise archivée ici : ne pas lui inventer de lien ni prétendre l'avoir revalidée. Obtenir la notice du lot et lever l'incohérence 3,5 × 1,1 / 3,5 × 1,5 avant achat/branchement. Prix et dimensions restent à confirmer à réception.

## Comparaison commerciale : Birdfy Nest

[Manuel Birdfy Nest (PDF constructeur)](https://support.birdfy.com/img/products/product-manual/birdfy-nest-manual.pdf).

Référence commerciale pour réfléchir à l'organisation d'un coffre technique et d'un panneau : séparer l'accès à l'électronique de la chambre et protéger les raccordements. Ce produit n'est ni notre plan coté ni une validation de nos dimensions LPO, de la XIAO ou de notre budget énergétique.

Différence importante : un panneau déporté peut être orienté et exposé indépendamment du nichoir, au prix d'un câble et de raccordements supplémentaires. Notre V1 impose le P126 intégralement sur le toit : ombre et orientation du nichoir contraignent donc la production. Ne pas transposer une autonomie commerciale à ce montage ni présenter le manuel comme preuve qu'un panneau fixé sur notre toit suffira. Le coffret batterie arrière séparé et ombragé est notre choix de conception, pas une cote copiée du produit.

## Projets ouverts candidats

| Référence réelle | Usage possible | Ce qui n'est pas établi dans ce dossier |
|---|---|---|
| [s60sc/ESP32-CAM_MJPEG2SD](https://github.com/s60sc/ESP32-CAM_MJPEG2SD) | Piste pour vidéo MJPEG enregistrée en AVI sur SD | Aucun commit figé, licence auditée, portage compilé ou essai XIAO/OV3660/PIR/sommeil réalisé ici |
| [TeTeHacko/chytra-budka](https://github.com/TeTeHacko/chytra-budka) | Piste nichoir avec XIAO | Ne pas présenter le solaire comme réalisé ; aucune preuve d'autonomie solaire ou de conformité à notre chaîne AVI |
| XiaoBird | Nom non identifié de manière fiable | Aucun dépôt ni auteur attribué, aucun lien inventé, aucune fonctionnalité retenue sur cette seule appellation |

Une disponibilité de code n'est pas une preuve de fonctionnement du système retenu. Lire licence, version, configuration et limites avant toute réutilisation. Aucun de ces projets n'est intégré au présent dépôt.
