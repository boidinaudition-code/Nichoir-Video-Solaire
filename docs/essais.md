# Essais et décision de pose

[Accueil](../README.md) · [Capture](capture.md) · [Énergie](energie.md) · [Bois](bois.md)

Statut de tous les essais matériels ci-dessous : **non exécuté**. Aucun firmware, montage, clip réel, relevé Wh ou température n'est disponible ici. Les tests Python ne valident que le modèle et la cohérence documentaire.

## Portes de validation sur nichoir vide

| Essai | Méthode / trace à conserver | Critère avant pose |
|---|---|---|
| Réception | Photos des références, ports V25, PID caméra, dimensions panneau et épaisseur bois | OV3660 et génération V25 conformes ; sinon réviser le dossier |
| Électricité | Contrôle polarité/DC et confirmation fournisseur P126/V25, tensions au démarrage/écriture | Compatibilité confirmée, pas de sous-tension/reset, aucune E/S > 3,3 V |
| Always On | Veille réelle 24 h puis capture ; essai de reprise après protection/décharge selon notice | USB-A maintenu, reprise documentée ou limitation explicitement acceptée |
| PIR / RTC | Fronts mesurés au banc, mouvement à courte portée dans chambre vide, REL maintenu haut/bas, faux positifs | Déclenchement reproductible et réarmement sans boucle de réveil ; limites notées |
| Vidéo | Clips 20 s VGA sur SD, scènes claires/sombres, mire à distances de nid possibles | Vrai AVI lisible sur PC, durée et cadence mesurées, netteté utile de jour ; nuit non exigée |
| Latence | Mesurer front PIR → première image, fermeture et réarmement | Profil compatible avec le modèle ou calculs refaits ; entrée rapide possiblement manquée documentée |
| SD / panne | Absente, pleine, erreur écriture, coupure durant capture, répétition des resets | Pas d'écrasement des clips clos, défaut borné, fichiers partiels distingués et redémarrage testé |
| Arrêt service | Demande d'arrêt pendant clip puis retrait SD hors tension | Fichier clos lisible ; aucun retrait durant écriture |
| Énergie | Au moins 72 h sans solaire, puis une semaine au site, Wh entrants/sortants et températures horodatés | Recalibrer veille/actif/pertes ; bilan cohérent pour l'usage retenu, pas une garantie annuelle |
| Température | Coffret et chambre instrumentés au site vide, limites fabricant contrôlées | Charge uniquement 0–45 °C ; blocage gel confirmé sans manipulation dangereuse de batterie |
| Pluie / condensation | Arrosage extérieur sans pression excessive, inspection après séchage, contrôle raccords et boucles | Chambre et électronique sèches, drainage/ventilation fonctionnels, aucune retenue d'eau |
| Mécanique / faune | Montage à blanc, panneau dans toit, retenues, support, passages optiques et pointes | Dimensions utiles respectées, aucun danger accessible, aucun perchoir, accès SD hors chambre |

Utiliser instruments adaptés ; un wattmètre USB peut perturber la veille et ne mesure pas directement la capacité cellule. Noter son influence. Ne pas provoquer volontairement surcharge, court-circuit, gel de charge ou surchauffe d'une batterie pour vérifier son BMS : utiliser la documentation et un protocole fabricant sûr.

## Fiche de résultat à remplir, sans préremplissage fictif

Pour chaque essai : date, opérateur, référence/lot matériel, version et commit firmware, configuration, instruments et précision, conditions, mesures brutes, critère, résultat conforme/non conforme, anomalies, corrections et nouveau résultat. Conserver les clips et relevés hors Git s'ils contiennent des données personnelles ; aucun échantillon n'est fourni ici.

## Go / no-go

Pas de pose active avant réalisation du firmware et clôture des portes obligatoires. Si une limite reste ouverte : différer l'électronique et garder le nichoir passif, ou laisser le système éteint. Ne pas compenser un bilan solaire mauvais en exposant la nichée au soleil. Confirmer l'absence de tout occupant avant pose, entretien ou récupération SD. Une fois occupé : aucune intervention, même par trappe technique ; une panne est laissée à l'arrêt jusqu'à libération confirmée.
