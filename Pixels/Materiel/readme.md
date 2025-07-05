# <p style="text-align : center"> **Génération de Tableaux** </p>


Ce court document présente documente l'utilisation du générateur de tableaux fourni dans le cadre de l'activité "Pixels".

Le générateur se décompose en deux fichiers : 
 - **grid_generator.py** : Définitions des structures de grille et des opérations sur les grilles
 - **testbed.py** : Fichier de test où il est préférable de regrouper les tableaux (Fichier d'exemple) 


</br>
</br>

# Utilisation du générateur de grille

Le fichier *grid_generator.py* déclare la construction de la classe "Grid", représentant un tableau. Cette classe contient une matrice carré, dont les entrées sont des listes à trois éléments **[R, G, B]** (entre $0$ et $255$).

Sont également définies quelques couleurs de base : Red, Green, Blue, Black, White.

Lors de la création d'un objet Grid, il est possible de modifier le nombre de cases que comporte une grille (paramètre *cell_nb*, par défaut vaut $6$), ainsi que la taille d'une cellule en pixels réels (paramètre *cell_size*, par défaut $200$ pixels).

*Note : Le système de coordonées est pour le moment fondé sur des couples $(x, y)$ représentant les coordonées réelles des pixels (commençant donc à $(0,0)$). Il peut être pertinent d'implémenter la conversion d'un système de coordonées semblables aux échecs, plus maniable pour des élèves de CM2*

Quelques fonctions sont disponibles pour intéragir avec le tableau:

- **make_image(name)** : Génère un fichier de nom "name" représentant le tableau

- **plot_pixel(x, y, color)** : Colorie le pixel $(x, y)$ avec la couleur color.

- **fill_grid(color)** : Remplit la grille avec la couleur color.

- **plot_horizontal_line((x_1, y_1), (x_2, y_2), color)** : Trace une ligne horizontale commençant en $(x_1, y_1)$ et terminant en $(x_2, y_2)$ avec la couleur color. Il est supposé que $y_1 = y_2$ pour tracer une ligne horizontale. Si ces deux valeurs diffèrent, $y_1$ est utilisé par défaut.
  
- **plot_vertical_line((x_1, y_1), (x_2, y_2), color)** : Trace une ligne verticale commençant en $(x_1, y_1)$ et terminant en $(x_2, y_2)$ avec la couleur color. Il est supposé que $x_1 = x_2$ pour tracer une ligne verticale. Si ces deux valeurs diffèrent, $x_1$ est utilisé par défaut.
  
- **plot_diagonal_line((x_1, y_1), (x_2, y_2), color)** : Trace une ligne diagonale commençant en $(x_1, y_1)$ et terminant en $(x_2, y_2)$ avec la couleur color. Il est supposé que $|x_1 - x_2| = |y_1 - y_2|$ pour tracer une ligne diagonale. Si ces deux valeurs diffèrent, la diagonale ne sera pas tracée.
  
- **flip_horizontal()** : Permet de retourner le tableau horizontalement
  
- **flip_vertical()** : Permet de retourner le tableau verticalement
