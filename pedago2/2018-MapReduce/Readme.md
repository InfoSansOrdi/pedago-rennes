# Activité MapReduce

Cette activité est basée sur une idée originale de Florestan De Moor.
Elle est distribuée sous license CC-BY-SA.

## Objectifs de l'activité


## Matériel requis

* Cartes motifs à imprimer et découper
* Cartes rôle (coordinateur, analyseur, rassembleur) : fichier `roles.pdf` à imprimer et découper

## Public visé

Cette activité requiert le calcul d'additions simples, et peut généralement être pratiquée dès le CE1.

## Générer le plateau

Des exemples de pages de carte motifs sont disponibles dans le dépôt.
Il est également possible de générer une page en utilisant le script Python fourni.
Il suffit pour cela d'exécuter la commande suivante :
```./generate.py```
Le script utilise certaines images de [Font Awesome](https://fontawesome.com/) qui sont sous license CC BY 4.0.
Les pages de cartes doivent ensuite être imprimées, et découpées.

## Déroulement de l'activité

### Problème à résoudre :

On dispose d'un plateau contenant un certain nombre de motifs. Le but est de compter le nombre de cases de chaque motif.

Afin de facilement détecter d'éventuelles erreurs, la génération est telle qu'un ensemble de cartes motifs issu d'un nombre entier de pages présente la propriété suivante : l'effectif de chaque motif est un multiple de 3.

### Première partie : approche naïve

Donner le plateau à un participant et lui demander de compter le nombre de cases de chaque couleur et d'inscrire le résultat sur les cartes couleurs.
Le but est de conclure que cette approche est très longue et fastidieuse à réaliser.
Demander aux participants comment le processus pourrait être rendu plus rapide et plus facile.

### Deuxième partie : avec le paradigme MapReduce

Désigner un coordinateur et lui donner cette carte rôle.
Le coordinateur soit distribuer les autres cartes rôles : 4 rassembleurs, et analyseurs pour tous les participants restant.
Donner le plateau découpé en blocs au coordinateur, qui va le répartir entre les analyseurs.
Chaque analyseur compte le nombre de cases de chaque couleur dans le(s) bloc(s) qui lui a(ont) été donné(s) et inscrit le résultat sur les carte couleurs.
Les cartes sont ensuite transférées aux rassembleurs correspondant (un par couleur) qui s'occupe de regrouper les résultats en les sommant et permet de récuper le résultat final.
Demander aux participants ce qu'ils pensent de cette nouvelle approche. Leur parait-elle plus efficace que la première ?

### Troisième partie : pour aller plus loin

#### Transition analyseur-rassembleur

Les rassembleurs ne commencent à travailler qu'une fois que les analyseurs ont terminé. Peut-on faire mieux pour aller plus vite ?

#### Déséquilibre de répartition des couleurs

Des cartes dont la distribution des motifs est biaisée sont également fournies en exemple.
Certains motifs sont alors bien plus présents que d'autre, menant à un déséquilibre de travail à effectuer pour les analyseurs et les rassembleurs.
Comment remédier à ce problème ?

#### Faire face aux imprévus

Un travailleur est parti faire la sieste, et on ne sait pas quand il va revenir. Comment gérer cette situation pour tout de même finir rapidement le travail ?

introduction crash de noeuds / relancement de tâches / duplication de tâches

