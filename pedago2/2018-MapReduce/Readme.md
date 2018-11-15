# Activité MapReduce

Cette activité est basée sur une idée originale de Florestan De Moor.
Elle est distribuée sous license CC-BY-SA.

## Objectifs de l'activité


## Matériel requis

* Cartes motifs à imprimer et découper
* Cartes rôle (coordinateur, analyseur, rassembleur) : fichier `ressources/roles.pdf` à imprimer et découper
* Cartes résultat : fichier `ressources/resultats.pdf` à imprimer et découper

## Public visé

Cette activité requiert le calcul d'additions simples, et peut généralement être pratiquée dès le CE1.

## Générer le plateau

Des exemples de pages de cartes motifs sont disponibles dans le dépôt.
Il est également possible de générer une page en utilisant le script Python fourni.
Il suffit pour cela d'exécuter la commande suivante :
```./generate.py```
Le script utilise certaines images de [Font Awesome](https://fontawesome.com/) qui sont sous license CC BY 4.0.
Les pages de cartes doivent ensuite être imprimées, et découpées.

## Déroulement de l'activité

### Problème à résoudre :

On dispose d'un ensemble de cartes sur lesquelles apparaissent un certain nombre de motifs. Le but est de compter le nombre de fois qu'apparaît chaque motif.

Afin de facilement détecter d'éventuelles erreurs, la génération est telle qu'un ensemble de cartes motifs issu d'un nombre entier de pages présente la propriété suivante : l'effectif de chaque motif est un multiple de 3.

### Première partie : approche naïve

Donner les cartes à un participant et lui demander de compter les effectifs de chaque motif et d'inscrire les nombres sur les cartes résultat.
Le but est de conclure que cette approche est très longue et fastidieuse à réaliser.
Demander aux participants comment le processus pourrait être rendu plus rapide et plus facile.

### Deuxième partie : avec le paradigme MapReduce

Désigner un coordinateur et lui donner cette carte rôle.
Le coordinateur doit distribuer les autres cartes rôles : 5 rassembleurs, et analyseurs pour tous les participants restant.
Le coordinateur doit ensuite répartir les cartes motifs entre les analyseurs.
Chaque analyseur compte les effectifs de chaque motif sur les cartes qui lui ont été attribuées et inscrit les nombres sur les carte résultat.
Sous ordre du coordinateur, les analyseurs doivent ensuite transférer ces dernières aux rassembleurs (un rassembleur par motif).
Les rassembleurs calculent les résultats finals en sommant les nombres qu'ils ont reçu.
Demander aux participants ce qu'ils pensent de cette nouvelle approche. Leur parait-elle plus efficace que la première ?

### Troisième partie : pour aller plus loin

#### Transition analyseur-rassembleur

Les rassembleurs ne commencent à travailler qu'une fois que les analyseurs ont terminé. Peut-on faire mieux pour aller plus vite ?

#### Déséquilibre de répartition des couleurs

Des cartes dont la distribution des motifs est biaisée sont également fournies en exemple.
Certains motifs sont alors bien plus présents que d'autre, menant à un déséquilibre de travail à effectuer pour les analyseurs et les rassembleurs.
Comment remédier à ce problème ?

#### Faire face aux imprévus

En plein milieu du travail, un participant doit aller chercher son goûter de toute urgence, et on ne sait pas quand il va revenir. Comment gérer cette situation pour tout de même finir rapidement le travail sans avoir à l'attendre ?

introduction crash de noeuds / relancement de tâches / duplication de tâches

