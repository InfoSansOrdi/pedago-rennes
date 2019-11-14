# Vue d'ensemble des travaux de l'année 2019

Cette page vise à présenter les travaux menés par les élèves de l'ENS Rennes
dans le cadre du module de pédago2 (niveau M2) pendant l'année scolaire
2019-2020. La plupart de ces travaux sont en cours de réalisation et sont loins
d'être terminés, mais le module continue jusqu'à fin janvier 2020.

## Nim, apprentissage et goblets

(participants: Killian Barrere et Romain Ferrand)

L'objectif est de faire une variante du jeu de Nim qui soit plus adaptée à
l'[activité sur l'apprentissage par
renforcement](https://projet.liris.cnrs.fr/lirismed/index.php?id=la-machine-qui-apprend-a-jouer-toute-seule)
existante.
  
Si le jeu est aussi compliqué que le Nim à 12 jetons/3 par tours,
l'apprentissage converge trop lentement pour être utilisable sans ordinateur. Si
le jeu est simplifié comme un Nim 8 jetons/2 par tours, certains élèves de 5ieme
résolvent le probleme d'instinct, sans réfléchir, et n'ont plus de plaisir à
jouer le jeu.
  
L'idée est de partir sur une variante irrégulière, où la stratégie gagnante
change à chaque tour. Pour que ça reste jouable, on va jouer sur un plateau
représentant le graphe d'évolution du jeu sous-jacent au lieu de se souvenir des
règles. Au final, c'est un jeu de déplacement de pions sur un graphe. Chaque
joueur déplace le pion, chacun à son tour.

Le graphe est un peu contextualisé : Deux personnes sont dans un même véhicule :
l'un avance le jour, l'autre la nuit, chacun se déplace d'une seule arrête.
L'objectif de chacun est d'être celui qui amène le véhicule à bon port.

Dans un premier temps, on utilise vraiment le graphe du jeu de Nim, puis on
utilise une variante moins régulière (dans un second niveau?).

Biblio:
 - https://fr.wikipedia.org/wiki/Géographie_généralisée (ce n'est pas exactement le même jeu)
 - https://perso.liris.cnrs.fr/eric.duchene/articles/HDR.pdf (Manuscript de Eric Duchêne sur ce genre de jeux)
 
En cours: invention d'un graphe intéressant à la fois à la main et pour les
goblets, ainsi que l'écriture d'un simulateur de goblets en python pour mesurer
les vitesses de convergence des différentes formes d'apprentissage sur les
différentes variantes du jeu.


## Traduction en français de CS unplug

(participants: Marco Freire, Thais Baudon, Clement Courageux-sudan, Martin
 Quinson, ainsi que Clément Mommessin, Yannick Parmentier et Samuel Chalifour
 qui sont membres d'infosansordi sans rapport avec l'ENS Rennes).
 
L'objectif est de participer à la traduction en français du site web de CS
unplugged. Pour s'organiser, on a [un wiki](https://translate-csunplugged.frama.wiki/start) 
et [un groupe de discussion](https://framateam.org/signup_user_complete/?id=s5fwenbchirmpf5iwdop19z3pr).

On est maintenant à 39% de complétion (contre 32% en début de semestre), mais ce
n'est pas représentatif car (1) certaines pages sont visiblement traduites par
des non-francophones, et il faut les reprendre (2) il y a des pages qui ne
contiennent que du code. Il n'est pas nécessaire de traduire -- il faudrait
plutôt trouver comment les retirer de la liste ? 

Les éléments de base du site sont traduits et repris, et il faut maintenant
avancer sur les différentes activités existantes sur ce site. On voudrait aussi
mettre en place un site beta afin de voir l'existant (et commencer à faire
profiter du fruit de notre travail), mais les auteurs néo-zélandais répondent
très rarement à nos messages. Ils sont visiblement occupés par un [projet de
manuel d'informatique](https://csfieldguide.org.nz/en/) qui a l'air intéressant
lui aussi. 

On réfléchi à mettre en place notre propre site web, puisque tout le code de
leur infra est [disponible sur github](https://github.com/uccser/cs-unplugged/).
On arrive à lancer le serveur en local, mais pas à lui faire afficher le texte
français [sans se connecter à Crowdin].
    
En attendant, les collègues néo-zélandais n'ont pas encore cliqué pour faire de
certains d'entre nous des validateurs officiels de traduction. C'est nécessaire
puisque la qualité des traductions existantes n'est pas optimale. À la place, on
a mis en place une page du wiki pour lister à la main où nous en sommes.
    
## Activité de logique dynamique temporelle

(participant: Dylan Bellier)

Objectif: inventer une activité originale en rapport avec la vérification de
logique temporelle (plutôt type QPTL que LTL -- càd LTL+quantificateurs).

Un aventurier veut rentrer dans le donjon pour trouver un trésor. Le donjon est
habité par un gentil mage et un fantôme malfaisant. C'est un jeu à deux joueurs,
qui prennent respectivement le rôle du mage et du fantôme.

Au début de la partie, le donjon n'existe pas. A chaque tour, le mage doit créer
des pièces (ajouter des tuiles de jeu avec des pions dessus pour spécialiser les
pieces) pour que l'aventurier puisse avancer, mais le fantome peut influer sur
chaque création soit en ajoutant des éléments ou en spécialisant les objets
créés par le mage. Les deux joueurs doivent suivre la table des règles, qui
spécifie ce qu'on peut créer à quel moment de la partie.

Le but du mage est que l'aventurier arrive au trésor, tandis que le but du
fantôme est de faire en sorte que le mage ne puisse plus créer de pièce (sans
boucle infinie). Au final, le jeu va ressembler à une sorte de chateau pas très
fort, mais où le chateau est construit dynamiquement, en ajoutant des tuiles
comme dans Carcassone.

Fait: une fiche explicative et un début de règles du jeu.
À faire: faire des règles jouables et intéressantes

Mais il est difficile de trouver une règle (des propriétés à respecter) pour
laquelle il n'existe pas de stratégie gagnante facile à voir pour l'un des
joueurs. Si Dylan ne trouve pas de règle rendant le jeu amusant pour les deux
joueurs, on envisage de transformer le jeu en une sorte de solitaire où il
s'agit de trouver et appliquer la stratégie gagnante face à des cartes tirées au
hasard.

## Simulateur en javascript de M99

(participant: Thibaud Balem)

La représentation graphique est découpée en trois parties. En haut: le support
d'exécution, avec l'état de la mémoire et les registres. On peut exécuter un
programme en pas à pas à ce niveau. 

Au milieu: l'éditeur de code où l'on peut avoir trois niveaux de langage: Le
langage machine, c'est à dire une représentation numérique du programme; Un
assembleur intermédiaire, avec les adresses en absolu et un assembleur
"relocalisable", avec des variables et des labels. On peut compiler dans un seul
sens : relocalisable -> absolu -> langage machine.

En bas de l'écran, on affiche des logs sur les erreurs de compilation ou
d'exécution. L'exécution sur M99 semble toujours possible (pas d'erreur fatale),
mais on peut vouloir faire des avertissements quand on passe une valeur négative
d'un registre vers la mémoire (qui est non signée).

Le travail en cours porte sur la compilation du langage absolu vers le langage machine.
  
## Texte "c'est de l'informatique parce que" sur les blasons

(participant: Benjamin Bordais)

L'objectif est de faire un document permettant aux animateurs de comprendre le
lien à l'informatique, avant de pouvoir l'expliciter aux participants. Ce texte,
à utiliser en fin de séance après avoir joué l'activité, sera découpé en trois
parties.

En introduction, un texte introductif au format libre argumentant sur l'intéret
de l'activité et des anectodes sur le problème sous-jacent. Sur les blasons, on
a peu de contenu ici, juste faire le lien à l'activité connue en primaire de la
figure téléphonée. On aurait beaucoup plus d'histoire et d'anectodes à raconter
sur le problème du crépier, par exemple.

Une seconde partie vise à expliciter le lien de l'activité avec les 4 concepts
phares de l'informatique: Algorithme, langage, information et données, machine.
Pour chaque concept, l'activité est notée de 0 à 2 étoiles : deux étoiles =
l'activité est vraiment focalisée sur ce concept, 0 étoile = le lien semble
inexistant. Dans le cas du blason, nous avons trouvé la classification
suivante : Algorithme (0), Langage (2), Information (1), Machine (0).

La troisième partie est assez similaire à la seconde, mais elle explore les
liens aux [6 compétences de la pensée informatique](https://csunplugged.org/en/computational-thinking/) 
telles qu'explicitées par le site CS unplugged: Pensée algorithmique, abstraction,
généralisation, logique, évaluation et décomposition.

Détail amusant : des idées d'extensions intéressantes sont apparues quand on
cherchait le lien aux compétences. En particulier, on pourrait faire des motifs
recursifs ou pseudo-récursifs pour travailler la compétence de décomposition.

La rédaction ([disponible ici](2019-cest-de-linfo/Blasons.md)) est
bien avancée, ce qui laisse envisager de rédiger le même genre de
choses pour une autre activité connue avant la fin du module.

## Deux activités autour de la modélisation et de la vérification

(participants: Julie Parreaux, Santiago Bautista, Quentin Le Dilavrec)

Contexte général: des îles au pirates, avec des trésors dessus (ou pas). Les
deux activitités peuvent se jouer séparément ou en séquence.

La première activité porte sur la modélisation. Il s'agit pour les participants
de passer d'une description textuelle d'îles de pirates à une carte (un graphe).
Nous avons 6 îles au total. Les premières descriptions sont sous forme d'items
assez faciles tandis que les dernières sont un peu plus complexes et forment de
petites histoires contenant des éléments narratifs inutiles pour la
modélisation. Toutes les îles ont 8 ou 9 noeuds chacune, et nous avons un
générateur en javascript permettant de présenter de jolis cartes en vectoriel en
guise de solution.

Dans une version courte, modéliser les deux premières peut être suffisant pour
l'activité.


La seconde activité porte sur la vérification de propriétés formelles. Les
participants recoivent des plans d'îles (pré-modélisées), et des propriétés sous
forme textuelles. Chaque propriété discrimine une île, qui n'est donc pas celle
où se trouve le trésor. 

Nous avons également 6 îles (pas exctement les mêmes qu'à la première activité
-- voir le texte de l'activité), et 5 propriétés. On peut faire varier la durée
de l'activité en limitant le nombre d'éléments.

Une extension potentielle à la seconde activité serait d'écrire certaines
propriétés dans un langage codé, qui correspond aux quantificateurs de la
logique des prédicats, appliqués sur des émoticons de singes, palmiers et autres
volcans.
 
## Un outil pour recaler les impressions recto/verso

(participants: Martin Quinson et Quentin Le Dilavrec)

Il s'agit d'un petit bout de javascript permettant de corriger les décalages dûs
à l'imprimante. C'est surtout pour que l'hexaflexagone s'imprime correctement,
bien aligné, sans devoir coller les deux faces.
