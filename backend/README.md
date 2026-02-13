# Module `backend`

## Raison d’être

Le module `backend` contient toute la logique applicative de la calculatrice web.

Il est responsable :

- Du traitement des requêtes HTTP via Flask
- De l’analyse et de l’évaluation des expressions mathématiques
- De l’implémentation des opérations arithmétiques
- De la gestion des erreurs

Ce module sépare clairement la logique métier de l’interface utilisateur (HTML/CSS), ce qui améliore la maintenabilité et la testabilité du projet.

---

## Fichiers et responsabilités

### `app.py`

Responsabilités principales :

- Initialise l’application Flask
- Configure les chemins vers les dossiers `templates/` et `static/`
- Définit la route principale (`/`)
- Récupère l’expression entrée par l’utilisateur
- Appelle la fonction `calculate`
- Transmet le résultat au template HTML

---

### `operators.py`

Ce fichier contient les fonctions arithmétiques de base :

- `add(a, b)` → addition
- `subtract(a, b)` → soustraction
- `multiply(a, b)` → multiplication
- `divide(a, b)` → division

Ces fonctions sont volontairement isolées afin de :

- Séparer la logique de calcul de la logique web
- Faciliter les tests unitaires
- Permettre l’extension future (ex: nouvelles opérations)

---

## Dépendances

- Python
- Flask

Le module dépend également des dossiers externes :

- `templates/` pour l’interface HTML
- `static/` pour les fichiers CSS
