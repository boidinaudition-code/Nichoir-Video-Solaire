# Décision V2 — brainstorm solaire, clips Wi-Fi et galerie Unraid

> **Partiellement remplacée par V3 : caméra, éclairage, résolution, audio, détection, panneau, toit et batterie → [README](../README.md) / [recherches V3](recherches-v3.md). §2 livraison durable reste valide.** Les autres choix et protocoles ci-dessous sont historiques V2, pas les prescriptions V3.

Statut : décision documentaire de conception, conditionnelle aux essais ci-dessous. Aucun firmware, service Unraid, transcodage ou déploiement n'est livré. Aucun essai matériel exécuté. Cette page remplace les choix V1 ; les huit pages anciennes restent des archives V1 signalées par bannière. Le comparatif PIR/OV5640 est un complément courant, pas une archive V1. Aucun prix ni total BOM V2 n'est établi.

[Accueil et archives V1](../README.md) · [CSV PVGIS fourni](pvgis-le-havre.csv) · [Comparatif des 14 dépôts PIR/OV5640](comparatif-pir-ov5640.md)

## 1. Chaîne retenue et limites

PIR BS612 → réveil XIAO ESP32S3 Sense, cible capteur **OV5640 à confirmer par PID à réception** → clip MJPEG dans un vrai **AVI sur microSD FAT32** → fermeture/synchronisation → envoi Wi-Fi différé → réception durable sur Unraid → conversion MP4 pour une galerie dédiée.

- La consigne OV5640 remplace l'OV3660 V2 antérieur ; l'OV3660 reste historique V1. Seeed annonce encore des lots mixtes : confirmer le lot, le PID, l'optique et la révision, sans substitution silencieuse. Précision V3 : selon le [guide Seeed](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started), l'OV5640 livré avec la Sense est à focale fixe ; seul le module long vendu séparément a un autofocus, et sa [fiche](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/new-res/OV5640_Camera_Module_Specification.pdf) indique un filtre IR-cut. La V3 choisit un NoIR dont le brochage reste à vérifier.
- Cible de travail : 100 clips/jour de 20 s, VGA 640 × 480 comme témoin de repli, 10 images/s à vérifier, sans audio, IR, éclairage ou flux permanent. Comparer photo 5 MP et 1080p, puis vidéo 1080p selon le [protocole sans oiseaux](comparatif-pir-ov5640.md) ; ni vidéo 5 MP, ni 10 images/s en 1080p ne sont promis. Résolution finale conditionnée à la qualité utile, aux FPS acquis, aux temps actifs, aux Wh et à la température mesurés. Les 3 s hors clip sont une hypothèse pour démarrage, exposition, fermeture et réarmement, pas une mesure ; toute dérive impose un nouveau budget.
- Pas d'import Frigate : Frigate n'est ni la galerie, ni le destinataire des clips, ni une dépendance. Le MP4 est un dérivé pour lecture web, pas le format d'enregistrement ESP32. Transcodage asynchrone sur Unraid, codec/navigateur à qualifier ; conserver l'AVI original selon rétention explicite.
- Le Wi-Fi est activé seulement pour des fenêtres bornées. Une panne réseau ne doit pas empêcher la capture tant que l'espace SD et la réserve le permettent. Pas de serveur vidéo permanent sur la carte.
- Préserver la chambre utile V1, trou LPO, ombre aux heures chaudes, absence de perchoir et séparation de la batterie. Le toit V1 et son débit ne valent plus pour le grand panneau. Aucune intervention sur nichoir occupé : panne laissée à l'arrêt ; essais sur nichoir vide uniquement.

## 2. Livraison durable, déduplication et réessais

Spécification future, non implémentée ; un HTTP 200 ou une arrivée en RAM n'est pas un ACK durable.

