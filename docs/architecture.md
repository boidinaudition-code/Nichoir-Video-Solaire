# Architecture V1

> **ARCHIVE V1 OBSOLÈTE.** Remplacée par la [décision V2](decision-v2.md). Le choix sans radio ci-dessous n'est plus la décision actuelle ; les protections faune restent à respecter. Aucun firmware livré.

[Accueil](../README.md) · [Sources](sources.md)

## Chaînes indépendantes

```text
Toit bois ventilé + P126 intégralement dans l'emprise du toit
    -> câble DC solaire -> V25 hors chambre, coffret arrière ombragé
    -> USB-A Always On 5 V -> USB-C XIAO Sense
                               |-> OV3660 -> JPEG -> mux AVI -> microSD FAT32
3V3 XIAO -> PIR BS612 -> D0/GPIO1 RTC -> réveil profond
                       D1/GPIO2 réservé au bouton service local
```

- Le RTC désigne le domaine basse consommation et le réveil de l'ESP32-S3, pas un module horloge DS3231 acheté séparément. Un timer RTC peut gérer les défauts et la périodicité ; l'heure civile après coupure totale n'est pas garantie.
- La microSD est celle de la Sense ; pas de module SPI externe ni d'extension SD longue. Monter toute la carte dans le compartiment supérieur, logement SD accessible par trappe latérale extérieure, caméra dirigée vers le bas par un passage optique affleurant au plafond. Le PIR est également exposé optiquement à la chambre, corps et câbles protégés dans le compartiment technique.
- Pas de radio en exploitation normale, pas de cloud, reconnaissance d'espèces, son ou serveur vidéo permanent. Wi-Fi uniquement outil de banc éventuel, consommation à comptabiliser séparément si ajouté.
- L'appareil doit produire des fichiers vidéo autonomes lisibles sur ordinateur ; une capture JPEG isolée ou un serveur HTTP multipart MJPEG n'est pas un enregistrement AVI.

## Deux niveaux de réalisation à ne pas confondre

1. Le présent dépôt fournit plans, calcul et protocole. Le firmware caméra/PIR/AVI/SD n'existe pas ici.
2. L'implémentation future pourra évaluer ESP32-CAM_MJPEG2SD (support XIAO/OV3660 et AVI annoncé) puis figer version/configuration et licence. Le réveil profond et la fermeture robuste ne sont pas considérés acquis par simple présence du mot PIR. Voir [capture](capture.md).

Le besoin « déclenché PIR + réveil RTC » est une spécification future testable, pas une fonctionnalité livrée. Ne pas installer en comptant sur un firmware exemple de photos.

## Priorité à la faune au Havre

Entrée orientée est/sud-est selon vent/pluie du site réel, à au moins 2 m, support stable et hors accès chats, sans branche horizontale donnant accès au trou. Ni plein soleil ni ombre totale selon LPO : privilégier ombre aux heures chaudes. Relever sur place les ombres du toit matin/midi/après-midi, y compris feuillage saisonnier. Ne pas garantir que le panneau produira parce que l'emplacement convient aux oiseaux.

Panneau sur entretoises au-dessus d'un toit étanche indépendant ; il ne remplace pas la couverture, ne doit pas boucher la ventilation, ni transmettre la chaleur directement à la chambre. Batterie à l'arrière séparée, jamais dans la chambre ou en sandwich panneau/toit. Coffret protégé des embruns, du soleil, de l'humidité et de la condensation ; protection de charge au gel nécessaire mais non suffisante pour une installation durable.

Aucun perchoir, lumière, câble libre, vis saillante ou mousse accessible. Pas d'intervention sur nid occupé : ni ouverture, mise au point, retrait SD, recharge, déblocage PIR, ni mise à jour nécessitant approche. Une panne pendant l'occupation se résout en laissant le système arrêté. Nettoyage en automne seulement après confirmation d'absence d'oiseaux et autres occupants ; retirer l'électronique avant entretien humide, aucun chalumeau à proximité d'une batterie.
