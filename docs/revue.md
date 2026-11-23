# État factuel du dossier local

[Accueil](../README.md) · [Essais](essais.md) · [Sources](sources.md) · [Vérificateur](../tools/verifier_dossier.py)

## Périmètre livré

Dossier de conception V1 : architecture, câblage, débit bois, modèle d'énergie Python, tests unitaires, spécification de capture AVI et protocole d'essais. Les pages capture, essais, sources et ce rapport complètent les liens du README. Le titre public ne contient plus de prénom ni de localisation personnelle. Le contexte climatique conservé dans l'étude énergétique n'est pas une donnée météo mesurée.

Aucun firmware caméra/PIR/AVI n'est implémenté. Aucun montage, essai matériel, vidéo réelle, relevé électrique, test d'étanchéité ou étude PVGIS n'a été réalisé. Les hypothèses énergétiques et prix/provisions ne sont pas des performances ou devis garantis.

## Contrôles reproductibles

Depuis la racine, avec Python ≥ 3.10 et bibliothèque standard :

```sh
python -m unittest discover -s tests -v
python tools/verifier_dossier.py
python tools/dimensionnement.py --clips 100 --hsp 1
python tools/dimensionnement.py --clips 100 --hsp 1 --ombre 0.5
```

Les 8 tests unitaires du calculateur ont été exécutés avec succès pendant la finalisation. La somme des 7 lignes à prix fixe a été recalculée : **123,33 €**. Les 8 provisions ajoutent **69–141 €**, soit **192,33–264,33 € TTC hors port**, lecteur PC inclus, instruments exclus. Les conversions HT → TTC sont arrondies par ligne à 20 %. Il s'agit d'une vérification arithmétique des montants du dossier, pas d'un panier marchand revalidé.

Le vérificateur contrôle les fichiers attendus, liens locaux, syntaxe HTTPS des références, somme de la BOM, conversions TVA, quatre lignes des deux tableaux d'énergie, formule indépendante du besoin cellule, réserve et ombre. Pour le bois, il recalcule seulement huit valeurs numériques (hauteur utile, deux marges panneau, bord inférieur du trou et quatre hauteurs de côtés) et vérifie leur présence textuelle dans la page. Il ne relie pas ces nombres à leurs libellés ou tableaux : ce n'est ni une validation complète des cotes ni un contrôle du plan ou du montage. Il échoue sur les incohérences couvertes par ces contrôles limités. Il ne teste pas la disponibilité des pages distantes, leur contenu, le stock, les prix actuels, les ancres Markdown ou le matériel ; un lien local à ancre est explicitement refusé plutôt que déclaré validé.

## Points ouverts avant toute pose active

- Confirmer PID OV3660, révision V25 et compatibilité P126/V25 ; lever l'ambiguïté de diamètre DC de la notice.
- Implémenter puis tester AVI, démarrage, arrêt propre, SD pleine/coupée, réarmement PIR et sommeil profond.
- Mesurer courants, énergie utile, latence, température et comportement Always On ; remplacer les hypothèses si nécessaire.
- Valider protections mécaniques, pluie/condensation, optique et respect de la faune sur nichoir vide.
- Références GitHub candidates non intégrées, sans compilation ni audit de licence ; XiaoBird non identifié. Aucun solaire réalisé n'est attribué à chytra-budka.

## Coordination et publication

Sur instruction explicite : finalisation et commit local uniquement, sans lancement de review ni sous-agent, sans push. Ce rapport n'est pas une revue indépendante et ne constitue pas un `VALIDATION_OK` de Jean Vérif. Aucune validation de sa part n'est revendiquée. Un éventuel push ultérieur reste soumis au workflow de validation applicable.
