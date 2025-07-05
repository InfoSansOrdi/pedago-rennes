// Cette fiche d'activité a été développée en 2017 par
//  + Santiago Bautista <Santiago.Bautista@ens-rennes.fr>
//  + Benjamin Bordais <Benjamin.Bordais@ens-rennes.fr>
// Convertie à Typst par Martin Quinson en 2025 avec pandoc

// Elle est distribuée sous la licence Creative-Commons by-nc-sa 4.0
// (Attribution, Non-Commercial, Share Alike)
// qui peut être trouvée dans
// [le site de Creative Commons](https://creativecommons.org/licenses/by-nc-sa/4.0/)


#set page(
  header: [  _Jeu de Nim - Plan de l'activité_]+ line(length: 100%),
  margin: (
    top: 3cm,
    bottom: 1cm,
    x: 1.5cm,
  )
)

*Auteurs:*   Santiago Bautista et Benjamin Bordais (ENS Rennes -- 2017)

*Niveau:* CM1-CM2

*Durée:* 45 minutes

*Prérequis:* Aucun

==== Description du jeu:
<description-du-jeu>
Dans le jeu de Nim, deux joueurs s’affrontent. Sur la table, entre eux,
il y a 16 pions/jetons/allumettes qui sont posés. A tour de rôle, chaque
joueur prend un, deux ou trois jetons. Le joueur qui prend le\(s)
derniers jetons a gagné.

#table(
  columns: (auto, 2.5cm, auto, 2.5cm,3cm),
  align: (col, row) => (center,left,left,left,left,).at(col),
  
  [*Durée*], [*Phase*], [*Activités et consignes*], [*Organisation*], [*Matériel*],

  [5’], [Présentation des règles],
  [Je vous propose de jouer à un petit jeu.

  Nous allons vous montrer comment on y joue.

  On montre le déroulement d’une partie au tableau.
  ],
  [\(Santiago et Benjamin)],
  [Tableau et craies \(ou feutres)],

  // //////////////////

  [5’],
  [Appropriation des règles],
  [On joue contre quatre élèves volontaires. Chacun de nous deux en
  rencontre deux. On fait remarquer aux élèves que l’on gagne à chaque
  fois.],
  [Idem],
  [Idem],
  [5’],
  [Exploration du jeu],
  [Les élèves jouent l’un contre l’autre par groupes de deux],
  [Par groupes de deux],
  [Une quinzaine de groupes de 16 jetons colorés],
  [10’],
  [Recherche de stratégie],
  [Recommencez à jouer entre vous, mais maintenant l’objectif est de
  mettre en place une stratégie pour gagner. \(leur rappeler que nous
  avons gagné chaque partie).

  Aide des groupes en difficultés et défis supplémentaires pour les
  groupes en avance.

  ],
  [Idem],
  [Idem],
  [10’],
  [Automatisation de la stratégie],
  [Dans chacun des anciens groupes de deux, il y en a un qui est un
  #emph[robot] et un qui donne les instructions, il a les yeux fermés.
  Ils alternent qui commence, ainsi que les rôles.],
  [Par groupes de quatre],
  [Idem],
  [5’],
  [Démonstration],
  [On choisit un élève à l’aise avec cet exercice pour faire une
  démonstration, l’un de nous est le robot.],
  [Oral collectif],
  [Tableau \(et craies ou feutres)],
  [5’],
  [En quoi est-ce de l’informatique],
  [Ce qu’on vient de faire, c’est de l’informatique car on a besoin de
  stratégies gagnantes \(que l’on appelle algorithmes) pour utiliser des
  ordinateurs.

  C’est que les ordinateurs sont très obéissants: ils font tout ce qu’on
  leur demande, mais seulement ce que l’on demande.

  Il faut donc avoir une stratégie gagnante pour chaque problème que
  l’on veut faire résoudre à l’ordinateur, afin de s’assurer qu’il
  résoudra le problème à coup sûr

  ],
  [Oral collectif],
  [Rien],
)

==== Coup de pouce pour débloquer la réflexion
<coup-de-pouce-pour-débloquer-la-réflexion>
\(si les élèves patinent) :

- Ranger les jetons/allumettes par couleurs, donc par groupes de 4

- On peut jouer avec seulement 4 jetons, puis rajouter 4 autres jetons
  une fois qu’ils auront compris, et ainsi de suite.

- On joue contre l’élève avec la consigne regarde bien ce que je fais
  puis on inverse les rôles en cours de partie.

- On propose des stratégies \(qui marchent pas) et on demande aux élèves
  de jouer contre.

  - prend toujours 3 pions \(ou tous les pions s’il en reste moins),
    systématiquement.

  - prend toujours un seul pion, systématiquement, quoi qu’il arrive.

  - détermination au D6 du nombre de pions pris

==== Variantes pour aller plus loin
<variantes-pour-aller-plus-loin>
\(si certains groupes d’élèves vont trop vite)

- Est-ce que tu préfères commencer ou pas?

- Et s’il y a 17 jetons au début, que se passe-t-il ?

- Maintenant, celui qui prend le dernier jeton perd
