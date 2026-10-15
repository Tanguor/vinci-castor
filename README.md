# Prix Castor VINCI

Estimation du prix de souscription Castor selon le calendrier 2027 : moyenne des 20 cours d'ouverture
précédant la fixation (le 15 du mois avant le quadrimestre), moins 5 %, avec la marge d'erreur.

| Fichier | Usage |
|---|---|
| `site/` | Version hébergée (GitHub Pages), lit `site/prices.json` |
| `index.html` + `server.py` | Version locale : `python server.py` puis http://localhost:8000 |
| `castor-vinci.html` | Page autonome, cours intégrés |
| `update_prices.py` | Réécrit `site/prices.json` avec les 60 dernières séances DG.PA |

## Mise en ligne sur GitHub Pages

1. Créer un dépôt vide sur GitHub (ex. `vinci-castor`).
2. Pousser ce dossier :
   `git remote add origin https://github.com/<compte>/vinci-castor.git` puis `git push -u origin main`
3. Sur GitHub : **Settings › Pages › Build and deployment › Source : GitHub Actions**.
4. **Actions › Mise à jour des cours › Run workflow** pour la première publication.

Le site est ensuite à `https://<compte>.github.io/vinci-castor/` et les cours sont relevés
chaque soir de bourse à 17 h 30 UTC. GitHub suspend les tâches planifiées d'un dépôt sans activité
depuis 60 jours : un clic sur **Enable workflow** dans l'onglet Actions les relance.

Les prix officiels des offres passées sont dans `KNOWN_OFFERS` (dans chaque page) : à compléter
à chaque annonce VINCI.
