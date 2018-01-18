L'activité initiée ici consiste à comparer les structures d'arbres de décision pour de la classification de masques.
Le matériel se composerait de 16 cartes représentant des masques, chacun étant composé selon les 15 caractéristiques binaires suivantes.
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
1. Forme du nez
2. Forme des yeux
3. Forme des cornes
4. Forme des sourcils
5. Nombre d'yeux
6. Nombre de dents
7. Couleur du nez
8. Couleur des yeux
9. Couleur des dents
10. Couleur des cornes
11. Couleur des oreilles
12. Couleur des sourcils
13. Taille du nez
14. Taille des cornes
15. Taille des oreilles

Chaque masque est codé par le vecteur binaire de réponse à ces questions.

Ensemble 1:
Les quatre premières caractéristiques décrivent les 16 premiers nombres
binaires qui assurent la répartition dans un arbre équilibré, la suite est
libre
1. 0000 10000000000
2. 0001 11000000000
3. 0010 11100000000
4. 0011 11110000000
5. 0100 11111000000
6. 0101 11111100000
7. 0110 11111110000
8. 0111 11111111000
9. 1000 01111111100
10. 1001 00111111110
11. 1010 00011111111
12. 1011 00001111111
13. 1100 00000111111
14. 1101 00000011111
15. 1110 00000001111
16. 1111 00000000111

Ensemble 2:
Les i premières caractéristiques du iè masques sont fixées à 0^{i-1}1 pour
assurer la répartition dans un arbre en peigne. La suite est libre mais agenceée de maniére à créer une certaine diversité des masques générés.
1. 1 01010101010101
2. 01 1010101010101
3. 001 010101010101
4. 0001 10101010101
5. 00001 0101010101
6. 000001 101010101
7. 0000001 01010101
8. 00000001 1010101
9. 000000001 010101
10. 0000000001 10101
11. 00000000001 0101
12. 000000000001 101
13. 0000000000001 01
14. 00000000000001 1
15. 000000000000001
16. 000000000000000
