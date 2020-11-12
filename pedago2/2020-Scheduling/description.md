# Scheduling

## Description de l'activité
On essaie de montrer quelques algorithmes d'ordonnancement. Chaque élève représente une ligne de production, et un groupe d'élèves doit se répartir des tâches pour finir le plus rapidement possible.


## Description du matériel

### Papier de tâches
De petits morceaux de papiers qui constituent une tâche à effectuer par une ligne de production (=un élève). Toutes les tâches ont un identifiant. Elles demandent de combiner deux couleurs, et quelquefois, on ne spécifie pas la couleur sur la tâche, mais l'identifiant d'une autre tâche. Il faut alors substituer l'identifiant par la couleur finalement obtenue après avoir terminé l'autre tâche. Cela crée un réseau de dépendances, qui est une contrainte au coeur du problème.

[ Image ]

### Disques de composition
Permettent de combine les couleurs sur les tâches, pour accomplir ces tâches. A une forme analogue à un disque de César, et un fonctionnement analogue à un monoïde.

## Déroulement des activités

**Activité 1** - chaque apprenant a un disque, tous identiques
-   **Objectif** : Prise en main du matériel pour les tâches
-  **Matériel** : Trois élèves, un disque par élève, un ensemble de tâches
-  **Consigne** : Résoudre le problème *le plus rapidement possible*
- On s'attend à ce que les élèves n'aient pas de stratégie particulière au début, et le but est de leur faire découvrir qu'ils perdent beaucoup de temps à remonter les dépendances de chaque tâche.

**Activité 2** - première abstraction de la solution
- **Objectif** : Introduire une première abstraction du problème, afin de prendre du recul. Permet de manipuler des graphes assez simples.
- **Matériel** : 
-   Commencer par introduire le diagramme de Gantt [https://fr.wikipedia.org/wiki/Diagramme_de_Gantt](https://fr.wikipedia.org/wiki/Diagramme_de_Gantt)
-   Expliquer comment les tâches peuvent être représentées, et faire un test run pour bien être sûr que les élèves aient compris l'abstraction
-   -> On peut éventuellement leur donner une assignation choisie par nous-mêmes pour commencer
-   Peut-être leur faire appliquer une heuristique simple : algo glouton ?

**Activité 3** - abstraction vers un graphe pour trouver une stratégie de résolution a priori
-   Montrer un graphe de dépendances (graphe causal). Méthode du chemin critique (PERT)

### Notes en vrac :

Algorithmes à présenter:
-   Shortest job first, shortest remaining time?
-  Longest job first
-   Méthode PERT

Ordonnancement en ligne ?
-   Round Robin

Peut-être ne pas utiliser des disques de César, mais des planches de symboles découpées en cases numérotées. Les cases numérotées ont toutes un type de symboles dominant, et il donne la couleur de l'identifiant associé

