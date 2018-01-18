L'activité initiée ici consiste à comparer les structures d'arbres de décision pour de la classification de masques.

16 cartes représentant des masques
15 caractéristiques binaires:
- Nez: forme, taille, couleur
- Yeux: forme, couleur, nombre
- Dents: nombre (toutes ou une sur deux), couleur
- Cornes: forme, taille, couleur
- Oreilles: taille, couleur
- Sourcils: forme, couleur
- Forme: carré ou triangle.
- Couleur: foncé ou clair (de la teinte qu'on veut).
- Taille: petit ou grand.

Séquence de question fixée:
- 1-Forme du nez
- 2-Forme des yeux
- 3-Forme des cornes
- 4-Forme des sourcils
- 5-Nombre d'yeux
- 6-Nombre de dents
- 7-Couleur du nez
- 8-Couleur des yeux
- 9-Couleur des dents
- 10-Couleur des cornes
- 11-Couleur des oreilles
- 12-Couleur des sourcils
- 13-Taille du nez
- 14-Taille des cornes
- 15-Taille des oreilles

Chaque masque est codé par le vecteur binaire de réponse à ces questions.

Ensemble 1:
Les quatre première caractéristiques décrivent les 16 premiers nombre
binaires qui assurent la répartition dans un arbre équilibré, la suite est
libre
- 0000 10000000000
- 0001 11000000000
- 0010 11100000000
- 0011 11110000000
- 0100 11111000000
- 0101 11111100000
- 0110 11111110000
- 0111 11111111000
- 1000 01111111100
- 1001 00111111110
- 1010 00011111111
- 1011 00001111111
- 1100 00000111111
- 1101 00000011111
- 1110 00000001111
- 1111 00000000111

Ensemble 2:
Les i première caractéristiques du iè masques sont fixées à 0^{i-1}1 pour
assurer la répartition dans un arbre en peigne
- 1 0101010101010
- 01 101010101010
- 001 01010101010
- 0001 1010101010
- 00001 010101010
- 000001 10101010
- 0000001 0101010
- 00000001 101010
- 000000001 01010
- 0000000001 1010
- 00000000001 010
- 000000000001 10
- 0000000000001 0
- 00000000000001
- 00000000000000
