#import "template.typ": *

// Take a look at the file `template.typ` in the file panel
// to customize this template and discover how it works.
#show: project.with(
  title: "Pédagogie collège (classe de 6e)\n La ville embourbée",
  
  authors: (
    "Vincent Nicolas",
    "Charvy Gaspard"
  )
)
\ 
= Objectifs :
Le but principal de l'activité est de faire découvrir aux élèves le principe d'un algorithme glouton, en particulier ici l'algorithme de Kruskal, ainsi que l'algorithme de Prim.



#table(
  columns: (30pt, auto, 150pt,auto, auto),
  inset: 6pt,
  align: center,
  [temps], [phase],                                [script],[objectif],[materiel],
  [5'],    [présentation (nous + activité)],      [on se présente puis

                                                    "La ville de Bruz a subit une inondation et ses routes sont détruites.
                                                    Il faut construire des routes reliant tous les batiments entre eux en 
                                                    utilisant le moins de béton possible !"
                                                          ],[Mettre les élèves en situation],[--],
  [5'],    [reformulation + exemple],              [On trouve une couverture non optimale au tableau, puis présentation du matériel
                                                          ],[Faire comprendre l'objectif de l'activité aux élèves],[ville facile projetée au tableau (la première que les élèves vont utiliser pour l'activité) + de quoi écrire au tableau],
  [3'],    [distribution du materiel],             [On leur précise de commencer par la première carte],[--],[feuille recto verso, avec les 2 premières villes (assez faciles)],
  [10-15'],   [Activité],[Passage dans les groupes, aide si besoin, recompter et regarder si c'est optimal],              [Que chaque groupe trouve une manière de résoudre le problème],[villes, jetons de Nim (environ 60 par groupe), deuxième feuille avec les plus grandes cartes],
  [10'],   [remise en commun, explication de Kruskal et Prim], [Comment s'y sont ils pris ? Comment résoudre le problème ? Explication des deux algorithmes sur la première ville], [Présenter les deux algorithmes], [projeter la première ville au tableau, + de quoi écrire],
  [10-15'],   [reprise de l'activité], [On fait tester aux groupes les deux algorithmes sur toutes les cartes],[que les élèves se familiarisent avec les algorithmes, et puissent les comparer],[même matériel que la première phase d'activité],
  [5-10'],   [Conclusion de l'activité en groupe], [Leur demander ce qu'ils en ont pensé, quel algorithme ils préfèrent, + trace écrite], [Restitution de l'activité, donner aux élèves une trace écrite pour qu'ils s'en rappellent], [distribuer la trace écrite, + le faire au tableau en même temps qu'eux (projeter + velleda)],
)

= Extensions
 + Donner aux groupes qui avancent plus vite les cartes plus grandes
 
 + Le but de cette intervention est aussi de faire comprendre aux élèves ce qu'est un algorithme. Une extension sera de mettre les élèves par binômes : l'un sera le seul à voir la ville et exécutera dessus les instructions données par l'autre. L'objectif de cette extension est de montrer aux élèves que l'ordinateur ne fait que suivre les instructions données par l'humain, sans réfléchir et de leur faire comprendre la notion d'algorithme : une même série d'instructions doit pouvoir résoudre le problème quelque soit la ville.

 + Trouver un algorithme de plus court chemin (A$*$ ou Dijkstra)

= Etayages
+ On veut un poids global le plus bas possible, il peut être judicieux de sélectionner les routes les moins coûteuses en béton.
+ Indication sur le fait que l'arbre final doit être sans-cycle, et pourquoi.
+ Ne pas essayer de résoudre le problème du premier coup d'oeil, raisonner route par route. (En effet, un ordinateur ne peut effectuer que des opérations élémentaires, et ne peut pas avoir d'intuition).


= Matériel

- 10 feuilles A4 avec des villes assez petites (1 ville par côté)

- 10 feuilles A3 avec des villes plus grandes (1 ville par côté)

- environ 60 jetons par  groupe (à adapter selon la solution optimale des villes utilisées)

= A preparer avant (ou au début de) la préparation :
- Préparer la ville à projeter
- avoir des sachets d'environ 60 jetons (à ajuster) pour chaque groupe