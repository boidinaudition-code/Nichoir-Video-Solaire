# Énergie — modèle reproductible, pas une garantie météo

[Accueil](../README.md) · [Calculateur](../tools/dimensionnement.py) · [Tests](../tests/test_dimensionnement.py)

## Référentiel d'énergie

V25 nouvelle génération : **6700 mAh / 24,12 Wh** cellule selon notice 2025. Les mAh ne sont pas à 5 V USB : ne pas calculer 6,7 Ah × 5 V. Réserve choisie = 24,12 × 0,8 = **19,296 Wh cellule** pour pertes de capacité/âge et marge, non une mesure.

Fiche fabricant V25 : Always On environ **7 mA / 26 mW**. C'est une consommation propre interne : **0,026 × 24 = 0,624 Wh/j**, pas 7 mA sous 5 V ajoutés à la charge USB. L'ordre de grandeur est sourcé, mais les variations avec charge/température/lot restent à mesurer. Sortie V25 efficace à 85 % dans le modèle : hypothèse séparée, pas valeur fabricant garantie. Éviter de recompter la consommation propre si un essai énergétique complet l'intègre déjà.

Conso Sense : Seeed distingue carte nue deep sleep14 µA et **Sense avec extension environ3 mA sous3,8 V** ; Gotronic annonce vidéo moyenne138 mA et prise photo341 mA sans que cela prouve notre profil AVI. Ne pas promettre 14 µA pour l'ensemble caméra/SD/PIR alimenté par USB. Hypothèses de travail sous USB5 V : **veille5 mA** comprenant carte/SD/caméra au repos/PIR, **actif350 mA**, phases démarrage/exposition/écriture incluses par marge. Il faut mesurer le profil réel, y compris la fermeture et le réarmement ; si >3 s hors clip, augmenter la latence du modèle.

## Équations (unités explicites)

```text
Tactif_s = Nclips × (20 s vidéo + 3 s démarrage/fermeture/réarmement forfaitaires)
Eusb_Wh/j = 5 × [Iactif_mA × Tactif_s + Iveille_mA × (86400 - Tactif_s)] / 3600000
Ebesoin_cellule = Eusb / 0,85 + 0,624
Esolaire_cellule = Pnominal_W × HSP × 0,50 × fraction_solaire_restante
HSP_min = Ebesoin_cellule / (Pnominal × 0,50 × fraction_restante)
jours_sans_soleil = 19,296 / Ebesoin_cellule
jours_sur_déficit = 19,296 / (Ebesoin_cellule - Esolaire_cellule), si déficit > 0
```

Le rendement solaire global50 % couvre orientation non optimale, température, tolérance, fonctionnement à tension non MPP idéale, câbles et charge cellule ; ombre est un facteur additionnel explicite. Le modèle proportionnel est grossier : une petite ombre sur cellules en série peut faire beaucoup plus mal que sa surface. P126 calculé à **2 W commerciaux**, pas à2,37 W crête revendeur. Recharge gel bloquée = solaire accepté nul, même sous soleil. La production excédentaire est écrêtée quand batterie pleine ; « bilan positif » ne prouve pas le passage d'une semaine sombre.

## Résultats par jour (sans ombre, HSP=1)

| Scénario | Actif s/j | USB Wh/j | Propre Wh/j | Cellule Wh/j | Bilan solaire Wh/j | HSP min | Jours sans soleil | Jours sur déficit à HSP1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 clips de20 s | 230 | 0,710 | 0,624 | 1,460 | -0,460 | 1,460 | 13,22 | 41,99 |
| 100 clips de20 s | 2300 | 1,702 | 0,624 | 2,626 | -1,626 | 2,626 | 7,35 | 11,86 |
| 500 clips de20 s | 11500 | 6,110 | 0,624 | 7,813 | -6,813 | 7,813 | 2,47 | 2,83 |
| Continu140 mA | 86400 | 16,800 | 0,624 | 20,389 | -19,389 | 20,389 | 0,95 | 1,00 |

La ligne continu est une comparaison optimiste à140 mA (proche webcam Seeed), pas l'assurance qu'AVI+SD tourne à ce courant. Le continu à350 mA serait encore pire. Le total quotidien vidéo n'est pas un débit de visites biologiques connu : les passages répétés/PIR faux positifs peuvent saturer le système.

### Sensibilités, 100 clips/j

Reproduire depuis la racine :

```sh
python tools/dimensionnement.py --clips 100 --hsp 0
python tools/dimensionnement.py --clips 100 --hsp 0.5
python tools/dimensionnement.py --clips 100 --hsp 1 --ombre 0.5
python tools/dimensionnement.py --clips 100 --hsp 3
python tools/dimensionnement.py --clips 100 --hsp 1 --veille-ma 15
python tools/dimensionnement.py --clips 100 --hsp 1 --propre-w 0.05
```

HSP0/0,5/1/3 sont des scénarios, **pas des données observées au Havre**. À50 % de solaire restant, seuil HSP doublé ; à ombre totale ou panneau0 W, seuil impossible (`null`), et durée sur déficit = durée sans soleil. `null` sur durée d'épuisement en bilan non déficitaire signifie « pas de déficit dans ce modèle journalier », pas autonomie infinie réelle. Le calculateur refuse entrées négatives/non finies, rendements hors limites, journée active >86400 s et HSP >24.

## Choix et portes de validation

P126 compact suffit pour une expérimentation saisonnière peu active, pas pour 500 clips/j en toutes saisons. P105 plus puissant impliquerait toit élargi et qualification version/stock/connectique ; ce n'est pas un échange transparent. Une power bank générique qui s'éteint à faible courant, n'accepte pas la charge solaire intermittente ou ne bloque pas la charge au gel n'est pas une alternative sûre.

Pour Le Havre, mesurer plusieurs journées représentatives avec ombres réelles et orientation finale, puis comparer Wh récoltés au besoin. Pour climat mensuel, employer PVGIS avec coordonnées du site et orientation/inclinaison réelles (outil européen : https://re.jrc.ec.europa.eu/pvg_tools/en/), en séparant ombre locale, stockage et blocage température. Aucune étude PVGIS locale n'a été exécutée dans ce dossier. **Pas de garantie hiver**, gel ou pluie persistante : arrêt vidéo acceptable.

Avant occupation, valider au moins72 h sans solaire et une semaine au site sur nichoir vide, mesures Wh et températures enregistrées. Capacité utile/efficacité réelle à recalibrer. Pas de seuil de charge « précis » inventé à partir des LED de la V25 ; la V1 n'implémente pas de télémétrie de batterie. Le BMS protège la batterie mais une coupure brutale peut corrompre l'AVI/FAT32 : clips courts et protocole de reprise requis. Si la réserve paraît insuffisante, réduire les clips avant saison ou laisser le système éteint, pas recharger au nid.
