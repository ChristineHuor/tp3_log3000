# Application Web de Calculatrice avec Flask

**Cours :** LOG3000  
**TP :** #3  
**Numéro d’équipe :** 10

## Description du projet

Ce projet consiste à configurer et structurer une application web de calculatrice simple développée avec Flask (Python).

---

## Objectif du projet

L’objectif principal du projet est de :

- D’organiser un projet Python selon une structure modulaire claire
- Mettre en place un dépôt GitHub collaboratif
- Appliquer de bonnes pratiques de gestion de versions et de documentation
- Préparer une base maintenable et testable

---

### Portée

L’application supporte actuellement les opérations arithmétiques suivantes :

- Addition (`+`)
- Soustraction (`-`)
- Multiplication (`*`)
- Division (`/`)

Limitations actuelles :

- Une seule opération par expression (ex: `3+4`)
- Pas de parenthèses

---

## Prérequis d’installation

Avant de commencer, assurez-vous d’avoir installé :

- Python et pip installés
- Git installé localement
- Un compte GitHub

Vérifiez que tout est installé correctement :

```bash
python --version
pip --version
git --version
```
---

## Instructions d’installation

1. Cloner le dépôt :
```bash
git clone https://github.com/ChristineHuor/tp3_log3000.git
cd tp3_log3000
```
2. Créer un environnement virtuel :

Sur Windows :
```bash
python -m venv env
env\Scripts\activate
```
Sur macOS / Linux :
```bash
python3 -m venv env
source env/bin/activate
```
3. Installer les dépendances :

```bash
pip install -r requirements.txt
```
---

## Utilisation
Dans le dossier principal, lancer l’application avec la commande:
```bash
python app.py
```
Une adresse sera affichée dans le terminal, comme:
```bash
http://127.0.0.1:5000
```
Ouvrez cette adresse dans votre navigateur.

---

## Utiliser la calculatrice
1. Cliquer sur un nombre, ce sera la première opérande
2. Cliquer sur un des quatre opérateurs (+, -, / ou *)
3. Cliquer sur un nombre, ce sera la deuxième opérande
4. Cliquer sur le bouton d'égalité
Le résultat s'affichera dans le champ prévu.
En cas d'erreur, un message explicite sera affiché dans le champ prévu.

---

## Tests

Les tests unitaires seront ajoutés dans le dossier `tests/` dans le fichier `test_calculator.py`.
Une fois les tests implémentés, ils pourront être exécutés avec la commande suivante depuis la racine du projet:
```bash
    python -m unittest discover tests
```

---

## Flux de contribution

Règles générales:
- La branche `main` contient la version stable
- Chaque nouvelle fonctionnalité/bogue doit être développée/corrigé dans une branche dédiée

Étapes du processus de découverte de bogue:
1. Identifier un bogue (ex. grâce à un test qui échoue)
2. Ouvrir une Issue sur GitHub 
3. Assigner l'Issue à un membre de l'équipe de développement
4. Inclure une description claire du problème dans l'Issue

Étapes du processus de correction de bogue:
1. Créer une branche:
```bash
    git checkout -b bugfix/[nomDuBogue]
```
2. Corriger le bogue sur la branche dédiée, commiter (avec un message clair expliquant comment la modification corrige le problème) et pousser la branche à l'aide des commandes suivantes:
```bash
    git add .
    git commit -m "Fix: [détail du bogue corrigé]"
    git push
```
3. Ouvrir une Pull Request (PR)
4. Détailler dans la PR comment le problème a été résolu
5. Sélectionner un membre de l'équipe qui devra approuver les changements
6. Fusionner la branche dans main si la PR si la PR est approuvée par au moins 1 membre de l'équipe

