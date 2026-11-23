# Nichoir vidéo solaire — conception V1

Dossier de conception du 23 novembre 2026. Pas un produit prêt à poser : **aucun firmware de capture n'est implémenté**, aucune vidéo réelle ni mesure électrique n'a été produite avec du matériel. Livrables exécutables : calculateur Python stdlib et tests. Les essais matériels restent des critères d'acceptation, pas des résultats.

## Décision

- Nichoir bois massif brut 20 mm, chambre charbonnière **140 × 140 × 230 mm utiles**, trou **32 mm** ; variante bleue **130 × 130 × 230 mm**, trou **28 mm**. Cotes fondées sur le [tableau LPO](https://www.lpo.fr/la-lpo-en-actions/mobilisation-citoyenne/refuges-lpo/tutoriels/nichoirs-pour-passereaux), pas un nichoir commercial à ces dimensions extérieures.
- XIAO ESP32S3 **Sense 113991115 avec OV3660** et lecteur microSD intégré ; contrôler le lot avant achat et le PID à réception. Le fabricant annonce une transition OV5640 : pas de substitution silencieuse.
- BS612 PIR maintenu sous 3,3 V ; réveil RTC sur GPIO1/D0 ; objectif : **vraies vidéos MJPEG dans un conteneur AVI sur SD**, 20 s, VGA 640 × 480, cible 10 images/s, sans audio ni Wi-Fi permanent. Le mode profond impose une latence et peut manquer l'entrée rapide d'un oiseau.
- Power bank **Voltaic V25 nouvelle génération 6700 mAh / 24,12 Wh**, sortie USB-A Always On ; panneau fabricant **P126 6 V / 2 W**, entièrement sur le toit, entrée solaire DC directe. Pas de panneau déporté ni de cellule LiPo ajoutée à la XIAO.
- **Faune avant image et rendement** : implantation protégée des pluies/vents, ombre aux heures chaudes, entrée est/sud-est, pas de perchoir. Si le toit reste trop ombragé, accepter l'arrêt de la vidéo plutôt que déplacer la nichée au soleil.
- V1 sans IR ni LED d'éclairage : intérieur parfois très sombre, nuit noire inexploitable acceptée. Pas d'agrandissement du trou ni de fenêtre lumineuse pour la caméra.
- Batterie dans un coffret extérieur séparé de la chambre, à l'ombre, protégé de l'eau et de la condensation ; jamais sous le panneau chaud. Charge autorisée **0–45 °C uniquement** ; pas de charge gel. Aucun entretien, retrait SD ou dépannage sur nid occupé, même par trappe externe.

## Lecture du dossier

1. [Architecture et limites](docs/architecture.md)
2. [Câblage et versions d'alimentation](docs/cablage.md)
3. [Débit bois et montage](docs/bois.md)
4. [Énergie et scénarios chiffrés](docs/energie.md)
5. [Capture AVI, réveil et réarmement](docs/capture.md)
6. [Essais et décision de pose](docs/essais.md)
7. [Sources vérifiées et projets candidats](docs/sources.md)
8. [Rapport local et demande de revue](docs/revue.md)

## Achats — une unité par ligne sauf mention

Prix relevés ou provisions TTC France, hors port, outils et main-d'œuvre. Les stocks sont un instantané, pas une réservation. Kiwi affiche ici des prix **HT (« Ex. VAT »)** : conversion prévisionnelle avec TVA France 20 %, panier livraison France à confirmer. Aucun prix USD n'est présenté comme un prix TTC européen.

| Élément / référence et lien direct | TTC € | Statut / contenu |
|---|---:|---|
| [XIAO Sense 113991115, Gotronic 38234](https://www.gotronic.fr/art-carte-xiao-esp32s3-sense-37063.htm) | 16,90 | Page OV3660, antenne/radiateurs/carte Sense inclus ; SD et câble USB non inclus ; stock affiché lors consultation |
| [PIR BS612, Gotronic 38058 / Adafruit 5578](https://www.gotronic.fr/art-capteur-pir-bs612-36148.htm) | 2,70 | En stock ; composant à câbler, pas module Grove |
| [SanDisk Ultra microSDHC UHS-I 32 Go, Gotronic 26870](https://www.gotronic.fr/art-carte-micro-sd-sandisk-32gb-49149.htm) | 18,50 | En stock au catalogue ; FAT32, pas de lecteur SD supplémentaire pour XIAO |
| [V25 KW-2655, Kiwi, génération USB-C/DC](https://www.kiwi-electronics.com/en/v25-usb-battery-pack-10076) | 52,79 | 43,99 HT ; fiche 6700 mAh, deux USB-A et entrée solaire 3,5 × 1,1 ; stock UE affiché |
| [P126 KW-3001, Kiwi](https://www.kiwi-electronics.com/en/solar-panel-6v-2w-etfe-coating-10922) | 24,59 | 20,49 HT ; stock UE affiché ; 136 × 112 mm ; fiche revendeur épaisseur 2,7 mm |
| [Joint de fixation P126 G110, Kiwi](https://www.kiwi-electronics.com/en/high-bonding-gasket-for-p126-10933) | 3,95 | 3,29 HT ; coller sur platine lisse, pas directement sur bois brut ; retenue mécanique ajoutée |
| [Lecteur PC microSD WT12370, Gotronic 32961](https://www.gotronic.fr/art-lecteur-de-carte-microsd-wt12370-27794.htm) | 3,90 | Facultatif si déjà équipé ; inclus dans total pour récupération externe |
| Câble USB-A vers USB-C court de qualité | 4–8 | Provision non cotée, modèle à choisir ; nécessaire en sortie V25 même si câble de recharge fourni |
| Fils, connecteurs, résistance de tirage et bouton service | 3–8 | Provision ; [barrette MH100](https://www.gotronic.fr/art-connecteur-he14-mh100-4457.htm) candidate, pas prix ferme du lot |
| Bois Douglas/mélèze non traité 20 mm, tasseaux, cloison | 20–35 | Provision scierie locale ; débit détaillé dans bois, chute/trait de scie inclus à prévoir |
| Visserie inox, charnières/loquet de nettoyage | 8–15 | Provision locale ; pas de pointe dépassant dans chambre |
| Platine panneau, entretoises, couverture toit et retenues | 8–18 | Provision ; pas de perçage arbitraire des cellules |
| Coffret batterie utile ≥ 120 × 120 × 60 mm, coffret technique/trappe et joints | 15–30 | Provision non cotée ; étanchéité finale à tester, batterie non étanche |
| Presse-étoupes, membrane anti-condensation, gaine et attache-câbles | 5–12 | Provision ; boucle goutte d'eau, pas de câble exposé aux becs |
| Fixation support, cales de protection arbre, renfort trou | 6–15 | Provision ; adapter au support, pas de perchoir |
| **Total complet prévisionnel** | **192,33–264,33** | **TTC hors port**, lecteur PC inclus, aucun outil de mesure inclus |

Provisions explicitement non vérifiées en panier : ce n'est pas une nomenclature industrielle entièrement qualifiée. Prévoir en prêt un multimètre, mesureur USB intégrateur Wh (qui peut lui-même consommer et fausser la veille), alimentation de labo et outillage bois/soudure ; leur achat n'est pas dans ce total. Adaptateur solaire **non requis pour la V25 actuelle** : fiche P126 3,5 × 1,1 mâle vers entrée V25 de même format. Ne pas acheter un adaptateur micro-USB d'ancienne génération par défaut. Rallonge solaire non incluse : implanter coffret sous débord arrière dans la portée du câble réel, sinon chiffrer une rallonge Voltaic compatible avant commande.

Alternative UE V25 : [SeeSense](https://seesense.eu/products/power/batteries/battery-voltaic-v25-23wh-lithium-with-always-on-capability/) décrit la nouvelle version, mais disponibilité annoncée en réapprovisionnement ; TVA affichée non française. Alternative panneau : [Robot Italy P126](https://robot-italy.com/products/5366-6v-2w-solar-panel-etfe), 30,67 € TVA italienne incluse affichée, stock ambigu dans extraction, à confirmer. Kiwi est retenu pour la disponibilité explicite des deux éléments. Aucun ASIN Amazon inventé : les références directes Gotronic suffisent pour caméra/PIR/SD.

## Énergie : décision d'usage

Modèle de travail conservateur : 5 mA en veille système sous USB 5 V, 350 mA pendant capture/démarrage, 20 + 3 s par événement, pertes USB 15 %, consommation propre V25 26 mW, solaire 2 W avec rendement global 50 %. Ces hypothèses doivent être remplacées par les mesures du montage complet.

| Usage | Besoin cellule Wh/j | HSP minimales sans ombre | Jours sans soleil depuis réserve pleine* |
|---|---:|---:|---:|
| 10 clips/j | 1,460 | 1,460 | 13,22 |
| 100 clips/j | 2,626 | 2,626 | 7,35 |
| 500 clips/j | 7,813 | 7,813 | 2,47 |
| Continu 140 mA, comparaison | 20,389 | 20,389 | 0,95 |

*Réserve de calcul 80 % de 24,12 Wh, pas capacité mesurée ni promesse. Les HSP sont des heures équivalentes à 1000 W/m² sur le plan du panneau, pas des heures de jour. Au Havre, hiver, ombre, pluie et gel rendent l'autonomie non garantie ; pas de météo fictive ni de moyenne locale utilisée comme preuve. Voir [énergie](docs/energie.md) pour sensibilités, pertes et arrêt.

## Reproduire la vérification logicielle

Depuis la racine, Python ≥ 3.10, aucune installation de package :

```sh
python -m unittest discover -s tests -v
python tools/dimensionnement.py --clips 100 --hsp 1
python tools/dimensionnement.py --clips 100 --hsp 1 --ombre 0.5
python tools/verifier_dossier.py
```

Le dossier reste au statut **prototype à valider avant occupation** : PID, vraie vidéo AVI, latence, comportement PIR, maintien Always On, froid/chaleur, SD et étanchéité sont des portes de validation obligatoires. La récupération SD se fait depuis le compartiment technique extérieur, après arrêt propre, uniquement quand le nichoir est confirmé inoccupé.
