# Projet : Apprentissage débranché du morpion

## But du projet

Ce projet s'inspire du projet d'apprentissage avec des gobelets sur le jeu de mims.
Le but est de faire apprendre à une IA une stratégie gagnante pour le morpion.
On utilise pour cela des gobelets contenant des jetons. Le joueur joue contre l'IA, 
pour jouer l'IA utilise l'information de ses gobelets pour prendre des décisions.
Après chaque partie, le joueur modifie la contenance des gobelets selon des instructions spécifiques pour modifier le fonctionnement de l'IA au fûr et à mesure des parties. L'IA converge ainsi vers une solution de stratégie gagnante à mesure de son apprentissage de partie en partie.

## Solution imparable pour gagner au morpion
On s'inspire d'une solution pour réussir à coup sûr au morpion (qui permet au mieux de gagner ou au pire de faire match nul). Cette stratégie suppose de commencer en premier avec le X.

Coup 1: Positionnez-vous dans un coin. 
Coup 2:
SI l’autre joueur ne s’est pas positionné 
à cet endroit  
ALORS  positionnez-vous dans le coin
diamétralement opposé au coup 1. 
SINON positionnez-vous dans un coin libre.
Coup 3:
S’IL y a 2 X et un espace sur une ligne 
ALORS positionnez-vous sur cet espace. 
SINON S’IL y a 2 O et un espace sur une ligne 
ALORS positionnez-vous dans cet espace. 
SINON positionnez-vous dans un coin libre.
Coup 4:
S’IL y a 2 X et un espace sur une ligne 
ALORS positionnez-vous dans cet espace. 
SINON S’il y a 2 O et un espace sur une ligne 
ALORS positionnez-vous dans cet espace. 
SINON positionnez-vous dans un coin libre.
Coup 5: Positionnez-vous dans l’espace libre.

## Solution approchée
On propose une solution approchée qui soit plus simple à apprendre et qu'on suppose efficace.

Coup 1-4 : S'IL y a 2 "X" ou 2 "O" et un espace sur une ligne, ALORS on se positionne sur cet espace.
           SINON on joue dans un coin libre.
Coup 5 : il ne reste qu'un espace libre, on se positionne dans cette espace.

## La solution d'apprentissage proposée

L'idée est d'utiliser 4 gobelets, chaque gobelet pour chaque coup 1-4.
Chaque gobelet contient des jetons, au début on place un jeton "centre", un jeton "bord" et un jeton "coin" dans chaque gobelet.
On enchaîne plusieurs parties, une partie se déroule comme suit :
- L'IA commence. S'IL y a 2 "X" ou 2 "O" et un espace sur une ligne (si l'IA ou le joueur est sur le point de gagner) alors L'IA joue sur cet espace (l'utilisateur place un X à l'endroit concerné). Sinon, le joueur tire un jeton au hasard dans le gobelet correspondant au numéro du coup (si c'est le premier tour, on tire dans le gobelet 1, si c'est le deuxième, dans le gobelet 2 etc...). Le jeton donne la position à jouer : "centre" l'IA joue au centre, "coin" l'IA joue dans un coin libre et "bord" : l'IA joue dans un bord libre (les bords sont les cases qui ne sont ni le centre ni un coin). Si le jeton correspond à une action impossible (par exemple si la consigne est de jouer un coin alors qu'il n'y a plus de coin libre) alors on tire un nouveau jeton jusqu'à ce qu'on arrive à une action faisable.
- Le joueur joue son tour après l'IA, pour simuler le tour du joueur, l'utilisateur choisit lui même un endroit où jouer son coup (il peut prednre la décsion au hasard ou comme il le souhaite) et place un O sur le tableau.
- Au dernier coup, il ne reste qu'une seule case libre, l'IA place son X dans cette case.

A la fin de la partie, on modifie les gobelets selon ces critères : en cas de victoire ou d'égalité on ne fait rien. En cas de défaîte, on repère la dernière action qui a été faîte selon l'indication d'un gobelet. On retire du gobelet qu'on a utilisé en dernier pour agir, le jeton qu'on avait tiré.
On peut s'attendre - sur le même modèle que le jeu de NIm préalablement proposée - à ce qu'au fûr et à mesure des tours et des mises à jours de gobelets, l'IA s'améliore.

## Matériel
Pour chaque groupe :
- 4 gobelets
- 3 types de jetons (couleur ou forme différente de manière à ce qu'ils soient différenciables facilement) et 4 jetons par type (12 jetons en tout)
- Papier/stylos

## C'est de l'informatique parce que
- Algorithimique : L'utilisateur doit modifier les gobelets selon des instructions établies. Il s'agit en fait d'appliquer un algorithme (une suite d'instructions) pas à pas qui mène à modifier des variables (représentées par les gobelets).

- Apprentissage artificielle : Le système d'apprentissage avec des gobelets correspond à un modèle dont les gobelets sont les paramètres d'apprentissage. A la fin de chaque partie, une erreur est déterminée (en fonction du résultat de la partie) et cette erreur est rétropropagée selon un protocole bien précis (équivalant de l'optimiseur dans un modèle d'apprentissage).

## TODO
Tester la viabilité de la solution d'apprentissage, en vrai ou via un algorithme de simulation de partie (une évbauche de programme de simulation peut être complétée dans le fichier simulation.py)

