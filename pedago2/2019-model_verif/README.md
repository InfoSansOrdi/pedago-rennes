---
author:
- Santiago Bautista
- Quentin LeDilavrec
- Julie Parreaux
date: 2019
title: Activité Pédago 2: Modélisation et vérification
---

# Description générale

Le matériel proposé ici permet de travailler deux aspects très liés,
mais distincts, de l'informatique: la modélisation et la vérification.
Ces aspects peuvent être travaillés séparément, un par un, ou ensemble,
ce qui donne place à trois activités différentes.

## Imaginaire / Motivation

>Un pirate a caché son magnifique trésor dans une île, mais vous ne savez
>pas laquelle! Vous disposez du journal du pirate, ainsi que de
>différents journaux de voyage de personnes éclairés, ayant exploré
>différentes îles. À vous de retrouver, à partir des descriptions des
>îles et de la description de l'aventure du pirate, dans quelle île est
>cachée le trésor.

Le journal du pirate contient les propriétés qu'on devra vérifier. Les
journaux de voyages contiennent les descriptions d'îles qu'on devra
modéliser.

## Activités

On décrit donc ici 3 activités différentes:

-   Une activité portant surtout sur la modélisation: dans ce cas-là les
    îles sont décrites avec des phrases et il faudra que les
    participants les modélisent correctement pour trouver le trésor. Ici
    le journal du pirate est très simple: il contient uniquement une
    description du chemin menant au trésor.

-   Une activité portant surtout sur la vérification. Les îles sont déjà
    données sous forme de carte, il n'y a pas besoin de les modéliser.
    Par contre le journal du pirate contient des propriétés de plus en
    plus complexes à vérifier.

-   Une activité joignant les deux, où les îles sont décrites sous forme
    de texte et on devra les modéliser, et le journal du pirate contient
    des propriétés de plus en plus complexes à vérifier.

# Activité A: Modélisation seule


## Objectif pédagogique

L'idée de cette activité est de mener les participants à modéliser sous
forme de carte des descriptions d'îles qu'ils auront reçus sous forme de
texte. L'activité se déroule en 5 tours. À chaque tour la description de
l'île est de plus en plus étoffée, compliquant la tâche de modélisation.

Dans cette activité, il n'y a qu'une seule propriété à vérifier, qui est
la même pendant tous les cinq tours.

## Matériel

Voici la propriété (contenu du journal du pirate) qui indique laquelle
des îles contient le trésor. Elle est distribuée au début et reste
identique tout au long de la partie.

>\"Pour cacher mon trésor, j'ai débarqué sur la plage au milieu de la
nuit. J'ai laissé la lumière des libellules me guider jusqu'à la forêt
de palmiers. J'étais alors perdu, mais des bruits métalliques m'ont
permis de repérer la cabane du pêcheur. Derrière celle-ci j'ai vu la
façade ouest du volcan. Illuminé par la lune, j'ai escaladé le volcan,
pour redescendre sur la façade opposée où j'ai trouvée une grotte. C'est
au fond de la grotte que j'ai caché mon trésor.

>Ça m'a pris 8h d'aller de la plage jusqu'à la grotte pour cacher mon
trésor.\"

