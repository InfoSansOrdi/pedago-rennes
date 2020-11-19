# Puzzle Humain #

Bienvenue dans cette fraiche version du jeu de vulgarisation informatique, le puzzle humain.

Ce dossier comprend : 
```
.
├── Exemples              -> Les dossiers d'autres exemples, à étendre.
│   ├── ...
│   └── tailleur
├── FichesDePreparation   -> Comment animer l'activité
│   └── fiche_de_preparation.odt  
├── Materiel              -> Le répertoire permettant de créer un nouveau puzzle
│   ├── config.py           -> un exemple de configuration, à changer pour de nouveaux puzzles
│   ├── main.py             -> le script principal, à lancer avec python3
│   ├── output-duchesse     -> le résultat du script sur l'exemple actuel
│   └── templates           -> fichiers SVG des pièces du puzzle utiles au script
│── Rapports              -> Rapports d'étonnement des animateurs
│   ├── ...
│   └── 2019_MavromatisThuillier_Rapport.pdf
└── README.md
```

## Script principal : ##

### Input ###

Fichier de configuration `config.py` contenant :

1. Une phrase d'entrée
2. La forme de puzzle voulue
3. Bordures externes ou non
4. Autres.

### Output ###

* PDF des pièces de puzzle
* N'utilise pas les nombres ambigus (96, 69, etc..)
* Métadonnées au dos :
	1. Nom du puzzle répété, généré de manière déterministe à partir des informations du fichier de configuration. Le nom est en majuscule si on a des numéros sur les bords, en minuscule sinon ;
	2. Numéro de pièce / Nombre de pièces total (dans un ordre aléatoire, pour ne pas donner la solution) ;
* Nombre de mots par pièce environ équitable
* SVG des pièces de puzzle disponible en bidouillant le code (simplement ne pas les supprimer après génération du PDF)

### Dépendances ###

* python3
* inkscape
* pdfunite
* peut-être plus..

