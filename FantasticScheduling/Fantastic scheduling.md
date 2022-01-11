# Fantastic scheduling

## Aperçu

L'activité est centrée sur l'ordonnancement des instructions au niveau matériel, par la découverte des notions de *graphe de dépendance* et *list scheduling*

## Contexte

Un dragon approche, il faut se défendre. Le roi veut des engins de siège, et Il les veut vite ! Nous jouons les chefs des artisans et devons planifier leurs travaux afin d'optimiser les temps de production des armes de siège.

## Déroulement de l'activité

### Installation

* Contexte et présentation des tâches de construction.

### Première phase

* Distribution du matériel pour chaque îlot d'élève.
* Distribution de la description textuelle des instructions


    > 10-15 minutes d'essai d'ordonnancement

* **Récapitulatif** : c'est pas évident, certainement faux

### Deuxième phase

* Présentation des graphes de dépendance, parce que simplement avec le texte c'est moins facile
* Distribution de la description graphique des instructions

    > 10-20 minutes d'ordonnancement, essayer de faire le moins de cycle possible

* **Récapitulatif** : plus facile avec les graphes, mais difficile de savoir quand faire quoi

### Troisième phase

* *Voir si on à réussi à sauver le royaume*
* Correction des ordonnancements proposés en expliquant le *list scheduling*
* **Optionnel** : refaire avec un autre exemple d'engin de siège
* **Optionnel** : introduire le *software pipelining* lorsque l'on fait plusieurs engins de siège à la suite. Sur le plateau de jeu, on pourra observer que les étapes de construction d'un engin "s'emboitent", et que l'on peut extraire plus de parallélisme.

### Conclusion 

* récapitulatif global
* (+ pourquoi c'est de l'informatique)



## Matériel
Le matériel suivant est nécessaire pour mettre en place l'activité (Par îlot d'élèves):

* **Première possibilité**
    * Un plateau représentant un tableau où on peut placer les instructions
    * Des pièces représentant les instructions
        * L'objet de l'instruction est imprimé sur chaque pièce
        * Ou alors la catapulte est représentée en entier, avec les parties non construites grisées
        * La couleur de la pièce dépend de l'unité d'exécution (Ex: Bleu pour le Forgeron, Vert pour le charpentier)

* **Deuxième possibilité** (moins marrant, mais moins de matos)
    * Un tableau plastifié avec les voies d'exécutions colorées
    * Un feutre pour tableau blanc : l'apprenant met juste le numéro de l'instruction sur le tableau
    * Problème: donner un feutre à des CM1 -> risque de bazar

| C   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| :-: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| F   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| A   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |

* Une feuille imprimée avec les recettes pour fabriquer chaque objet 
    * Une première avec une description textuelle de chaque instructions
    * Une seconde avec les graphes de dépendance



## C'est de l'Informatique parce que...
Le scheduling d'instruction est une étape importante lors de la compilation de programmes pour des systèmes embarqués et des processeurs de type VLIW (Very Long Instruction Words).

Plusieurs algorithmes existent pour mettre en place un ordonnancement efficace d'instructions
* **Le list scheduling** qu'on essaye de faire découvrir dans cette activité. C'est un algorithme glouton qui consiste à maintenir une liste d'instructions prêtes à être exécutées, et qui à chaque cycle décide les instructions à ordonnancer à l'aide d'une fonction de priorité. Simple à mettre en œuvre, il donne une première solution qui n'est pas toujours optimale. Idéalement, on amène l'apprenant vers cette solution gloutonne avec une fonction de priorité naïve (ordre naturelle des instructions). Puis on les mène vers une fonction plus optimale (graphe de dépendance, mobilité).
* **Integer Linear Programming (ILP)** pour obtenir la solution optimale. Il faut modéliser le problème comme un ensemble de contraintes sur des nombres entiers. Un solveur permet ensuite d'obtenir la solution optimale.

## TODO
- [ ] mettre les descriptions des instructions, textuelles et graphiques
- [ ] définir les quantités de matériel pour un groupe
- [ ] estimer les temps d'activité
- [ ] schema de catapulte -> illustration des cartes *instructions* : colorer qui est construit, griser reste

## Auteurs
* Léo Cosseron & Louis Savary
* Images svg tirées de https://openclipart.org/ sous la licence Creative Commons Zero 1.0 Public Domain License
