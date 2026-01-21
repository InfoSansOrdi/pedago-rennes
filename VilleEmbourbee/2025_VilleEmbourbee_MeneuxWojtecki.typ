#set page(
  flipped: true,
  header: align(left)[
    *Ville embourbée* #h(1fr) 24 mars 2025
    #line(length: 100%)
  ]
)

#set text(size: 20pt) // font: "Fraktur BT")

#set par(justify: true)

// #let dotsline(n) = box(width: 1fr, repeat(" _ ",))
#let dotsline(n) = " _ "*n

#grid(
  columns: (53%, 47%),
  align: horizon,
  [
Toutes les routes de la ville ont été détruites ! Pour pouvoir se déplacer à nouveau sans problème dans la ville, il faut reconstruire des routes, de manière à pouvoir accéder à toute la ville. Cependant, on veut utiliser le moins de béton possible, pour pouvoir construire une piscine avec le reste.
  ],
  image("2025_Carte_TraceEcrite_MeneuxWojtecki.jpg",)
)


Pour cela, on peut utiliser l'algorithme de *Kruskal* : on regarde toutes les routes en commençant par les #dotsline(10) à construire, telle qu'elles permettent de rejoindre deux bâtiments qui #dotsline(15) reliés.

C'est de l'informatique parce qu'on cherche un algorithme pour résoudre un problème. L'algorithme de Kruskal est très souvent utilisé, par exemple pour trouver comment construire les réseaux électriques les moins chers possibles.