Cette propriété correspond à deux choses. La première est que le chemin
de la figure [\[chemin\]](#chemin) doit exister dans l'île en question. La deuxième est
que le chemin met en tout 8h a être parcouru, ce qui permettra de
choisir entre les deux dernières îles.

![Chemin caractérisant l'île au trésor](chemin_final.svg)
<a name="chemin"></a> 

Voici les descriptions des îles qu'il faudra donner au fur et à mesure.

#### Île Scorpion

-   Dans cette île, on ne peut débarquer que sur la plage.

-   De la grotte on peut aller au volcan.

-   Du volcan on peut descendre jusqu'à la forêt de palmiers.

-   Du volcan on peut aller à la rivière.

-   De la plage, on peut atteindre la forêt de palmiers.

-   La rivière débouche sur un lac.

-   La rivière permet d'aller jusqu'à la cabane du pêcheur.

#### L'île tortue

-   On peut arriver à l'île par la plage ou par la crique.

-   De la plage, un chemin tortueux mène à la forêt de palmiers.

-   En traversant la forêt de palmiers, on atteint la rive de la
    rivière.

-   De la cabane du pêcheur, on peut atteindre le lac ou la rivière.

-   En descendant par la façade est du volcan on atteint la grotte.

-   La cabane du pêcheur se trouve sur la façade ouest du volcan.

-   La crique mène à la forêt de conifères.

#### L'île de la fortune 

-   Le seul moyen d'arriver à l'île est de débarquer sur la plage.

-   De la plage, un chemin fleuri mène à la forêt de palmiers.

-   En traversant la forêt de palmiers on peut arriver sur le lac ou sur
    la cabane du pêcheur.

-   Le lac est au pied du volcan.

-   Une grotte se cache sur la façade est du volcan.

-   La rivière prend sa source sur le volcan, et coule sur sa façade
    sud.

-   De la cabane du pêcheur, un chemin très escarpé mène jusqu'à la
    forêt de conifères.

#### L'île des oiseaux rapides 

-   La plage et la crique offrent toutes deux de bons endroits pour
    débarquer sur l'île.

-   Cette île a deux forêts: la forêt de palmiers, à côté de la plage,
    et la forêt de conifères, à côté de la crique.

-   Au fond de la crique, se dissimule la cabane du chasseur.

-   Sur la plage, baignent les eaux du lac Azur, dont l'autre rive donne
    accès à la grotte de l'Ours Brun.

-   La forêt de palmiers abrite une rivière, et se termine sur la façade
    ouest du volcan.

-   Par contre, la rivière ne prend pas sa source au sommet du volcan.

-   La cabane du pêcheur, qui se trouve sur la façade est du volcan,
    permet d'atteindre la grotte.

#### L'île des singes hurleurs 

-   Une légende ancestrale raconte, que quiconque oserait poser les
    pieds sur cette île pour la première fois ailleurs que sur la plage
    ou sur la crique, serait perdu pour toujours dans l'île.

-   Sur la plage, on trouve le delta de la rivière Papamouan.

-   En remontant la rivière Papamouan pendant trois heures, on
    arrive à la cabane de pêcheur.

-   De la plage, après avoir gravit pendant deux heures un chemin
    tortueux, la forêt de palmiers s'ouvre devant nous.

-   Au milieu de la crique, se dresse la cabane du chasseur.

-   Traverser la crique prend une demie-heure et à sa lisière se trouve
    une forêt de conifères.

-   Traverser la forêt de palmiers pour atteindre la cabane du pêcheur
    prend une heure.

-   À l'arrière de la cabane du pêcheur, un chemin plein de cendres
    permet de monter au sommet du volcan en 3h.

-   Descendre par la façade est du volcan prend également 3h et on
    arrive à la grotte.

#### Île des dauphins roses (version simple) 

-   Il y a deux façons de débarquer dans l'île: une crique et une plage.

-   De la crique un chemin étroit et sombre à une magnifique forêt de
    conifères.

-   Un sentier bien entretenu mène de la crique à la cabane du chasseur.

-   De la plage, un chemin scabreux monte vers la forêt de palmiers.

-   De la rivière, on peut atteindre la cabane du pêcheur ou le volcan.

-   Pour descendre à la grotte, il faut marcher sur la façade ouest du
    volcan.

-   En descendant la façade est du volcan, on arrive à la cabane du
    pêcheur.

-   Le pêcheur fait tous les matins une promenade jusqu'à la forêt de
    palmiers pour ceuillir des noix de coco.

*C'est dans cette dernière île que se trouve le trésor.*

#### Île des dauphins roses (version compliquée) 

-   Marcher sur cette île est très compliqué. Pour le faire, il faut
    disposer de souliers magiques que seuls les peuples indigènes vivant
    sur la plage et sur la crique savent fabriquer.

-   De la crique un chemin étroit et sombre mène en deux heures de
    marche à une magnifique forêt de conifères, alors qu'un sentier bien
    entretenu mène à la cabane du chasseur en une heure.

-   De la plage, un chemin scabreux monte vers la forêt de palmiers, il
    faut une bonne heure pour le trajet.

-   De la rivière, une heure de marche permet d'atteindre la cabane du
    pêcheur.

-   Pour descendre à la grotte, il faut marcher sur la façade ouest du
    volcan pendant deux heures.

-   En descendant la façade est du volcan pendant trois heures, on
    arrive à la cabane du pêcheur.
	
-   Si par contre on descend sur la façade sud du volcan pendant quatre
    heures, on arrive à la rivière.

-   Le pêcheur fait tous les matins une promenade de deux heures jusqu'à
    la forêt de palmiers pour y cueillir des noix de coco.

*C'est dans cette dernière île que se trouve le trésor.*

Déroulement 
-----------

### Mise en place 

On donne le contexte de l'activité aux participants: on a retrouvé le
journal d'un pirate décrivant où est-ce qu'il a caché son trésor, mais
on n'est pas sûr de quelle île il s'agit. On dispose également de
journaux de voyage de vaillants explorateurs ayant exploré différentes
îles. Il faudra, en regardant les descriptions des différentes îles,
savoir quelle est l'île cachant le trésor.

### Modélisation de la propriété 

On donne aux participants le texte du journal du pirate (*Temps de
lecture et de compréhension si nécessaire*). On leur demande quel est le
chemin que le pirate a suivi. On emmène les participants à, tous
ensemble, construire/dessiner le schéma du
[chemin caractérisant la propriété](#chemin). (*Ça
peut par exemple se faire au tableau dans un premier temps, puis on
pourra leur distribuer une version papier lors de l'étape suivante*).

On explique aux participants qu'on leur donnera les descriptions des
différents îles possibles une par une.

### Première modélisation 

On distribue la description de la première île (l'île Scorpion) et on
demande "Est-ce que c'est l'île cachant le trésor?\".

L'objectif est que, pour répondre, les participants dessinent/tracent la
carte de l'île, pour s'assurer que le chemin décrit n'existe pas.

La principale difficulté sera que certains participants voudront
répondre à la question juste avec le texte, sans faire de dessin. Dans
ces cas-là, trois stratégies successives pourront être mises en place:

1.  Demander "Est-ce que tu es sûr(e)?\". Effectivement, dans un texte,
    il est facile de rater une phrase, de s'emmêler les pinceaux, etc...

2.  Dire "Prouve-le moi\". L'encadrant ne voudra pas se plonger dans les
    détails du texte, il ne se laissera convaincre que par un
    dessin/schéma.

3.  Donner au participant des images prédécoupées des différents
    endroits de l'île, une feuille en papier, de la colle et un crayon
    et lui dire "Montre-le moi\".

4. S'ils ne pensent pas à tracer un trait
    entre les parties de l'île qui sont reliées entre elles d'après le
    texte, on pourra leur distribuer une carte de l'île (fournies dans
	le document "fiche élève") comme celle ci-dessous:
	
![Exemple de carte d'île (île de la fortune)](iles/svgs/modelisation/ile_fortune.pdf)
<a name="fortune_mode"></a> 

<iframe src="iles/svgs/modelisation/ile_fortune.pdf"></iframe>

Quand certains participants auront trouvé comment faire, une mise en
commun permettra de montrer à tout le monde comment faire un schéma à
partir de la description textuelle, et comment vérifier sur le schéma si
le chemin décrit par le pirate existe ou pas.

En fonction de l'âge des participants, et du temps à disposition, on
peut continuer avec soit les instructions de la version courte, soit les
instructions de la version longue.

### Version courte 

#### Île au trésor 

On distribue ensuite aux participants la description de l'île des
dauphins roses (version simple), qui contient le trésor. On laisse les
participants modéliser par eux-mêmes et vérifier que le chemin décrit
dans le journal du pirate est bien présent.

En cas de difficulté lors de la modélisation, se ramener aux mêmes aides
que dans l'étape précédente.

#### Pour ceux qui vont vite 

Ils ont trouvé une île qui contient le chemin décrit par le pirate Mais
s'il faut, d'autres îles contiennent aussi ce chemin-là. Pour être sûrs
que c'est bien l'île des singes hurleurs qui contient le trésor, il faut
également modéliser les autres îles. On leur distribue la description de
l'île des oiseaux rapides. S'ils finissent de la modéliser et de
vérifier qu'elle ne contient pas le chemin décrit par le pirate, on leur
distribue l'île des singes hurleurs. Sur l'île des singes hurleurs, le
chemin décrit est présent également! Comment savoir donc laquelle des
deux îles (dauphins roses, singes hurleurs) contient vraiment le trésor?
Laisser les participants chercher. La clef est dans le temps qu'on met
pour aller d'un endroit à l'autre. Le pirate précise qu'il lui faut 8h
pour faire tout le chemin, or sur l'île des singes hurleurs il faut 9h
pour parcourir le chemin jusqu'à la grotte. Ce n'est donc pas l'île des
singes hurleurs qui contient le trésor.

### Version longue 

#### Consolidation. 

En distribuant l'île de la tortue et l'île de la fortune, une par une,
et en laissant les participants les modéliser par eux-même, ils
consolideront leur capaciter de modélisation. La description des îles
est de plus en plus complexe, en rajoutant ainsi une difficulté de
modélisation à chaque fois, mais les schémas obtenus ne sont pas
particulièrement plus complexes.

En cas de difficulté lors de la modélisation, se rammener aux mêmes
aides que dans l'étape précédente.

#### Complexification du modèle 

On distribue la description de l'île des oiseaux rapides. Après
modélisation, surprise! L'île contient le chemin décrit par le journal
du pirate. Certains participants croiront avoir trouvé la bonne île...

On leur distribue à ce moment-là la description de l'île aux singes
hurleurs et ils trouveront que là aussi, le chemin décrit par le pirate
est présent! Comment savoir dans laquelle des deux îles se cache
vraiment le trésor?

Il faudra prendre en compte un élément qu'on a ignoré jusqu'ici: le
temps. Le pirate précise qu'en tout ça lui a prit 8 heures d'aller de la
plage jusqu'à la grotte. Hors, pour les deux dernières îles on sait
combien de temps il faut pour aller d'un endroit à un autre. Il faudra
revenir sur les modèles (schémas/dessins/collages) qu'on a fait des deux
dernières îles et les **enrichir** en rajoutant sur chaque flèche/trait
le nombre d'heures nécessaires.

Après, en sommant les durées sur le chemin qui mène au trésor, on
comprendra que c'est l'île des singes hurleurs qui cache le trésor!

Pour l'instant, nous ne nous rendons pas compte de la difficulté de
cette étape, et donc nous ne savons pas s'il vaudrait mieux qu'elle soit
faite \"tous ensemble\" ou \"chacun dans son coin\".

Activité B: Vérification seule 
==============================

Objectif pédagogique 
--------------------

L'idée de cette activité est de mener les participants à vérifier des
propriétés de plus en plus complexes sur un ensemble d'îles.

Chacune des propriétés correspond à une phrase différente dans le
journal du pirate. Chaque propriété permet de se rendre compte que l'une
des îles à disposition ne contient pas le trésor.

Matériel 
--------

Les différentes îles seront distribuées sous forme de graphe (carte de
l'île).

Voici les différentes propriétés à vérifier (c'est à dire les
différentes phrases présentes dans le journal du pirate).

Propriété 1:   
	Pour cacher le trésor, j'ai débarqué sur la plage et je suis passé
    successivement par la forêt de palmiers, la cabane de pêcheur et le
    volcan avant d'arriver à la grotte, où j'ai caché mon trésor.

Propriété 2:   
	Quand je passais par la cabane du pêcheur, j'ai vu un chemin qui
    descendait jusqu'à la rivière, mais il était trop étroit pour que je
    passe avec mon trésor. Je ne l'ai donc pas emprunté.

Propriété 3:   
	Quand j'étais dans la forêt de palmiers, j'aurais voulu aller à la
    forêt de conifères, mais je ne pouvais pas.

Propriété 4:   
	Pour aller à la grotte depuis la plage, on passe forcément par la
    cabane du pêcheur.

Propriété 5:   
	Pour aller de la plage jusqu'à la grotte en empruntant le chemin que
    j'ai décrit, il m'a fallu huit heures en tout.

<a name="tableau_verif"></a> 

| **Nom de l'île**        | Propriété 1 | Propriété 2 | Propriété 3 | Propriété 4 | Propriété 5 |
|:------------------------|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| Île Scorpion            | &#215;      |             |             |             |             |
| Île de la tortue        |             | &#215;      |             |             |             |
| Île de la fortune       |             |             | &#215;      |             |             |
| Île des oiseaux rapides |             |             |             | &#215;      |             |
| Île des singes hurleurs |             |             |             |             | &#215;      |
| Île des dauphins roses  |             |             |             |             | ✓           |

Le tableau de 
[1](#tableau_verif) montre quelles propriétés permettent
d'éliminer quelles îles.

## Déroulement

### Mise en place 

#### Adapter la longueur de l'activité 

Les cartes d'îles et les propriétés à distribuer, varient en fonction du
temps à disposition. On prendra autant de propriétés que l'on veut qu'il
y aie de tours dans le jeu (au moins deux). Pour chacune des propriétés
prises, on prend également la carte de l'île marquée d'une croix dans la
colonne correspondante du tableau
[1](#tableau_verif), plus l'île aux dauphins roses.

#### Contexte 

On donne le contexte de l'activité aux participants: on a retrouvé le
journal d'un pirate décrivant où est-ce qu'il a caché son trésor, mais
on n'est pas sûr de quelle île il s'agit. On dispose également des
cartes de différentes îles qui pourraient correspondre à l'île où le
pirate a caché son trésor. Il faudra, en comprenant les différentes
phrases du journal du pirate, comprendre quelle est l'île cachant le
trésor.

#### Étapes de l'activité 

On commence par distribuer aux participants les cartes des différentes
îles. Puis, on leur distribue un par un les extraits du journal du
pirate (c'est à dire les différentes propriétés que l'île au trésor
vérifie). Si on souhaite une difficulté croissante, il est conseillé de
distribuer les propriétés dans l'ordre de leur numéro.

### Aides pour les participants bloqués 

La façon d'aider un participant qui serait bloqué varie, en fonction de
la propriété en question.

Propriété 1:   
	Sur une feuille, dessiner le chemin qu'a pris le pirate (comme à la
    Figure [\[chemin\]](#chemin)). Donner deux pions au participants (deux pièces
    de monnaie, par exemple), pour lui permettre, pour chaque île,
    d'essayer de suivre en parallèle le chemin du pirate sur son dessin,
    et sur chacune des îles. Les îles où il n'arrive pas à faire le
    chemin sur sa feuille et sur l'île en parallèle ne peuvent pas être
    l'île au trésor, car on n'y retrouve pas le chemin emprunté par le
    pirate!

Propriété 2:   
	L'information que nous donne la propriété 2 est que depuis la cabane
    du pêcheur, on peut aller à la rivière. On pourra là aussi prendre
    un pion. En plaçant initialement le pion sur la cabane de pêcheur,
    on essaie d'aller à la rivière, tout en restant sur les chemins
    présents dans l'île. Si on n'y arrive pas, c'est que l'île en
    question n'est pas l'île au trésor. Si on veut vérifier cette
    propriété avec une difficulté croissante, le faire dans cet ordre:
    Île aux Dauphins Roses, Île de la Fortune, Île des Oiseaux Rapides,
    les autres îles.

Propriété 3:   
	Même principe que la propriété précédente, mais cette fois-ci c'est
    quand on *réussi* à faire bouger le pion de la forêt de palmiers à
    la forêt de conifères qu'en on conclu que l'île en question n'est
    pas l'île au trésor.

Propriété 4:   
	Sur les cartes des îles, colorier tous les chemins allant de la
    plage à la grotte. Une fois que tous les chemins sont coloriés,
    vérifiés qu'ils passent tous par la cabane du pêcheur. Cela peut
    poser une question pas évidente: comment être sûrs qu'on a bien
    colorié *tous* les chemins qui permettent d'aller de la plage à la
    grotte? Cette question est répondue dans la mini-activité \"Parcours
    dans un graphe\" ci-dessous, qu'on pourra faire jouer aux plus
    rapides.

Propriété 5:  
	Comme pour la propriété 1, on pourra dessiner le chemin sur une
    feuille de papier, suivre le chemin en parallèle, avec deux pions,
    sur la feuille et sur la carte de l'île, sauf que cette fois, il
    faudra additionner au fur et à mesure le temps mis pour aller d'un
    endroit à l'autre.

### Pour ceux qui vont vite: parcours dans un graphe 

Pour être sûrs de trouver tous les chemins, on peut utiliser des pions
de couleurs différentes. Une couleur par chemin trouvé, plus deux
couleurs spéciales: le gris et le noir. Le sens des pions gris est «On
n'a pas fini d'explorer tous les chemins passant par ce nœud-là», alors
que le sens des pions noirs est «On a fini d'explorer tous les chemins
passant par ce nœud-là». Deux nœuds jouent un rôle spécial: le départ et
l'arrivée. On commence par placer un pion gris sur le départ. Tant que
l'on peut, on choisi un voisin du dernier nœud où l'on a placé un pion
gris qui n'aie pas de pion dessus et on y place également un pion gris.
Si à n'importe quel moment on place un pion gris sur l'arrivée, on a
trouvé un chemin. On prend alors des pions d'une autre couleurs, et on
les place dans sur tous les nœuds ayant un pion gris. Quand le dernier
nœud sur lequel on a placé un pion gris n'a plus de voisin sans pions,
on remplace son pion gris par un pion noir, et on reviens au nœud
précédent avant un pion gris.

Combiner les activités modélisation et vérification 
---------------------------------------------------

Si on veut jouer les deux premières activités au même temps, on pourra
suivre les instructions de l'activité vérification (Activité B), mais au
lieu de distribuer les îles en forme de graphe/carte, on distribuera les
description textuelles ci-dessous, et on les modélisera en suivant les
conseils/étapes de l'activité modélisation (activité A).

#### Île Scorpion 

-   Dans cette île, on ne peut débarquer que sur la plage.

-   Pour descendre à la grotte, il faut marcher sur la façade ouest du
    volcan.

-   En passant par la façade est du volcan, on arrive à la forêt de
    palmiers.

-   En passant par la façade sud du volcan, on arrive à la rivière.

-   Sur la plage pousse une forêt de palmiers.

-   La rivière débouche sur un lac.

-   Sur la rive droite de la rivière, est installée la cabane du
    pécheur.

#### L'île tortue 

-   On peut arriver à l'île par la plage ou par la crique

-   De la plage, un chemin tortueux mène à la forêt de palmiers.

-   De la cabane du pêcheur, on peut atteindre le lac ou la forêt de
    palmiers

-   En descendant par la façade est du volcan on atteint la grotte

-   La cabane du pêcheur se trouve sur la façade ouest du volcan

-   La crique mène à la forêt de conifères

-   En traversant la forêt de conifère, on arrive à la rive de la
    rivière

#### L'île de la fortune 

-   Le seul moyen d'arriver à l'île est de débarquer sur la plage.

-   De la plage, un chemin fleuri mène à la forêt de palmiers

-   En traversant la forêt de palmiers on peut arriver sur le lac ou sur la cabane
    du pêcheur

-   Le lac mène à la forêt de conifères, mais ne permet pas d'atteindre
    directement la cabane du pêcheur

-   Une grotte se cache sur la façade est du volcan

-   La rivière prent sa source sur le volcan, et coule sur sa façade sud

-   De la cabane du pêcheur, un chemin très escarpé mène jusqu'au sommet
    du volcan

#### L'île des oiseaux rapides 

-   La plage et la crique offrent toutes deux de bons endroits pour
    débarquer sur l'île

-   Cette île a deux forêts: la forêt de palmiers, à côté de la plage,
    et la forêt de conifères, à côté de la crique

-   Au fond de la crique, se dissimule la cabane du chasseur

-   Sur la plage, baignent les eaux du lac salé, dont l'autre rive donne
    accès à une grotte.

-   La fôret de palmiers habrite la rivière et la cabane du pêcheur

-   Par contre, de la rivière, on ne peux aller directement à la cabane
    du pêcheur, qui se trouve sur la façade ouest du volcan.

-   Sur la façade est du volcan se cache la grotte.

#### L'île des singes hurleurs 

-   On peut arriver à l'île par la plage ou par la crique

-   Sur la plage, on trouve le delta de la rivière Papamouan.

-   En remontant la rivière Papamouan, on peut arriver à la cabane du
    pêcheur au bout de trois heures.

-   De la plage, on peut accéder à la forêt de palmiers en gravissant
    pendant deux heures un chemin tortueux

-   Au milieu de la crique, se dresse la cabane du chasseur.

-   Traverser la crique prend une heure et à sa lisière se trouve
    une forêt de conifères

-   Traverser la forêt de palmiers pour atteindre la cabane du pêcheur
    prend une heure.

-   À l'arrière de la cabane du pêcheur, un chemin plein de cendres
    permet de monter au sommet du volcan en 3h.

-   Descendre par la façade est du volcan prend également 3h et on
    arrive à la grotte

#### Île des dauphins roses 

-   Il y a deux façons de débarquer dans l'île: une crique et une plage.

-   De la crique un chemin étroit et sombre mène en deux heures de
    marche à une magnifique forêt de conifères, alors qu'un sentier bien
    entretenu mène à la cabane du chasseur en une heure

-   De la plage, un chemin scabreux monte vers la forêt de palmiers, il
    faut une bonne heure pour le trajet.

-   De la rivière, une heure de marche permet d'atteindre la cabane du
    pêcheur. En remontant la rivière, on peut atteindre le volcan au
    bout de quatre heures.

-   Pour descendre à la grotte, il faut marcher sur la façade ouest du
    volcan pendant deux heures.

-   En descendant la façade est du volcan pendant trois heures, on
    arrive à la cabane du pêcheur.

-   Le pêcheur fait tous les matins une promenade de deux heures jusqu'à
    la forêt de palmiers pour ceuillir des noix de coco.

*C'est dans cette dernière île que se trouve le trésor.*

# Activité C: Notations de la logique

## Objectif pédagogique
Quand il s'agit de vérifier des propriétés
(que ce soit sur des programmes informatiques ou sur des
graphes d'île), il faut les ennoncer de façon non-ambigüe.
Pour cela, des notations mathématiques sont utilisées
pour écrire les formules logiques.

Dans cette activité, à travers le déchiffrement
de formules qu'un pirate aurait êcrit 'avec des symboles cabalistiques'
pour 'les rendre difficile à comprendre pour les autres',
les participants seront amenés à comprendre comment
lire une formule logique /  comment fonctionnent ces notations.

## Matériel
On a 3 jeux de propriétés / formules,
en français et en notation logique;
et un jeu d'îles sur lesquels on pourra vérifier
certaines des formules.
Les îles seront fournies sous forme de cartes.

Les différents symboles qui apparaîtront dans les formules sont

| Nom en logique             | Symbole       | Traduction                |
|----------------------------|---------------|---------------------------|
| Quantificateur existenciel | &exist; x, P  | Il existe un x tel que P  |
| Quantificateur universel   | &forall; x, P | Pour tout x, on a P       |
| Négation                   | &not;   P     | Non P / Il est faux que P |
| Conjonction                | P1 &and; P2   | P1 et P2                  |
| Implication                | P1 &rArr; P2  | Si P1 alors P2            |

Symboles spécifiques à notre activité

| Nom    | Symbole | Traduction                            |
|--------|---------|---------------------------------------|
| Chemin | l1 C l2 | chemin entre l1 et l2                 |
| Arête  | l1 A l2 | arête entre l1 et l2                  |
| Temps  | T(A)    | Le temps mis pour parcourir l'arête A |

### Premier jeu de propriétés: découverte
#### En notation logique
+ Propriété 1:   
  ( &exist; A1, plage A1 forêt de palmiers) &and; (&exist; A2, Forêt de palmiers A2 cabane de pêcheur ) 
  &and; (&exist; A3, cabane de pêcheur A3 volcan) &and; (&exist; A4, volcan A4 grotte)
+ Propriété 2:   
  &exist; C (Cabane du pêcheur C rivière)
+ Propriété 3:   
  &not; &exist; C (forêt de palmiers C forêt de conifère)
+ Propriété 4:   
  &forall; C (plage C grotte) &rArr; &exist; C1 C2, (plage C1 volcan) &and; (volcan C2 grotte) &and; C = C1C2
+ Propriété 5:   
  &exist; A1 A2 A3 A4, (plage A1 forêt de palmiers) &and; (Forêt de palmiers A2 cabane de pêcheur ) &and; (cabane de pêcheur A3 volcan) &and; (volcan A4 grotte) &and; T(A1) + T(A2) + T(A3) + T(A4) = 8h
#### En français
+ Propriété 1:   
	Pour cacher le trésor, j'ai débarqué sur la plage et je suis passé
    successivement par la forêt de palmiers, la cabane de pêcheur et le
    volcan avant d'arriver à la grotte, où j'ai caché mon trésor.

+ Propriété 2:   
	Quand je passais par la cabane du pêcheur, j'ai vu un chemin qui
    descendait jusqu'à la rivière, mais il était trop étroit pour que je
    passe avec mon trésor. Je ne l'ai donc pas emprunté.

+ Propriété 3:   
	Quand j'étais dans la forêt de palmiers, j'aurais voulu aller à la
    forêt de conifères, mais je ne pouvais pas.

+ Propriété 4:   
	Pour aller à la grotte depuis la plage, on passe forcément par la
    cabane du pêcheur.

+ Propriété 5:   
	Pour aller de la plage jusqu'à la grotte en empruntant le chemin que
    j'ai décrit, il m'a fallu huit heures en tout.

### Deuxième jeu de propriétés: Décodage (+ vérification)
#### En notation logique
+ Propriété 1:   
  ( &exist; A1, plage A1 Cabane du pêcheur) &and; (&exist; A2, Cabane de pêcheur A2 volcan ) 
  &and; (&exist; A3, volcan A3 forêt de palmier) &and; (&exist; A4, forêt de palmier A4 lac)
+ Propriété 2:   
  &exist; C (forêt de palmier C forêt de conifères)
+ Propriété 3:   
  &not; &exist; A (forêt de conifères C lac) &and; &exist; C (forêt de conifères C lac)
+ Propriété 4:   
  &forall; C (plage C lac) &rArr; &exist; A, (cabane de pêcheur A volcan) &and; &exist; C1 C2, (plage C1 cabane du pêcheur) &and; (volcan C2 lac) &and; C = C1AC2
+ Propriété 5:   
  &exist; A1 A2 A3 A4, 
  (  plage A1 Cabane du pêcheur) &and; ( Cabane de pêcheur A2 volcan ) 
  &and; ( volcan A3 forêt de palmier) &and; ( forêt de palmier A4 lac) 
  &and; T(A1) + T(A2) + T(A3) + T(A4) = 8h
#### En français
+ Propriété 1:   
	Pour cacher le trésor, j'ai débarqué sur la plage et je suis passé
    successivement par la cabane du pêcheur, le volcan, la forêt de palmiers
	et le lac, où j'ai caché mon trésor.

+ Propriété 2:   
	Quand je passais par la forêt de palmiers, j'ai vu un chemin qui
    descendait jusqu'à la forêt de conifères.

+ Propriété 3:   
  Il n'y a pas de chemin direct entre la forêt de conifères et le lac,
  mais il y a un chemin indirect pour aller de l'un à l'autre.

+ Propriété 4:   
	Pour aller au lac depuis la plage, on passe forcément successivement par la
    cabane du pêcheur et le volcan.

+ Propriété 5:   
	Pour aller de la plage jusqu'au lac en empruntant le chemin que
    j'ai décrit, il m'a fallu huit heures en tout.
### Troisième jeu de propriétés: Encodage
#### En notation logique
+ Propriété 1:   
	( &exist; A1, cirque A1 Cabane de chasseur) &and; (&exist; A2, Cabane de chasseur A2 forêt de conifères ) 
  &and; (&exist; A3, forêt de conifères A3 volcan) &and; (&exist; A4, volcan A4 grotte)
+ Propriété 2:   
	&exist; C (volcan C lac)
+ Propriété 3:   
  &not; &exist; C (volcan C rivière) &and; &exist; A (rivière C cabane de pêcheur)
+ Propriété 4:   
  &forall; C (crique C grotte) &rArr; &exist; C1 C2, (crique C1 cabane du chasseur) &and; (cabane du chasseur C2 grotte) &and; C = C1C2
+ Propriété 5:   
  &forall; C (crique C grotte) &rArr; &not; &exist; A C1 C2, (crique C1 cabane de chasseur) &and; (cabane de chasseur A forêt de palmiers)  &and; (forêt de palmiers C2 grotte) &and; C = C1AC2
#### En français
+ Propriété 1:   
	Pour cacher le trésor, j'ai débarqué sur la crique et je suis passé
    successivement par la cabane du chasseur, la forêt de conifères, le volcan,
	et la grotte, où j'ai caché mon trésor.

+ Propriété 2:   
	Depuis le volcan, les aventuriers endurants peuvent aller jusqu'au lac.

+ Propriété 3:   
    Depuis le volcan on ne peut pas aller jusqu'à la rivière. 
	Cependant, on peut aller de la rivière à la cabane de pêche.

+ Propriété 4:   
	Pour aller à la grotte depuis la crique, on passe forcément par la
    cabane du chasseur.

+ Propriété 5:   
	Pour aller de la crique jusqu'à la grotte,
	on ne passe par aucun chemin direct entre la
	cabane du chasseur et la forêt de palmiers.

Pour voir quand distribuer quoi aux participants,
voir la section suivante.

## Déroulement
### Mise en place

### Context

Dans cette activité, le pirate n'a pas écrit son journal en français,
mais avec des symboles cabalistiques qu'il va falloir apprendre à
déchiffrer. C'est l'occasion d'apprendre ce qu'est un quantificateur en
logique.


### Étapes de l'activité

Cette activité se déroule en trois étapes. 

La première étape permet aux participants de découvrir les éléments de logique.
On leur donne le premiers jeu de propriétés en français et celle codée (pas 
nécessairement dans le même ordre, elles peuvent être mélangées). Le but des
participants est alors d'identifier grâces aux propriétés en français les 
symboles des propriétés codées. Cette étape peut être guidée via deux sous-étapes
intermédiaires : identifier les paires de propriétés en français avec celle 
codée; puis inférer la traduction des symboles. 

La seconde étape permet aux participants de manipuler les définitions logiques
en les décodants dans des formules logiques. On leur distribue alors le deuxième
jeu de propriétés uniquement codées. Leur objectif est donc de les traduire en 
français.

La troisième étape permet aux participants de manipuler à l'inverse les 
définitions logiques. On leur distribue le troisième jeu de propriété uniquement
en français et leur objectif est coder ces propriétés.


### Modification de l'étape 3

Si on veut mettre en place un peu de vérification, après avoir décodé les
propriétés, on peut les tester sur le jeu d'îles fourni avec cette activité. Le 
but ici est toujours le même et consiste à trouver l'île au trésor. Cependant, 
pour des raisons de temps, l'activité de vérification devraient avoir été faite
en amont.

## Aides pour les participants

En cas de difficulté, on peut appliquer à chaque étape ces différentes aides.
+ Pour la première sous-étape de l'étape 1: on peut aider le participant en 
réassemblant les propriétés en français avec les propriétés codées.
+ Pour la seconde sous-étape de l'étape 2: on propose cette ordre pour inférer les symboles
    + le symbole représentant les arêtes via la propriété 1
    + le symbole représentant les chemins via les propriétés 2 et 3
    + le symbole représentant le temps via la propriété 5
    + le symbole représentant la conjonction via les propriétés 1 et 5
    + le symbole représentant "il existe" via les propriétés 1 et 2 (la difficulté
    ici est que dans la traduction le "il existe" n'apparait pas, il peut être 
    utile de reformuler les traduction soit par le participant soit par l'aidant)
    + le symbole représentant la négation via la propriété 3 (ici on peut demander 
    au participant de traduire la propriété via les symboles connus, tous sauf la
    négation, et comparer sa traduction avec la traduction donnée)
    + les deux symboles restant apparaissent uniquement dans la propriété 4. On 
    commence par demander aux participants de traduire la deuxième partie de la 
    propriété (à droite de l'implication) afin d'obtenir "on passe par la cabane 
    du pêcheur". Un fois que cette traduction est faite, il faut traduire le 
    "forcément" qui est représenter par l'implication et le pour tout. Cette 
    dernière étape est vraiement délicate et peut être effectuée en classe entière.
+ Pour la seconde et la troisième étape, on donne un tableau récapitulatif de la
 traduction des éléments codés.
















