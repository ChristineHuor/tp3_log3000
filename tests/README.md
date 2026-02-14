# Module `tests`

## Objectif

Ce module contient les tests unitaires du projet.

Son rôle est de vérifier que les fonctions arithmétiques du module `backend.operators`
fonctionnent correctement et produisent les résultats attendus.

---

## Fichier de test

### `test_calculator.py`

Ce fichier contient une suite de tests implémentée avec le module standard `unittest` de Python.

La classe `TestCalculator` valide le comportement des fonctions suivantes :

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

---

## Couverture des tests

Les tests actuels couvrent :

- Addition de deux nombres positifs
- Soustraction de deux nombres positifs
- Multiplication de deux entiers
- Division produisant un résultat flottant

Chaque test vérifie que la valeur retournée correspond exactement au résultat attendu.

Les tests se concentrent uniquement sur la logique métier et sont indépendants
de l’interface web Flask.

---

## Comment exécuter les tests

Depuis la racine du projet, exécuter les tests avec la commande suivante:

```bash
python -m unittest discover tests
```