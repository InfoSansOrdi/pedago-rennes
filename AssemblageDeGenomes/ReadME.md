# ASSEMBLAGE

Kerian Thuillier et Joseph Cabrita

*Copyright 2020 - Licence: cc-by-sa*

## Objectif

L'objectif de cette activité est de faire comprendre le principe et la complexité de l'assemblage de génome.
L'idée est de voir apparaître l'algorithme OLC qui sera détaillée dans une autre section.

**Prérequis :** Aucun

# Mise en Place

## Matériel

Différentes planches de dominos de longueur variable.
Les sigles *A*, *C*, *G* et *T* sont simplifiés par des formes colorées :

* *A* : carré bleu
* *C* : triangle jaune
* *G* : rond vert
* *T* : étoile rouge

Pour un rendu visuelle optimisé pour du A4, il est conseillé d'utiliser des pièces de 12 nucléotides.
Les paramètres du script de génération des puzzles sont optimisés pour ce nombre.

## Type de niveaux

Chacun de ces niveaux est composée de pièces contenant 12 nucléotides.
Il faut plusieurs ensembles de pièces avec différents niveaux de difficultés de reconstruction d'une séquence :

* simple :
    Le jeu est composé de 14 pièces simples. On distingue 2 types de configurations :
    - Il n'existe qu'un chevauchement possibles entre les différentes pièces.
    - Il n'existe qu'un ensemble de chevauchement optimale entre les différentes pièces, *i.e.* plusieurs pièces sont possibles pour une succession, mais un seul agencement permet de maximiser les chevauchements.
    - Ajout de la prise en compte du backtracking.
* ... avec répétitions :
    Cette fois-ci, le jeu est composé d'entre 14 et 28 pièces. Certaines pièces sont présentes plusieurs fois, encore une fois nous pouvons distinguer deux situations :
    - Toutes les pièces ont une position (14 pièces).
    - Certaines pièces ne servent à rien et sont redondantes (14-28 pièces). x2 Avec augmentation du ratio d'utilisation.
* ... avec erreurs :
    Des erreurs de séquençage sont ajoutées. Des pièces sont donc totalement inutiles et ne contribuent pas à la solution finale. Deux cas sont à distinguer :
    - Les erreurs sont uniquements dans les parties non-chevauchantes des séquences. Elles n'impactent donc pas les chevauchements.
    - Les erreurs sont présentes aussi bien dans les partis non-chevauchantes que les partis chevauchantes. Elles peuvent donc impacter l'assemblage.
* ... reverse complément :
    Les pièces deviennent recto-verso : d'un côté la séquence classique dite en *Forward* et de l'autre la séquence inversée dite *Reverse Complémentée*. Il faut donc désormais choisir le bon sens de chaque pièce. En notant que le Forward d'une pièce peut-être égale au Reverse d'une autre, dans ce cas-ci elles sont identiques et représentent la même séquence.
    L'ajout du reverse complément peut se faire de manière progressive : en reprenant chaque étape précédente, ou bien directement traiter le cas avec erreur.

## Extension

Ce système de puzzles peut être étendu au problème d'assemblage en méta-génomique (*i.e.* d'assemblage de plusieurs génomes en simultanée).
Pour cela, il suffit de reprendre les étapes précédentes en ajoutant des pièces issues de plusieurs (2-3) génomes.
La progression peut ainsi se faire selon les étapes suivantes :

* simple :
    Les pièces issues de chaque génome ne se chevauchent pas entre elles. Dans ce cas, il est possible d'ajouter des erreurs et le reverse complément.
    **NB :** L'activité peut-être corcée si le nombre de génomes à reconstruire est inconnus.
* compliqué :
    Les génomes partagent des tronçons communs (cas de l'haplotypage). Il faut donc réussir à reconstruire l'ensemble des structures dans un graphe de pièces contenant dans le pire des cas $2^\text{nombre de pièces}$ génomes candidats.
    **WARNING** Le problème n'est pas solvable en l'état. Il est nécessaire de donner des informations complémentaires aux utilisateurs : un ensemble de faits.
    Un fait est un ensemble de pièces provenant d'un même génome. Un génome possède plusieurs faits, et on ignore quels faits est associé à quel génome. Avec suffisament de faits, il est possible de déterminer une unique solution (en pratique il n'y a jamais assez de faits et on reconstruit uniquement des candidats).

## Pourquoi c'est de l'informatique ?

### Discours

### Classification
