# Module `static`

## Raison d’être

Ce module contient tous les fichiers statiques de l’application Flask.  
Ces fichiers sont servis directement au navigateur et ne sont pas générés dynamiquement par le serveur.

---

## Principaux fichiers et responsabilités

- `style.css` : fichier principal de styles CSS pour la calculatrice web.  
  Il gère :
  - La mise en page de la calculatrice
  - Les couleurs et les polices
  - Le style des boutons et du champ de résultat

---

## Dépendances / Hypothèses

- Les fichiers statiques sont référencés dans les templates HTML via 
```html
    {{ url_for('static', filename='style.css') }}
```
- Ce module suppose l'existence des classes HTML suivantes :
```bash
    .calculator
    .buttons
    .btn
    .operator
```