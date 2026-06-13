# Usine à chaudrons (A.K.A. 9001 chaudrons) : une activité sur les graphes de flot de contrôle
Cette activité est une variation testée en classe en 2025 de l'activité initiale (située dans le dossier `TestsUniquement`), qui portait à l'origine uniquement sur les tests. Elle a été modifiée afin de montrer plus d'utilisations du graphe de flot de contrôle. Ainsi, elle possède plusieurs objectifs, qui se font en plusieurs étapes :

## Mise en contexte
L'activité porte sur un sorcier pacifiste qui aime faire de la confiture dans son temps libre. Pour cela, il suit des recettes (sous forme de graphe), qui lui indiquent comment faire évoluer la quantité d'ingrédients (sucre, fraise, cerise), qui représentent des variables (elles ont des quantités arbitraires au début, qui vont évoluer en passant dans des instructions de la recette).

## Compréhension du graphe de flot de contrôle
Cette première étape est la plus importante pour qu'ils puissent comprendre la suite. Elle passe par l'explication des éléments qui composent les graphes de flot de contrôle (les variables, les instructions et les conditions), et dans les premiers graphes que l'on utilise, il n'y a qu'un résultat possible. Ceci peut être fait sur vidéo-projectuer/tableau interractif en faisant intervenir plusieurs élèves (avec la première page du fichier `materiel/schemas.pdf`).

Ensuite, on peut donner les 3 pages suivantes aux élèves pour qu'ils s'exercent (où plusieurs jeux de donnée sont fournis), en insistant les consignes suivantes :
- Dessiner les chemins empruntés dans le graphe pour que cela soit lisible pour les intervenants (et pour mieux expliquer les notions de couverture par la suite)
- Raturer bien les valeurs précédentes en écrivant les nouvelles
- Utiliser une couleur de stylo par valeurs initiales pour que l'on puisse encore une fois lire

## Couverture de tests
L'étape suivante se fait en reprennant la parole. On peut alors expliquer la notion de couverture par sommet et par arête, expliquer pourquoi la couverture par arête implique par sommet. On peut alors donner une première intuition de l'intérêt : imaginons que nos recettes aient des instructions qui pourraient être risqués (faire flamber le chaudron et le remuer par exemple), on aimerait bien savoir si on risque de les atteindre. 

## Exécution symbolique
On a donc une première méthode : essayer pleins de valeurs différentes en s'assurant de parcourir une grande partie du graphe (les couvertures), et voir si on l'atteint. Cependant, cette condition ne suffit pas pour assurer que cette instruction ne soit réellement jamais atteinte. 

On introduit donc dans nos graphes un nouvel élément : un nouveau type de résultat, nommé `Boom`, correspondant à l'explosion du chaudron, que l'on voudrait éviter, peu importe les quantités d'ingrédients qu'on avait à la base.

On peut alors donner les autres graphes situés dans `materiel/schemas.pdf`, et leur demander si le `Boom` pourrait être atteint pour une certaine quantité des ingrédients au début, et si oui, peut-il donner un exemple.

Lorsque les élèves ont du mal à expliquer pourquoi dans certains cas il n'existe pas d'entrée pour atteindre le `Boom`, commencer à leur donner l'intuition de remonter depuis le `Boom` jusqu'au début de la recette et notant les contraintes que l'on doit suivre.

## Institutionnalisation
A la fin on peut reprendre l'attention des élèves et retourner sur l'image classique d'un programme informatique comme recette de cuisine. On explique que ce qui préoccupe les informaticiens c'est l'absence de bug (les `Boom` du graphe), qui peuvent être de plein de natures (on peux prendre l'exemple de la division par 0).

Pour cela, on a donc vu deux solutions :
- Ecrire des tests à la main, ie donner des quantités d'ingrédients pour lesquelles il faudrait faire la recette et s'assurer qu'il n'y a pas d'explosion.
- Remonter des possibles bugs jusqu'au début de programmes avec de l'exécution symbolique en faisant des équations (termes qu'ils connaissent rapidement en CM2) pour s'assurer qu'il n'y en a pas.
On peut intuitionner le fait que la seconde solution, bien que sembler plus élégante, est en réalité plus difficile à mettre en place par la lenteur des résolutions des systèmes géants qui y sont créés.

On peut aussi parler du fait qu'ici on s'est interessé à des bugs qu'on a clairement indiqué dans notre programme (comme des `assert(false)`), mais qu'en réalité il y a bien d'aurtres choses qu'on voudrait éviter (comme dans un des exemples où on a des boucles infinies).

## Crédits images
Les images utilisées dans `materiel/schemas.typ` viennent du site [svgrepo.com](https://www.svgrepo.com/), et sont licences MIT (pour [strawberry.svg](https://www.svgrepo.com/svg/510244/strawberry)) ou Public Domain, équivalente à un CC0 Public Domain (pour [cherry.svg](https://www.svgrepo.com/svg/481663/cherry) et [sugar.svg](https://www.svgrepo.com/svg/482072/sugar-cube-1)).

