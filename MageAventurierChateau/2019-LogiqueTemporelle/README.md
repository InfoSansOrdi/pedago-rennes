Le Mage, l'Aventurier et le Chateau Hanté
=========================================


Ce document est un premier jet présentant une activité de pédagogie 
informatique sans ordinateur dans le cadre du module PEDAGO pour les masters
2 de l'ENS Rennes en informatique. L'objectif ici est de présenter une 
activité autour d'un sujet de recherche. La recherche qui nous intéresse est
une recherche théorique en logique fondamentale. Ce document contient une 
description de l'activité (et contiendra une mise en situation). Libre à vous de
vous l'approprier et de l'adapter si vous en ressentez le besoin.

Le Public
---------

Malheureusement, je n'ai aucune expérience dans ce genre de domaine, je ne 
sais donc pas du tout à qui faire cette activité. Mon intuition me dit que 
pour des lycéens, il n'y aura pas de problème. Les retours, même sans mise 
en pratique sont les bienvenus.

Le Contexte
-----------

Un aventurier en quête de trésors part à l'aventure dans un donjon. Le mage 
qui a construit magiquement le donjon est ravi d'avoir un visiteur et veut 
tout faire pour aider l'aventurier mais le chateau est hanté par un fantôme 
malfaisant qui va tout faire pour empecher l'aventurier d'arriver au trésor.
	 
Le chateau est initialement vide et le mage va devoir créer les pièces du 
chateau au fur et à mesure que l'aventurier progresse. Cependant, le fantôme 
va pouvoir les hanter et les modifier avant que l'aventurier ne les atteigne. De 
plus, la magie qui crée les pièces est très spéciale et ne permet pas de faire 
ce que l'on veut. Une table des règles de création doit être consultée pour 
chaque pièce. 
	  
L'activité est pour deux joueurs, l'un incarne le mage et l'autre le fantôme. 
Le but du joueur incarnant le mage est que l'aventurier atteigne une pièce 
avec le trésor; le but du joueur incarnant le fantôme est que le mage 
n'atteigne pas son objectif.

Table Des Règles de Construction
--------------------------------

Chaque pièce a des caractéristiques spécifiques: la couleur de la pièce, le 
mobilier, etc. Certains choix seront faits par le mage et d'autres par le 
fantôme. Le document récapitulatif des choix des joueurs et des règles est 
appelé la *Table des règles de construction*.
  
Voici un exemple de table:
 	  
Choix des joueurs :

* Le mage choisi si la pièce est de couleur bleu ou orange. 
* Le mage choisi si il y a un trésor ou pas dans la pièce.
* Le fantome choisi si il y a un tableau ou pas dans la pièce.
    
Règles:

* Pour placer le trésor, si deux pièces avant, il y avait un tableau, la pièce précédente doit être orange.
* Le trésor ne peut etre placé qu'à la troisième pièce.

Une table de règle caractérise entièrement une instance du jeu. 
Celle présentée ci-dessus est très simple mais donne une idée des
règles possibles. Avec seulement quelques règles, on peut arriver 
à un jeu très dur à résoudre.

**Idées de règles**

Je n'ai pas réussi à créer une table des règles simples à lire et à comprendre 
mais qui donneraient un jeu pas si simple à résoudre. (Pour comprendre ce concept, 
pensez aux échecs ou au go... Ces jeux ont des règles globalement simples mais 
il est impossible de savoir qui va remporter la partie dès le début). Cependant 
j'ai pensé à certaines règles qui pourraient aider à avoir une table avec cette 
bonne propriété.

* Le mage choisit si il y a un tableau ou non, mais ne peut en placer que 3.
* Le fantome choisi si il y a une épée mais dans une certaine configuration, si il n'y en a pas, il ne pourra pas mettre le monstre plus tard.
* À chaque étape le fantome doit mettre un objet d'une liste donnée d'objet dont un objet qui le fera gagner si il en met suffisamment.

Lien avec l'informatique
------------------------
	
En informatique, on se demande si les programmes utilisés partout ont des bugs.
C'est d'autant plus critique lorsque le dit programme fait fonctionner une 
centrale nucléaire ou fait voler un avion. De nombreuses approches pour
vérifier les programmes ont été envisagées et l'une d'elles consiste à se 
demander si un système peut arriver dans un certain état et ce alors que 
l'environnement peut l'influencer.

Ici c'est presque pareil: on veut savoir si malgré les agissements du fantôme,
le mage peut amener l'aventurier jusqu'au trésor.

**Objets:**

Les activités débranchées peuvent être caractérisées par les objets qu'elles
font manipuler. Il y en a 4 types différents : les langages, l'information, 
les algorithmes et les machines. Pour chaque type, nous précisons à quel point
l'activité est pertinente.

* Langage(-): Pas pertinent.
* Information(\*): Le jeu se base sur l'adaptation aux décisions de son adversaire, donc des informations qu'il nous donne.
* Algo(\*): Pour résoudre le jeu de manière automatique, il faut développer un algorithme.
* Machine(\*): L'aventurier symbolise la machine : on ne le manipule pas directement il agit de manière prévisible.

**Competence:**

De même que pour les objets de l'informatique, des compétences spécifiques 
à la discipline peuvent être reliées à l'activité. Elles sont au nombre de 
7 et listées ci-dessous.

* Pensée Algo(\*): Pour résoudre le jeu de manière, il faut développer un algorithme.
* Abstraction/Modélisation(\*): On peut transformer les règles en un graphe des états possible.
* Generalisation/Motif(-): A priori, pas pertinent.
* Logique(\*\*): Les règles sont en réalité des formules de logique temporelle.
* Décomposition(-): A priori pas pertinent.
* Évaluation(-): A priori pas pertinent.

Idée d'extension : Chateau aléatoire
------------------------------------

Il est peut etre plus facile de créer un jeu avec des cartes tirées aléatoirement.
Le joueur est alors tout seul et à chaque étape, il joue une ou plusieurs cartes 
pour tenter de gagner.

Attention, le lien avec l'informatique n'est plus exactement le meme ! Il s'agit 
alors de verifier des systèmes probabilistes.

