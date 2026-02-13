# Module `templates`

## Raison d’être

Ce module contient tous les fichiers HTML utilisés par Flask pour générer les pages web de l’application. Il assure également 
l’affichage dynamique des données transmises par le backend.

---

## Principaux fichiers et responsabilités

- `index.html` : template principal de la calculatrice web.  
  Il contient :
  - Le formulaire pour entrer les expressions
  - Le champ d’affichage du résultat
  - Les boutons pour les chiffres et opérateurs
  - Les liens vers le CSS dans `static/style.css`
  - Le code JavaScript pour gérer l’affichage et le nettoyage du champ

---

## Dépendances / Hypothèses

- `index.html` utilise `{{ result }}` pour afficher dynamiquement le résultat renvoyé par Flask, alors ce module suppose qu'on lui transmet une telle variable.
- Dépend de `static/style.css` pour l’affichage et le style des éléments  
- Doit rester dans `templates/` pour que Flask puisse le trouver automatiquement