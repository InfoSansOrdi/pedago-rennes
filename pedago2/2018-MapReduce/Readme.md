# Activité MapReduce

Cette activité est basée sur une idée originale de Florestan De Moor.
Elle est distribuée sous license CC-BY-SA.

## Objectifs de l'activité


## Matériel requis

* Plateau de couleurs en deux exemplaires dont une avec lignes de séparation en blocs à découper (à générer en utilisant le script Python fourni, voir ci dessous)
* Cartes rôle (coordinateur, analyseur, rassembleur)
* Cartes couleurs

## Public visé

Cette activité requiert le calcul d'additions simples, et peut généralement être pratiquée dès le CE1.

## Générer le plateau

La librairie `svgwrite` est utilisée, elle peut être installée avec la commande suivante : `pip3 install svgwrite`.
Divers paramètres peuvent être modifiés dans le fichier de configuration `boardConfig.yml` dont le nom du fichier généré (`board.svg` par défaut).
Puis exécuter :
```python3 board.py```
Pour avoir les deux exemplaires, exécuter le script une première fois avec `divide: 0` puis une seconde avec une autre valeur de `divide` et la même valeur de `seed`.

## Déroulement de l'activité

### Problème à résoudre :

On dispose d'un plateau contenant un certain nombre de cases colorées. Le but est de compter le nombre de cases de chaque couleur.

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

Un plateau déséquilibré peut être généré avec le script Python en passant le paramètre `skew: True`.
Certaines couleurs sont alors bien plus présentes qua d'autre, menant à un déséquilibre de travail à effectuer pour les rassembleurs.
Comment remédier à ce problème ?

#### Faire face aux imprévus

Un travailleur est parti faire la sieste, et on ne sait pas quand il va revenir. Comment gérer cette situation pour tout de même finir rapidement le travail ?

introduction crash de noeuds / relancement de tâches / duplication de tâches

## Avancement de la conception de l'activité

* [x] Script pour générer plateau sous forme d'une image svg
* [ ] Créer cartes rôle et couleurs
* [ ] Ecrire objectifs de l'activité
* [ ] Ecrire déroulement complet de l'activité de base (première et deuxième partie)
* [ ] Ajouter extensions à l'activité (troisième partie)