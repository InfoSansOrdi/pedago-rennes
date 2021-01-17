# PEDAGO - Fantastic Scheduling

## Aperçu

L'activité est centrée autour des notions de *scheduling* au niveau du
matériel.  On cherche à faire découvrir aux apprenants de algorithmes
d'ordonnancement de tâches sur des unités d'exécution (*list
scheduling*, *software pipelining*).

## Contexte

Un dragon approche et va attaquer le royaume de Compilos ! Le roi doit
apprêter ses troupes pour défendre la population. Il s'entoure des
meilleurs savants et artisans de son royaume. Ces derniers vont devoir
équiper toute l'armée du roi le plus rapidement possible.

## Déroulement de l'activité

On commence par introduire le matériel utilisé tout au long de l'activité en
proposant aux apprenants de réaliser un ordonnancement pour la fabrication d'une
épée et d'un bouclier. Une représentation textuelle sous forme SSA de ces deux
éléments est donnée ci-après :
```mlir
// Epée
%0 = @forgeron()
%1 = @alchimiste()
%2 = @enchanteur(%0, %1)
```
et
```mlir
// Bouclier
%0 = @forgeron()
%1 = @tailleur()
%2 = @enchanteur(%0, %1)
```
Ces deux ordonnancement simples permettent d'introduire les pièces et le plateau
qui seront utilisés pour la réalisation des *Gantt charts* illustrant l'ordre
dans lequel les tâches devront être effectuées.

Dans un deuxième temps, on donne aux apprenants un objet plus difficile à
concevoir : la catapulte. La représentation SSA du processus de fabrication est
telle que
```mlir
%0 = @charpentier()        // roue_1
%1 = @charpentier()        // roue_2
%2 = @charpentier()        // roue_3
%3 = @charpentier()        // roue_4
%4 = @forgeron(%0, %1)     // axe
%5 = @forgeron(%2, %3)     // axe
%6 = @charpenter(%4, %5)   // monter les roues
%7 = @charpentier()        // bras de lancement
%8 = @forgeron(%7)         // mécanisme de lancement
%9 = @charpentier(%6, %7)  // assemblage catapulte
```
On laisse les apprenants essayer de trouver un ordonnancement sans les aider,
puis on fait le bilan de leur réflexion. On donne ensuite des indications qui
leur permettront de trouver un algorithme similaire au *list scheduling* (cf.
ci-dessous). Une fois cet ordonnancement obtenu, on cherche à pipeliner la
fabrication de plusieurs catapultes. Cette nouvelle phase va introduire
d'éventuels conflits de ressource qui devront être résolus par les apprenants.
Pour cela, on peut observer que retarder une action dans la fabrication de la
catapulte $A$ permet de mieux imbriquer son ordonnancement avec celui de la
catapulte $B$.

### Ordonnancements pour la catapulte

- Ordonnancement d'une seule instance

  |   |   |   |   |   |   |    |
  |---|---|---|---|---|---|----|
  | C | 1 | 3 | 7 |   |   | 10 |
  | C | 2 | 4 |   |   | 8 |    |
  | F |   |   | 5 | 6 | 9 |    |

- Ordonnancement de deux instances simultanées

  |   |   |   |    |    |    |    |    |    |    |     |
  |---|---|---|----|----|----|----|----|----|----|-----|
  | C | 1 | 3 | 1' | 3' | 7  |    | 7' | 10 |    | 10' |
  | C | 2 | 4 | 2' | 4' | 8  |    | 8' |    |    |     |
  | F |   |   | 5  | 6  | 5' | 6' | 9  |    | 9' |     |

### Autres idées d'objets

Boulet en métal pour la catapulte :
```mlir
%0 = @forgeron()
%1 = @enchanteur(%0)
```
Tissu résistant :
```mlir
// Peut sevir pour : cotte de maille, pantalon hyper resistant, gant, etc ...
%0 = @forgeron()          // Maille
%1 = @tailleur()          // Tissu
%2 = @enchanteur(%0)      // Augmente la résistance
%3 = @alchimiste(%1, %2)  // Fusion tissu-metal
%4 = @tailleur(%3)        // Assemblage
```

### Aller plus loin

Une fois que les apprenants ont compris l'idée pour un type d'objets, on peut
chercher à faire frabriquer plusieurs objets différents en même temps. Dans le
cas le plus avancé, on place tous les artisans sur le plateau et on demande la
fabrication simultanée d'épées, de boucliers, de catapultes, de boulets et de
tissu renforcé.

**Note** : Les apprenants peuvent se servir d'un dé pour déterminer la quantité
d'objets à concevoir par les artisans du royaume.

### Matériel

Un exemple de pièce basée sur l'apparence des cartes du jeu 7 Wonders est donné
dans le fichier `img/card-example.svg`.

## C'est de l'informatique parce que

C'est de l'informatique parce que les processeurs spécialisés, de type
VLIW (Very Long Instruction Word), dépendent de l'ordonnancement des
instructions. Ce dernier, effectué par les compilateurs optimisants,
cherche à exposer du parallèlisme à l'exécution, notamment en
superposant l'exécution de plusieurs itérations d'une même boucle. On
appelle ce processus *software pipelining*, ou *pipeline logiciel*.

Il existe plusieurs algorithmes d'ordonnancement pour le pipeline
logiciel, notamment le *list scheduling*. On considère un processeur
avec $n$ unités d'exécution, $E_1,\ldots,E_n$ et le graphe de
dépendance $G$ associé à une tâche. On note $V$ l'ensemble des noeuds
de $G$. Chaque noeud de $G$ ne peut être exécuté que lorsque tous ses
noeuds parents ont été exécutés. De plus, pour un noeud $v$ donné,
seul un sous-ensemble de $(E_i)_{1\leqslant i\leqslant n}$ peut
exécuter l'opération associée à $v$. Le principe de l'algorithme de
list scheduling est le suivant :

- On part des noeuds de $G$ qui ne possèdent pas de parents, et on
place ces noeuds sur les unités d'exécution correspondantes. Si deux
noeuds devraient être exécutés par le même $E_i$, on choisit
arbitrairement un ordre d'exécution.

- On place ensuite les noeuds fils des noeuds déjà ordonnancés sur la
table d'ordonnancement, en veillant à ce qu'un noeud $v$ ne soit pas
exécuté avant l'un de ses parents.

- On répète le processus jusqu'à avoir épuisé tous les noeuds de $G$.

La table d'ordonnancement obtenue après exécution de l'algorithme de
list scheduling donne un bon point de départ pour la mise en place
d'un pipeline logiciel. Cependant, on note que certaines tâches
pourraient avoir à être décalées pour exposer plus de parallèlisme.

### Liens utiles

- https://en.wikipedia.org/wiki/List_scheduling
- https://en.wikipedia.org/wiki/Dependency_graph
- https://en.wikipedia.org/wiki/Software_pipelining
- https://www.cs.cmu.edu/afs/cs/academic/class/15745-s12/public/lectures/L19-Software-Pipelining-1up.pdf
