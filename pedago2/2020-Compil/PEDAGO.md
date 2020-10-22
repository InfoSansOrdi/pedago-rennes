# Activité compilation optimisante
## Première idée
*Apprenant 1* : programmeur
*Apprenant 2* : compilateur optimisant

Le programmeur cherche à établir un chemin sur une carte d'un point $A$ à un
point $B$. Pour cela, il dispose d'un jeu de pièces qui permettent de
construire une route. Le compilateur optimise la route ainsi construite en
ayant des connaissances plus étendues sur le terrain qui devrait accueillir la
route (obstacles, dénivelé, etc.).

## Développement
Coût de construction et temps d'exécution : chaque pièce a un coût, le
temps d'exécution est la longueur du chemin.
Les apprenants jouent collectivement le rôle de compilateur. On leur fournit
des pièces de coût plus élevé mais qui permettent de contourner des
obstacles plus facilement. L'origine et la destination doivent rester les
mêmes (éventuellement ajouter des points de passage obligatoires).

Grille carrée ou hexagonale. Plateau aimanté avec hexagones aimantés aussi.
Plateau à plusieurs niveaux, pièces en carton (?).

Pièces possibles :
- Route droite
- Virage 90°
- Pont
- Tunnel
- Montée + descente (avec des plateaux de différents niveaux sur la carte)

## Deuxieme idée
*Présentateur* : Bâtisseur
*Apprennants* : Compilateur optimisant

### Partie 1
On a une grande carte avec des reliefs et le bâtisseur y met des points et
indique quels points doivent être connectés ensemble. Cela peut se faire sous
la forme d'un graphe qui vient au dessus de la carte.
Les apprenants doivent construire les routes en fonction du relief.
On peut leur indiquer plus tard que pour relier des points ils peuvent utiliser
des points intermédiaire (pour relier A B et C ils peuvent faire une étoile a
la place d'un triangle).

### Partie 2
On introduit une notion de traffic et maintenant on sait que X voitures veulent
aller de A à B. Les cases de route ayant une capacité il va falloir aggrandir
certaines parties de la route pour qu'elle s'ajuste au traffic voulu.


## Troisième idée
Plusieurs étapes :
- On fournit un plateau avec beaucoup d'obstacles et uniquement des pièces de
route simples.
- On introduit des ponts, tunnels, etc. qui représentent des instructions plus
complexes. On ne s'intéresse alors qu'au temps de trajet, i.e. à la longueur
de la route.
- On contraint le problème en imposant un coût maximal de construction de la
route, qui correspond à une contrainte énergétique par exemple IRL.

## Quatrième idée
Deux apprenants : un programmeur et un compilateur.

Le programmeur dispose d'une carte grossière sans grille qui représente le
terrain et doit relier les points "à la main" en évitant les obstacles.
Le compilateur travaille sur la grille hexagonale à partir du modèle établi
par le programmeur. Il sait construire des parties de route plus complexes que
le programmeur (*e.g.* des ponts) qui permettent de réduire le temps
d'exécution.

Adapter le rythme lors de la présentation + inventer des niveau, ne pas
laisser les apprenants faire le dessin sur la carte initiale.

Pour chaque niveau, avoir un objetif (pédagogique ou non). Avec un ou deux
niveaux de prise en main pour les apprenants. Mettre en place les objectifs
pédagogiques avant de concevoir les niveaux.