1. Finaliser l'index AVI, synchroniser et fermer sur SD avant mise en file. Les fichiers temporaires/incomplets restent distincts. Attribuer une identité persistante (identifiant appareil + séquence monotone persistée), indépendante de l'heure civile et non réutilisée après reset ; joindre taille et empreinte SHA-256 du contenu fermé.
2. Uploader vers un récepteur local authentifié avec transport TLS validé, secrets hors Git, ni port public ni endpoint sans authentification. Écrire en temporaire, contrôler taille/empreinte, synchroniser le fichier, publier par renommage sur le même système de fichiers, synchroniser le répertoire et persister l'index de déduplication. Vérifier la sémantique réelle du stockage Unraid ; une file de transcodage en mémoire ou un cache non qualifié ne suffit pas.
3. ACK seulement après cette persistance de l'AVI et de son identité. Il contient identité, taille, empreinte et statut durable vérifiables. La conversion MP4 n'est pas un prérequis de l'ACK : elle est relançable depuis l'AVI durable. Publier le MP4 atomiquement après validation indépendante ; ne jamais montrer un MP4 partiel dans la galerie.
4. ACK perdu : renvoi du même identifiant/contenu → même ACK sans deuxième clip. Même identifiant avec empreinte différente → conflit explicite, aucune substitution silencieuse. Après crash serveur, reconstruire/réconcilier index et fichiers avant d'acquitter ; tester les coupures à chaque étape.
5. La carte persiste l'ACK sur SD avant toute suppression locale. Aucun effacement sans ACK correspondant exactement au clip. Une suppression après ACK n'est pas une sauvegarde : fixer quotas/rétention Unraid et sauvegarde séparée. Une perte serveur après ACK ne doit pas être masquée par une garantie d'archivage inexistante.
6. Proposition de bornes à qualifier : au plus 3 tentatives par clip et 6 fenêtres réseau/jour, espacées avec backoff et gigue ; chaque fenêtre radio plafonnée à 30 s, puis sommeil. Compteur persistant entre resets, pas de boucle de reboot réinitialisant les limites. Après épuisement, conserver le clip en attente bloquée jusqu'à réarmement explicite de la politique hors occupation ; pas de suppression automatique. Dimensionner et mesurer le budget des fenêtres, associations et réessais, pas seulement des transferts réussis.
7. SD pleine : arrêter proprement les nouvelles captures, conserver les clips non acquittés ; aucune rotation silencieuse. Borner aussi attentes PIR haut, erreurs SD, DNS/TLS et indisponibilité serveur. Tester la reprise après coupure, le réarmement PIR et la latence avant de promettre les 100 clips/j.

Le scénario énergétique ci-dessous compte 10 ou 30 s **par clip** de réseau total (association, transfert, ACK et éventuels réessais inclus), pas une autorisation de multiplier cette durée par trois sans recalcul. Taille réelle AVI et débit Wi-Fi restent inconnus. La politique proposée plafonne l'activité ; elle ne garantit pas de vider chaque jour une file de 100 clips.

## 3. PVGIS Le Havre : requête et provenance

