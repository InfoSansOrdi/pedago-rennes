# Activité les marmottes au sommeil léger
## Objets de l'informatique
### Algorithme (\*\*)
* On utilise l'algorithme de Huffman (1952) qui permet de compresser un texte en construisant son arbre de Huffman. Dans un texte, on commence par compter les
fréquences de chaque lettre, et on crée une forêts d'arbres, où initialement chaque arbre n'est qu'une lettre. A chaque étape, on regroupe les deux arbres avec les
poids les plus faibles. On continue ainsi jusqu'à n'avoir plus qu'un arbre. A la fin, les lettres les plus fréquentes sont proches de la racine, tandis que les
lettres rares sont placées profondément dans l'arbre. En associant un codage binaire à chaque lettre grâce au chemin entre la racine et la lettre (Gauche = 0, Droite = 1),
on obtient un codage permettant de compresser notre texte.
* Cette technique est utilisée par exemple pour créer des archives .zip
### Machine (\*)
* Les fichiers que peuvent manipuler les élèves sont compressés avec Huffman
### Langage (\*)
* C'est une façon de coder des textes
### Information(\*\*)
* On manipule des textes, mais on pourrait utiliser des images, du son. Compression de données.
## Compétences informatique
### Pensée algorithmique (\*\*)
* Trouver un algorithme optimal, comprendre et appliquer Huffman
### Abstraction/Modélisation (\*)
* Transformer le problème des marmottes en problème de compression
### Generalisation et motifs (.)

### Logique (.)

### Évaluation (\*)
* Trouver un algorithme optimal
### Décomposition (.)

## Vécu des élèves
* Utilisé pour des fichiers compressés (.zip) ou multimédia que les élèves ont déjà manipulé.
* Sur un roman comme Vingt milles lieues sous les mers, on peut gagner 65% de taille par exemple.
