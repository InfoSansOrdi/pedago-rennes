Le Mage, l'Aventurier et le Chateau Hanté
=========================================


Ce document est un premier jet présentant une activité de pédagogie 
informatique sans ordinateur dans le cadre du module PEDAGO pour les master 2 
de l'ENS Rennes en informatique. L'objectif de ce papier est de présenter une 
activité autour d'un sujet de recherche. La recherche qui nous intéresse est 
une recherche théorique en logique fondamentale. Ce document contient une 
decription de l'activité ainsi qu'une mise en situation. Libre à vous de vous 
l'approprier et de l'adapter si vous en ressentez le besoin.

Le Public
---------

Malheureusement, je n'ai aucune expérience dans ce genre de domaine, je ne 
sais donc pas du tout à qui faire cette activité. Mon intuition me dit que 
pour des lycéens, il n'y aura pas de problème. 

Le Contexte
-----------

Un aventurier en quete de trésors par à l'aventure dans un donjon. Le mage 
qui a construit magiquement le donjon est ravi d'avoir un visiteur et veut 
tout faire pour aider l'aventurier mais le chateau est hanté par un fantome 
malfaisant qui va tout faire pour empecher l'aventurier d'arriver au trésor.
	 
Le chateau est initialement vide et le mage va devoir créer les pièces du 
chateau au fur et à mesure que l'aventurier progresse. Cependant, le fantome 
va pour les hanter et les modifier avant que l'aventurier ne les atteigne. De 
plus, la magie qui créer les pièces est très spéciale et ne permet pas de faire 
ce que l'on veut. Une table des règles de création doit etre consultée pour 
chaque pièce. 
	  
L'activité est pour deux joueurs, l'un incarne le mage est l'autre le fantome. 
Le but du joueur incarnant le mage est que l'aventurier atteigne une pièce 
avec le trésor; le but du joueur incarnant le fantome est que le mage 
n'atteigne pas son objectif.

Table Des Règles de Construction
--------------------------------

Chaque pièce a des caractéristiques spécifiques: la couleur de la pièce, le 
mobilier, etc. Certains choix seront faits par le mage et d'autres par le 
fantome. Le document récapitulatif des choix des joueurs et des règles est 
appelé la *Table des règles de construction*.
  
Voici un exemple de table:

 	  
Choix des joueurs :

* Le mage choisi si la pièce est de couleur bleu ou orange. 
* Le mage choisi si il y a un trésor ou pas dans la pièce.
* Le fantome choisi si il y a un tableau ou pas dans la pièce.
    
Règles:

* Pour placer le trésor, si deux pièces avant, il y avait un tableau, la pièce précédente doit etre orange.
* Le trésor ne peut etre placé qu'à la troisème pièce.

Une table de règle caractérise entièrement une instance du jeu. Celle présentée ci-dessu est très simple mais donne une idée des
règles possibles. Avec seulement quelques règles, on peut arriver à un jeu très dur à résoudre.


Lien avec l'informatique
------------------------
	
En informatique, on se demande si les programmes utilisés partout ont des bugs. C'est d'autant plus critique lorsque le dit programme 
fait fonctionner une centrale nucléaire ou fait voler un avion. De nombreuses approches pour vérifier les programmes ont été 
envisagées et l'une d'elle consiste à se demander si un système peut arriver dans un certain état et ce alors que l'environement peut 
l'influencer.

Ici c'est presque pareil: on veut savoir si malgrès les agissements du fantome, le mage peut ammener l'aventurier jusqu'au trésor.

Une autre approche peut etre celle de la sécurité.

Objets:

* Langage(-): Rien
* Information(\*): Le jeu se base sur l'adaptation aux décisions de son adversaire, donc des informations qu'il nous donne.
* Algo(\*): Pour résoudre le jeu, il faut développer un algorithme
* Machine(\*): L'aventurier symbolise la machine


Competence:

* Pensée Algo(\*): Pour résoudre le jeu, il faut développer un algorithme.
* Abstraction/Modelisation(\*): On peut transformer les règles en un graphe des états possible.
* Generalistation/Motif: ?
* Logique(\*\*): Les règles sont en réalité des formules de logique temporelle.
* Decomposition: ?
* Evaluation: ?

