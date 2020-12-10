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
