# BIOLOGIE DES SYSTÈMES

# ASSEMBLAGE

## Objectif

L'objectif de cette activité est de faire comprendre le principe et la complexité de l'assemblage de génome.
L'idée est de voir apparaître l'algorithme OLC qui sera détaillée dans une autre section.

**Prérequis :** Aucun

## Matériel

Différentes planches de dominos de longueur variable.
Les sigles *A*, *C*, *G* et *T* sont simplifiés par des formes colorées :

* *A* : carré bleu
* *C* : triangle jaune
* *G* : rond vert
* *T* : étoile rouge

### Scripts

Le script `generate_puzzle.py` permet de générer un fichier PDF contenant une pièce de puzzle pour chaque séquence d'un fichier FASTA.
Ce script nécessite Python3 et la librairie Python *ArgParse*, ainsi que les modules Linux : *pdfjam* et *inkscape*.
Pour l'exécuter, il suffit d'utiliser la commande suivante :
```shell
    python generate_puzzle.py -fasta <fasta_filename> -pdf <output_pdf_filename> [--reverse]
```
L'option `--reverse` permet d'ajouter le reverse complement de chaque séquence, *i.e.* la séquence complémentaire inversée.

Les fichiers FASTA d'entrée doivent avoir le format suivant :
* pour une séquence lambda :
```text
    > ID:<Sequence_UNIQUE_ID>|POS:<First_occurency_position_in_the_solution><Direction>/<Solution_Length>;...|REP:<Number_of_repetitions>
    <Sequence_A_C_G_T>
```
* pour les séquences initiales et finales :
```text
    > FIRST
    <Sequence_A_C_G_T>
    > LAST
    <Sequence_A_C_G_T>
```

#### Exemple

```text
> ID:1|POS:1F/17;2R/17|REP:2
ACGTACGTACGT
> ID:2|POS:3R/17|REP:1
TGCATGCATGCA
> ID:3|POS:4F/17|REP:1
ACGTACGTACGT
> ID:4|POS:5F/17|REP:1
TGCATGCATGCA
> ID:5|POS:6F/17|REP:1
ACGTACGTACGT
> ID:6|POS:7F/17|REP:1
TGCATGCATGCA
> ID:7|POS:8F/17|REP:1
ACGTACGTACGT
> ID:8|POS:9F/17|REP:1
TGCATGCATGCA
> ID:9|POS:10F/17|REP:1
ACGTACGTACGT
> ID:10|POS:11R/17|REP:1
TGCATGCATGCA
> ID:11|POS:12F/17|REP:1
ACGTACGTACGT
> ID:12|POS:13F/17|REP:1
TGCATGCATGCA
> ID:13|POS:14F/17|REP:1
ACGTACGTACGT
> ID:14|POS:15F/17|REP:1
TGCATGCATGCA
> ID:15|POS:16F/17|REP:1
ACGTACGTACGT
> ID:16|POS:17F/17|REP:1
TGCATGCATGCA
> FIRST
ACGTACGTACGT
> LAST
TGCATGCATGCA
```

### Type de niveaux

Il faut plusieurs ensembles de pièces avec différents niveaux de difficultés de reconstruction d'une séquence :

* simple
* ... avec répétitions
* ... avec redondances
* ... avec erreurs
* ... reverse complément

## Pourquoi c'est de l'informatique ?

### Discours

### Classification