Source primaire : [API PVGIS JRC MRcalc](https://re.jrc.ec.europa.eu/api/v5_3/MRcalc?lat=49.49&lon=0.10&startyear=2005&endyear=2023&raddatabase=PVGIS-SARAH3&horirrad=1&optrad=0&selectrad=1&angle=9&aspect=0&outputformat=json). [Documentation API JRC](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/getting-started-pvgis/api-non-interactive-service_en).

Paramètres explicites : latitude 49.49, longitude 0.10 ; 2005–2023 inclus ; base PVGIS-SARAH3 ; MRcalc ; `selectrad=1`, `angle=9` degrés depuis l'horizontale, `aspect=0` = sud (pas nord), `optrad=0` ; `horirrad=1` ajoute la série horizontale mais les calculs utilisent **H(i)_m**, pas H(h)_m. Horizon topographique par défaut (`use_horizon=true` confirmé dans la réponse), pas de masque des arbres, du bâtiment ou du toit local. Aucun azimut optimal substitué au sud demandé.

Le CSV provient de `/opt/data/cache/scratch/nichoir-pvgis-le-havre.csv` : données et en-têtes inchangés, seules les fins de ligne CRLF sont normalisées en LF pour le contrôle Git. L'API a été interrogée pour vérifier les paramètres et la concordance des moyennes ; le CSV fourni reste le jeu documentaire de référence. Méthode : pour chaque mois, moyenne sur 19 années de `H(i)_m / nombre_de_jours_du_mois` (février bissextile compris). Les kWh/m²/j donnent numériquement les HSP/j. Arrondir les HSP à 3 décimales ; les colonnes Wh sont arrondies, pas des mesures. La précision des totaux mensuels API peut influer sur la dernière décimale.

| Mois de référence | HSP/j moyennes | P126 2 W, rendement 50 % | P110 calculé à 9,54 W, rendement 50 % |
|---|---:|---:|---:|
| Décembre | 1,023 | 1,02 Wh/j | 4,88 Wh/j |
| Avril | 4,966 | 4,97 Wh/j | 23,69 Wh/j |

`Esolaire = P × HSP × 0,50 × fraction solaire restante`. Le rendement global 50 % est une hypothèse incluant conversion, charge, câbles, température et fonctionnement hors MPP, à mesurer ; ne pas compter ces pertes deux fois. Ombre locale et blocage de charge au gel sont supplémentaires. Demi-soleil en décembre : **2,44 Wh/j** avec 9,54 W ; ce facteur 0,5 est une sensibilité simplifiée, pas un modèle physique des ombres partielles. Moyenne climatique ≠ jour minimum, prévision météo ou garantie d'autonomie.

## 4. Besoin énergétique V2 reproductible

Hypothèses V25 héritées, **à remesurer intégralement avec l'OV5640** : USB régulé 5 V ; veille système complète 5 mA (PIR/caméra/SD compris), actif capture et réseau 350 mA ; conversion batterie→USB 85 % ; consommation propre 26 mW = 0,624 Wh/j. Seeed laisse la consommation OV5640 à « TBD » : aucune ancienne valeur OV3660 ne qualifie ce montage. Courants, stabilisation d'exposition, FPS réels, taille AVI, débit SD, radio et réessais restent inconnus. Les phases actives remplacent la veille, elles ne s'y ajoutent pas. Les tableaux et autonomies ci-dessous restent des **sensibilités historiques de calcul**, pas un dimensionnement OV5640 validé ; recalculer panneau, réserve et marges après intégration des Wh mesurés par phase.

```text
N = 100 clips/j ; T = N × (20 + 3 + upload_s)
Eusb = 5 × [350 × T + 5 × (86400 − T)] / 3600000
Ecellule = Eusb / 0,85 + 0,026 × 24
```

| Upload total par clip | Actif s/j | USB Wh/j | Besoin cellule Wh/j |
|---|---:|---:|---:|
| 10 s | 3300 | 2,181 | **3,19** |
| 30 s | 5300 | 3,140 | **4,32** |

Comparaison : USB 5 V × 140 mA × 24 h = **16,8 Wh/j USB** en continu (environ 20,39 Wh/j cellule avec ces pertes/propre), pas 16,8 Wh/j cellule. Le continu est exclu, même si le grand panneau paraît suffisant en avril.

P126 **2 W : printemps seulement, conditionnel**. Avril à 4,97 Wh/j dépasse les deux besoins moyens, mais la marge du profil lent est faible : ombre, latence, réessais, gel, veille et semaines grises peuvent l'annuler. Mars à 3,20 Wh/j ne couvre pas le profil 30 s et laisse le profil 10 s sans marge fiable. Décembre à 1,02 Wh/j est déficitaire dans les deux cas. Ne pas annoncer une autonomie printemps acquise.

P110 : décembre à 4,88 Wh/j laisse environ 0,56 Wh/j de marge sur le besoin 4,32 ; à demi-soleil 2,44 Wh/j, déficit dans les deux scénarios. Le passage d'épisodes sombres dépend donc du stockage et de la température, pas seulement de la moyenne mensuelle.

## 5. Panneau et toit V2

Source primaire consultée : [Voltaic P110, page historique « 9-watt-panel »](https://voltaicsystems.com/9-watt-panel/), actuellement présentée comme **10 Watt 6 Volt Solar Panel – ETFE**, SKU P110. La page donne **9,54 W**, Vmp 5,71 V, Imp 1670 mA, Voc 6,94 V, tolérance puissance ±10 %, **223 × 274 × 4 mm**, 328 g. « Classe 10 W » est un nom commercial ; la révision vendue doit être identifiée et sa fiche contrôlée avant achat. Pas de substitution silencieuse à une ancienne version ou autre tension. Le calcul garde 9,54 W, sans présumer un 10 W garanti.

Toit proposé **250 × 300 mm**, panneau 223 en largeur et 274 sur rampant : marges centrées **13,5 mm latérales et 13 mm longitudinales**. À confirmer par gabarit avec fixations, sortie câble, étanchéité indépendante, ventilation et tenue au vent ; ce n'est pas encore un débit bois validé. Inclinaison cible 9°, à vérifier au montage. Garder chambre et batterie ombragées, coffret batterie distinct et jamais sous le panneau chaud. Une exposition défavorable impose l'arrêt vidéo, pas le déplacement du nid au soleil.

## 6. Deux options d'alimentation, aucune qualifiée

### A — USB régulé par power bank

Option la plus simple si un modèle documenté et testé convient : sortie 5 V stable à faible charge, maintien Always On, charge et alimentation **simultanées** sans interruption, reprise automatique après entrée solaire intermittente, batterie vide, coupure et protection thermique. Essayer chaque transition, pas seulement vérifier une mention « pass-through ». V25 est une référence de comportement/hypothèses, pas la preuve que toute power bank convient. Respecter ports et génération ; sa réserve V1 n'est pas 72 Wh. Pas de panneau brut branché en USB.

La [notice V25 constructeur](https://voltaicsystems.com/content/batteries/V25_50_75_Instructions_2025.pdf) et les [spécifications V25](https://voltaicsystems.com/v25/) doivent être confrontées au panneau réel : plage d'entrée, polarité, connecteur, Vmp et surtout **Voc à froid avec tolérances**. Une compatibilité ne se déduit ni de « 6 V », ni de la forme du connecteur. Les ambiguïtés V1 restent des points ouverts, pas une autorisation de branchement.

### B — Pack professionnel 1S5P protégé, cible nominale 72 Wh

Pack assemblé/qualifié par un professionnel avec cellules appairées, protections adaptées, fusible, sonde thermique, connectique et coffret extérieur sûrs. **Pas de couplage direct de cinq XTAR**, pas de cellules amovibles mélangées en parallèle, pas de raccordement aux pastilles BAT de la XIAO en parallèle de l'USB. Capacité 72 Wh = spécification cible à confirmer par fiche/mesure, pas un modèle commercial déjà sélectionné.

Réserve de calcul 80 % × 72 = **57,6 Wh cellule**. Sans aucun solaire : 57,6 / 4,3176 ≈ **13,34 jours** ; 57,6 / 3,1902 ≈ **18,06 jours**, soit **13–18 jours**. Ce sont les mêmes hypothèses V25 de conversion/propre appliquées provisoirement au pack ; elles ne caractérisent pas sa future électronique. Froid, vieillissement, BMS, rendement boost, courant de repos et seuil d'arrêt à mesurer ; ne pas présenter cette autonomie comme garantie.

Chaîne à qualifier : panneau → chargeur **Li-ion 1S 4,20 V CC/CV**, power path → pack protégé / régulateur USB 5 V → XIAO. Le BMS ne remplace ni chargeur, ni régulation, ni inhibition de charge au gel. NTC physiquement au contact du pack, défaut ouvert/court-circuit sûr, blocage charge sous 0 °C et au-dessus de la limite fabricant (0–45 °C au plus dans ce dossier), hystérésis/reprise validées. La régulation thermique du circuit n'est pas une protection du pack contre le gel.

Candidat seulement : [TI BQ25185](https://www.ti.com/product/BQ25185), [datasheet primaire](https://www.ti.com/lit/ds/symlink/bq25185.pdf). Chargeur **linéaire**, power path, support solaire VINDPM (ne pas promettre un MPPT complet), réglable à 4,20 V, charge **1 A maximum**, entrée de fonctionnement 3–18 V ; tolérance absolue 25 V ≠ tension normale autorisée. Qualifier le module réel et ses composants, pas seulement la puce : TS/NTC, configuration 4,20 V, limites d'entrée, Voc panneau à froid, surtensions, polarité et courant disponibles.

À 1 A, la dissipation linéaire approche `(Vin − Vbat) × Icharge`, plus pertes système : par exemple (5,71 − 3,7) × 1 ≈ **2,01 W**, ordre de grandeur à confronter à la tension réelle et au partage de charge. Examiner cuivre/pad thermique, coffret chaud et repli thermique ; charge 1 A et puissance panneau ne sont pas garanties simultanément. Rendement réel peut être inférieur aux 50 % globaux choisis. Une sortie SYS annoncée 4,5 V ne remplace pas le **5 V USB régulé** ; vérifier boost et priorités power path. Aucune carte électronique n'est conçue ou déployée ici.

## 7. Sources primaires et portes d'essais

Autres références : [Seeed Sense et variantes caméra](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/), [Voltaic P126](https://voltaicsystems.com/P126/), [fiche P126 et historique de révisions](https://voltaicsystems.com/content/P126_ds.pdf), [LPO nichoirs](https://www.lpo.fr/la-lpo-en-actions/mobilisation-citoyenne/refuges-lpo/tutoriels/nichoirs-pour-passereaux). Les pages P110, TI et la réponse MRcalc ont été consultées pour cette V2 ; les références héritées ne sont pas une nouvelle vérification de tous les lots/prix. Aucun stock ou prix V2 revalidé. Un dépôt de firmware candidat n'est pas une preuve d'intégration.

Tous les essais suivants restent **non exécutés** :

| Porte | Traces et critères à recueillir avant toute pose active |
|---|---|
| Réception | PID OV5640, lot/optique et révision Sense, références/révisions panneau/pack/chargeur, dimensions, gabarit toit ; aucune substitution implicite |
| Capture | Sur nichoir vide : photos 5 MP contre 1080p en basse lumière, clips AVI 20 s 1080p et témoin VGA décodés indépendamment ; FPS acquis distincts de la lecture, latence/exposition et température, SD absente/pleine, coupure en écriture, PIR haut et faux positifs ; pas de perte de clips clos, aucune cadence promise |
| Réseau et durabilité | Serveur indisponible, timeout, ACK perdu/faux, doublon, conflit d'identité, crash avant/après sync/renommage/index/ACK, reset ESP ; un seul original durable, aucun effacement prématuré, bornes persistantes respectées |
| Galerie | AVI→MP4 sur Unraid après réception, durée et décodage contrôlés, transcodage raté relançable, rétention/quotas/sauvegarde et absence d'import Frigate ; aucune publication de fichier partiel |
| Énergie | Avec OV5640 : Wh et courants du système complet, veille/démarrage/exposition/capture/fermeture/radio/réessais, temps par phase, poids AVI et débit ; revoir budgets 10/30 s et réserve utile ; 72 h sans solaire et au moins une semaine au site vide, comparaison CSV sans confondre météo et climat |
| Sécurité électrique | USB stable, faible charge, simultanéité et reprise après coupure/vide, compatibilité Voc à froid/entrée, protection pack, charge 4,20 V et blocage NTC/gel par protocole fabricant sûr, rendement et dissipation à 1 A |
| Mécanique/faune | Pluie/condensation, ventilation, tenue vent, températures chambre et pack, marges panneau/câbles, ombre et chambre utile ; pas d'intervention occupée |

Consigner date, opérateur, lots, version/commit firmware futur, instruments, conditions, mesures brutes, anomalies et critères. Ne pas provoquer court-circuit, surcharge ou charge gel réelle pour tester une protection : protocole fabricant/simulation de sonde au banc. Sans clôture de ces portes : nichoir passif ou vidéo arrêtée.

## 8. Contrôles locaux et périmètre des outils V1

`tools/dimensionnement.py`, `tools/verifier_dossier.py` et `tests/test_dimensionnement.py` restent **V1 uniquement** ; seuls les chemins du vérificateur sont adaptés aux [archives V1](archive/v1/README-v1.md), avec contrôle récursif des liens. La logique de calcul ne change pas. Ils ne modélisent pas automatiquement le réseau V2, le pack 72 Wh ou le nouveau toit et ne valident pas la V3.

Rejouer les tests V1 et le contrôle de format depuis la racine :

```sh
python -m unittest discover -s tests -v
python tools/verifier_dossier.py
git diff --check
```

Contrôle V2 minimal exécutable, sans dépendance ni modification des outils :

```sh
python -c 'import csv; from pathlib import Path; r=list(csv.DictReader(Path("docs/pvgis-le-havre.csv").open(),delimiter=";")); assert [int(x["mois"]) for x in r]==list(range(1,13)); h=list(r[0])[1]; assert float(r[11][h])==1.023 and float(r[3][h])==4.966; assert all(abs(float(x[list(x)[2]])-2*float(x[h])*.5)<.011 and abs(float(x[list(x)[3]])-9.54*float(x[h])*.5)<.011 for x in r); besoins=[(5*(350*(100*(23+t))+5*(86400-100*(23+t)))/3600000)/.85+.624 for t in (10,30)]; assert [round(x,2) for x in besoins]==[3.19,4.32]; assert round(9.54*1.023*.5,2)==4.88 and round(9.54*1.023*.25,2)==2.44; assert [round(57.6/x,2) for x in besoins]==[18.06,13.34]; print("OK V2 : CSV 12 mois, production, besoins et reserve")'
```

Les contrôles arithmétiques ne sont pas des essais de batterie, de vidéo, de livraison durable ou d'autonomie. Aucun push ni déploiement demandé ; le commit reste local. Toute publication ultérieure demeure soumise à la validation applicable de Jean Vérif.

### Résultats locaux de cette mise à jour

Les résultats PVGIS et calculs ci-dessous proviennent de la mise à jour V2 antérieure ; ils ne constituent pas des mesures OV5640. La nouvelle revue des 14 dépôts, les corrections des résumés et le protocole matériel non exécuté figurent dans le [comparatif](comparatif-pir-ov5640.md). Aucun changement sur Unraid.

- 8 tests unitaires V1 : réussis ; vérificateur V1 : cohérence locale réussie (BOM historique, énergie V1, valeurs bois et liens, sans qualification matérielle).
- CSV : données identiques au fichier fourni après normalisation des fins de ligne CRLF→LF ; 12 mois uniques et ordonnés ; colonnes de production cohérentes avec rendement 50 %.
- Requête MRcalc ci-dessus exécutée : moyennes de `H(i)_m / jours_du_mois` sur 19 ans concordantes avec les **12 HSP du CSV à 3 décimales**, dont décembre 1,023 et avril 4,966.
- Besoins cellule recalculés : 3,190176 et 4,317627 Wh/j ; réserve 57,6 Wh : 18,0554 et 13,3407 jours théoriques. Sources P110 et TI consultées, aucun achat ou déploiement effectué.
