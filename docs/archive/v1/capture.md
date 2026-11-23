# Capture AVI — spécification à implémenter

> **ARCHIVE V1 OBSOLÈTE.** La [décision V2](../../decision-v2.md) ajoute Wi-Fi, ACK durable, déduplication, réessais bornés et galerie MP4 Unraid ; voir aussi les [décisions V3](../../recherches-v3.md). Les étapes SD ci-dessous ne constituent pas le protocole complet courant ; aucun firmware livré.

[Accueil](../../../README.md) · [Câblage](cablage.md) · [Essais](essais.md) · [Sources](sources.md)

Aucun firmware n'est livré. Les étapes suivantes sont des exigences, pas des fonctions testées. Cible : XIAO ESP32S3 Sense avec OV3660 confirmé par PID, microSD FAT32, JPEG VGA 640 × 480, AVI MJPEG de 20 s, cible 10 images/s, sans audio ni éclairage.

## Séquence attendue

1. Au démarrage, distinguer réveil PIR, timer et démarrage après coupure. Initialiser les GPIO RTC, caméra et SD selon les pins Sense ; refuser proprement un capteur inattendu ou une SD absente. Pas de boucle infinie énergivore en défaut : temporisation puis sommeil, diagnostic consultable au banc.
2. Attendre exposition stable avec un délai borné, sans promettre une capture immédiate. Mesurer du front PIR à la première image exploitable. Les 3 s du modèle couvrent démarrage, fermeture et réarmement : si dépassées, recalculer.
3. Créer un nom unique même sans heure civile fiable (compteur persistant ou recherche de nom libre) et écrire d'abord un fichier temporaire. Ne jamais écraser un clip existant après reset.
4. Écrire les trames JPEG dans un vrai conteneur RIFF/AVI : tailles, alignements, nombre de trames et index cohérents. Une concaténation de JPEG ou un flux HTTP MJPEG n'est pas un AVI. Mesurer débit effectif et images perdues ; ne pas déclarer 10 images/s si non atteint.
5. Après 20 s, finaliser les en-têtes et l'index, synchroniser, fermer, puis renommer en `.avi`. Ce protocole réduit le risque sans garantir l'atomicité de FAT32 ni protéger contre toute coupure BMS.
6. À saturation SD, arrêter la capture sans supprimer d'anciens clips dans cette V1. Au redémarrage, isoler les fichiers incomplets sans les présenter comme valides ; récupération éventuelle uniquement hors occupation.
7. Attendre REL bas stable avant d'armer EXT0 haut sur GPIO1. Une sortie maintenue haute peut provoquer des réveils immédiats en boucle. Borner l'attente puis utiliser un sommeil timer de repli si nécessaire ; mesurer et comptabiliser cette consommation. Tester PIR maintenu haut, retrigger et faux positifs.
8. Désinitialiser caméra/SD proprement, préparer les GPIO RTC et entrer en sommeil profond. Conserver l'alimentation PIR ; ne pas supposer que la Sense complète consomme comme la carte nue.

Le bouton service doit demander un arrêt propre, puis indiquer au banc que les écritures sont terminées avant coupure/retrait SD. Il ne constitue pas une permission d'approcher un nid occupé.

## Pistes existantes, non intégrées

[s60sc/ESP32-CAM_MJPEG2SD](https://github.com/s60sc/ESP32-CAM_MJPEG2SD) est le candidat pour l'enregistrement MJPEG/AVI. Avant réutilisation : figer un commit, lire licence et configuration, confirmer support exact XIAO/OV3660/SPI SD et tester sommeil profond, PIR et finalisation ; aucun de ces points n'est validé ici par compilation.

[TeTeHacko/chytra-budka](https://github.com/TeTeHacko/chytra-budka) est une piste de nichoir avec XIAO. Ce lien ne prouve ni une alimentation solaire réalisée, ni l'autonomie de notre montage, ni notre chaîne AVI/PIR.

## Stockage et validation

À 10 images/s, 20 s donnent 200 images cibles. Le poids JPEG dépend de la scène et de la qualité : mesurer les octets par clip avant de calculer la capacité SD et la rétention. Ni les 32 Go commerciaux ni une moyenne JPEG supposée ne garantissent une durée. Limiter chaque fichier sous la limite FAT32 de 4 Gio et vérifier l'espace disponible avant écriture.

Lire chaque clip d'essai sur ordinateur avec un lecteur vidéo indépendant ; si disponible, `ffprobe -v error -show_streams -show_format fichier.avi` complète le contrôle. Vérifier aussi durée, nombre de trames décodées, absence de troncature et lisibilité après coupure pendant le clip suivant. Aucun fichier AVI ni résultat ffprobe n'a été produit dans ce dépôt.
