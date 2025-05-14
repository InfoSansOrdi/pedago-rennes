#set page(
  flipped: true,
)

#set text(size: 18pt) // font: "Fraktur BT")

#let algo(body) = grid(
  columns: 2,
  row-gutter: 8pt,
  column-gutter: 8pt,
  grid.vline(),[],
  [#body]
)

= Algorithme 1 : Tri par sélection
#algo[
  Trouver la carte la plus petite et la placer à part

  Puis répéter tant que toutes les cartes n’ont pas été mises à part :\
    #h(1em) Trouver la carte la plus petite parmi les cartes qui n’ont pas été mises à part\
    #h(1em) La mettre à droite de la dernière carte mise à part
]
= Algorithme 2 : Tri à bulles
#algo[
  Pour chaque carte de gauche à droite :\
    #h(1em) La comparer à la suivante\
    #h(1em) Si la première est plus grande que la deuxième, les échanger\
    #h(1em) Revenir au départ si on a fait au moins un échange
]


= Algorithme 3 : Tri rapide
#algo[
  S’il n’y a qu’une seule carte, c’est terminé\
  Sinon :\
  #h(1em) Regarder la première carte\
  #h(1em) Mettre toutes les cartes plus petites à gauche et les plus grandes à droite\
  #h(1em) Répéter l’opération pour les cartes à gauche et les cartes à droite
]