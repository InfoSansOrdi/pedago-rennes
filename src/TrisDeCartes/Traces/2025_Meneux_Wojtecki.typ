#set page(
  flipped: true,
  header: align(left)[
    *Activité "Algorithmes de Tris"* #h(1fr) 28 avril 2025
    #line(length: 100%)
  ]
)

#set text(size: 18pt) // font: "Fraktur BT")

#set par(justify: true)

// #let dotsline(n) = box(width: 1fr, repeat(" _ ",))
#let dotsline(n) = " _ "*n

Un premier joueur choisit un carte parmi plusieurs et l’autre joueur doit la trouver. Quand les cartes ne sont pas triées, on n’a pas de stratégie pour la trouver en peu de coups. Mais quand on trie les cartes et qu’on aide l’autre joueur en indiquant si sa carte est plus grande ou plus petite que celle
choisie, on peut trouver la carte très rapidement !

C’est ce qu’on appelle la *dichotomie*. En choisissant la carte du milieu parmi les cartes restantes, on peut à chaque essai éliminer la #dotsline(5) des cartes. Ainsi dans le pire cas, on a besoin que d’un très petit nombre d’essais. Par exemple, dans notre cas avec *10 cartes*, on a besoin au maximum de *4 essais*. Et si on avait *1 000 000 cartes*, on aurait besoin au maximum de *20 essais* !

#let algo(body) = grid(
  columns: 2,
  // row-gutter: 8pt,
  column-gutter: 4pt,
  grid.vline(),[],
  [#body]
)

#grid(
  columns: 2,
  column-gutter: 12pt,
  [
    *Algorithme 1 : Tri par sélection*
    #algo[
      Trouver la carte la plus petite et la placer à part

      Puis répéter tant que toutes les cartes n’ont pas été mises à part :\
        #h(1em) Trouver la carte la plus petite parmi les\
        #h(1em) cartes qui n’ont pas été mises à part\
        #h(1em) La mettre à droite de la dernière carte mise à\
        #h(1em) part
    ]
  ],[
    * Algorithme 2 : Tri à bulles*
    #algo[
      Pour chaque carte de gauche à droite :\
        #h(1em) La comparer à la suivante\
        #h(1em) Si la première est plus grande que la\
        #h(1em) deuxième, les échanger\
        #h(1em) Revenir au départ si on a fait au moins un\
        #h(1em) échange
    ]
  ]
)